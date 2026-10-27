# q14

- adopted: `agg1`
- components: 1 skill; 2,992 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: skills/fcf_margin_trend/SKILL.md
candidates: inv1, dom1, agg1
change: Added a multi-year FCF-margin skill (base had none). All three versions define FCF as CFO minus purchases of property and equipment, with intangibles shown only as a sensitivity. They tell the agent to flag the Zillow Offers discontinued-operations mismatch behind a margin above 100%, and to report percentage-point changes per step. inv1 also bans aggregator-precomputed margins as inputs. dom1 adds reading the FY2022 comparatives from a later 10-K and a monotonicity statement. agg1 merges the two and removes task-specific URLs.
observed: base1 (no skill) reached the same figures (224.16% / 11.26% / 12.75%) and already explained the Zillow Offers distortion and the intangibles sensitivity, so the skill did not change the numbers. All three skill runs loaded it at turn 1 and gave per-step pp changes (−212.90, +1.49) and an "excluding the outlier" trend, which base1 only partly did. inv1 and agg1 gave source typing. dom1 labelled capex and FY2022 revenue as aggregator or derived. dom1 still took capex from an aggregator, and inv1 and agg1 used excerpts and aggregators for FY2022 capex. The skill banned using aggregator values as inputs, yet inv1 used MarketBeat for FY2022 capex. Each candidate has one rollout, and the skill was bundled with the trigger line and tool guidance.
verdict: confounded

component: systemprompt.md (trigger line to load fcf_margin_trend)
candidates: inv1, dom1, agg1
change: Added one line telling the agent to call load_skill with `fcf_margin_trend` for FCF or FCF-margin trend questions.
observed: All three candidates called load_skill as their first action (turn 1). base1 never loaded a skill. The trigger works mechanically. The skill's own benefit is confounded.
verdict: helped

component: tool_guidance.md
candidates: inv1, agg1
change: Went from empty to a bounded 403 fallback: pass a non-empty query, do not retry edgar_search after a 403, use web_search, and say whether each figure came from an opened filing, an excerpt or a third-party page. Do not write "verified" without seeing filing text. Write plain text with no raw citation tags. inv1 also named the stockanalysis URL, which parsed in base1. agg1 dropped that URL.
observed: base1 hit edgar_search 403 and a null-query web_search, then parse 403, and cited 10-K URLs that never opened. inv1 and agg1 made no edgar_search calls. inv1 still issued a null-query web_search at turn 3 and a parse_html_page 403 at turn 2, despite the guidance. agg1 ran four targeted searches in one turn and submitted in 2 turns. Both disclosed the excerpt basis. inv1 also disclosed the third-party basis of FY2022 capex. agg1 listed 10-K URLs as sources while saying it opened no filing. dom1 had no guidance and hit edgar_search 403 three times, plus a null-query search. Its answer left raw cite-index tags in the text. inv1 cost $0.097 and agg1 $0.047. All final figures were identical, so the effect is on call economy and disclosure, and each side rests on one rollout.
verdict: confounded

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: No candidate touched them. Both remain empty. The editors declined to store the figures because no run read FY2022 capex or revenue from an opened filing.
observed: Not applicable.
verdict: no observed effect

## Transferable lesson
- **cue**: A multi-year ratio question (FCF margin, payout, margin trend) where the earliest year is distorted by a discontinued operation or wind-down, where sec.gov fetches return 403, and where some inputs are reachable only through search excerpts or aggregator pages.
- **lesson**: In the SKILL.md for the multi-year ratio, require three things. (1) Name the exact line used for each input. (2) Give a source-type label per input (opened filing, search excerpt, or third-party page). A year whose input came only from an aggregator or was backed out from a percentage must be named. (3) Report the headline on the stated formula, then flag the distorted year, with the cause and the comparable-year change shown separately. In tool_guidance.md, say to go straight to web_search after a 403, to pass a non-empty query, and to cite only URLs that were seen. Do not embed the task's figures in the skill.
- **evidence**: Skill row and tool_guidance row. All four runs reached the same figures (224.16% / 11.26% / 12.75%), so the observed contrast is only in disclosure and call economy. Candidates with the guidance (inv1, agg1) avoided the edgar_search 403 chains that base1 and dom1 hit, and all three skill runs gave pp-per-step and outlier-excluded trend wording. inv1 and agg1 labelled source types, and inv1 named the third-party basis of FY2022 capex. Even with the guidance, inv1 issued a null-query search and agg1 cited unopened URLs, so it only partly enforces the rules.
- **confidence**: low. One rollout per candidate, bundled edits, identical numbers across runs, and the guidance was not fully followed.
