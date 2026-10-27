# q27

- adopted: `agg1`
- components: 0 skills; 3,770 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (open-primary-document, no null-query search, cite-only-opened, plain-text rules)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. A snippet is a lead, not evidence. The 10-K must be opened with parse_html_page and queried with retrieve_information. Only opened documents may be cited. The answer is plain text. Web searches with an empty query are forbidden. agg1 also required ending with the sources dictionary.
observed: base1 never called parse_html_page or retrieve_information. It answered from snippets, leaked raw cite markup, issued a null-query web_search, listed the unopened Financial_Report.xlsx, ARS PDF and A.M. Best release as sources, and admitted it found no seniority clause. inv1, dom1 and agg1 each parsed the 10-K and retrieved the Note 14 terms: $500M, 6.500% fixed to May 15, 2037, then Term SOFR plus a spread adjustment, maturities of 2057 and 2067, redemption, 10-year deferral, dividend restrictions, and the replacement capital covenant (RCC). None leaked markup or listed unopened sources. The core terms were the same as in base1. The edited runs added the RCC, the "ranking not stated" caveat and a prior-year amount. Every edited run also carried a task-lead block, so the rules cannot be separated from the lead. One rollout per candidate.
verdict: confounded

component: tool_guidance.md (task lead: 10-K URL and snippet-derived terms)
candidates: inv1, agg1 (dom1 carried the same content in its skill)
change: Gave the FY2024 10-K URL and snippet-reported terms, labelled "re-confirm". agg1 gave only the URL and the Note 14 pointer.
observed: inv1 and agg1 parsed the 10-K in turn 1 and finished in 4 turns. dom1 spent a turn loading its skill and took 6. base1 had no URL and searched. In inv1, the retrieved text matched the lead figures, so the lead changed no number. It saved discovery turns.
verdict: helped

component: tool_guidance.md ("terms of" checklist: every stated term, kept apart from look-alike instruments, "not stated" when silent)
candidates: inv1 (shorter), agg1 (full checklist: prior-year amount, RCC, deferral, ranking)
change: Told the agent to retrieve every term the filing states and to say "not stated" instead of inferring.
observed: Both runs flagged that the ranking and issue date are not stated in the filing. This corrects base1, which implied seniority from ratings. inv1 and agg1 gave the RCC, which base1 missed. dom1 had the same checklist in its skill and reached the same completeness. This is consistent with the checklist working but is not isolated, because retrieval itself surfaced the RCC.
verdict: confounded

component: skills/debt_instrument_terms/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill with a term checklist, a rule to keep look-alike instruments apart, an answer contract and the Allstate leads. systemprompt.md gained a line telling the agent to load it.
observed: dom1 called load_skill first, then needed three retrievals (6 turns, $0.192) against 4 turns for inv1 and agg1 without a skill ($0.172 and $0.180). Content was equivalent. dom1 added a wasted extra retrieval and an MD&A aside about subordinated debentures. No benefit over the skill-free runs is visible.
verdict: no observed effect

component: tool_guidance.md (end the answer with the sources dictionary)
candidates: agg1
change: Told the agent to end with the sources dict that the system prompt requires.
observed: agg1 and dom1 ended with the dict. inv1 ended with a plain "Source:" line, so it lacked the format. dom1 had no such rule but complied anyway, so the rule's effect is unclear.
verdict: confounded

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A "what are the terms of instrument X (debt, hybrid, preferred) as of FY Y" question where one 10-K debt note holds the terms. The base run finds the 10-K URL but answers from snippets, never opens the filing, lists unopened spreadsheets and press releases as sources, and leaks citation markup.
- **lesson**: In tool_guidance.md, require parse_html_page on the 10-K and then retrieve_information on the debt note. Set a term checklist: amount with prior year, coupon and reset benchmark and spread, scheduled and final maturity, call and make-whole, deferral and compounding, stock-issuance obligation, dividend restrictions, replacement-capital covenant, ranking. Say "not stated" when the filing is silent instead of inferring seniority from names or ratings. Add a sources-dict reminder and a ban on citing unopened pages. Keep it in always-on guidance, not a skill. The skill run added a turn and no content.
- **evidence**: Rows 1 and 3. base1 opened nothing and leaked markup, while inv1, dom1 and agg1 all opened the 10-K and returned the RCC and the "ranking not stated" caveat. Row 4. The skill-equipped dom1 took 6 turns against 4 for the skill-free runs with equivalent content.
- **confidence**: low. One rollout per candidate, and the rules were bundled with a URL lead in each edited run. The core figures were the same across all runs, so the evidence concerns sourcing, completeness and turn count, not accuracy.
