"""final_rank: blend the full-pass prior with sourced verification for the top 100.

Re-run rows (reverified_*.csv) replace earlier rows for the same rid. Scores average only the
factors that were actually sourced; rows with too few sourced core factors are flagged.

usage: python final_rank.py [--rubric rubric.yaml]
"""
import argparse, glob
import pandas as pd
import yaml

CORE = ["pain_low_pass_rate", "takers_per_year_fit", "weak_incumbents"]


def load(pattern):
    files = sorted(glob.glob(pattern))
    return pd.concat([pd.read_csv(f) for f in files], ignore_index=True) if files else pd.DataFrame()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--rubric", default="rubric.yaml")
    a = ap.parse_args()
    rb = yaml.safe_load(open(a.rubric))["verified"]
    w = {k: v for k, v in rb["weights"].items() if v > 0}
    first, rerun = load("out/full/verified_*.csv"), load("out/full/reverified_*.csv")
    v = pd.concat([rerun, first], ignore_index=True).drop_duplicates("rid", keep="first")
    for k in rb["weights"]:
        v[k] = pd.to_numeric(v.get(k), errors="coerce")
    v["sourced_core"] = v[CORE].notna().sum(axis=1)
    num = v[list(w)].mul(pd.Series(w)).sum(axis=1)
    den = v[list(w)].notna().mul(pd.Series(w)).sum(axis=1) * 5
    v["verified_score"] = (num / den * 100).round(1)
    top = pd.read_csv("out/full/verify_top100.csv")[["vrank", "rid", "org", "type", "score"]]
    d = top.rename(columns={"score": "prior"}).merge(v, on="rid", how="left")
    d["status"] = d["sourced_core"].ge(rb["min_sourced_core"]).map({True: "verified", False: "needs_rerun"})
    d["final"] = (rb["blend"]["prior"] * d["prior"] + rb["blend"]["verified"] * d["verified_score"]).round(1)
    # beatable + painful: the thesis filter J cares about
    d["thesis_fit"] = (d["weak_incumbents"].ge(3) & d["pain_low_pass_rate"].ge(4)).map({True: "yes", False: ""})
    d = d.sort_values(["status", "final"], ascending=[False, False]).reset_index(drop=True)
    d.index += 1
    d.to_csv("out/final_ranked.csv", index_label="final_rank")
    print(d["status"].value_counts().to_dict())
    print(d.head(30)[["name", "final", "thesis_fit", "pain_low_pass_rate", "weak_incumbents",
                      "takers_per_year_fit", "status"]].to_string(max_colwidth=42))
