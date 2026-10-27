# q46

- adopted: `agg1`
- components: 1 skill; 3,415 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. Snippets are leads only. Primary documents are opened with parse_html_page and then retrieve_information. Never send an empty or null query. Re-retrieve narrowly when output is truncated. Cite only opened documents. Write plain text with no citation markup. inv1 and agg1 added a rule that events after the as-of date appear only as labelled later developments. inv1 also embedded a Zillow lead block with the 10-K URL, deal amounts and revenue table. dom1 and agg1 left the lead block out of the always-on file.
observed: base1 parsed only the FY2024 10-K. It leaked raw <cite index> markup throughout the answer. It listed the unopened Q4, Q2 and Q1 letters and the Q3 10-Q as sources. It pulled the Feb 2025 Redfin deal and the "ShowingTime+" and "mortgage marketplace" claims from snippets and mixed them into the core answer. It also issued null-query searches. inv1, dom1 and agg1 had no markup, listed only opened 10-Ks, and issued no null-query searches in the visible turns. inv1 labelled the Redfin deal as a later development. The final figures were the same in all runs (2024 revenue 2,236 vs 1,945; Follow Up Boss $399M; $433M vs $7M cash paid). The effect was on sourcing and presentation, not the numbers. The rules were bundled with other edits in every run, and each candidate is one rollout.
verdict: confounded

component: tool_guidance.md (embedded Zillow task-fact lead block)
candidates: inv1
change: Embedded the 10-K URL, acquisition list with amounts, cash paid figures and revenue table, labelled as unverified.
observed: inv1 skipped discovery search and parsed the 10-K in turn 1. It finished in 3 turns, against 4 for agg1 and 5 for dom1. It retrieved only from the FY2024 10-K, so it covered no 2022 base, no FY2023 10-K and no VRX Media. Its figures matched the lead, so the lead changed speed and scope and not accuracy. The task-specific content does not transfer.
verdict: no observed effect

component: skills/acquisition_strategy_vs_revenue_mix/SKILL.md and the trigger line in systemprompt.md
candidates: dom1, agg1
change: Added an on-demand skill covering six steps. Fix the window. Build the deal list from the acquisitions note, the cash-flow line and risk-factor mentions. Compute spend intensity. Pull the revenue mix with growth. Map each deal to a revenue line and separate deal-driven from organic growth. Then use an answer contract. agg1's version added prior-year 10-K coverage, a flag for filing-to-filing discrepancies, a "say when the filing does not quantify" line, and a rule to mark inferences. The trigger sentence was added to systemprompt.md.
observed: Both runs loaded the skill in turn 1. Both then parsed the FY2023 10-K as well as the FY2024 10-K, which inv1 did not do. Both added the 2022 revenue base and the 2022 cash paid ($4M). Both added the intensity ratios, such as Follow Up Boss at 92.15% of 2023 net acquisition cash. Both added the VRX Media Group mention. dom1 flagged the Follow Up Boss goodwill discrepancy ($401M vs $402M), and agg1's run also surfaced it. Both gave a window-aware, organic-versus-acquired attribution. inv1 had none of this and had no skill. The skill, the two-10-K behavior and the task-fact lead are bundled, and the skill carries the same task facts as inv1's lead. The skill's separate effect is not isolated. The skill-equipped runs show wider coverage than the skill-free run, but each is one rollout.
verdict: confounded

component: systemprompt.md (trigger line only)
candidates: dom1, agg1
change: Added one sentence telling the agent to call load_skill with `acquisition_strategy_vs_revenue_mix` for acquisition-strategy-versus-revenue-mix questions.
observed: Both runs called load_skill as their first action. No skill-equipped run lacks the trigger, so its separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: An open-ended "what has the company's strategy been, and how does it align with X" question with a stated time window and as-of date. The agent needs the deal or event list, the spend, and the X breakdown. The base run opens only the latest annual report. It fills the rest from search snippets and lists the unopened documents as sources.
- **lesson**: In tool_guidance.md, put three rules in always-on text. First, cite only opened documents and write plain text with no citation markup. Second, a claim that rests on a snippet is either opened or labelled snippet-only. Third, events after the as-of date are labelled later developments. Add a rule to open the prior-year annual report when the window starts before the latest report's comparative years, so the early-window events and the base-year figures come from opened text. Put the step-by-step procedure (window, deal list, spend intensity, mix table, deal-versus-organic attribution) in an on-demand skill, and do not rely on the skill to enforce the sourcing rules.
- **evidence**: The tool_guidance.md row, where base1 leaked markup and listed unopened letters while inv1, dom1 and agg1 did not. The skill row, where the skill-equipped runs opened the prior-year 10-K and added the 2022 base and intensity ratios, and the skill-free inv1 run did not. The skill row is confounded with the other edits.
- **confidence**: low. Each candidate is a single rollout, the sourcing rules were bundled with the skill and a task-fact lead, and the headline figures were identical across all four runs. The evidence supports a difference in sourcing hygiene and window coverage, not in accuracy.
