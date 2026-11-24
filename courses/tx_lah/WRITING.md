# Writing brief: Texas Life, Accident and Health exam course

You are writing ONE topic file for an exam-prep course built on the Mastery Field Guide format.
Read these first:
- `/home/claude/exam_prep/FORMAT_field_guide.md` (schema, compact standard, body HTML rules). Follow the schema exactly.
- `/home/claude/exam_prep/courses/tx_lah/outline.md` (the official Pearson VUE outline, effective 2026-09-01). Your topic covers the outline items listed under its heading.

## The reader and the goal
An adult studying for the Texas General Lines - Life, Accident and Health exam (100 general + 30 Texas law
questions, 70 to pass, first-time pass rate about 56%). Many are career changers with no insurance background.
Goal: after studying this topic they can answer any exam question on its outline items. Depth and
comprehensiveness win over brevity here: EVERY outline item in your section must be covered by at least one
concept, and the cards must drill what the exam asks.

## Concept shape (overrides the compact standard where they differ)
- 8 to 16 concepts per topic. First concept in group `map`: the organizing schema of the topic plus a one-line
  "how the exam tests this section".
- Sections in this order, titles exactly: `Model` (how it works, the definitions and rules, the numbers), `Traps`
  (trap blocks: the distractors and confusions the exam exploits), `Example` (one concrete case; worked numbers
  where numbers matter), optional `Exam angle` (how questions are phrased, the keyword that gives it away).
- At most 300 words per concept (summary + section bodies; cards not counted).
- Summary `s`: the rule in ONE sentence.
- Cards: 3 to 5 per concept, written as exam-style discrimination or scenario prompts with one right answer
  ("A policyowner stops paying premiums on a whole life policy with cash value and wants coverage for the full face
  amount for as long as possible without more payments. Which nonforfeiture option?"). No yes/no, no "list the X".
  Answers 1-2 sentences, plain text.
- Add to every concept an `"o"` array of the outline codes it covers, e.g. `"o": ["G-II.B.6", "G-II.B.7"]`
  (section code from outline.md + letter + item number in the order listed). Every item in your section must
  appear in some concept's `o`.

## Accuracy (strict)
- The date is 2026-11-23. General insurance principles you know well (contract law, policy types, uniform
  provisions, nonforfeiture options) need no search. Verify anything numeric, legal or perishable before stating it.
- Texas law topics: every rule must come from the Texas Insurance Code (statutes.capitol.texas.gov), 28 Texas
  Administrative Code, or TDI publications (tdi.texas.gov) that you opened this session. Name the section in prose
  ("Texas Insurance Code Sec. 1101.011 sets..."). If you cannot confirm a Texas-specific number, say so in the
  text rather than guessing, and leave it off the cards.
- Perishable federal numbers (2026 Medicare premiums and deductibles, HSA/HDHP limits, retirement plan
  contribution limits, Social Security figures): confirm on cms.gov, medicare.gov, irs.gov or ssa.gov and
  date-stamp them ("2026:"). Exam questions rarely need the exact current dollar figure; put the durable rule on
  the cards and the figure in prose.
- Where national prep material and Texas law differ (e.g. free-look length, grace period length), the Texas rule
  goes in the Texas topic; the general topic states the general rule and says "Texas specifics: see Texas law tab".
- Never copy text or questions from prep companies (Kaplan, ExamFX, Achievable, open-exam-prep, Quizlet, etc.).
  Write everything in your own words. You may read them only to see what candidates find confusing.
- Plain, direct sentences. No em-dash asides, no marketing language.

## Search budget
The session shares about 200 web searches per turn across all agents. Use at most the number in your assignment.
Prefer WebFetch on official pages you already know (statutes.capitol.texas.gov, tdi.texas.gov, medicare.gov,
irs.gov) over new searches.

## Output
Write the FULL topic file to the path in your assignment: id, title, updated "2026-11-23", refreshDays (365 for
general topics, 180 for Texas law and for topics with federal dollar figures), note (what it covers, outline
codes, when to refresh), groups, concepts, sources (8-25 {"title","url"} you actually opened or saw; never
construct URLs). Validate with `python3 -c "import json;json.load(open(PATH))"`. Then run
`python3 /home/claude/exam_prep/tests/check_topic.py PATH` and fix every error it reports.
Return a 3-line summary: concepts and cards written, outline items covered, anything you could not verify.
