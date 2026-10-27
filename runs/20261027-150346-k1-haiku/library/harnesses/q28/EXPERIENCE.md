# q28

- adopted: `agg1`
- components: 0 skills; 4,003 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, open the 10-K with parse_html_page, retrieve the whole table, re-sum against the printed total, cite only opened documents, plain text, no empty-query searches)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. The 10-K must be opened and the full obligations table (every row, every column, printed total) retrieved. Rows are re-added against the printed total. Only opened documents may be listed as sources. The answer is plain text with no citation markup. Empty-query web_search is forbidden.
observed: base1 ran an edgar_search and a null-query web_search, then submitted from snippets. It leaked <cite index> markup and listed an unopened Financial_Report.xlsx and a third-party PDF as sources. inv1, dom1 and agg1 each parsed the 10-K in turn 1 or 2, retrieved the table, verified that the sums match the printed totals, and listed only the 10-K. None leaked markup. All reached the same figure as base1 ($14,426,266K, about $14.43B), so the effect was on verification and sourcing, not the number. Every edited run also carried the URL lead, so rules and lead cannot be separated. There is one rollout per candidate.
verdict: confounded

component: tool_guidance.md (task lead: Netflix FY2024 10-K URL and snippet-derived figures labelled "re-confirm")
candidates: inv1, agg1 (dom1 put the same lead in its skill)
change: Gave the accession and URL of the 10-K and the snippet-derived row values, flagged as unverified.
observed: inv1 and agg1 parsed the URL in turn 1 with no discovery search and finished in 3 turns. The retrieved values matched the lead, so no number changed. The lead saved turns only.
verdict: helped

component: tool_guidance.md (retrieve the table footnotes and state obligations outside the table: unknown future titles, unrecognized tax benefits)
candidates: agg1 (dom1 did the same through its skill)
change: agg1 added an explicit line. inv1 had only a generic "if the text names an obligation outside the table, say so".
observed: agg1 and dom1 retrieved the footnotes. They reported the $1-4B unknown future titles estimate, the $432M unrecognized tax benefits and the roughly $800M tax deposits, and said actual outflows may be larger. inv1's retrieval returned only the table and printed a generic caveat that no other rows exist. base1 mentioned only unknown titles, and that came from a snippet. The headline number was the same in all runs. The extra context is the analyst-ready difference.
verdict: helped

component: skills/material_cash_requirements_table/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill covering where the table sits, mapping "next 12 months" to the following calendar year, row and column checks, the content-note cross-check, the exclusions, and an answer contract. The skill also carried the lead. systemprompt.md gained a line telling the agent to load it.
observed: dom1 loaded the skill first and then took 4 turns, against 3 for inv1 and agg1, which had no skill. The figures were identical. dom1's exclusion reporting matched agg1's, and agg1 got it from tool_guidance without a skill. Beyond the extra load_skill turn, no behavior difference is visible. The skill's content cross-check against the commitments note was not run.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A "what are the company's material cash requirements / contractual obligations for next year" lookup answerable from one table in the latest 10-K's MD&A. The base run answers from snippets, leaks citation markup, and lists an unopened spreadsheet and PDF as sources. The filing's table footnotes name obligations excluded from the table.
- **lesson**: In tool_guidance.md, require opening the 10-K and retrieving the full table together with its footnotes. Re-add the rows against the printed total, and state in the answer any obligation the footnotes say is outside the table (unknown future commitments, unrecognized tax benefits) with the filing's own estimate. Map "next 12 months" to the question's calendar year. List only opened documents, in plain text. Keep this in always-on guidance and do not add a skill, since a skill-loading run took an extra turn and showed no different behavior.
- **evidence**: The general-rules row, where base1 never opened the 10-K and the three edited runs did, all with the same figure. The footnote row, where agg1 and dom1 reported the exclusions with estimates and inv1 gave only a generic caveat. The skill row, where dom1's skill run took 4 turns against 3 for the skill-free runs.
- **confidence**: low. One rollout per candidate, all runs gave the same headline number, and the rules were bundled with a URL lead in every edited run. The footnote contrast comes from only one skill-free run against another.
