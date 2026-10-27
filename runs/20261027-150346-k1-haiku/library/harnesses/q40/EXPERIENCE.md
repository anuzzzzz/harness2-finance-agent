# q40

- adopted: `agg1`
- components: 0 skills; 4,387 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (snippet-is-a-lead, open the primary document, cite only opened documents, plain text with no citation markup, no empty or null-query search)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. Snippets are leads only. The primary 10-K is opened with parse_html_page and queried with retrieve_information. Only opened documents may be listed as sources. The answer is plain text with no `<cite>` fragments. A web_search with a null query is banned. A PDF note was included.
observed: base1 opened a null-query web_search in turn 1, then parsed the 10-K and retrieved the right table. Its final answer leaked `<cite index=...>` fragments. It listed the Q2 and Q3 10-Qs and a shareholder-letter PDF as sources, though it had opened none of them. It also claimed the categories were "consistent with the 2024 10-Q reconciliations". inv1, dom1 and agg1 each parsed the 10-K in turn 1, ran one retrieval, and submitted in 3 turns. None leaked markup, none made an empty search, and none listed an unopened source. The reconciliation figures were identical in all four runs, so the effect was on sourcing honesty and presentation, not on the number. dom1 and agg1 listed only the 10-K. inv1 gave no sources block and said it had not opened the 8-Ks. All three edited runs also carried a task-fact lead with the 10-K URL, so the rule and the lead cannot be separated.
verdict: confounded

component: tool_guidance.md (reconciliation-question rule: full table with labels, signs and amounts, stated rationale, footnotes, foot-to-total check, latest filing's labels, full-year versus quarterly columns)
candidates: inv1, dom1, agg1
change: Added a rule for "what adjustments does the company make" questions. Give every line from the GAAP start to the non-GAAP total with its sign, give the company's stated reason and item definitions, check that the lines foot, and do not use memory or an earlier year's list. inv1 and agg1 also said to retrieve labels exactly as printed. agg1 added an explicit "end with the sources dictionary" instruction.
observed: base1 already produced the full table and the footing check without this rule, so the figures did not change. The edited runs added item definitions: acquisition-related impacts as fair-value changes in contingent consideration, and the lodging tax item as joint-and-several liability and transactional tax uncertainty. They also added sign notes and foot checks for both years. base1 had given the definitions less cleanly, with FY2022 columns requested and then reported missing. dom1 and agg1 ended with a sources dictionary. inv1 did not, so agg1's explicit instruction may have mattered, but the contrast is one rollout. agg1 added an unrequested aside on 10.62% growth in Adjusted EBITDA and a note that the 2023 tax-benefit reason was unchecked.
verdict: confounded

component: tool_guidance.md (Airbnb task-fact lead: 10-K URL, line items, FY2024/FY2023 amounts, labelled "re-confirm in the text")
candidates: inv1, dom1, agg1
change: Embedded the 10-K URL and the verified reconciliation lines and totals. It noted that the 10-K table covers only two years.
observed: All three parsed the 10-K as their first action and skipped discovery. base1 spent turn 1 on a web_search that returned nothing and then an edgar_search, and did not open the 10-K until turn 2. The runs then re-retrieved the same figures from the opened document, so the lead saved turns without changing any figure. This is task-specific content with no transfer value.
verdict: no observed effect

component: LongTermMEMORY.md, guardrails.md, systemprompt.md, skills
candidates: none
change: No candidate changed these files or added a skill.
observed: None. Every candidate declined a skill because the procedure is short.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks for the line items of a company's non-GAAP reconciliation (for example, the adjustments from net income to Adjusted EBITDA). The full-year table sits in the 10-K MD&A, and the base run reaches it but pads its answer with unopened filings.
- **lesson**: In tool_guidance.md, require that sources be listed only if their figures were retrieved from an opened document. Do not write "consistent with" a filing that was not opened. Require plain text with no citation markup, no empty-query searches, and the final sources dictionary. For this question type, also require the full table with exact labels, signs, the company's stated rationale and item definitions, and a check that the lines foot to the stated total. Keep this in always-on guidance and do not add a skill.
- **evidence**: Rows 1 and 2. base1 retrieved the correct table but leaked `<cite>` fragments, made a null-query search, and listed two unopened 10-Qs and a PDF as sources. inv1, dom1 and agg1 carried the cite-only-opened and plain-text rules, parsed the 10-K once, retrieved once, submitted in 3 turns, and listed only opened sources or none. The figures were the same in all four runs, so the evidence concerns sourcing and presentation, not accuracy.
- **confidence**: low. There is one rollout per candidate. The rules were bundled with a task-fact lead in every edited run, so the sourcing improvement cannot be separated from the lead. The contrast with base1 is clear on behavior but small in effect.
