# Review: batch texas_a (topics txcommon, txlife)

Reviewed 2026-11-23. Statutes read on tcss.legis.texas.gov through WebFetch, rules on Cornell LII, plus TDI pages. Both files pass `tests/check_topic.py` after the edits.

## txlife (Texas law: life insurance)

| Concept | What was wrong | What it says now | Source |
|---|---|---|---|
| Policy summary, buyer's guide and free look | The Texas annuity free look was missing. The tab gave only the 15-day disclosure free look, and a card taught "15 days" as the annuity answer. Insurance Code Sec. 1116.002 requires at least 20 days after delivery for every individually solicited annuity (since 2011). TDI's annuity guide also says 20 days. | Model gives the Sec. 1116.002 rule: 20 days from delivery, an unconditional refund of premiums and fees for fixed annuities, and cash surrender value plus fees for variable and MGA contracts. The 15-day rule is kept and described as running at the same time. New trap. New card on the 20-day rule. The 15-day card now names both rules. The summary sentence and the example were rewritten to match. | https://tcss.legis.texas.gov/resources/IN/htm/IN.1116.htm ; https://tdi.texas.gov/pubs/consumer/cb078.html |
| Same | The annuity disclosure rules were cited as 28 TAC Secs. 3.9708 and 3.9711 (Ch. 3 Subchapter PP). The current rules are Secs. 4.2308 and 4.2311 in Ch. 4 Subchapter W, effective 1/24/2024. | Cites Secs. 4.2308 and 4.2311 and notes that older material cites 3.9708. | https://www.law.cornell.edu/regulations/texas/28-Tex-Admin-Code-SS-4-2308 ; https://www.law.cornell.edu/regulations/texas/28-Tex-Admin-Code-SS-4-2311 |
| Same | Ordinary life free look: the tab cited TDI's "10 to 20 days" and said the controlling statute was unconfirmed. | Now says that Ch. 1101 and TDI's individual life checklist (LAC006) set no free look for an ordinary, non-replacement policy, that TDI's guide says 10 to 20 days, and that no single Texas number was confirmed. Kept off the cards. | IN.1101 ; https://agate.tdi.texas.gov/forms/lhlifehealth/lac006.pdf ; https://tdi.texas.gov/pubs/consumer/cb018.html |
| Map of Texas life-only law | The map named the annuity rule location as 28 TAC Ch. 3 Subchapter PP, and its number anchors left out the annuity free look. | Names 28 TAC Ch. 4 Subchapter W and Insurance Code Ch. 1116, and adds a "20 days (annuity free look)" anchor. | as above |
| Grace, reinstatement and policy loans | Reinstatement was sourced "per TDI's checklist", not the rule itself. The death-during-grace deduction was attributed to TDI's guide as if it always applied. | Taken from the rule text of 28 TAC 4.611: reinstatement within three years of default, or longer at the insurer's option, if the policy was not surrendered and canceled, with evidence of insurability and overdue premiums plus interest. Grace taken from 28 TAC 4.602 and Sec. 1101.005: at least one month, or 31 days if stated in days, with stated interest allowed. The policy may deduct the overdue premium, and the example now says "if the policy allows the deduction". The unsourced line "most companies allow five years" was cut to stay under the word limit. | https://www.law.cornell.edu/regulations/texas/28-Tex-Admin-Code-SS-4-611 ; https://www.law.cornell.edu/regulations/texas/28-Tex-Admin-Code-SS-4-602 ; IN.1101 |
| Claims, maturity and prohibited provisions | The suicide trap said a Texas cap was "not confirmed". | Now says that neither Sec. 1101.055 nor TDI's life checklist sets a time limit on the suicide exclusion. The rule is still off the cards. | IN.1101 ; LAC006 |
| note | Contained outline-code lettering. | Rewritten in plain language with the check date. | n/a |
| sources | Included a link to the blocked statutes.capitol site, the old Sec. 3.9711 and a 2010 adoption order. | Those three were replaced with Ch. 1116, 28 TAC 4.602, 4.611, 4.2308 and 4.2311, and TDI cb078 (23 sources). | n/a |

