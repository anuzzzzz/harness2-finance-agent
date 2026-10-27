# q30

- adopted: `agg1`
- components: 0 skills; 4,155 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: tool_guidance.md (inv1 version: as-of-date rule, defined-term literal-search rule, one-headline-number rule, plus a Snap-specific fact block with the 85,945 figure, the filing and the note numbers)
candidates: inv1
change: Added generic guidance to use only documents dated on or before the as-of date, to search the filing for the question's literal term ("maximum", "if-converted"), and to lead with a single filing-stated figure. It also added a labelled block of task facts, including the filing name and the 85,945 value.
observed: base1 hedged between 85.95M and a 96.93M hybrid built from the 2030 notes' 8-K maximum rate, and it cited a June 2025 10-Q dated after the as-of date. inv1 went to the 10-K at turn 1 and ran one retrieve call that searched for "maximum". That call found no maximum share cap for the notes, and it submitted a single 85,945K answer in 3 turns for $0.135, with no post-as-of-date citation. The fact block named the filing and the value, so the contribution of the generic rules alone is confounded. There is one rollout.
verdict: confounded

component: skills/convertible_notes_dilution/SKILL.md and the systemprompt.md trigger line
candidates: dom1
change: Added a skill, loaded on a prompt trigger, covering where the if-converted line and conversion terms live. It carries a rule against mixing maximum-rate and base-rate series, and embeds Snap's retrieved facts as leads.
observed: dom1 spent turn 1 on load_skill. It then parsed the 10-K and retrieved the figures at turn 3. It also spent turns 4-6 fetching the 2030 notes' 8-K and indenture to get the 59.7371 maximum rate. It submitted at turn 7 for $0.214, versus inv1's 3 turns and $0.135 for the same headline 85,945K. It did not present the hybrid as the maximum, but it still printed the 96.9M figure as an "illustration". The extra turns and cost were spent on a lead the 10-K did not support. Any gain from the no-mixing rule cannot be separated from the load turn and the extra 8-K fetches.
verdict: no observed effect

component: tool_guidance.md (agg1 version: generic as-of-date and defined-term rules, a convertible-dilution reconcile rule with a no-mixed-basis clause, and no company-specific block)
candidates: agg1
change: Kept inv1's generic rules and dropped the Snap fact block. It added a generic rule to reconcile the reported if-converted line to principal × rate per series, never to combine one series at a maximum rate with others at base rates, and to treat capped calls separately.
observed: agg1 found the 10-K by edgar_search at turn 1, with no task hints. It then parsed it and retrieved the Note 3 table at turn 3, and ran a second retrieve for "maximum conversion rate", "make-whole" and "capped call" at turn 4. It submitted a single 85,945K headline in 5 turns for $0.261, which was the highest cost of the three runs. It reported that the filing states no maximum, and it listed the unquantified 2030 make-whole as a caveat. It did not repeat base1's hybrid number or a post-as-of-date citation. The result matches inv1 without any task-specific content. The second retrieve added cost, and how much the no-mixing clause contributed cannot be separated. There is one rollout.
verdict: helped

## Transferable lesson
No separate row needed.

## Transferable lesson
- **cue**: A question uses a defined-sounding term ("maximum", "if-converted", "aggregate") for a figure that the filing may report under a different label, and the base run mixes bases from several sources (for example one series' make-whole maximum from an 8-K combined with other series' base rates) or cites documents dated after the as-of date.
- **lesson**: In tool_guidance.md, add a generic defined-term rule. Run one retrieve_information call that searches the opened 10-K for the literal term. If the filing states the figure, lead with it. If it does not, say so and lead with the closest reported line, reconciled to its components. Use computed variants only as labelled cross-checks, and never present a mixed-basis total as the answer. Add an as-of-date line forbidding later-dated filings. Do not build a skill and do not embed company facts in this rule.
- **evidence**: base1 versus inv1 and agg1. base1 ended on a hedged 85.95M / 96.93M answer built from an 8-K maximum rate and cited a 2025 10-Q. inv1 and agg1 each ran a literal-term search of the 10-K and submitted one clean 85,945K headline, with the reconciliation shown, in 3 and 5 turns. dom1's skill-based route reached the same headline but spent a load turn and three more turns chasing the 8-K and indenture, at about 1.6 times inv1's cost. inv1's fact block confounds how much the generic rule contributed, but agg1 reached the same result without any task content.
- **confidence**: low. There is one rollout per arm and all three edited runs reached the same figure. The evidenced gain is a cleaner single-number presentation with no post-as-of-date citation, not a different value, and inv1's fact block confounds the first comparison.
