"""build_page: render out/final_ranked.csv into a self-contained results page (out/cert_ranker.html)."""
import json, math
import pandas as pd

d = pd.read_csv("out/final_ranked.csv")
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
n_all = len(pd.read_csv("out/full/all_items.csv"))
n_ver = int((d.status == "verified").sum())
data = json.dumps(rows).replace("</", "<\\/")

html = open("page_template.html").read()
html = html.replace("__DATA__", data).replace("__N_ALL__", f"{n_all:,}").replace("__N_VER__", str(n_ver))
open("out/cert_ranker.html", "w").write(html)
print("wrote out/cert_ranker.html", len(html), "bytes;", n_ver, "verified")
