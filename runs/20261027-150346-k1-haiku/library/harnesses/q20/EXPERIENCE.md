# q20

- adopted: `agg1`
- components: 1 skill; 1,689 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1
change: Went from empty to a rule set: use edgar_search, treat snippets as leads, and open the primary document. Prefer the 10-K for full-year and prior-year comparatives, and cite only opened documents. A company-stated ratio is the headline input, so compute the delta from the stated rates and show the unrounded recompute as one labelled cross-check. Recompute before submitting and follow the prescribed answer format. It also embeds an Oracle task fact (10.9% vs 6.8%, with the 19.2%/16.3% non-GAAP distractor).
observed: base1 recomputed from dollars and headlined "Delta: 402bps". It mentioned the stated-rate 410bps only as a side note. inv1 parsed the 10-K in turn 1, made one retrieval, and headlined "Delta: 410bps" from the stated rates. It gave 402bps as a labelled cross-check and cited only the 10-K, in 3 turns. The headline flip coincides with the new rule, but the Oracle task fact in the same file also supplied the stated rates and the URL, so the rule's effect is not isolated. It is one rollout.
verdict: confounded

component: skills/effective_tax_rate_change/SKILL.md
candidates: dom1, agg1
change: Added an on-demand skill for effective-tax-rate level and change. The headline is the company-stated rates, with bps = (stated current - stated prior) x 100. The unrounded provision / pre-tax recompute is a separate labelled cross-check, and the two are not presented as equal. It warns that non-GAAP adjusted rates are a distractor, and tells the agent to check the fiscal year-end, quote the MD&A drivers, and cite only opened documents. It carries Oracle's verified figures and the 10-K URL.
observed: dom1 and agg1 both loaded the skill first, parsed the 10-K once, ran one combined retrieval, and submitted in 4 turns. Both headlined "Delta: 410bps" with 402bps as a cross-check, which base1 had reversed. Both listed only the 10-K as a source and excluded the 19.2%/16.3% non-GAAP rates. base1 had also kept only opened sources and the non-GAAP note, and used 4 turns. The skill therefore added one turn and a changed headline. The skill carried the figures and the headline rule together, so the content of the rule is not separated from the task lead. No run has the same rule without the skill other than inv1, which put it in tool_guidance.
verdict: confounded

component: systemprompt.md
candidates: dom1, agg1
change: Added one trigger line telling the agent to call load_skill with `effective_tax_rate_change` for effective-tax-rate or year-over-year change questions.
observed: Both candidates called load_skill as their first action. No skill-equipped run lacks the trigger, so its separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks for the change in a company-published ratio or rate (effective tax rate, margin, growth %) in bps or points. The filing states the rates rounded to one decimal, and recomputing from dollar amounts gives a slightly different delta.
- **lesson**: In tool_guidance.md, add a rule for this situation. The headline delta is computed from the company-stated rates at their published precision. The unrounded recompute from dollar figures is one labelled cross-check line, and the answer names which delta is the headline. Do not present both as equal answers. Put the Oracle-style task figures in a skill or a lead, not in always-on text.
- **evidence**: tool_guidance.md row and skill row. base1 headlined the unrounded 402bps and put the stated-rate 410bps in a side note. inv1 (guidance only), dom1 and agg1 (skill) all headlined 410bps with 402bps as a cross-check. All four runs retrieved the same inputs (10.9%/6.8%; 1,274/11,741; 623/9,126) and cited only the 10-K, so the contrast is in which delta was the headline. Which headline is the correct one is not shown by the record. Selection compared answers with the harnesses hidden and gave no verdict on this point.
- **confidence**: low. One rollout per candidate, with the rule and the task figures bundled in the same file in every edited run. The record shows a consistent behavior shift but not that it is the better answer.
