# q04

- adopted: `agg1`
- components: 0 skills; 4,160 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: tool_guidance.md (generic "enough evidence = primary document actually opened" rule, parallel opening of one release per guided quarter, pre-submit re-check)
candidates: inv1, dom1, agg1
change: All three added a tool guide defining verified evidence as figures read from opened primary documents. All also added a forward-guidance recipe: the outlook for quarter N sits in the quarter N-1 release, range % = width / midpoint. inv1 and agg1 required opening the documents; dom1 allowed a verbatim snippet to count as evidence.
observed: base1 ran 4 searches and submitted without opening any filing. inv1 parsed all four releases in parallel at turn 1, retrieved each outlook sentence verbatim at turn 2, and submitted at turn 3 for $0.009. dom1 ran 2 searches and submitted in one turn, never opening a filing, yet its answer says it "checked against the 8-K outlook text". agg1 ran 4 searches and submitted in one turn with no parse or retrieve call. Only inv1 followed the open-the-document rule. All runs reached the same midpoints (5.7, 6.7, 7.5, 7.1, each ±$300M), so the gain is document-backed sourcing and not a different value. dom1's snippet allowance and agg1's non-compliance both left the delivered answer's sourcing as a lead and not as evidence. One rollout per arm.
verdict: confounded

component: tool_guidance.md (output-format rule: question template overrides the default two-decimal rule, no citation markup, no process commentary)
candidates: inv1, dom1, agg1
change: Added a rule saying that when the question gives a template such as "[X.X]%", it is followed exactly, with unrounded working shown above the formatted lines. agg1 also added "including line breaks and labels". inv1 and dom1 banned citation tags and notes on earlier recollections.
observed: base1 gave 10.53%, 8.96%, 8.00%, 8.45% against a one-decimal template. It also left raw cite tags and a "my initial recollection" note in the answer. inv1, dom1 and agg1 all gave 10.5%, 9.0%, 8.0%, 8.5% in the template layout, with unrounded values in the working and no cite markup. The behavior shift is the same in all three, so the rule is the likely cause. There is no run that has the rule alone, since each edited run also carried other changes.
verdict: helped

component: tool_guidance.md (task-specific AMD block with release URLs and snippet-derived midpoints)
candidates: inv1 (URLs and midpoints), dom1 (midpoints only)
change: Listed the four 8-K URLs and the snippet midpoints, flagged as unverified. dom1's version named only the midpoints and accession-less sources.
observed: inv1 went straight to parse_html_page on the four URLs at turn 1 with no search, finishing in 3 turns for $0.009. dom1, which had the midpoints but no URLs, searched and submitted from snippets. agg1, with no block, also searched and submitted from snippets. The URLs likely saved search effort for inv1. They are confounded with inv1's stricter evidence rule, and are not reusable.
verdict: confounded

component: tool_guidance.md (agg1 clause: do not say a figure was "checked against" or "read from" a filing unless a retrieve call returned it)
candidates: agg1
change: Dropped dom1's snippet-evidence allowance and added a rule against claiming a read-through without a retrieve call.
observed: agg1 did not open any filing. Its final answer states plainly that it "did not open the full documents ... figures rest on search-result excerpts". This is an honest disclosure that dom1's answer lacked. The rule did not make the agent open the documents, but it did change what the answer claimed. One rollout.
verdict: helped

## Transferable lesson
- **cue**: A question needs figures from several dated filings, for example guidance stated in each prior-quarter release. The base run answers from search snippets, and the figures are easy to find in the search results.
- **lesson**: In tool_guidance.md, state the open-the-document rule as a turn-1 operation: after a search returns primary-document URLs, call parse_html_page on each in the same turn, then use retrieve_information to quote each figure. Add a companion rule that the answer may only say a figure was "read from" or "checked against" a filing if a retrieve call returned it, and otherwise must say it rests on search excerpts. Do not add a clause that lets a verbatim snippet count as verified evidence. Do not embed company URLs or values in the rule.
- **evidence**: The "tool_guidance generic evidence rule" row and the "agg1 no-claim clause" row. Only inv1 opened all four filings (3 turns, $0.009). dom1, which allowed snippet evidence, and agg1, which required opening, both submitted from snippets with no parse call. dom1's answer overstated its checking and agg1's disclosed that it had not opened the filings. inv1's URL block confounds how much the rule itself caused its behavior.
- **confidence**: low. One rollout per arm, all arms reached the same numbers, and inv1's run was helped by supplied URLs. The evidenced gain is honest sourcing, not a different value, and a rule alone has not been shown to force the opening of documents.
