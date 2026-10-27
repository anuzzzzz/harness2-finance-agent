# q45

- adopted: `agg1`
- components: 0 skills; 3,538 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, agg1 (dom1 carried a shorter two-bullet version)
change: Went from empty to a rule set. A search snippet is a lead, not evidence. Open the primary filing and confirm each figure, period and unit with retrieve_information. Prefer the 10-K for a full-year figure and cross-check any quarterly sum against an annual figure. Cite only documents actually opened and retrieved from. Both versions also embedded task facts (the 8-K URL, the 10-K URL, 295+382+362+368 = 1,407). agg1 added a "re-confirm in the text" label and the $1,424M equity-credit distractor. dom1's version kept only the verify-and-cite-only-opened-documents bullets.
observed: base1 got $1,407M from the 8-K via two retrievals, then listed three 10-Qs and the 10-K as sources and attributed Q1-Q3 figures to the 10-Qs. It had opened none of them. inv1 and agg1 parsed the 10-K, retrieved the annual reconciliation row (1,120 / 1,407), and cross-checked it against the 8-K quarterly sum. Both cited only the two documents they had opened. dom1 also listed only opened documents. The 10-K pointer in the guidance may have prompted the early 10-K fetch, so the cause is not isolated. agg1's answer said the 10-K has no quarterly breakdown and put the full-year total on the 8-K. Those claims were extracted by retrieve_information from the same text, and one retrieval (8-K) said the reconciliation had no annual column. The figure was $1,407M in every run, so the effect was on sourcing honesty and verification, not the number.
verdict: confounded

component: skills/nongaap_addback_lookup/SKILL.md (plus trigger line in systemprompt.md)
candidates: dom1
change: Added an on-demand skill for pulling an annual add-back from a non-GAAP reconciliation. It names the 10-K MD&A, the SBC footnote and the cash-flow statement as controlling sources, says to sum quarters only if there is no annual column, keeps the add-back separate from other SBC measures, and says to cite only documents opened. It carries a verified lead ($1,407M). The trigger line was added to systemprompt.md.
observed: dom1 loaded the skill first, parsed both the 8-K and the 10-K, ran one combined retrieval and submitted in 4 turns. The answer was correct, cited only opened documents, and excluded the $1,424M equity credit. The 3-turn runs without the skill (inv1, agg1) reached the same number with the same sourcing hygiene, so the skill added a turn and nothing visible. The skill and the tool_guidance bullet were both present in dom1, so the sourcing behavior cannot be assigned to either.
verdict: no observed effect

component: systemprompt.md
candidates: dom1
change: Added one sentence telling the agent to call load_skill with `nongaap_addback_lookup` for non-GAAP add-back questions.
observed: dom1 called load_skill as its first action. There is no skill-equipped run without the trigger, so its separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks for one full-year line from a non-GAAP reconciliation or footnote. The earnings-release exhibit gives only quarterly columns, so the agent sums quarters from the 8-K. The base run then lists other filings (10-Qs, the 10-K) as sources that it never opened.
- **lesson**: In tool_guidance.md, state that a source may be listed only if its figure was retrieved from that parsed document. For a full-year figure, require opening the 10-K (or another annual document) and cross-checking it against any quarterly sum. Then the final answer cites only the documents actually read.
- **evidence**: The tool_guidance.md row. base1 submitted $1,407M but attributed Q1-Q3 figures to three unopened 10-Qs. inv1, agg1 and dom1, which carried a cite-only-opened rule, listed only the 8-K and the 10-K they had parsed. inv1 and agg1 also retrieved the 10-K's annual row and matched it to the quarterly sum. The number was identical in all four runs, so the evidence is about sourcing honesty and verification, not accuracy.
- **confidence**: low. Each candidate is a single rollout. The tool_guidance bullets and the skill (dom1) were not separated. The only contrast is a base-run sourcing flaw against three runs that carried a rule against it.
