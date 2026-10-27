# q08

- adopted: `agg1`
- components: 0 skills; 4,792 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, open primary docs, match the question's qualifier such as "at close", re-retrieve narrowly before saying "not disclosed", cite only opened documents, plain text with no citation markup, no null-query searches)
candidates: inv1, agg1 (dom1 carried a shorter three-bullet version)
change: Went from empty to a rule set. inv1 and agg1 added a qualifier-matching rule and a rule against concluding "not disclosed" after a single retrieval. They also barred unretrieved accounting characterizations and "(correction: ...)" asides, and agg1 added a 403 tip for hyphenated accession URLs. dom1's version only said to open the closing 8-K when a summary lacks the figure, avoid null queries, and cite only opened documents.
observed: base1 parsed the 10-Q, ran one retrieval, and submitted $3.30B in 4 turns. It leaked cite markup, listed unopened ARS/10-K/Q2 PDFs, asserted common-control accounting from an unretrieved source, and left a "(correction: ...)" aside. inv1 ran 8 turns and made narrower retrievals of the 10-Q. It also opened the FY2024 10-K and tried the closing 8-K, which returned a 403. Its answer was clean and listed only the two opened filings. It said openly that $3.30B is not a closing-date measurement. agg1 took 4 turns and made two targeted 10-Q retrievals, but it issued a null-query search despite the rule. Its answer still leaked <cite> markup and gave $3.30B with a "not disclosed at close" caveat. It listed only the 10-Q and an 8-K exhibit it never opened. dom1 leaked markup too and listed an unopened ARS PDF and the 10-K. All runs gave the same headline figure ($3.30B). inv1 shows the rules changing sourcing and presentation, while agg1 and dom1 show they did not reliably prevent leaks. The rules were bundled with task-fact leads in every run, and each candidate is one rollout.
verdict: confounded

component: tool_guidance.md (task-fact lead: 10-Q URL, $3.25B + $50M, 26.54M units, Feb 28 2025 closing, 8-K URL, "still to check" items)
candidates: inv1, agg1 (dom1 put its leads in the skill)
change: Embedded the 10-Q URL and the headline figures already found in base1, plus pointers to the acquisition note and closing 8-K. agg1 trimmed the leads and added the 8-K EX-99.1 fact.
observed: inv1 and agg1 parsed the 10-Q straight away, with no discovery search. inv1 also tried the leaked 8-K URL, which returned HTTP 403. The leads did not change the figure, which matched base1's. Task-specific content has no transfer value.
verdict: no observed effect

component: skills/deal_consideration_at_close/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill on separating headline price, closing adjustments and the closing-date measure, plus a common-control caveat and the TKO leads. systemprompt.md gained a line telling the agent to call load_skill.
observed: dom1 loaded the skill in turn 1 after a failed web_search, then made a null-query search. It parsed the 10-Q and an 8-K EX-99.1, and made three retrievals. The answer was $3.30B with a caveat, the same as the other runs. It still leaked <cite> markup and listed unopened sources (ARS PDF, 10-K). It reproduced the skill's common-control caveat, and the skill told it to look for a closing-date figure. The skill and trigger did not change the number or fix the sourcing. The trigger's separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question that carries a measurement qualifier ("at close", "as of the closing date", "fair value") on a figure, where the first filing's retrieval returns only the headline or announced amount and says it does not break the figure down.
- **lesson**: In tool_guidance.md, add a rule that a retrieval which does not show the qualified figure is not proof the filing lacks it. Before the answer says "not disclosed", require at least one narrower retrieval on the likely home of the figure (the acquisition or consideration note, the subsequent-events note, the closing 8-K). If none exists, the answer must label the headline figure as the announced amount and not as the qualified measure. Enforce the plain-text and "cite only opened documents" rules by also telling the agent to re-read its draft answer for <cite> tags and for sources it never retrieved from, because rules alone did not stop those leaks in two of the three edited runs.
- **evidence**: Rows 1 and 2. base1 answered from one retrieval and asserted an unretrieved accounting claim. inv1, with the qualifier and re-retrieval rules, ran four retrievals across the 10-Q and 10-K, labelled $3.30B as not a closing-date measurement, and listed only opened sources. agg1 and dom1, which had the same or shorter rules, still leaked <cite> markup. All four runs reached the same figure.
- **confidence**: low. One rollout per candidate, and the rules were bundled with task-fact leads. The only clear contrast is inv1's cleaner answer. The headline number did not differ, so no accuracy effect can be shown.
