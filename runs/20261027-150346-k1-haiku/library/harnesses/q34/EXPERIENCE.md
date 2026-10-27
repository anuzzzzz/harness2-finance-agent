# q34

- adopted: `agg1`
- components: 0 skills; 3,285 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (snippet-is-a-lead, open the primary document, cite only opened documents, plain text, no empty-query search)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. The 10-K must be opened with parse_html_page and confirmed with retrieve_information. Only opened documents may be cited. The answer is plain text, and no null-query searches. inv1 and agg1 added "Financial_Report.xlsx in search results is not a parsed source". dom1 added the same rules with a task-fact block.
observed: base1 never called parse_html_page or retrieve_information. It took the figures from search results, ran a null-query web_search, and listed Financial_Report.xlsx and the 10-K as sources without opening either. inv1, dom1 and agg1 each parsed the 10-K and retrieved the Note 3 disaggregation table, and each cited only the 10-K. inv1 and dom1 went straight to parse_html_page in turn 1. inv1 and dom1 also carried the 10-K URL in tool_guidance, so the direct route is not isolated from the rules. agg1 had no URL, ran edgar_search, then parsed. The figures were the same in every run (337,394 / 1,669,626, with a printed 20%). The effect was on verification and sourcing honesty, not on the numbers. Each candidate is one rollout.
verdict: confounded

component: tool_guidance.md (share-of-revenue rule: lead with the company-stated percentage, show the unrounded recomputation as a labelled cross-check; use the 10-K revenue note and the same-year total)
candidates: inv1, agg1 (dom1 had a variant that put the computed value first)
change: Told the agent to retrieve both the printed percentage and the dollar amounts. The stated 20% is the headline. 20.21% is a cross-check. dom1's variant led with the computed 20.21%, with 20% labelled as printed.
observed: base1 headlined 20.21% and mentioned the rounded 20% in a trailing sentence. inv1 and agg1 headlined 20% and showed 20.21% as a cross-check. dom1 headlined about 20.21% and gave the printed 20% alongside. The three edited runs therefore differ in which number leads. The record contains nothing that shows which ordering is better. The rule changed presentation, not the retrieved data.
verdict: confounded

component: tool_guidance.md (task-fact lead with the Cloudflare 10-K URL and figures)
candidates: inv1, dom1
change: Embedded the 10-K URL and the figures, labelled "re-confirm in the text". agg1 omitted it.
observed: inv1 and dom1 skipped discovery and parsed the 10-K in turn 1, finishing in 3 and 4 turns. agg1 used edgar_search first and also finished in 4 turns. All three retrieved the numbers from the opened text. The lead saved at most one search call and did not change the outcome. A lead tied to one task has no reuse value.
verdict: no observed effect

component: skills/, systemprompt.md, LongTermMEMORY.md, guardrails.md
candidates: none changed them
change: Left unchanged. No skill was added in any candidate.
observed: The task was a single retrieval from one document, and every edited run finished without a skill.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks for a share or mix percentage (channel partners, a customer type, a segment or region) that the 10-K prints in a revenue note, and the base run answers from search snippets or XBRL spreadsheet results. It cites the 10-K and a Financial_Report.xlsx it never opened, and it issues a null-query search.
- **lesson**: In tool_guidance.md, state that a snippet or a spreadsheet link seen only in search results is not a source. Require parse_html_page on the 10-K, then a retrieve_information call for the revenue-note table (amount, same-year total, printed percentage). Require citing only documents actually parsed, and plain-text output. Decide explicitly which number leads when the printed percentage is rounded and the recomputed one differs, and show the other as a labelled cross-check. Do not add a skill, since this is one retrieval from one document.
- **evidence**: The tool_guidance rows. base1 never opened a document and listed the unopened 10-K and Financial_Report.xlsx as sources. inv1, dom1 and agg1 each parsed the 10-K once, retrieved the Note 3 table, and listed only the 10-K. The figures were identical in all four runs (20% printed, 20.21% recomputed), so the contrast is in verification and sourcing, not accuracy. Which number should lead is unresolved, since the candidates split.
- **confidence**: low. One rollout per candidate, the rules and the URL lead were bundled in inv1 and dom1, and the final figures did not change.
