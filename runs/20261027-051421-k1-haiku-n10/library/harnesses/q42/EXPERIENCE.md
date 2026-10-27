# q42

- adopted: `agg1`
- components: 1 skill; 3,032 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: skills/peer_payout_ratio_ranking/SKILL.md (inv1 and agg1; dom1 added a near-duplicate skill, peer_payout_ratio_comparison)
candidates: inv1, dom1, agg1
change: Added a peer-ranking skill. It fixes the peer set up front, with non-payers shown at 0.00%. The headline is cash dividends paid ÷ GAAP net income attributable to common, with a DPS/EPS cross-check. Adjusted-EPS ratios are a labelled secondary comparison, and third-party precomputed payout ratios are banned as inputs. inv1 and agg1 share the same skill name. dom1's version is a separate skill whose headline allows paid or declared dividends, does not mix them across companies, and requires a GAAP versus adjusted comparison. agg1 merged the two skills.
observed: base1 (no skill) used DPS ÷ GAAP EPS and took PepsiCo and KDP dividend inputs from Fidelity and Divvydiary. It used a data-provider payout figure for PepsiCo as context, and its caveats section flagged the GAAP versus adjusted flip. All three skill runs loaded the skill at turn 1 and used the cash-dividends ÷ net income method for the headline. They reached the same ratios: KDP 82.86%, KO 78.63%, PEP 75.48%, MNST 0%. inv1 added Celsius as a fifth peer (0%, tied with Monster). agg1 and dom1 gave a GAAP versus adjusted ranking comparison, and agg1 also gave a DPS/EPS cross-check for all companies. Order was the same everywhere: KDP, KO, PEP, MNST. Presentation and sourcing discipline improved, but no outcome difference is visible, and each run is a single rollout bundled with other edits.
verdict: confounded

component: systemprompt.md (trigger line to load the peer payout skill)
candidates: inv1, dom1, agg1
change: Added one line telling the agent to load the skill when asked to compare or rank a payout ratio against competitors.
observed: All three candidates called load_skill first, at turn 1. base1 never loaded one. The trigger works mechanically, and the skill's value is confounded (see the skill row).
verdict: helped

component: tool_guidance.md
candidates: inv1, agg1
change: Went from empty to guidance on searching by company, form, year and statement name, treating search results as leads and not as evidence, not retrying 403s, and writing plain text with no raw citation tags. agg1 softened the 403 rule to "start with web_search".
observed: inv1 and agg1 made no edgar_search calls and went straight to targeted per-company web_searches, finishing in 2 turns. dom1, which had no tool guidance, made four consecutive edgar_search calls in turn 2 and all returned 403. base1 (no guidance) made no edgar calls and simply ran six searches in one turn. inv1 still left raw cite-tag artefacts in its answer despite the guidance, while agg1's text was clean. Each side rests on one rollout and the edit was bundled with the skill.
verdict: confounded

component: skill clause requiring adjusted-basis (non-GAAP EPS) ratio comparison
candidates: dom1, agg1
change: Required a labelled secondary ratio on non-GAAP EPS. The skill says to state whether the ranking changes versus GAAP and to name the one-off that causes it. inv1's skill limits adjusted ratios to context only and only when GAAP is distorted.
observed: dom1 and agg1 both produced the adjusted ranking (KO 67.36%, PEP about 66% or 65.32%, KDP about 46%, MNST 0%) and named KDP's impairments as the reason KDP's GAAP ratio is inflated. inv1 gave no adjusted ranking. base1 included the adjusted figures only as a caveat. The explicit flip analysis is visible only in the two runs with this clause. In agg1 some per-share inputs (KDP DPS $0.89 from stockanalysis) were taken from a third-party excerpt, and the impairment attribution ($306M) differs from the $718M in base1 and dom1 without being reconciled.
verdict: helped

## Transferable lesson
- **cue**: A question asks to rank one company's ratio (payout, margin, yield) against competitors for a fiscal year, where peers differ in whether they pay or report the metric and where GAAP earnings carry one-offs that can reorder the ranking.
- **lesson**: In the SKILL.md for peer-ratio ranking, require four things. (1) A single stated definition, with both inputs taken from each company's own FY statements. (2) The peer set and non-payers listed, with a one-line reason each. (3) A labelled adjusted-basis ranking next to the GAAP one, naming the one-off that causes any flip. (4) A requirement to reconcile any one-off figure (for example an impairment amount) across sources before quoting it. Put the load trigger in systemprompt.md. In tool_guidance.md, say to start with web_search for each company and not to chain edgar_search calls after a 403.
- **evidence**: The skill row and the adjusted-ratio row. dom1 and agg1 gave GAAP versus adjusted rankings with the cause of the flip, while base1 only noted the flip in a caveat and inv1 did not give one. The tool_guidance row: dom1 wasted four edgar_search 403 calls while inv1 and agg1 avoided them. All runs reached the same order and ratios, so the effect is on method discipline and call economy, not the number.
- **confidence**: low. One rollout per candidate, edits bundled, identical numbers across runs, and agg1's own impairment attribution ($306M) is unreconciled against the $718M figure seen elsewhere.
