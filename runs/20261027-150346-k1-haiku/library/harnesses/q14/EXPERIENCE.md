# q14

- adopted: `agg1`
- components: 1 skill; 3,345 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. inv1 and agg1 added: use edgar_search with company filters; a snippet is a lead; name the capex lines used and show the alternate definition as a labelled cross-check; compute every year unrounded; flag one-off distortions; cite only opened documents; submit once verified. inv1 also embedded the Zillow figures and URLs here. agg1 added "recompute each division". dom1 added a shorter five-bullet version covering recast comparatives and cite-only-opened.
observed: base1 parsed the FY2024 and FY2023 10-Ks but listed the FY2022 10-K as a source. It had never opened that filing. It chose PP&E plus intangibles as capex and showed no alternate. All three edited runs parsed only the FY2024 10-K and cited only it. agg1 and dom1 said explicitly that prior-year figures came from comparative columns. All three showed the PP&E-only alternate. inv1 had a rounding slip (257/2,236 = 11.494%, reported as 11.50%). agg1 and dom1 reported 11.49%, and agg1 carried the recompute rule. Each candidate is one rollout and the skill was present in dom1 and agg1, so the cite-only-opened behaviour cannot be assigned to the guidance alone. dom1 carried it in both guidance and skill.
verdict: confounded

component: skills/fcf_margin_trend/SKILL.md (plus the trigger line in systemprompt.md)
candidates: dom1, agg1
change: Added an on-demand skill for FCF and margin trends. It sets the capex definition and reconciles to the MD&A capital-spending total. It requires a labelled PP&E-only alternate. It checks that continuing-operations revenue and cash-flow scope match. It flags and quantifies one-offs (margin above 100%). It requires unrounded inputs and a fixed answer contract. It carries verified Zillow figures and the three 10-K URLs, marked "re-confirm". agg1 trimmed it and added "recompute each division". systemprompt.md gained one trigger line.
observed: Both runs called load_skill first and then used edgar_search once and parse_html_page once. They made one combined retrieval and submitted, in 4 turns. The answers reached the same figures as base1 and inv1 (222.88%, 9.72%, 11.49%). The answers added the quantified 3,904 inventory driver and the continuing-operations versus discontinued cash-flow mismatch note. They also gave year-over-year and end-to-end percentage-point changes. inv1 had the 3,904 driver and the alternate series without the skill, but not the basis-mismatch note or the point changes. The skill therefore plausibly added the basis note and the point-change table, but the leads also carried the figures. The skill cost one turn and changed no number.
verdict: confounded

component: systemprompt.md
candidates: dom1, agg1
change: Added one sentence telling the agent to call load_skill with `fcf_margin_trend` for FCF, FCF margin or multi-year cash-flow ratio questions.
observed: Both candidates called load_skill as their first action. No run has the skill without the trigger, so the trigger's separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A multi-year ratio or trend question (for example FCF margin) is answerable from one filing's three-year comparative columns. The base run opened the latest two or three 10-Ks and listed a filing it never opened as a source. It also picked one ambiguous input definition (capex) without a labelled alternate, and left a distorted year unquantified.
- **lesson**: In tool_guidance.md, add a rule that a three-year trend is read from the latest 10-K's comparative columns. A source may be listed only if a figure was retrieved from that document, and prior-year figures taken from comparative columns must be described as such. Add a rule that the headline uses the definition the company's MD&A cites. A labelled alternate for any ambiguous input (such as PP&E-only capex) must appear as a one-line cross-check. Add a rule that any year distorted by a one-off must be flagged and its driver quantified from retrieved text.
- **evidence**: Edit row for tool_guidance.md. base1 listed the unopened FY2022 10-K and showed no capex alternate. inv1, dom1 and agg1 all cited only the FY2024 10-K they had parsed and showed the PP&E-only alternate. The skill row also shows the basis-mismatch note and the quantified distortion. The numbers matched across every run, so the contrast is in sourcing and framing, not in accuracy.
- **confidence**: low. One rollout per candidate. The guidance and the skill were never varied independently, so the tool_guidance carrier is not isolated, and the figures did not change.
