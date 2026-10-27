# q12

- adopted: `agg1`
- components: 1 skill; 3,309 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (snippet-is-a-lead, open primary documents, cite only opened documents, plain text with no citation markup, as-of-date rule)
candidates: inv1, agg1 (dom1 carried a shorter three-bullet version)
change: Went from empty to a rule set. Every figure in the calculation must come from an opened document. Inferred assumptions such as the FX rate must be confirmed or labelled. The as-of date excludes post-dated documents. Only opened documents may be cited. No citation markup in the answer. agg1 also added "never send an empty or null query".
observed: base1 ran seven searches and opened nothing. It called the 32.8 FX rate an inference, listed ten unopened sources and leaked <cite index> markup. inv1, dom1 and agg1 all parsed the Q4'24 release and retrieved the 32.8 rate and the US$25.0–25.8B range. No edited run leaked markup. All three reached about NT$825.11B and US$25.16B, so the number did not change. The null-query searches were not eliminated: inv1 made 2 and dom1 made 3 (dom1 had no such rule). agg1 made none, and it also had the rule in its tool_guidance. A parse-everything-first route is also consistent with the skill's URL leads, so the guidance cannot be separated from them.
verdict: confounded

component: skills/monthly_revenue_projection_vs_guidance/SKILL.md (inv1) and its revised version (agg1); trigger line in systemprompt.md
candidates: inv1, agg1
change: Added an on-demand skill for projecting a quarter from monthly reports against guidance. It uses MoM as the headline growth definition, with a labelled YoY alternate. It converts guidance at the stated FX rate, compares against the low end, midpoint and high end, and carries labelled leads with URLs. agg1 added URLs for the Feb 2022 and Feb 2023 reports, an explicit "do not list snippet-only pages" clause, and an exclusion of later FX presentations.
observed: Both runs loaded the skill, and the FX rate and guidance range came from opened text. inv1 never opened the Feb 2022 or Feb 2023 reports. It took Feb 2022 (146,933) from the skill's lead and from snippets, and still listed two snippet-only pages as sources, despite its own rule. agg1 had the extra URLs and opened both reports. It then retrieved Feb 2022 only as rounded NT$146.93B, and used 146,930 and 171,970 for 2022 where inv1 used 146,933 and 171,967. The average came out at 4.5404% in agg1 and 4.5389% in inv1. Both gave the same verdict: within the range, above the low end and below the midpoint. agg1 listed only documents it had opened. Neither run isolates the skill from the guidance. No skill-free run exists on an edited harness, so the skill's own contribution to the answer is not shown.
verdict: confounded

component: skills/monthly_revenue_vs_quarter_guidance/SKILL.md, tool_guidance.md and trigger line (dom1)
candidates: dom1
change: Added a skill that fixes MoM growth and takes the FX rate from the guidance release. It excludes the later presentation and states the verdict against the midpoint with FX sensitivity. Task figures were carried as leads. tool_guidance was three bullets.
observed: dom1 opened only the Q4'24 release and the Feb 2025 report. It took the 2022–2024 Feb/Mar figures from the skill's lead text, not from retrievals. It listed six or more sources it never opened (Jan 2025, Feb 2024, Mar 2024, Feb and Mar 2023, and others). That is the failure its own rule targets. It also included a muddled YoY "cross-check" line ("34.3%... not needed here"). It did add a useful FX break-even (about 32.48), and the verdict was the same as the other runs. dom1 had a shorter rule set, so the lapse may reflect that, or the figure leads in the skill, or the particular rollout.
verdict: confounded

component: systemprompt.md (skill trigger line)
candidates: inv1, dom1, agg1
change: Added one sentence telling the agent to call load_skill for projection-versus-guidance questions.
observed: inv1 made a failed web_search first and then loaded the skill. agg1 and dom1 loaded it as their first action. No skill-equipped run lacks the trigger, so its separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks to project a period from several monthly or earlier-period reports (a historical average growth rate applied to a base) and compare the result with guidance stated in a different currency, and the base run works from search snippets.
- **lesson**: In tool_guidance.md, require that every input to the projection be retrieved from its own opened document before it is used. That means the guidance range, the FX or other assumption, each reported month, and both months of every historical year. A figure that is only a lead from a skill or a snippet must be labelled as such, and its page must not be listed as a source. Keep the method (growth definition, conversion, comparison against low end, midpoint and high end) in a skill, but have the skill list the report URLs for every needed input, including prior-year base months, so each can be opened. Also state that "never send an empty query" is a rule to check against the run.
- **evidence**: Rows for tool_guidance.md and for the skill. base1 opened nothing, inferred the FX rate and listed ten unopened sources. inv1 and agg1 retrieved the 32.8 rate and the guidance range from the Q4'24 release. agg1, which was given the missing Feb 2022 and Feb 2023 URLs, opened every report it cited. inv1, which was not, listed two snippet-only pages. dom1 took historical figures from skill leads and listed unopened sources. The figure was the same in every run (about US$25.16B, above the low end and below the midpoint).
- **confidence**: low. One rollout per candidate, the guidance and the skill were never varied independently, and the answer did not change. The evidence concerns verification and sourcing, and the 32.8 FX rate was still not found in a document other than the Q4'24 release.
