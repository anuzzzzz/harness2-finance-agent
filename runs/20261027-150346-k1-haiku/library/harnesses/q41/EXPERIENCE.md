# q41

- adopted: `agg1`
- components: 0 skills; 3,768 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: a snippet is a lead, open the primary document with parse_html_page then retrieve_information, numeric CIK for edgar_search, no empty queries, cite only opened documents, plain text)
candidates: inv1, agg1 (dom1 left tool_guidance unchanged)
change: Went from empty to a short rule set. The release is opened and the quarter line retrieved before answering. Tickers in `ciks` are barred, and one fix attempt is allowed after an empty result. Null queries are barred. Only opened documents may be cited, with no citation markup. The company's own metric name ("comparable store sales") is mapped to the question's "same-store sales", and a decline must not be reported as growth. agg1 added a clause against opening a second large filing once the figure is confirmed.
observed: base1 passed the ticker "FND" as a cik, which returned zero results. It never parsed anything and answered from snippets. It listed the IR page and TradingView as sources and leaked "source index" markup. inv1 and agg1 each parsed the release in turn 1, ran one retrieve_information, and submitted in 3 turns. Each listed only the opened release as a source, wrote plain text, and stated the figure as -0.8% (a decline). Both also carried the lead block below, so the rules cannot be separated from the leads. Only one rollout per candidate.
verdict: confounded

component: tool_guidance.md (task-fact lead block: FND CIK 1507079, release and 10-K URLs, snippet figure -0.8%, labelled "re-confirm")
candidates: inv1, agg1
change: Gave the Q4 FY2024 release URL directly and told the agent to open it first and use the 10-K only if the release fails to parse.
observed: inv1 and agg1 skipped discovery search and parsed the release in turn 1. The retrieved text matched the lead (-0.8%, $1,107.4M, +5.7%), so no figure changed. dom1, which had the same URLs in its skill, also parsed the release but additionally parsed the 336k-character 10-K. The lead saved turns, but the task-specific content will not transfer.
verdict: helped

component: tool_guidance.md (agg1's added clause: do not open a second large filing once the figure is confirmed)
candidates: agg1
change: Told the agent to stop after the first source confirms the figure instead of parsing the 10-K too.
observed: agg1 opened only the release, ran one retrieval, and ran at $0.003 per rollout. inv1, with the "use the 10-K only if the release fails" lead but no explicit clause, also opened one document at the same cost. The clause's separate effect cannot be seen, since dom1 is the only run that parsed the 10-K and it had no tool_guidance at all.
verdict: no observed effect

component: skills/retail_comparable_sales/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill on mapping same-store wording to the company's metric. It carries an answer contract (signed figure, period end date, a retrieved definition, total sales growth versus comp growth) and the FND leads. systemprompt.md gained a line telling the agent to call load_skill.
observed: dom1 loaded the skill in turn 1, parsed both the release and the 10-K, and ran two retrievals. It took 4 turns at $0.076, against 3 turns at $0.003 for inv1 and agg1, which had no skill. The figure was the same, -0.8%. dom1's answer added the comp definition and the explanation that new stores drive total growth, which the skill-free runs lacked. That extra context was not part of the question. The cost came with the 10-K parse, and the skill and the 10-K parse cannot be separated.
verdict: confounded

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A simple single-figure lookup (a quarterly KPI such as comparable store sales) where the question's wording differs from the company's metric name and the sign may be negative. The base run answers from search snippets, passes a ticker to a CIK-only search field, and lists unopened pages as sources.
- **lesson**: In tool_guidance.md, state that edgar_search takes numeric CIKs and never tickers, with one fix attempt before falling back to a known URL. Also add a rule to open the one primary release with parse_html_page and retrieve the period line. Add a rule to map the question's term to the company's own term and report direction explicitly (a decline is not growth). Cite only the opened document. Keep this in always-on guidance and do not add a skill, because a skill-equipped run reached the same figure at higher cost.
- **evidence**: Rows 1 and 2. base1 sent the ticker as a cik (zero results), answered from snippets, and leaked markup with unopened sources. inv1 and agg1 opened the release in turn 1 and submitted in 3 turns citing only that release. Row 4. dom1's skill run reached the same figure in 4 turns at about $0.076 against about $0.003, after also parsing the 10-K.
- **confidence**: low. One rollout per candidate, the rules were bundled with a lead block in both edited runs, and every run reached the same -0.8% figure, so the evidence covers sourcing behavior and cost, not accuracy.