Confirmed unchanged against the official text:
- Ch. 1101: entire contract, two-year incontestability, two-month claim deadline, three-year loans, backdating, two-year suit floor, one-year preliminary term, 90-day notice.
- Ch. 1110 loan rates: 10% fixed; adjustable up to the lesser of 15% or the Moody's/cash value rate plus 1%; reset every 12 months; 30-day notice.
- Ch. 1103: interest runs from proof of loss, slayer rule, discharge on payment, insurable interest for funeral businesses and caregivers.
- Ch. 1105: 60-day election, three years (five for industrial), six-month deferral, term exemption, 20-year table.
- Ch. 1111 accelerated benefits: term only, two-year terminal illness, reduces the death benefit and the convertible amount.
- Ch. 1131 group sizes and participation, 31-day grace and conversion, $250, five years and $2,000, dependents under 25, assignment.
- Ch. 1153: 10 years, 15 days, 45 days, $3, creditor not the claim representative.
- Ch. 1114: 5 business days, 30-day return, 4 months before to 13 months after, five-year term exemption, 30 business days for annuities (2025).
- 28 TAC 21.2209: Revised Illustration, three-year retention.

### Could not confirm (left marked uncertain, not on cards)
- A Texas free look number for an ordinary, non-replacement individual life policy. TDI's guides say "at least 10 to 20 days", but no statute or rule was found. A standard exam may expect "10 days". Consider adding to the Exam angle that the national answer is 10 days, after a human check of current TDI exam guidance.
- A Texas rule requiring a life insurance buyer's guide or policy summary at delivery, apart from the Sec. 1114.003 replacement definition.
- The Texas time limit on the suicide exclusion. The statute has none; TDI's guide says companies usually use two years.
- Not edited (word limit): the replacement right to return in Sec. 1114.053(e) refunds cash value plus fees for variable and MVA contracts. The duties concept says "full refund". That is correct for fixed products.

**Verdict: publish after the listed fixes (applied).**

## txcommon (Texas law: rules for both lines)

| Concept | What was wrong | What it says now | Source |
|---|---|---|---|
| Continuing education | Said "I could not confirm a carryover rule". 28 TAC 19.1003(a)(2)(B) bars carrying excess hours forward. Under (a)(2)(C), hours made up late under Sec. 4004.055 do not count for the current period. | Model states both rules. The nonresident card (its rule is still in the Model) was replaced with a carryover scenario card. | https://www.law.cornell.edu/regulations/texas/28-Tex-Admin-Code-SS-19-1003 ; https://tdi.texas.gov/agent/agent-questions.html#continuingEducation |
| Appointments, notices to TDI and records | No error. The notice timing had no card. | New card: under Sec. 4001.252, an individual reports address changes, felony convictions and regulatory actions monthly, and TDI's license page asks for contact changes immediately. (Agencies report within 30 days; already in the Model.) | https://tcss.legis.texas.gov/resources/IN/htm/IN.4001.htm ; https://tdi.texas.gov/agent/life-agent-manage.html |
| note | Contained outline-code lettering. | Rewritten in plain language with the check date. | n/a |
| sources | 25 sources, at the cap. | Dropped Ch. 801 and Ch. 885 (basic definitions; sections are still named in the text). Added 28 TAC 19.1003 and the TDI CE FAQ. | n/a |

Confirmed unchanged against the official text:
- Commissioner: two-year term ending Feb. 1, five years' experience.
- Chs. 83 and 84: 60 days, final on day 61, $25,000 penalty; 20 days and 30 days.
- Ch. 4001:
  - license: age 18, exam passed within 12 months, the 25% premium rule;
  - agency: $250,000 E&O or $25,000 bond;
  - temporary license: 180 days, 40/10 training hours within 30 days, 70%/50% over two quarters, 500 a year;
  - appointments: 30 days;
  - notices: monthly reports, 30 days for agencies.
- Ch. 4003: birthday expiration, 30-day notice, 90 days and one year, half fee.
- Ch. 4004: 24 hours with 3 of ethics, 50% classroom, 4 association hours, 90 days, 20-year exemption, 8 annuity hours, 8+4 Medicare hours with no exemption.
- TDI fees: $50 application, $150 temporary, $50 renewal, $25 late fee, $50 per hour CE fine with a $500 cap.
- Ch. 4005: 5-year bar and its exclusions, third-degree felony, $1,000 or six months.
- Ch. 1702 (HB 2221, eff. 9/1/2025): $25 items, the commissioner's gift amount.
- Ch. 701: 30 days, immunity, 15 + 10 days.
- Ch. 463: $300k/$100k/$250k/$500k/$300k/$200k limits, $300k aggregate, 2% assessment cap, exclusions.

### Could not confirm (left marked uncertain)
- Ethics hours: 28 TAC 19.1003(a)(1)(B), as shown on Cornell (amended 2023), still says two hours of ethics. Insurance Code Sec. 4004.054 and TDI's CE page say three. The tab keeps three, which the statute controls, but the rule text should be rechecked on the SOS site.
- The adopted Chapter 1702 gift limit amount (already marked uncertain in the tab).
- A general retention period for agent sales records (already marked uncertain).

**Verdict: publish (fixes applied).**
