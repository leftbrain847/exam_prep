# Review brief: independent accuracy check (Texas Life, Accident and Health course)

You did not write these topics. Your job is to find and fix errors before the course is published to the public,
where a wrong rule could make a candidate fail the exam.

Read `/home/claude/exam_prep/courses/tx_lah/WRITING.md` (the rules the writers followed) and your assigned topic
files in `/home/claude/exam_prep/courses/tx_lah/topics/`.

## What to check, in priority order
1. **Every card** (q and a) and every number, deadline, percentage, dollar figure or legal rule in `Model` and
   `Traps`. Cards matter most: students memorize them.
2. **Texas law**: confirm against the Texas Insurance Code (read it at
   https://tcss.legis.texas.gov/resources/IN/htm/ , e.g. .../IN.1101.htm, because statutes.capitol.texas.gov is
   blocked here), 28 TAC (Cornell LII law.cornell.edu/regulations/texas/... or the Texas SOS site), or
   tdi.texas.gov pages. Federal figures: cms.gov, medicare.gov, irs.gov, ssa.gov, healthcare.gov, dol.gov.
3. **Consistency across tabs**: a general tab must not contradict the Texas tab (free look, grace period,
   reinstatement, time limit on certain defenses, dependent age). Where the national textbook rule and Texas law
   differ, the general tab states the general rule and says the Texas rule is in the Texas tab; the Texas tab
   states the Texas rule with its citation.
4. **Exam-correctness**: answers must be what the exam expects. Flag any card whose answer is technically defensible
   but likely marked wrong on a standard licensing exam, and fix it.
5. **Plain-language note**: rewrite each topic's `note` for a student: what the tab covers and when it was last
   checked. Remove outline codes (G-I.A.1 style) from the note only; keep the `o` arrays on concepts unchanged.

## How to fix
- Edit the JSON directly. Only change a claim when an official source you opened this session supports the
  change; otherwise mark it uncertain in prose ("could not be confirmed as of Nov 2026") and remove it from cards.
- Keep the file passing `python3 /home/claude/exam_prep/tests/check_topic.py <file>` after your edits.
- Add any source you used to the topic's `sources` (keep 8-25; drop weaker ones if needed).
- Do not rewrite for style. Do not copy text from prep companies.

## Report
Write `/home/claude/exam_prep/courses/tx_lah/review/<your-batch>.md`: for each topic, a table of every change
(concept, what was wrong, what it says now, source URL), then a list of claims you could not confirm and left
marked as uncertain, then a one-line verdict per topic (publish / publish after the listed fixes / hold).
Return a 5-line summary: errors found and fixed (count, worst three), open uncertainties, verdicts.

## Search budget
About 200 web searches per turn are shared by all agents in this session. Use at most the number in your
assignment; prefer WebFetch on the official URLs above.
