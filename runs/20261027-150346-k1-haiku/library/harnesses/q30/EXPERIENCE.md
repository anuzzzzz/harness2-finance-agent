# q30

- adopted: `agg1`
- components: 1 skill; 3,039 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, agg1 (dom1 added a shorter two-bullet sourcing version)
change: Went from empty to rules. Treat snippets as leads. Open the primary 10-K with parse_html_page and confirm figures with retrieve_information. Re-query when a retrieval is truncated or derived. Reconcile derived totals to disclosed totals. Cite only opened documents. Do not run empty-query searches. inv1 and agg1 also carried a Snap-specific lead. In inv1 that lead sat in tool_guidance. In agg1 it sat in the skill.
observed: base1 started with a null-query web_search and an edgar_search. It then listed an unopened Q3 press release as a source and flagged the $249.8M 2026 principal as unconfirmed without re-querying. inv1 parsed the 10-K in turn 1, made one retrieval and submitted with only the 10-K as a source. It did make one failed web_search in turn 3, and the retrieval it relied on was truncated. agg1 and dom1 also listed only the 10-K. The 85,945 thousand figure was the same in every run. The difference is sourcing and verification hygiene, not the number. inv1 also had the lead telling it to go straight to the 10-K, so the rule and the lead cannot be separated. Each candidate is a single rollout.
verdict: confounded

component: skills/convertible_dilution_lookup/SKILL.md
candidates: dom1, agg1
change: Added an on-demand skill for convertible-note dilution. The headline is the if-converted line in the EPS note. Reconcile principal / 1,000 × conversion rate by series against that line. Keep if-converted shares distinct from diluted-EPS shares and from capped-call offsets. State units and the date. Cite only opened documents. agg1 added that filings often state no separate "maximum". Both carry the Snap task lead.
observed: Both loaded the skill first, parsed the 10-K and ran one retrieval that returned per-series principal, including the 2026 figure of $249,754K that base1 had not confirmed. Both submitted a table with a sum of about 85,945.13 thousand reconciled to the disclosed 85,945 thousand, in 4 turns. inv1 reached the same total in 3 turns without the skill and also reconciled it, though less exactly (about 85,944). The skill's visible contribution is the per-series table with a sum check, and exact principal for the 2026 notes. It did not change the number. The task lead carried the URL and inputs, which may explain the direct route.
verdict: confounded

component: systemprompt.md
candidates: dom1, agg1
change: Added one line telling the agent to call load_skill with `convertible_dilution_lookup` for convertible-note dilution questions.
observed: Both candidates called load_skill as their first action. There is no skill-equipped run without the trigger, so its separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks for a total that a filing discloses in one table line (for example an if-converted share count) and that can also be rebuilt from per-instrument inputs in a debt note. The base run reports the disclosed total plus a derived split. It flags one input as unconfirmed, and it lists a filing it never opened as a source.
- **lesson**: In tool_guidance.md, add two rules. First, when a retrieval is truncated or labels a number as derived, run a second targeted retrieval for the exact row or sentence. Second, reconcile any component-built total to the disclosed total, say which figures are disclosed and which are derived, and cite only documents actually retrieved from. Put the per-series inputs and the reconciliation step in the skill, not in always-on text.
- **evidence**: The tool_guidance.md row and the skill row. base1 left the 2026 principal unconfirmed, listed an unopened press release, and made a null-query search. dom1 and agg1 retrieved the principal for all five series, summed them to 85,945.13 thousand and cited only the 10-K. inv1 reached the same number with the guidance alone and its own lead. The figure was identical in every run, so the evidence is about verification and sourcing, not accuracy.
- **confidence**: low. Every candidate is one rollout, the guidance and skill were never varied independently, and the answer did not change across runs.
