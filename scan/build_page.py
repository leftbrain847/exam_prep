"""build_page: render scan/out/final_ranked.csv into the results page web/exam_scan.html.

    python3 scan/build_page.py

The page is a snapshot of the Nov 2026 scan. tests/test_scan.py fails if the committed page drifts from this build.
"""
import json, math, os
import pandas as pd
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "web", "exam_scan.html")

d = pd.read_csv(os.path.join(HERE, "out", "final_ranked.csv"))
cols = ["final_rank", "name", "final", "status", "thesis_fit", "pain_low_pass_rate", "weak_incumbents",
        "takers_per_year_fit", "exam_fee_and_retake_cost", "employer_pays", "liability",
        "takers", "pass_rate", "fee", "top_competitors", "newcomer_evidence", "verdict", "sources"]
rows = []
for _, r in d[cols].iterrows():
    rec = {}
    for c in cols:
        v = r[c]
        rec[c] = None if (isinstance(v, float) and math.isnan(v)) else (v.item() if hasattr(v, "item") else v)
    rec["name"] = str(rec["name"]).split(" | ")[0]
    rows.append(rec)
n_all = yaml.safe_load(open(os.path.join(HERE, "rubric.yaml")))["meta"]["total_items"]   # rows scored in the full pass
n_ver = int((d.status == "verified").sum())
data = json.dumps(rows).replace("</", "<\\/")

html = open(os.path.join(HERE, "page_template.html")).read()
html = html.replace("__DATA__", data).replace("__N_ALL__", f"{n_all:,}").replace("__N_VER__", str(n_ver))
if __name__ == "__main__":
    open(OUT, "w").write(html)
    print("wrote", OUT, len(html), "bytes;", n_ver, "verified")
