# q48

- adopted: `agg1`
- components: 0 skills; 4,741 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, open the primary documents with parse_html_page then retrieve_information, cite only opened documents, plain text with no citation markup, no empty-query searches)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. Snippets are leads only. Both the guidance letter and the results letter must be parsed and retrieved from. Only opened documents may be listed as sources. The answer is plain text. All three also said to prefer a stated full-year figure over a sum of quarters. inv1 and agg1 added the "guidance is in the release for the quarter before" procedure. dom1's version was shorter.
observed: base1 ran four web_searches and never parsed or retrieved anything. It listed about eight unopened sources, including a PDF and a proxy statement. It summed four quarters from separate letters to get GEP of $827.3M, and it leaked raw <cite index> markup. inv1, dom1 and agg1 each parsed the Q3 and Q4 letters in turn 1 or 2. Each retrieved the stated full-year GEP of $827.3M from the Q4 table and listed only the two opened letters. None leaked markup. All finished in 4 turns. All three edited candidates also carried a task-fact lead with both URLs, which may account for the direct route, so rules and lead cannot be separated. Each candidate is one rollout.
verdict: confounded

component: tool_guidance.md (task-fact lead: Q3 and Q4 letter URLs and snippet-derived FY2024 guidance ranges)
candidates: inv1, dom1, agg1
change: Each embedded the two letter URLs and the guided ranges (IFP 940-944, GEP 823-826, revenue 522-524, Adj. EBITDA loss (155)-(151)), labelled "re-confirm in the text". inv1 and agg1 added snippet actuals and a "look for full-year GEP in the Q4 letter" pointer.
observed: All three skipped discovery search and parsed both letters at once. All three re-retrieved the ranges from the opened Q3 letter, and the retrieved values matched the lead. base1 needed several searches and never opened either letter. The lead saved turns without changing any figure. The task-specific content carries no transfer value.
verdict: no observed effect

component: tool_guidance.md (guidance-vs-actual procedure: compare against both range and midpoint, loss-smaller-is-better wording, garbled-table cross-check)
candidates: inv1, agg1 (dom1 carried similar content in its skill)
change: Added explicit rules to compute position against the range and the midpoint at full precision. The loss sign gets its own wording. A garbled parsed table must be cross-checked against the document text or a second source (agg1).
observed: inv1, dom1 and agg1 gave the same variance figures (revenue +$3.5M versus midpoint, Adj. EBITDA loss $3.3M smaller). All stated the loss was smaller (better) than guided. dom1 and agg1 flagged a garbled table. agg1 also noted that the Q4 letter's February IFP guidance of $938-942M differs from the Q3 column. Its prose summary said "three metrics finished above the top" while counting IFP, which sits inside the range. This was a small internal inconsistency that the rule did not prevent. Only agg1's and dom1's runs show the garbled-table behavior.
verdict: confounded

component: skills/guidance_vs_actual_range/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill for multi-metric, range-based guidance-versus-actual comparison. It covers per-metric BEAT, IN RANGE or MISS, the midpoint calculation, loss-sign handling and an answer contract. It carries the Lemonade leads. systemprompt.md gained a line telling the agent to call load_skill for such questions.
observed: dom1 loaded the skill in turn 1, then parsed both letters, ran two retrievals and submitted, 4 turns. That is the same count as inv1 and agg1, which had no skill. The answer was equivalent to theirs. The skill was bundled with tool_guidance in dom1, and no skill-free run is shown, since inv1 and agg1 are the skill-free runs. Those two behaved the same, so no extra effect of the skill is visible.
verdict: no observed effect

component: systemprompt.md, LongTermMEMORY.md, guardrails.md
candidates: dom1 (systemprompt trigger line only); none for the others
change: dom1 added one trigger sentence to systemprompt.md. The other candidates left all three files unchanged.
observed: dom1 called load_skill first. No run isolates the trigger from the skill. Memory and guardrail files stayed empty.
verdict: no observed effect

## Transferable lesson
- **cue**: A "how did the actual results compare with the company's prior-quarter full-year guidance" question that needs two documents, the earlier release that issued the guidance and the release that reports the full-year actual. Search snippets carry both sets of figures, and the base run answers from snippets without opening either document.
- **lesson**: In tool_guidance.md, require that the guided range and the actual each be read from an opened primary document (parse_html_page, then retrieve_information). Say to prefer a stated full-year figure over a sum of quarters. For a loss metric, say whether the loss was smaller or larger than guided. Allow only opened documents as sources, and write plain text with no citation markup. Keep this in always-on tool_guidance and do not add a skill, because the procedure is short and a skill-equipped run showed no extra effect.
- **evidence**: Rows 1 and 3. base1 used four web_searches and opened nothing. It summed four quarters for full-year GEP, listed about eight unopened sources and leaked <cite> markup. inv1, dom1 and agg1 parsed both letters, retrieved the stated full-year GEP of $827.3M, and listed only the two opened letters. dom1 and agg1 also flagged the garbled guidance table. The skill row shows dom1's skill run matching the skill-free runs.
- **confidence**: low. One rollout per candidate, and the rules were bundled with a task-fact lead in every edited run. The figures were the same across edited runs, so the evidence is about verification and sourcing behavior, not accuracy.
