# q43

- adopted: `agg1`
- components: 1 skill; 3,174 always-on chars

## Why this was chosen
trivial: single candidate

## Transferable lesson
- **cue**: A question asks how much of a revenue change came from a rate (take rate, price, margin) versus volume. The filing gives both years of the volume metric and of revenue, and also discloses a reclassification or business-model change that moves the reported rate without moving volume. The base run improvises the split and mixes reported and adjusted figures.
- **lesson**: Put a decomposition skill on demand, with a trigger line in systemprompt.md. Have it fix a single formula that sums exactly to the revenue change, and require a sum check. Make the reported basis the headline and the disclosed adjustment a separately labelled alternate view. Give the segment take-rate check an explicit "complete or state it was skipped" line in the answer contract, because the run that loaded the skill still skipped that step.
- **evidence**: The rows for the two decomposition skills. All four runs produced the same reported split of 100.58% / -0.58% and the same adjusted split of 81.42% / 18.58%, so the base harness already got the numbers right. The only behavioural contrast is that dom1 ran the segment mix check and agg1 left it undone, both under the same skill, and the skill did not force the step. The base run had no explicit headline and no labelled alternate.
- **confidence**: low. Each candidate is a single rollout, the skill was bundled with tool_guidance in two of three candidates, and the figures did not differ between runs. The lesson concerns answer structure and completeness, not accuracy.
