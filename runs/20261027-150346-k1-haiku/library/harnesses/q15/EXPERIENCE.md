# q15

- adopted: `agg1`
- components: 0 skills; 3,996 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, open the 10-K with parse_html_page then retrieve_information, cite only opened documents, plain text with no citation markup, no empty-query searches)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. Snippets are leads only. The 10-K is opened first, since it carries both year-end balance-sheet columns. Sources are limited to opened documents. The answer is plain text. Null or empty queries are banned. inv1 and agg1 added a bounded retry for when edgar_search returns other companies. dom1's version was shorter.
observed: base1 ran two searches and never opened a document. It answered from Business Wire snippets, listed two unopened release pages as sources, and leaked raw <cite index> markup. It also issued a null-query search after edgar_search returned Nucor and Olympic Steel. inv1, dom1 and agg1 each parsed the FY2024 10-K and retrieved cost of sales 14,060 and inventories 2,168 / 2,128 from it. Each listed only the 10-K, and none leaked markup. The numbers were identical to base1's (6.55x average, 6.49x ending), so the change was in verification and presentation. All three edited candidates also carried the 10-K URL as a lead, which may account for the direct route to the filing. The rules and the lead cannot be separated, and each candidate is one rollout.
verdict: confounded

component: tool_guidance.md (task-fact lead: the 10-K URL, with or without snippet figures)
candidates: inv1, dom1 (via skill), agg1
change: inv1 embedded the 10-K URL plus the snippet figures (14,060 / 2,168 / 2,128) and the D&A note. agg1 trimmed the lead to the URL only, so the figures had to be retrieved from the filing. dom1 put the lead in its skill.
observed: inv1 and agg1 parsed the 10-K in turn 1 without any discovery search. inv1 finished in 3 turns and agg1 in 4. dom1 ran an edgar_search that returned unrelated steel companies, then parsed the 10-K, for 5 turns. The retrieved figures matched the snippet leads in every run, so the lead saved turns without changing any number. The task-specific content does not transfer.
verdict: no observed effect

component: tool_guidance.md (ratio convention rule: average balance as headline, ending balance as a labelled alternate; cost line that excludes separate D&A is used as-is with one sentence of note)
candidates: inv1, agg1 (dom1 carried the same content in its skill)
change: Added an explicit rule for ratio questions. If the question does not fix the convention, compute the standard one as the headline and show the alternate on one labelled line. If a cost line excludes a separate D&A line, use the reported line and say so.
observed: base1 gave 6.49x and 6.55x without clearly ranking them. All three edited runs gave 6.55x as the headline and 6.49x as a labelled alternate, and all noted the D&A exclusion. agg1 also added a net-sales reference figure of 7.28x, which is unneeded. Because dom1 reached the same framing through its skill, the rule's separate effect is not isolated.
verdict: confounded

component: skills/ratio_from_10k_statements/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill covering the inventory turnover definition, the average-versus-ending choice, the D&A caveat, period alignment and an answer contract. It carries the task figures as leads. systemprompt.md gained a line telling the agent to call load_skill for statement-based ratio questions.
observed: dom1 loaded the skill first, then ran a discovery edgar_search, parsed the 10-K, made one retrieval and submitted, 5 turns. inv1, with no skill, reached the same answer in 3 turns, and agg1, also with no skill, in 4. The answer content and sourcing were equivalent. The skill added turns and nothing visible. No run isolates the trigger line.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A simple ratio question (turnover, margin) answerable from one 10-K's income statement and two balance-sheet columns. The base run answers from earnings-release snippets without opening any filing, lists unopened release pages as sources, leaks citation markup, and shows two unranked ratio variants.
- **lesson**: In tool_guidance.md, state that every input to the ratio must be retrieved from the opened 10-K, with the latest 10-K opened first. Add that the average-balance convention is the headline and the ending-balance version a labelled alternate, and that sources are limited to opened documents in plain text. Keep this in always-on guidance. Do not add a skill for the ratio definition, because skill-free runs reached the same answer in fewer turns.
- **evidence**: Rows 1 and 4. base1 submitted from snippets with unopened sources and <cite> markup. inv1, dom1 and agg1 all parsed the 10-K and listed only it. The skill-equipped dom1 run took 5 turns against 3 and 4 for the skill-free runs, with an equivalent answer. The numbers were the same across all four runs, so the contrast concerns sourcing and verification, not accuracy.
- **confidence**: low. One rollout per candidate, the rules were bundled with a task-fact lead in every edited run, and the figures did not differ.
