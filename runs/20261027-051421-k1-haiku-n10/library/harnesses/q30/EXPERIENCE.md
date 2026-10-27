# q30

- adopted: `agg1`
- components: 1 skill; 3,059 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: tool_guidance.md
candidates: inv1, agg1
change: Went from empty to a bounded fallback for SEC 403s. It says to pass a non-empty query, not to retry edgar_search after one 403, to make one or two targeted web_searches, to cite only URLs seen in tool output, and to disclose whether a figure came from an opened filing or an excerpt. agg1 added "plain text, no raw citation tags".
observed: base1 hit edgar_search 403, then a null-query web_search, then parse_html_page 403, and cited an 8-K URL it had not seen. inv1 made no failed fetch, ran three targeted web_searches and submitted in 2 turns. It disclosed the excerpt basis and left raw cite tags in its answer despite the guidance. agg1 still made a failed web_search with a null query and an edgar_search 403 (turn 2), even though the guidance forbade both, and also disclosed the excerpt basis. dom1 had no guidance and made one edgar_search 403 and one parse_html_page 403, then a retrieve_information KeyError. All runs reached the same 85,945 thousand headline. Each candidate has one rollout and the edit was bundled with the skill, so the effect is confounded.
verdict: confounded

component: skills/convertible_dilution_lookup/SKILL.md
candidates: inv1, agg1
change: Added a skill for "maximum shares from convertible notes". The aggregate comes from the EPS anti-dilutive table's if-converted line. It must then be reconciled to per-series principal × conversion rate from the debt note. Single-series issuance maxima must not be used as the total. inv1 embedded the 85,945 figure as an unconfirmed task fact. agg1 removed that figure and added: use principal outstanding at the date, exclude series repaid before it, and a 10-Q comparative column can supply year-end principal.
observed: inv1 searched per-series principals and rates and summed them to 85,945,095, matching the EPS line. This reconciliation is the strongest evidence in the record. agg1 followed the same procedure but did not find the year-end 2026 principal. Its 2026 estimate was $487.3M (a stale reduction from the 2024 repurchase), so its sum was 96,359 thousand and it reported "does not fully reconcile". It still headlined 85,945. base1 never attempted a reconciliation and mixed in the 2030 notes' 44.8M ceiling unreconciled. inv1 had the figure embedded in its skill and agg1 did not, which may explain why inv1 reconciled and agg1 did not. One rollout each, so confounded.
verdict: confounded

component: skills/convertible_notes_dilution/SKILL.md
candidates: dom1
change: Added a similar skill with the same hierarchy (EPS table, then debt note, then issuance 8-K) and a reconciliation step. It embedded the 85,945 figure and the 44.8M 2030 ceiling as a task fact.
observed: dom1 loaded it at turn 1 but could not open the 10-K, failed to find the 2025/2026/2027 year-end principal, and ended with a partial reconciliation. It estimated 2027 using the original issue size, said it could not reconcile, and still headlined 85,945. It repeated the 44.8M figure "from the research desk's notes", so the embedded fact leaked into the answer. It was also the cheapest run, at $0.025.
verdict: confounded

component: systemprompt.md (trigger line to load the convertible skill)
candidates: inv1, dom1, agg1
change: Added one line telling the agent to load the convertible dilution skill for dilutive impact or maximum shares questions.
observed: All three candidates called load_skill as their first action (turn 1). base1 never loaded a skill. The trigger works mechanically. The value of the skill itself is confounded.
verdict: helped

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: No candidate changed them. Both stayed empty. The 85,945 figure was placed in skill text (inv1, dom1) rather than in memory.
observed: Not applicable. Embedded figures in dom1 showed up in the final answer as unverified context.
verdict: no observed effect

## Transferable lesson
- **cue**: A "total shares / maximum dilution from instruments outstanding at a date" question where the 10-K aggregate line is reachable only through search excerpts, and per-series terms (principal, conversion rate) are spread over several filings.
- **lesson**: In the SKILL.md for dilution or conversion-share lookups, require a per-series cross-check against the aggregate anti-dilutive/if-converted line. Name where each series' year-end principal can be found (the 10-K debt note, or the comparative column of the next 10-Q) and state that issuance-8-K maxima are not totals. Add an answer-contract line: if the series do not sum to the aggregate, report the gap and say which series' principal is unconfirmed, and headline the reported aggregate. Do not put the task's own figure in the skill; two of three skill runs repeated embedded figures without re-verifying them.
- **evidence**: Skill rows. inv1's per-series search summed to 85,945,095, matching the EPS table. agg1 and dom1 used the same procedure but failed to find year-end 2026/2027 principal and ended unreconciled, with 96,359 thousand and an unverified partial sum respectively. base1 attempted no reconciliation and mixed in a single-series ceiling. All runs reached the same headline, 85,945 thousand.
- **confidence**: low. One rollout per candidate, the skill was bundled with the trigger line and tool guidance, and the headline number was the same in every run. The record shows only a difference in reconciliation quality, and the inv1 success may owe something to its embedded figure.
