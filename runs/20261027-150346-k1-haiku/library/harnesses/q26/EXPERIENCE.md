# q26

- adopted: `agg1`
- components: 0 skills; 3,822 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, open the primary 10-K with parse_html_page then retrieve_information, cite only opened documents, plain text with no citation markup, no empty-query searches)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. Snippets and third-party reproductions (Stocklight, Statista, stockdividendscreener) are leads only. The 10-K must be parsed and the sentence retrieved from it. Only opened documents may be cited, and the answer is plain text. dom1 and agg1 added an explicit "third-party reproductions are not sources" line. inv1 and agg1 added a parts-sum-to-total check and a rounding note.
observed: base1 made a null-query web_search and a second search, opened nothing, and answered in 2 turns from a Stocklight snippet. It listed the unopened SEC 10-K and two third-party pages as sources and leaked raw <cite index> markup. inv1, dom1 and agg1 each parsed the 10-K in turn 1, ran one retrieve_information and got the sentence "approximately 228,000 ... 126,000 in the U.S. and 102,000 internationally". None leaked markup, none sent an empty query, and each listed only the opened 10-K. The figures and the 44.74% result were identical to base1's. The gain is in verification and sourcing, not the number. Every edited run also carried a task-fact lead with the 10-K URL, so the rules and the lead cannot be separated. Each candidate is one rollout.
verdict: confounded

component: tool_guidance.md (task-fact lead: 10-K URL and snippet-derived 228,000/126,000/102,000, labelled "re-confirm")
candidates: inv1, dom1, agg1
change: Gave the verified FY2024 10-K URL and the Human Capital location. The headcount figures were marked as snippet-derived and to be re-confirmed in the opened text.
observed: All three went straight to parse_html_page in turn 1 and skipped discovery search. The retrieved text matched the lead, so no figure changed. They finished in 3 to 4 turns, against base1's 2 turns, which skipped the filing. The lead saves discovery but has no transfer value beyond this task.
verdict: no observed effect

component: tool_guidance.md (headcount-specific line: Item 1 Human Capital, "internationally" treated as non-U.S. and said so, rounding makes the share approximate)
candidates: dom1, agg1
change: Added the location of the headcount disclosure and a wording-match rule (full-time, the date named). Also added a note that the filing's rounding makes the percentage approximate.
observed: dom1's and agg1's answers state that "internationally" is the non-U.S. group and that the figures are rounded. inv1, which had only the rounding note, also states that the figures are approximate. base1 also noted the "internationally" wording. The line produced no change in the figure and no clear behavior difference beyond phrasing.
verdict: no observed effect

component: systemprompt.md / LongTermMEMORY.md / guardrails.md / skills
candidates: none
change: Left unchanged in every candidate. No skill was added.
observed: Nothing to observe. All three edited runs finished in 3 to 4 turns without a skill.
verdict: no observed effect

## Transferable lesson
- **cue**: A simple lookup-and-ratio question whose inputs sit in one sentence of a single 10-K (for example a headcount split in Human Capital). The base run answers from a snippet of a third-party reproduction of the filing. It lists the unopened SEC filing as a source and leaks citation markup.
- **lesson**: In tool_guidance.md, state that a snippet or third-party reproduction of a filing is a lead only. Require parse_html_page on the primary filing and one targeted retrieve_information call that quotes the sentence. Allow only opened documents as sources, and require plain text with no citation markup and no empty-query searches. No skill is needed, since this takes 3 to 4 turns in always-on guidance.
- **evidence**: The general-rules row. base1 searched twice, opened nothing, cited unopened sources and leaked <cite> markup. inv1, dom1 and agg1 each parsed the 10-K, quoted the sentence and cited only that filing, with no markup. The figure was the same in all four runs, so the contrast is in verification and sourcing, not accuracy.
- **confidence**: low. One rollout per candidate, a task-fact lead with the filing URL in every edited run, and an identical numeric answer, so the effect of the rules alone is not isolated.
