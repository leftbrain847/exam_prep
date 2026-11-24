"""rank_all: stage-1 scoring of every CareerOneStop certification and license family.

usage: python rank_all.py <certs.xlsx> <licenses.pkl> [--rubric rubric.yaml] [--outdir out]
"""
import argparse, math, os, re
import pandas as pd
import yaml


def rx(words):
    return re.compile("|".join(r"\b" + re.escape(w.lower()) for w in words))


def frac(series, words, cap):
    r = rx(words)
    return series.map(lambda s: min(len(r.findall(s)), cap) / cap)


def norm(score, weights):
    pos = sum(v for v in weights.values() if v > 0)
    return (score.clip(lower=0) / pos * 100).round(1)


def score_certs(df, rb):
    c, kw = rb["certs"], rb["keywords"]
    w = c["weights"]
    blob = df[c["text_fields"]].fillna("").astype(str).agg(" ".join, axis=1).str.lower()
    org = df["ORG_NAME"].fillna("").str.lower()
    reasons = pd.Series("", index=df.index)
    reasons[df[c["gates"]["require_exam_column"]] != 1] += "no_exam;"
    reasons[df["TYPE"].isin(c["gates"]["exclude_types"])] += "vendor_product;"
    reasons[org.str.contains(rx(c["gates"]["exclude_entrenched_orgs"]))] += "entrenched_vendor;"
    reasons[blob.str.contains(rx(c["gates"]["exclude_clinical"]))] += "clinical;"
    renewal = pd.to_numeric(df["RENEWAL"].astype(str).str.strip(), errors="coerce")
    f = pd.DataFrame({
        "type_level": df["TYPE"].map(c["type_scores"]).fillna(0),
        "recurring": (df["CEU"].fillna(0) + df["REEXAM"].fillna(0)
                      + (renewal <= 3).astype(float)) / 3,
        "high_stakes": frac(blob, kw["high_stakes"], 3),
        "format_fit": frac(blob, kw["format_fit"], 3),
        "own_edge": frac(blob, kw["own_edge"], 2),
        "ladder": df.groupby("ORG_ID")["CERT_ID"].transform("count")
                    .map(lambda n: min(math.log2(n) / 5, 1)),
        "practical_penalty": frac(blob, kw["practical_penalty"], 1),
    })
    raw = sum(f[k] * v for k, v in w.items())
    out = pd.DataFrame({"kind": "cert", "id": df["CERT_ID"], "name": df["CERT_NAME"],
                        "org": df["ORG_NAME"], "type": df["TYPE"],
                        "excluded": reasons.str.rstrip(";")})
    out["stage1"] = norm(raw, w).where(out["excluded"] == "", 0.0)
    return pd.concat([out, f.round(2).add_prefix("f_")], axis=1)


def score_licenses(df, rb):
    L, kw = rb["licenses"], rb["keywords"]
    w = L["weights"]
    df = df.copy()
    df["occcode"] = df["occcode"].fillna("").astype(str).str.strip()
    df["examdesc"] = df["examdesc"].fillna("Undetermined").str.strip()
    stop = r"\b(" + "|".join(L["title_stopwords"]) + r")\b"
    df["family"] = (df["lictitle"].fillna("").str.lower()
                    .str.replace(r"[^a-z ]", " ", regex=True)
                    .str.replace(stop, " ", regex=True)
                    .str.split().str.join(" "))
    df = df[df["family"] != ""].drop_duplicates(["family", "st", "licenseid"])
    n_states_total = df["st"].dropna().nunique()
    rows = []
    for occ, g in df.groupby("family"):
        is_fed = (g["licensetypedesc"] == "Federal license").mean() > 0.5
        if g["st"].nunique() < L["gates"]["min_states"] and not is_fed:
            continue
        exam_rows = g[g["examdesc"] != "No exam"]
        titles = g["lictitle"].dropna().str.strip().value_counts()
        blob = " ".join(g[["lictitle", "licdesc", "examdesc"]].fillna("").astype(str)
                        .agg(" ".join, axis=1).head(80)).lower()
        excl = []
        if L["gates"]["exclude_no_exam"] and exam_rows.empty:
            excl.append("no_exam")
        occs = g["occcode"].value_counts(dropna=False)
        if any(occs.index[0].startswith(p) for p in L["gates"]["exclude_soc_prefixes"]) \
                or rx(rb["certs"]["gates"]["exclude_clinical"]).search(occ):
            excl.append("clinical")
        states = exam_rows["st"].dropna().nunique()
        federal = (g["licensetypedesc"] == "Federal license").mean() > 0.5
        rows.append({
            "kind": "license", "id": occ, "name": " | ".join(titles.index[:2]),
            "occcode": occs.index[0],
            "org": "federal" if federal else f"{states} states", "type": "license",
            "excluded": ";".join(excl), "n_states": states,
            "f_exam_strength": exam_rows["examdesc"].map(L["exam_scores"]).fillna(0).mean()
                               if not exam_rows.empty else 0,
            "f_state_breadth": states / n_states_total,
            "f_federal": float(federal),
            "f_high_stakes": min(len(rx(kw["high_stakes"]).findall(blob)), 3) / 3,
            "f_format_fit": min(len(rx(kw["format_fit"]).findall(blob)), 3) / 3,
            "f_own_edge": min(len(rx(kw["own_edge"]).findall(blob)), 2) / 2,
            "f_practical_penalty": min(len(rx(kw["practical_penalty"]).findall(blob)), 1),
        })
    out = pd.DataFrame(rows)
    raw = sum(out[f"f_{k}"] * v for k, v in w.items())
    out["stage1"] = norm(raw, w).where(out["excluded"] == "", 0.0)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("certs"); ap.add_argument("licenses")
    ap.add_argument("--rubric", default="rubric.yaml"); ap.add_argument("--outdir", default="out")
    a = ap.parse_args()
    rb = yaml.safe_load(open(a.rubric))
    os.makedirs(a.outdir, exist_ok=True)
    certs = score_certs(pd.read_excel(a.certs), rb).sort_values("stage1", ascending=False)
    lic = score_licenses(pd.read_pickle(a.licenses), rb).sort_values("stage1", ascending=False)
    certs.to_csv(f"{a.outdir}/certs_ranked.csv", index=False)
    lic.to_csv(f"{a.outdir}/license_families_ranked.csv", index=False)
    m = rb["meta"]
    for name, d, n in [("certs", certs, m["shortlist_certs"]), ("licenses", lic, m["shortlist_license_families"])]:
        kept = (d["excluded"] == "").sum()
        print(f"\n== {name}: {len(d)} scored, {kept} passed gates; exclusions: "
              f"{d['excluded'].str.split(';').explode().value_counts().drop('', errors='ignore').to_dict()}")
        print(d.head(n)[["id", "name", "org", "stage1"]].to_string(index=False, max_colwidth=60))
