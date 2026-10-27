# q23

- adopted: `agg1`
- components: 0 skills; 3,557 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, open primary documents with parse_html_page then retrieve_information, cite only opened documents, plain text with no citation markup, no empty-query searches)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. Each version says to open the primary filing or release and confirm the wording, and to list only opened sources. All three also say to write plain text. inv1 and agg1 added a "when is X expected" rule: quote the original announcement and the latest filing before the as-of date, and label later status as an update. agg1 also said never to send a null query.
observed: base1 made two web_searches and opened nothing. It leaked <cite> markup, truncated a quote mid-word and listed unopened SEC filings as sources. inv1 opened the 2021 release, the FY24 10-K and two 10-Qs. dom1 opened the release, the 10-K and the Jan 2025 10-Q. Neither leaked markup, and both listed only opened sources. agg1 opened only the Jan 2025 10-Q. It still listed four unopened documents as sources: two 10-Qs, the 10-K and a Shelby Report article. Its earlier-expectation bullets were attributed to filings it never retrieved from. It also issued a null-query web_search despite the rule. All three reached the same core answer: 2025 was the expectation, and the latest 10-Q says production began in fiscal Q2 2025. The rule produced opened-source behavior in inv1 and dom1 but not in agg1, so adherence was uneven. Each is one rollout, and the rules were bundled with other edits.
verdict: confounded

component: tool_guidance.md (embedded task-fact lead block with Smucker URLs and snippet-derived timing)
candidates: inv1
change: Embedded the press-release URL, the Jan 2024 10-Q URL and a hint to check later filings, labelled as snippet-only.
observed: inv1 parsed the press release in turn 1 and used the hint to find the Oct 2024 and Jan 2025 10-Qs. dom1 had no lead and reached the same filings in a similar number of turns. The figures matched in every run. The lead sped up discovery and changed no answer.
verdict: no observed effect

component: tool_guidance.md (fiscal-label conversion rule)
candidates: agg1
change: Added a rule to check the fiscal year-end and convert "second quarter of 2025" to calendar months. It also says not to call a past-tense filing statement inconsistent before checking the fiscal calendar.
observed: agg1's answer converted the label to August to October 2024. inv1 did the same without the rule. dom1, which used a skill that told it to check fiscal years, still left the label unresolved and called it inconsistent with a February 2025 filing date. The conversion appears in two of the three runs and a rule exists only in one, so the evidence is thin. agg1's resolved reading was not itself confirmed from the company's fiscal calendar in an opened document.
verdict: confounded

component: skills/milestone_timing_lookup/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill for "when is X expected" questions. It covers matching the project, ordering the sources (announcement, then latest filing, then later releases), checking calendar versus fiscal wording, reporting original and latest timing, and an answer contract. The trigger sentence was added to systemprompt.md.
observed: dom1 loaded the skill in turn 1, then issued a failed web_search and a null-query web_search. It finished in 8 turns at $0.136, against 7 turns and $0.230 for inv1 (no skill) and 5 turns and $0.036 for agg1. The skill's fiscal-year step did not stop dom1 from leaving the Q2 2025 label unresolved. Its answer also headlined "calendar year 2025" as the expectation, while noting the conflict. No skill-free run isolates a benefit, and the skill was bundled with the tool_guidance edit.
verdict: no observed effect

component: systemprompt.md, LongTermMEMORY.md, guardrails.md
candidates: dom1 (trigger line only); none for the others
change: dom1 added one sentence naming the skill. The other candidates left all three files unchanged.
observed: dom1 called load_skill first. Memory and guardrail files stayed empty.
verdict: no observed effect

## Transferable lesson
- **cue**: A "when is X expected to start or open" question with an as-of date, where later filings before that date report that the event has already happened. The company uses a fiscal year that differs from the calendar year, and the later filing says "second quarter of 2025". The base run answers from snippets and a news item that gives a calendar date.
- **lesson**: In tool_guidance.md, require that the expectation be taken from an opened announcement or periodic filing and quoted with its filing date. Require that the latest filing before the as-of date be opened and its status wording quoted. Add a rule to convert fiscal-quarter labels to calendar months using a fiscal year-end shown in an opened document. Also add that only opened documents may appear in the sources, including the filings cited for earlier expectations.
- **evidence**: The general tool_guidance.md row and the fiscal-label row. base1 opened nothing, leaked markup and listed unopened filings. inv1 and dom1 opened the primary documents and listed only those. agg1 carried the same rule but opened one 10-Q, listed four unopened sources, and issued a null query anyway, so the sources clause needs to be stated explicitly. The fiscal-label conversion appears in inv1 and agg1, but dom1's skill version left it unresolved, so the fiscal rule is only weakly supported.
- **confidence**: low. Each candidate is one rollout, the rules were bundled with leads or a skill in every edited run, and the core answer was the same across all four runs. The evidence concerns sourcing and verification, not accuracy.
