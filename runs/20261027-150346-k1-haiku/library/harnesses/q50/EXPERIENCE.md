# q50

- adopted: `agg1`
- components: 0 skills; 4,495 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (open-primary-document, cite-only-opened, plain-text, no-empty-query rules)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. A snippet is a lead, not evidence. The guidance release (prior quarter) and the actual release must each be opened with parse_html_page and queried with retrieve_information. Only opened documents may be cited. The answer is plain text. All three also covered the as-of window, implied value = midpoint x margin, and taking actual non-GAAP gross profit from the reconciliation table.
observed: base1 made only web_search calls and opened nothing. It used the guided margins (53.5% for Q3, 54% for Q4) from snippets without opening a release. It listed unopened sources and gave two-decimal percentages. inv1, dom1 and agg1 each parsed all five releases, including the Feb 2025 Q4 release, and retrieved the guide text and the reconciliation-table gross profit. Each listed only the five opened releases. The per-quarter figures in all runs were the same as base1's: guides of 52/53/53.5/54%, actuals of 2,861/3,101/3,657/4,140, and beats of 1.89/2.65/2.02/2.22%. The effect was on verification and sourcing, not the numbers. Every edited run also carried release-URL leads, so the rules and the leads cannot be separated.
verdict: confounded

component: tool_guidance.md (AMD release URL leads, including the Q4 2024 exhibit URL)
candidates: inv1, agg1 (dom1 put the same leads in its skill)
change: Listed the four 2024 8-K EX-99.1 URLs. agg1 also listed the Q4 2024 HTML exhibit URL. inv1 told the agent to find that release with edgar_search. inv1 also gave unverified guide figures, labelled "re-confirm".
observed: agg1 parsed all five releases in turn 1 and finished in 3 turns. inv1 needed one edgar_search for the Feb 2025 release and took 4 turns. dom1 loaded a skill first and took 7 turns, with an edgar_search and separate actuals retrievals. The leads saved turns. In inv1 the retrieved guide text matched the lead figures, so the leads changed no number.
verdict: helped

component: tool_guidance.md (format rule: follow the prescribed decimals and layout)
candidates: agg1, dom1 (inv1 had a weaker "match the format" bullet)
change: Told the agent to use the number of decimals the question shows ("X.X %") and to show the unrounded working beneath it.
observed: dom1 printed one-decimal percentages (1.9, 2.6, 2.0, 2.2) and a whole-dollar Q3 ($73M), with the working below. agg1 still printed two decimals (1.89 %) and used the literal label "QX" on every line instead of Q1 to Q4. inv1 used Q1 to Q4 labels and two decimals. The rule changed output in only one of three runs. agg1's literal "QX" labels are a presentation defect it did not avoid.
verdict: confounded

component: skills/guidance_implied_gross_profit/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill covering the procedure: the N-1 release holds quarter N's guide, margins are quoted exactly, actuals come from the reconciliation table, and the answer contract. It carried the AMD leads. systemprompt.md gained a line telling the agent to load it.
observed: dom1 loaded the skill first and took 7 turns, against 4 for inv1 and 3 for agg1, which had no skill. Its figures and sources matched theirs. dom1 also ran separate retrievals for the actuals, which the others folded into the guide retrievals. The only visible difference from the skill is the one-decimal format. That format rule was also in dom1's always-on tool_guidance, so it cannot be attributed to the skill alone.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A multi-quarter "beat or miss versus the prior quarter's guidance (revenue midpoint x margin guide)" question with a prescribed output format, such as "QX - $XXX million (X.X %)". The base run answers from search snippets, opens no earnings release, and lists unopened sources.
- **lesson**: In tool_guidance.md, require opening two 8-K EX-99.1 releases per period, the prior-quarter release for the guide and the period's own release for the actual dollars from the reconciliation table. Give the release URLs as leads so the agent skips discovery. Add an explicit format rule: copy the question's prescribed decimals and label each line with its real quarter (Q1, Q2, ...), never a literal placeholder like "QX", and show unrounded working beneath. Keep this procedure in always-on tool_guidance and do not add a skill.
- **evidence**: Row 1. base1 opened nothing, while inv1, dom1 and agg1 each opened all five releases and listed only those. Row 2. agg1, with the full URL list, finished in 3 turns, inv1 in 4, and dom1 with a skill in 7. Row 3. The format rule held in only one of three runs: dom1 used one decimal, while agg1 printed two decimals with "QX" labels.
- **confidence**: low. The edited rules were bundled with leads in every edited run, there is one rollout per candidate, and all runs produced the same numbers, so the evidence concerns verification, turn count and formatting rather than accuracy.
