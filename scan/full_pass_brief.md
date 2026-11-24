# Full-pass brief: judge every certification/license (no web, knowledge-based prior)

Goal: J wants to sell exam prep (compressed notes + flashcards + spaced repetition, marketed via
searchable YouTube explainers). He wants money: big or under-served markets where people pay to
pass a consequential exam and where a sharper product could win share. Do NOT dismiss a cert
because a big company runs it or because prep already exists: a huge market with mediocre prep
(e.g. AWS, CompTIA, PMP) can be very attractive. Judge on evidence you know.

Input CSV columns: rid, name, acronym, org, type, exam (1 = exam required). type "license" rows
are state/federal license families (org shows "N states" or "federal").

For EVERY row, from your own knowledge (no web searches; this is a fast prior that a later
sourced pass will verify), score 0-5:
- takers: est. candidates per year. 0 = unknown/tiny (<100), 1 = hundreds, 2 = ~1k,
  3 = several thousand, 4 = tens of thousands, 5 = 100k+
- stakes: how much passing matters (job gate, legal requirement, pay jump = high)
- spend: do candidates (or employers) visibly pay for prep today? 0 = no prep market,
  5 = thriving paid prep market
- fee: exam cost. 0 = free/<$50, 1 = <$150, 2 = <$300, 3 = <$500, 4 = <$1000, 5 = $1000+
- crushable: could a better compressed/SRS/video-led product realistically win paying users?
  5 = dated/overpriced/thin incumbents OR a large market where differentiation clearly works;
  1 = locked (official-only prep, closed content, or entrenched cheap dominant player)
- written_fit: 5 = written knowledge exam (memorization, rules, concepts); 0 = practical/hands-on
- safe: 5 = low liability; 1 = clinical/legal-advice risk if content is wrong
- conf: your confidence in these scores, 0 = guessing, 1 = some knowledge, 2 = know it well

Many rows will be obscure: score them honestly low on takers with conf 0; that is fine and
expected. Be consistent across rows. Do not skip rows.

Output: CSV with header exactly
rid,takers,stakes,spend,fee,crushable,written_fit,safe,conf,note
(note = optional <=8 words, quote if it contains commas). One output row per input row.
Write it with the Write tool (in chunks if needed, appending via Bash `cat >>` is fine) to the
output path in your assignment. Verify the row count matches the input before finishing, then
return a 2-line summary: rows written, and the 5 highest-potential rids with names.
