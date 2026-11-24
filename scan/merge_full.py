"""merge_full: combine the 15 full-pass score files into one ranking of every item.

usage: python merge_full.py [--rubric rubric.yaml]
"""
import argparse, glob
import pandas as pd
import yaml

DEFAULT_W = {"takers": 3, "stakes": 2, "spend": 3, "fee": 1.5, "crushable": 3,
             "written_fit": 2, "safe": 1.5}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--rubric", default="rubric.yaml")
    a = ap.parse_args()
    w = yaml.safe_load(open(a.rubric)).get("full_pass", {}).get("weights", DEFAULT_W)
    items = pd.read_csv("out/full/all_items.csv")
    parts = [pd.read_csv(f) for f in sorted(glob.glob("out/full/scored_*.csv"))]
    s = pd.concat(parts, ignore_index=True).drop_duplicates("rid")
    d = items.merge(s, on="rid", how="left")
    missing = d["takers"].isna().sum()
    for k in w:
        d[k] = pd.to_numeric(d[k], errors="coerce")
    d["score"] = (d[list(w)].fillna(0).mul(pd.Series(w)).sum(axis=1)
                  / (5 * sum(w.values())) * 100).round(1)
    # a market of zero can't be rescued by other factors
    d.loc[d["takers"].fillna(0) <= 1, "score"] *= 0.6
    d = d.sort_values("score", ascending=False).reset_index(drop=True)
    d.index += 1
    d.to_csv("out/full/all_ranked.csv", index_label="rank")
    print(f"{len(d)} items, {missing} unscored")
    print(d.head(60)[["rid", "name", "org", "score", "takers", "spend", "crushable", "conf"]]
          .to_string(max_colwidth=50))
