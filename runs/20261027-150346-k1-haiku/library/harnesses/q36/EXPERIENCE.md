# q36

- adopted: `agg1`
- components: 0 skills; 4,715 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, open primary docs with parse_html_page then retrieve_information, no null or empty queries, cite only opened documents, plain text with no citation markup)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. Snippets are leads only, and each figure must be retrieved from an opened press release, 425 or 8-K. Only opened documents may be listed as sources. The answer is plain text. Empty queries are banned.
observed: base1 opened no document, answered from snippets, listed five unopened sources including a PDF, and called $2.36B "more precise" without any opened support. Its first web_search returned nothing, and its null-query search was the second search. inv1, dom1 and agg1 all parsed the Rocket press release or the Redfin 8-K and 425 and retrieved the $12.50, $1.75B and $2.4B figures from opened text. None leaked markup. dom1 still made one empty-query web_search despite the ban. inv1 and dom1 still listed the unopened investor-presentation PDF, and inv1 labelled it "search snippet only". agg1 listed only opened documents. Every edited candidate also carried a lead block with URLs, which may explain the direct route, so the rules cannot be separated from the leads. Each is one rollout.
verdict: confounded

component: tool_guidance.md (deal-price procedure: consideration form, exchange ratio and implied acquirer price, equity value cross-check, EV composition, pending status, conflicting-figure handling)
candidates: inv1, agg1 (dom1 carried the same content in a skill)
change: Added explicit steps for a stock deal. State the exchange ratio, say the value floats with the acquirer's share price, and check equity value divided by price. Say the deal is pending as of the as-of date. Report both values when two sources differ on EV. agg1 added "lead with the figure confirmed in opened text, and do not call one more precise unless an opened document supports it".
observed: All three edited runs reported the pending status, the fixed 0.7926 ratio, the implied RKT price of about $15.77 and the $1.75B / $12.50 share-count check. base1 gave status and ratio from snippets but did no checks from opened text. The EV treatment diverged. inv1 still called $2.36B "precise" from a snippet it could not open, which the rule had discouraged. agg1 led with the opened $2.4B and flagged $2.36B as unverified, but dropped it from its sources. agg1's headline EV is $2.4B and omits any $2.36B figure from the main answer. base1, inv1 and dom1 all reported $2.36B as the main EV. Which EV is correct is not settled by this record. The rule's effect on checks looks real, but it is bundled with the leads and each candidate is a single rollout.
verdict: confounded

component: tool_guidance.md (do not parse a very large S-4 for headline terms; use input_character_ranges)
candidates: agg1 (inv1 parsed the S-4 and had no such rule)
change: Told the agent not to parse the 1.1M-character S-4 when the press release, 425 or 8-K already state the terms.
observed: inv1 parsed the S-4 and spent two retrievals finding no EV or price in it, over 6 turns and $0.278. agg1 skipped the S-4 and finished in 3 turns at $0.005. The 8-K, 425 and press release already held the terms. This is a cost contrast between two single rollouts, and agg1 also carried the leads that pointed at the 8-K directly.
verdict: confounded

component: tool_guidance.md (task-fact lead block: press release, 425 FAQ, 8-K and S-4 URLs, reported figures labelled "re-confirm")
candidates: inv1, dom1, agg1
change: Listed the primary-document URLs and the snippet-derived figures, including the $2.36B versus $2.4B discrepancy.
observed: All three skipped discovery and parsed the documents in turn 1 or 2. base1 never opened anything. All three re-retrieved the figures from opened text, and the values matched the leads. The leads saved turns, and the $2.36B vs $2.4B cue pushed inv1 and dom1 to report both figures. The task-specific content has no transfer value.
verdict: helped

component: skills/announced_acquisition_terms/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill for announced-deal pricing, with the status check, the stock exchange-ratio check, the equity value cross-check and the EV reconciliation. It carries the Redfin leads. systemprompt.md gained a line telling the agent to load it.
observed: dom1 made an empty web_search, loaded the skill, made a null-query search, parsed the press release and FAQ, and ran two retrievals. It did not parse the 8-K or 425 that carries the EV sentence. It submitted in 4 turns with the same figures as the skill-free runs. It listed the unopened PDF as a source with a snippet-only note. The skill's rule that the EV bridge be retrieved was not followed, because no bridge was found. No behavior is visible that the skill-free inv1 and agg1 lacked, and the trigger's separate effect is not shown.
verdict: no observed effect

component: systemprompt.md (trigger line only)
candidates: dom1
change: One sentence telling the agent to call load_skill with `announced_acquisition_terms` for acquisition-price questions.
observed: dom1 loaded the skill after one empty search. No skill-equipped run lacks the trigger.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A deal-terms question ("what price was X acquired at", with equity value and enterprise value) where the target's and acquirer's filings print different figures for the same measure. One figure appears only in an investor-presentation PDF that parse_html_page cannot read. The base run answers from snippets and lists unopened sources.
- **lesson**: In tool_guidance.md, require every headline deal figure (per-share value, exchange ratio, equity value, EV) to be retrieved from an opened HTML document, such as the acquirer's 8-K EX-99.1 or the target's 425 and merger 8-K. State that a figure seen only in a PDF snippet is reported as an unverified lead in the text and is not listed in sources, and that no figure is called "more precise" without opened support. Also say not to parse a very large S-4 for headline terms when the press release, 425 or 8-K already carry them.
- **evidence**: The general-rules, deal-price-procedure and S-4 rows. base1 opened nothing and listed five unopened sources. The three edited runs all retrieved the figures from opened exhibits. agg1, which carried the strictest "opened-only" wording, listed only opened sources and flagged $2.36B as unverified. inv1 and dom1 still listed the unopened PDF, and inv1 asserted "precise" from a snippet. inv1's S-4 parse cost two empty retrievals and $0.278 against agg1's $0.005 over 3 turns.
- **confidence**: low. Each candidate is one rollout, the rules were bundled with a lead block in every edited run, and the correct EV is not settled by the record.
