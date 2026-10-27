# q37

- adopted: `agg1`
- components: 0 skills; 4,273 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: CIK not ticker, no empty or null queries, snippet is a lead, cite only opened documents, plain text with no citation markup)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. edgar_search takes a numeric CIK, so a ticker is not valid. web_search is never sent an empty query. Search snippets are leads only. Sources may be listed only if opened and retrieved from. The final answer is plain text.
observed: base1 hit "Unknown ticker 'WBD'" on edgar_search in turn 1 and issued a null-query web_search. It listed Financial_Report.xlsx and the FY2022 10-K as sources without opening them. It took 6 turns. inv1, dom1 and agg1 each parsed the 10-K in turn 1, made no failed or empty calls, and listed only the opened 10-K. They finished in 3-4 turns. The stated figure was $4.7B in every run. Every edited run also carried the task-fact lead with the 10-K URL, so the rules cannot be separated from the lead. Each candidate is one rollout.
verdict: confounded

component: tool_guidance.md (program-to-date rule: use the company's stated cumulative total, treat the annual sum as a cross-check, flag any gap)
candidates: inv1, dom1, agg1
change: Told the agent to look first for the company's own "incurred as of" sentence in MD&A or the restructuring note. The sum of annual income-statement lines is a cross-check only. If the two differ, report the stated total and say the filing does not reconcile them. agg1 and dom1 added a scope check against look-alike figures such as cash expenditures and impairment lines.
observed: base1 found the same mismatch itself (3,757+585+447 = 4,789 vs the stated 4.7B). It spent a third retrieval on it and made the gap a late caveat. All three edited runs retrieved the stated sentence and the annual lines in a single query and gave $4.7B with the $4,789M sum as a labelled cross-check. dom1 explained the gap as a broader income-statement caption. That is an inference from the filing text, which dom1's own retrieval did not support. agg1 additionally noted that Note 6 gives no cumulative total. The headline figure was the same as base1's, so the effect was on efficiency and framing and not on the number. The lead also stated the answer.
verdict: confounded

component: tool_guidance.md (embedded task-fact lead: WBD 10-K URL, $4.1-5.3B range, $4.7B incurred, annual lines)
candidates: inv1, dom1, agg1
change: Each embedded the verified 10-K URL and the key figures, labelled "re-confirm in the text".
observed: All three skipped discovery search and parsed the 10-K in turn 1. Each retrieved text matching the lead. Turn counts were 3 or 4, against 6 for base1. The lead saved turns and did not change any figure. Because it carries the answer, it is task-specific and does not transfer.
verdict: no observed effect

component: LongTermMEMORY.md, guardrails.md, systemprompt.md, skills
candidates: none
change: No candidate edited these files, and none added a skill.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks for a program-to-date total "incurred as of" a date (merger restructuring, integration or synergy costs). The annual income-statement lines sum to a number that differs from the company's own stated cumulative figure. The base run finds both only after extra retrievals and lists unopened filings or spreadsheets as sources.
- **lesson**: In tool_guidance.md, add a program-to-date rule. Search the latest 10-K MD&A or the restructuring note for the company's own cumulative "incurred as of" sentence and report that as the answer. Show the sum of annual lines as a labelled cross-check. If the two differ, say the filing does not reconcile them and do not invent a reason. Ask for both in one retrieve_information call. Pair this with a cite-only-opened-documents rule and a CIK-not-ticker note for edgar_search.
- **evidence**: The rule rows above. base1 took 6 turns, hit the ticker error, made a null-query search and listed unopened sources. inv1, dom1 and agg1 parsed the 10-K first, retrieved the stated total and the annual lines in one query, and listed only the opened 10-K. They took 3-4 turns. All runs gave the same $4.7B, so the contrast is about efficiency, sourcing and framing and not the headline figure. The rule, the sourcing rules and the answer-bearing lead were bundled in each edited run.
- **confidence**: low. One rollout per candidate. The rules were bundled with a lead that gave the location of the answer, and the figure did not differ between base and edited runs.
