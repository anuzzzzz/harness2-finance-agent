# q49

- adopted: `agg1`
- components: 0 skills; 5,467 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (open-primary-document, cite-only-opened, plain-text, as-of exclusion rules)
candidates: inv1, agg1 (dom1 carried a shorter four-bullet version)
change: Went from empty to a rule set. Snippets are leads only. The releases are opened with parse_html_page and queried with retrieve_information. Only opened documents may be cited, and the answer is plain text. inv1 and agg1 added a rule to ignore filings dated after April 7, 2025. They also added a rule to judge each fiscal year against both the initial and the final guidance and to state the count under each reading.
observed: base1 made only web_search calls and opened nothing. It leaked raw citation markup and listed unopened PDFs and articles. It also compared actuals only with the final raised range, so it never saw that FY2024 only matched the top of the initial range. inv1, dom1 and agg1 all parsed the Q4 FY2022, Q3 FY2023, Q4 FY2023, Q3 FY2024, Q4 FY2024 and Q3 FY2025 releases and retrieved the guidance and actuals from them. Their sources list only opened releases, and none leaked markup. All three gave the same counts: 2 of 2 against final guidance, and 1 of 2 against initial guidance because FY2024 sat at the top of the 4-6% range. All three gave the same FY2025 range (down 8% to down 7%, about $4.16 to $4.20 derived). The difference between base and edited runs is in verification, sourcing and the dual-benchmark framing. The rules were bundled with a task-lead block in every edited run, so the cause cannot be isolated.
verdict: confounded

component: tool_guidance.md (task-fact lead block with the General Mills release URLs)
candidates: inv1, agg1
change: Listed the SEC 8-K EX-99.1 URLs for the Q3 and Q4 releases for FY2023 to FY2025. agg1 also added the Q4 FY2022 URL, which inv1 had to find with edgar_search. Both labelled the list "re-confirm in the opened text".
observed: agg1 parsed all six releases in turn 1 and finished in 4 turns. inv1 needed an edgar_search for the June 2022 release and finished in 6 turns. dom1 had no URL for it and used 9 turns. The leads saved turns and did not change any figure.
verdict: helped

component: skills/guidance_beat_count_multi_year/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill covering the multi-year beat-count procedure. It reports the initial and final benchmarks, compares constant currency with constant currency, says "at the top end" is not "above", and labels derived dollar ranges. It also carries leads. systemprompt.md gained a line telling the agent to load it.
observed: dom1 loaded the skill first and then took 9 turns, against 6 for inv1 and 4 for agg1, which had no skill. The figures and the dual-benchmark framing were the same across all three. dom1 added a 2024 initial-range dollar derivation, and agg1 and inv1 had the same ones. No behavior is visible that the skill-free runs lacked. The skill was bundled with its own short tool_guidance, so the trigger line's separate effect is not shown.
verdict: no observed effect

component: systemprompt.md (trigger line)
candidates: dom1
change: One sentence telling the agent to call load_skill with `guidance_beat_count_multi_year` for beat-count questions.
observed: dom1 called load_skill as its first action. No skill-equipped run lacks the trigger.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A "how many times did the company beat its own guidance over the last N years, and what is the current guidance" question. The base run answers from search snippets. The guidance is revised during each year, and the Q4 release of one year holds both that year's actual and the next year's initial outlook.
- **lesson**: In tool_guidance.md, require opening the Q4 release for each year in the window and the last pre-result release (Q3), then retrieving the low and high ends from each. State the count against both the initial and the final guidance, say which one the headline uses, and say that "at the top end" is not "above". Also require that a quarterly-consensus beat count is flagged as a different measure and not invented. Cite only the releases actually opened. Do not add a skill for this. Keep the procedure in always-on tool_guidance.
- **evidence**: The tool_guidance.md row, where base1 used only snippets, compared against the final range alone and listed unopened sources. inv1, dom1 and agg1 opened every release and showed the FY2024 split (a beat of the final 4-5% range, at the top of the initial 4-6% range). The skill rows, where dom1's skill run took 9 turns against 4 and 6 for the skill-free runs with the same answer.
- **confidence**: low. Each candidate is one rollout, the rules were bundled with a lead block in every edited run, and all three edited runs reached the same figures.
