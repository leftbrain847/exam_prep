# Verify brief: sourced check of the top 100 (focus: can a new entrant win?)

J sells exam prep (compressed notes + flashcards + spaced repetition, marketed through searchable
YouTube explainers, solo operator with AI-built content). A first pass guessed these exams are
attractive. Your job is to test that with sources, above all the competition question.

Input CSV: rid, name, org, type, score. For EACH row, use 3-6 WebSearch calls (WebFetch where a
snippet is ambiguous) to find, each with a source URL:
1. takers per year (or best proxy) and most recent pass rate (with year)
2. exam fee + retake cost
3. competition: name the top 3-6 paid prep products with prices; note any free/cheap dominant
   option (e.g. a $15 Udemy course or free YouTube channel everyone recommends); note review
   complaints (outdated, too long, expensive)
4. new-entrant evidence: has any solo creator / small app broken in recently (popular YouTube
   channel, indie app with traction)? Yes = market is open to newcomers
5. who pays (employer reimbursement common?)
6. content change cadence and whether source material is public
7. community: main subreddit + member count, or forum
8. check whether open-exam-prep.com (free notes + flashcards + AI tutor) already covers this exam; mention in top_competitors if so

Scores 0-5 (5 = best for J), BLANK if unsourced:
pain_low_pass_rate, exam_fee_and_retake_cost, takers_per_year_fit (5 = tens of thousands+ with
paying intent; for J big is fine IF beatable), weak_incumbents (5 = dated/overpriced/thin prep, or
clear evidence newcomers win; 1 = a cheap dominant player everyone uses), employer_pays,
refresh_cadence, public_source_material, reachable_community, expansion_ladder,
liability (5 = safe; 1 = clinical/legal-advice risk)

Never invent numbers; "not found" is fine. Paraphrase, no long quotes.

Output CSV (quote fields with commas), header exactly:
rid,name,takers,pass_rate,fee,top_competitors,newcomer_evidence,community,pain_low_pass_rate,exam_fee_and_retake_cost,takers_per_year_fit,weak_incumbents,employer_pays,refresh_cadence,public_source_material,reachable_community,expansion_ladder,liability,verdict,sources
(verdict <= 20 words; sources = semicolon-separated URLs)
Write to the output path in your assignment; return a 3-line summary.
