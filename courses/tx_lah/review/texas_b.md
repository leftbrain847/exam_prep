# Review: texas_b batch (txhealth)

Reviewed 2026-11-23. I read every card, summary, Model, Traps and Example in topic-txhealth.json and checked them
against sources opened this session: Texas Insurance Code Chapters 843, 1201, 1271, 1367, 1368, 1501, 1651, 1652
(tcss.legis.texas.gov); 28 TAC Secs. 3.3306, 3.3309, 3.3312, 3.3324, 3.3818, 3.3824, 3.3825, 3.3832, 3.3841,
11.506, 11.1600, 21.704, 21.705 (Cornell LII / Justia); IRS premium tax credit eligibility page (reviewed
Nov. 6, 2026); IRS "Repayment caps eliminated" page (reviewed Oct. 7, 2026); KFF, 9 things to watch for 2027 open
enrollment (Nov. 6, 2026). The file passes check_topic.py.

## txhealth

| Concept | What was wrong | What it says now | Source |
|---|---|---|---|
| ACA marketplaces, subsidies and taxes (Model) | Said excess advance premium tax credit is repaid "in full at 400% of poverty or more", implying income-based caps below 400%. Those caps were repealed starting tax year 2026 | Starting with tax year 2026, excess advance credit is repaid in full at every income level | https://www.irs.gov/tax-professionals/eitc-central/repayment-caps-eliminated-for-excess-advance-payments-of-the-premium-tax-credit |
| ACA marketplaces (Model) | 2026 status of the 400% cap not stated | 400% cap applies for 2026; enhanced 2021 to 2025 credits expired and were not extended as of Nov. 6, 2026 | https://www.irs.gov/affordable-care-act/individuals-and-families/eligibility-for-the-premium-tax-credit ; https://kff.org/affordable-care-act/9-things-to-watch-for-the-2027-aca-open-enrollment-period/ |
| ACA marketplaces (Example, new card) | Example said "repay the excess" without the 2026 rule | Example says full repayment; new card drills full repayment at 250% of poverty | IRS repayment caps page (above) |
| Small employer eligibility (Model) | Said employees with other coverage who decline "can be handled under Sec. 1501.155". Wrong: Sec. 1501.002 excludes an employee covered under another health plan from "eligible employee"; Sec. 1501.155 is the lower-participation / no-pressure-to-decline exception | Eligible employee bullet now excludes employees covered by another plan; Sec. 1501.155 described correctly | https://tcss.legis.texas.gov/resources/IN/htm/IN.1501.htm |
| Small employer eligibility (Example) | Example counted spouse-covered employees in the 75% base | Two spouse-covered workers drop out; 75% of 18 is 13.5, so 14 must enroll | same |
| Long-term care rules (Model) | Said Sec. 1651.056 requires "contingent nonforfeiture benefits"; the statute only sets the 45-day rate-increase notice | Phrase removed | https://tcss.legis.texas.gov/resources/IN/htm/IN.1651.htm |
| Long-term care rules (Model, summary, new card) | Outline of coverage (priority check) missing | 28 TAC 3.3832: delivered at initial solicitation; agent delivers it before presenting the application; direct response sends it with the application. New card | https://law.cornell.edu/regulations/texas/28-Tex-Admin-Code-SS-3-3832 |
| Medicare supplement renewal (Model) | "Under 65" window stated with no eligibility group | Secs. 1652.059 and 1652.060: under-65 people on Medicare because of ESRD or ALS get the same offer and a six-month window from first Part B month | https://tcss.legis.texas.gov/resources/IN/htm/IN.1652.htm |
| ACA marketplaces / EHB (sources) | Source list would exceed 25 | Dropped TDI shopping checklist and HealthCare.gov EHB page; removed the checklist-only claims (TDI approves plans, most shoppers qualify, TDI warning wording) and cited ACA Sec. 1302 for the 10 EHB categories | n/a |
| (note) | Outline codes in the note | Plain-language scope plus "Last checked 2026-11-23" | n/a |

