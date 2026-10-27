# q33

- adopted: `agg1`
- components: 1 skill; 3,694 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. Snippets are leads only. Open the 10-K with parse_html_page and retrieve from it. Cite only opened documents. Write plain text with no citation markup. Never send a null query. inv1 and agg1 added "decide which inputs the calculation needs before collecting them", "state the reading of '3% higher'", and "take tax only from opened statements". dom1 kept a shorter four-bullet version. inv1 also embedded a Boeing leads block (10-K URL, debt $53,864M, loss $(11,817)M, and a warning that the 10-K gives no weighted-average rate). agg1 dropped that block from always-on text.
observed: base1 pulled a third-party weighted rate (5.32%) and a 3.10% tax rate from snippets of pages it never opened. It listed the unopened Financial_Report.xlsx and an FCFF page as sources and leaked <cite> markup. inv1, dom1 and agg1 each used only the opened 10-K as the source, leaked no markup, and took the tax line from the 10-K income statement. inv1 still issued a null-query web_search in turn 2 despite the rule. The inv1 lead block pointed straight to the 10-K, so inv1 skipped discovery and finished in 4 turns. The rules were bundled with a skill (dom1, agg1) or a lead block (inv1) in every run. Each candidate is one rollout.
verdict: confounded

component: skills/interest_rate_sensitivity_net_income/SKILL.md (plus the trigger line in systemprompt.md)
candidates: dom1, agg1
change: Added an on-demand skill for the what-if. Incremental interest equals debt times the shift, so the current rate is not needed. Use the carrying-value debt total, and show a differing capital-resources figure as a sensitivity. Lead with the simple debt x shift against the reported loss, with an after-tax alternate. If the base is a loss, state that the loss grows by X%. Answer contract. It carries verified Boeing facts. agg1 added a total-net-loss alternate and a labelled effective-rate alternate. Both runs loaded the skill in turn 1.
observed: Both runs led with $1,615.92M pre-tax and a 13.67% larger loss, and both explained the 53,864 vs 54,369 debt figures. dom1's run showed a derived 5.06% rate, labelled as derived. Both labelled the sign convention. Both gave the 21% statutory alternate (10.80%). Neither pulled a third-party rate. inv1, with no skill, took the 3.1% after-tax variant as its lead (13.24%), still computed the pre-tax alternate, and did not address the 54,369 figure. So the headline framing differed. The skill carries the same facts as inv1's lead block and rode with tool_guidance rules, so its separate effect is not isolated. There is one rollout per candidate.
verdict: confounded

component: systemprompt.md
candidates: dom1, agg1
change: Added one sentence telling the agent to call load_skill with `interest_rate_sensitivity_net_income` for rate-change questions.
observed: Both runs called load_skill as the first action. No skill-equipped run lacks the trigger, so its separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A what-if question whose arithmetic is a delta times a balance (a rate shift on debt, a price change on volume), where the base run fetches a third-party "current rate" or tax rate from search snippets that the calculation does not need. The base run also lists unopened pages as sources, and the base net income is a loss.
- **lesson**: In tool_guidance.md, add a rule to write down which inputs the calculation needs before collecting any. Do not import a snippet or third-party figure the arithmetic does not use. Take tax lines only from the opened income statement. When the question's wording allows two readings (for example percentage points vs relative), state the reading used. If the base is a loss, say what the percentage means (the loss widens). Cite only opened documents. Keep the step-by-step method and any verified task facts in an on-demand skill, not in always-on text.
- **evidence**: The tool_guidance.md row. base1 imported 5.32% and 3.10% from unopened snippet pages and listed unopened sources. inv1, dom1 and agg1 carried a rule against it and used only the opened 10-K, with no third-party rate. The skill row is confounded, because the same behavior appears with and without the skill. The numbers were the same in the debt x 3 points step across all runs.
- **confidence**: low. One rollout per candidate, and the rules were bundled with a skill or a task-fact lead in each edited run. The evidence concerns sourcing and input choice, not accuracy.
