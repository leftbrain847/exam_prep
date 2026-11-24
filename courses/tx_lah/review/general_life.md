# Review: general_life batch (lifepolicies, lifeprovisions, underwriting, retirement)

Reviewed 2026-11-23. I read every card, summary, Model, Traps and Example in all four topics and checked them against
standard licensing-exam answers and against the Texas tabs (txlife, txcommon; not edited). I opened these official
sources this session: IRS Notice 2026-66 (n-26-66.pdf), SSA 2026 COLA fact sheet, IRS Publication 15-B, 26 USC 7702A
(Cornell LII) and Texas Insurance Code Ch. 1103 (tcss.legis.texas.gov). All four files pass check_topic.py.

## lifepolicies

| Concept | What was wrong | What it says now | Source |
|---|---|---|---|
| (note) | Outline codes in the note | Plain-language scope plus "last checked Nov 23, 2026" | n/a |

Checked and correct, no change: ordinary, limited-pay and single-premium whole life (incl. MEC link), UL Options A/B,
VWL and VUL (separate account, prospectus, securities registration), interest-sensitive WL, indexed life (cap,
participation, floor math), term types, renewal and conversion (attained vs original age), annuity structure,
fixed/variable (AIR, accumulation and annuity units), indexed annuity math, payout options, joint vs survivorship
premium ranking.

## lifeprovisions

| Concept | What was wrong | What it says now | Source |
|---|---|---|---|
| (note) | Outline codes in the note | Plain-language scope plus "last checked Nov 23, 2026" | n/a |

Checked and correct, no change: nonforfeiture options (extended term as automatic option, 60-day election, cash value
after three full years, six-month deferral; all match txlife Ch. 1105 concept), settlement options (fixed period vs
fixed amount, interest taxable), dividend options (PUA, one-year term, interest taxable), consideration (application
plus first premium), beneficiary rules (common disaster, per capita/per stirpes, irrevocable consent), assignments,
grace period, APL, reinstatement (3 years, matches txlife), loans (worked numbers correct), incontestability and
suicide, misstatement of age, riders, exclusions (status vs results).

## underwriting

| Concept | What was wrong | What it says now | Source |
|---|---|---|---|
| Insurable interest (Traps) | Said a stranger cannot buy a policy on you "even with your consent, unless the law allows", which conflicts with Texas, where an adult may consent in writing to a third-party purchase | States the general rule, then that Texas lets an adult consent in writing to a third party buying a policy on his life (Sec. 1103.056), with a pointer to the Texas law tab | https://tcss.legis.texas.gov/resources/IN/htm/IN.1103.htm |
| (note) | Outline codes in the note | Plain-language scope plus "last checked Nov 23, 2026" | n/a |

Checked and correct, no change: conditional receipt (later of application or exam, insurable as applied for),
binding and approval receipts, signatures and corrections, waiver for incomplete applications, representations vs
warranties, replacement, twisting and churning, HIPAA authorization, GLBA notices and opt-out, AML covered products,
$5,000 SAR, Form 8300, FCRA 3-day and 5-day notices, 60-day free report, 7/10-year limits, MIB, risk classes and table
rating math, constructive delivery, contract elements, offer and acceptance, adhesion, aleatory, unilateral,
conditional.

## retirement

| Concept | What was wrong | What it says now | Source |
|---|---|---|---|
| (note) | Outline codes in the note | Plain-language scope, says which 2026/2027 figures were checked where and when | n/a |
| (sources) | Section 79 spouse $2,000 de minimis and FICA rule had no IRS fringe-benefit source | Added IRS Publication 15-B | https://www.irs.gov/publications/p15b |

Verified, no change needed:
- 2026 and 2027 plan limits all match IRS Notice 2026-66: 415(c) $72,000 to $75,000; DB $290,000 to $300,000;
  compensation $360,000 to $375,000; deferral $24,500 to $25,500; catch-up $8,000 to $8,500; 60-63 catch-up $11,250;
  SIMPLE $17,000 to $17,500 (catch-up $4,000); IRA $7,500 and catch-up $1,100 (unchanged for 2027); Roth catch-up wage
  threshold $150,000 for 2026; Roth phase-outs $153,000-$168,000 single and $242,000-$252,000 joint; covered single
  deduction phase-out $81,000-$91,000. (https://www.irs.gov/pub/irs-drop/n-26-66.pdf)
- SSA 2026: COLA 2.8%, taxable maximum $184,500, credit $1,890, maximum benefit at FRA $4,152.
  (https://www.ssa.gov/cola/factsheets/2026.html)
- Section 79: $50,000 exclusion, excess subject to Social Security and Medicare tax, reduced by employee payments,
  $2,000 spouse/dependent de minimis, key employee rule. (IRS Pub 15-B)
- MEC: June 21, 1988; 60-day return of excess premium with interest; benefit-reduction retest. (26 USC 7702A)
- Worked numbers checked: MEC loan example, surrender gain, buy-sell policy counts, needs analysis, Section 79 example,
  indirect rollover example, Social Security blackout example.

## Cross-tab consistency (checked against txlife and txcommon)
Grace period, reinstatement (3 years), incontestability (general tab notes the general exceptions and points to the
Texas tab; Texas allows only nonpayment of premium), nonforfeiture (60 days, 3 years, 6-month deferral), group life
conversion (31 days, attained age, coverage during the window), accelerated benefits (24 months / two years),
misstatement of age, free look (10 days general, Texas tab) and loans all agree. The only conflict found was the
insurable-interest consent point, fixed above.

## Claims I could not confirm and left as uncertain
None new. The writers' own uncertainty markers (Texas suicide cap, Texas ordinary-life free-look statute) are in
txlife, which I did not edit.

## Other notes (not changed: style, not accuracy)
- Several cards are phrased as yes/no questions, against WRITING.md, although their answers are correct and explained:
  lifepolicies (VUL "Can the policy still lapse?"), retirement ("Is this a viatical settlement?", "Can he contribute to an IRA?", "Is this allowed under Section 1035?",
  "Is imputed income ... subject to FICA?", "Does the 10% additional tax apply?").
- lifeprovisions sources include statutes.capitol.texas.gov (blocked here) and an Illinois rule; these are weaker
  sources but within the 8-25 range, so I left them.

## Verdicts
- lifepolicies: publish.
- lifeprovisions: publish.
- underwriting: publish after the listed fix (applied).
- retirement: publish. Recheck 2027 figures in January 2027 when they take effect.
