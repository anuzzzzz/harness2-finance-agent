# q39

- adopted: `agg1`
- components: 1 skill; 3,344 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, dom1, agg1
change: Went from empty to a sourcing rule set. A snippet is a lead, not evidence. Open the primary document with parse_html_page, then retrieve_information. Cite only opened documents. Write plain text with no citation markup. Never send an empty query. inv1 and agg1 added a rule to read the outlook of the LATEST release on or before the as-of date, not an older deck, and to ignore later releases. inv1 also embedded a Delta lead block. dom1 kept a three-bullet version.
observed: base1 ran two searches and never parsed anything. It listed the January 2024 deck as the guidance set, hedged that fuel price and FCF/leverage "may not match", and listed unopened sources. inv1, dom1 and agg1 each parsed the January 2025 8-K EX-99.1 and listed only that document as a source. All three returned the same 1Q25 table (revenue +7-9%, operating margin 6-8%, EPS $0.70-1.00) and the FY25 table (EPS growth >10%, FCF >$4B, gross leverage <=2x). All three said fuel and capex were not guided numerically. base1 had presented fuel, capacity and CASM-ex as guided items. The edits were bundled with skills and leads in dom1 and agg1, and each candidate is one rollout.
verdict: confounded

component: skills/guidance_metrics_inventory/SKILL.md and the trigger line in systemprompt.md
candidates: dom1, agg1
change: Added an on-demand skill for "what metrics does the company guide on" questions. It covers finding the latest release, asking for every guided line, grouping into quarterly, full-year and long-term, recording unit and basis, and an answer contract. agg1 added a narrative-only group and a rule to re-query a figure that appears in one retrieval but not in the table. It also dropped dom1's "do not claim not guided" wording in favour of "not found in the opened documents". A short Delta lead was embedded.
observed: Both loaded the skill first. dom1 took 5 turns, agg1 took 7, and inv1 (no skill) took 3 with the same core table. dom1 labelled the ">$7.35" EPS level "unconfirmed" after one extraction missed it from the table. agg1 re-queried (turns 5 and 6), confirmed $7.35, pre-tax income >$6B and CASM-ex low-single-digit from the CEO and CFO quotes, and reported them as narrative-only. inv1 also reported them without the skill. The skill therefore added turns, and the only visible gain was the grouping and the re-query rule. Whether that rule drove agg1's confirmation is not isolated, since inv1 got the same facts unaided.
verdict: confounded

component: systemprompt.md (trigger line)
candidates: dom1, agg1
change: Added one sentence telling the agent to call load_skill with `guidance_metrics_inventory`.
observed: Both called load_skill as their first action. No skill-equipped run lacks the trigger, so its separate effect is not shown.
verdict: no observed effect

component: tool_guidance.md (embedded Delta lead block with the 8-K URL)
candidates: inv1
change: Embedded the Q4 2024 8-K EX-99.1 URL, the January 2024 deck URL and a warning that the base run used the old deck.
observed: inv1 skipped discovery and parsed the 8-K in turn 1, finishing in 3 turns. agg1 used edgar_search and found the same URL. The answers had the same core content. The lead saved a turn and changed no figures.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: An open-ended "what metrics does company X guide on / provide outlook for" question with an as-of date. The base run answers from search snippets and an older year's supplemental deck, and mixes guidance items across years.
- **lesson**: In tool_guidance.md, say that an inventory of guided metrics must be built from the outlook section of the latest earnings release dated on or before the as-of date. Open it with parse_html_page, retrieve every guided line with its period, unit and basis, and list only items seen in that opened text. Items from an older deck or from snippets may appear only if they are labelled with their source document. Items given only in management quotes go in a separate narrative-only group. Items not found must be reported as "not found in the opened document", not as asserted guidance.
- **evidence**: tool_guidance.md row. base1 opened nothing and presented the 2024 deck's fuel, capacity and CASM-ex as the guided set. inv1, dom1 and agg1 all opened the January 2025 8-K, gave the same table-based lists, and cited only that document. The skill rows show that inv1 with no skill matched the skill runs, so the procedure fits in always-on text.
- **confidence**: low. One rollout per candidate, the rules were bundled with skills and leads, and the runs agree on content, so the evidence shows sourcing behavior and period discipline, not accuracy.
