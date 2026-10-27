# q04

- adopted: `agg1`
- components: 1 skill; 3,072 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, agg1
change: Went from empty to a rule set. A search snippet is a lead, not evidence. Open each primary 8-K EX-99.1 with parse_html_page and ask retrieve_information one question per document. Cite only opened documents. Write plain text with no citation markup. Follow the question's output format, one line per period. inv1 also stated that guidance for quarter N sits in the quarter N-1 release and carried the four AMD URLs and figures as a lead. agg1 dropped the task lead and the N-1 mapping and moved them into the skill.
observed: base1 ran four web_searches, opened no filing, listed an unopened ir.amd.com press-release URL as a source, and leaked raw cite markup in the answer. inv1 and agg1 parsed all four releases and retrieved each Outlook sentence ("$X billion, plus or minus $300 million") before submitting, in 3 and 4 turns. dom1 had no tool_guidance but also parsed and retrieved, because its skill said to read the filing text. The retrieval behavior therefore appears under either carrier and the two cannot be separated. All runs reached the same midpoints ($5.7B, $6.7B, $7.5B, $7.1B) and the same ranges, so the effect was on verification and sourcing, not the numbers.
verdict: confounded

component: skills/guidance_range_width/SKILL.md (plus trigger line in systemprompt.md)
candidates: dom1, agg1
change: Added an on-demand skill. Guidance for quarter N comes from the quarter N-1 release. For "plus or minus" wording, width = 2Y / midpoint. Convert units before building low and high. The question's format string controls. Verify each midpoint in retrieved text. It carries the four release URLs and the expected figures as an unverified lead. systemprompt.md gained one line telling the agent to load it.
observed: dom1 and agg1 loaded the skill in turn 1, then parsed the four releases, retrieved each outlook sentence and submitted in 4 turns. inv1 reached the same document set in 3 turns without the skill, because its tool_guidance carried the same URLs. The skill therefore added a turn and no visible change in the figures. Its URL lead may explain the direct route. dom1's skill-only run shows that verification can happen from the skill alone.
verdict: no observed effect

component: systemprompt.md (format-deference sentence)
candidates: dom1, agg1
change: Changed the default "at least two decimal places" instruction to defer to a format the question prescribes ("unless the question prescribes a format").
observed: base1 used 10.53/8.96/8.00/8.45 against the question's "[X.X]%" format. dom1 and agg1 gave 10.5/9.0/8.0/8.5 in the requested one-line-per-period layout. inv1 had no prompt change but a tool_guidance "follow the format exactly" rule. It gave one-decimal lines and added a two-decimal note. The format was followed in all three edited runs. The prompt edit was never isolated from the tool_guidance format rule.
verdict: confounded

component: systemprompt.md (skill trigger line)
candidates: dom1, agg1
change: Added one line telling the agent to call load_skill with `guidance_range_width` for guidance-range-width questions.
observed: Both candidates called load_skill as their first action. No skill-equipped run lacks the trigger, so its separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A multi-period question asks about guidance (a range or a comparison) with an exact answer format. Each period's guide is printed in the prior period's earnings release. The base agent answers from search snippets, opens no filing, and defaults to two decimals.
- **lesson**: In tool_guidance.md, require one parse_html_page and one targeted retrieve_information per period-specific release (guidance for N sits in the N-1 release), cite only releases actually opened, and follow the question's prescribed format over the system prompt's two-decimal default. If the question's format clashes with the system prompt's rounding default, edit systemprompt.md to defer to the question.
- **evidence**: The tool_guidance.md row and the format-deference row. base1 searched only, listed an unopened source and printed two-decimal percentages against a "[X.X]%" format. inv1, dom1 and agg1 all parsed the four releases and retrieved each outlook sentence, and all gave one-decimal lines. The skill row shows the skill added no visible benefit beyond what tool_guidance or the skill's own text provided.
- **confidence**: low. Each candidate was a single rollout, and every run reached the same numbers. The evidence shows a difference in verification, sourcing and format compliance, not in the figures. Which carrier (tool_guidance, skill or prompt edit) produced it is not isolated.