Confirmed correct, no change (priority checks):
- Newborns: Sec. 1367.003 bars limiting initial newborn coverage before the 61st day and excluding congenital
  defects; Sec. 1501.157 small group coverage ends on day 61 unless notice and premium arrive by day 60; 28 TAC
  11.506 HMO newborn covered 31 days, 31 days to notify orally or in writing, HMO may require premium, congenital
  defects treated like other illness. Adoption: Sec. 1201.061 (party to suit) and Sec. 1501.158 (31 days).
- Dependent age: 25 in Secs. 1201.053, 1201.062, 1501.002 and 1271.006; trap correctly notes the federal ACA age 26.
  Disabled child: proof within 31 days, then no more than yearly after the second anniversary (Sec. 1201.059).
- Chemical dependency: Ch. 1368 group-only mandate, self-funded 250-or-fewer exemption, parity, three lifetime
  treatment series, series ends at discharge or 30 days of noncompliance, treatment center treated as hospital.
- Medicare supplement: 6-month exclusion and 6-month look-back (1652.058), outline at application (1652.152),
  30-day free look with notice on first page (1652.155), ads filed 60 days ahead (1652.156), guaranteed renewable,
  cancel only for nonpayment or material misrepresentation, Medicaid suspension up to 24 months with 90-day notices
  (3.3306), replacement notice and five-year list (3.3309), 63-day guaranteed issue (3.3312), open enrollment from
  first Part B month (3.3324).
- HIV: 21.704 separate written consent form, allowed questions, barred proxies, counseling protection, positive
  result to named physician or else the state health department; 21.705 two ELISAs plus Western Blot.
- LTC: 12 months (1651.003), 6/6 preexisting (1651.052, 3.3824), 30-day return (1651.054), 45-day rate notice
  (1651.056), two-ADL trigger (3.3818), no prior hospitalization, 30-day cap for noninstitutional (3.3825), lapse
  designee, 30/30-day notices and five-month reinstatement (3.3841).
- Small employer: 2-50 average in prior calendar year plus 2 on first day of plan year, 51+ large, 30-hour eligible
  employee, 75% participation, 31-day enrollment, 90-day waiting period, late enrollee rules, renewal grounds
  (1501.108), 30-day notice to employer (1501.110), 180-day market exit and five-year bar, 90-day product
  discontinuance (1501.109), 60-day rate notice (1501.216), substance abuse waiver 50% and three years (1501.254),
  agent steering and pay rules (1501.352, 1501.353).
- HMO: definitions and limited vs single service plans (843.002), certificate of authority (843.071), EOC to each
  Texas enrollee and not an insurance policy (1271.002/.003), no discretionary clauses (1271.057), 31st-day deemed
  approval plus 30-day extension (1271.102), complaints 5 business days / 30 calendar days / 1 business day for
  emergencies (843.252), 30-day grace and 15/15/30-day cancellation notices, 60-day rate change notice (11.506),
  individual renewal grounds (1271.307), continuation 3 months / 60 days / +2% / 9 months or 6 after COBRA
  (1271.301-.304), reside-live-or-work enrollment, plan description before selection (11.1600), specialist as PCP
  (1271.201), out-of-network emergency and referral payment at usual and customary rate, 30/45-day clean claims,
  1-hour post-stabilization, balance-billing limit, 5-business-day referral decision (1271.055, 1271.155, 1271.157,
  1271.158, 843.338).

Claims I could not confirm and left marked uncertain: none. Two nuances left as written but worth knowing: (1) the
topic presents 31 days as "the HMO rule" for newborns; a small employer plan issued by an HMO is also a "small
employer health benefit plan" under Ch. 1501, whose Sec. 1501.157 uses the 61st day. The exam is likely to key on
31 days for HMO and 61 for insured plans, so I did not change the cards. (2) The IRS eligibility page still words
the 400% exception as "2021 and 2022" only; the 2026 cap status relies on that page plus KFF.

Verdict, txhealth: publish after the listed fixes (fixes applied in the file). The course page was not rebuilt by
this review; run `python3 build/build.py courses/tx_lah` after all batches finish.
