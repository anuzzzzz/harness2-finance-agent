# q24

- adopted: `agg1`
- components: 0 skills; 2,344 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: agg1 (inv1 and dom1 left it empty)
change: Went from empty to five bullets. A snippet or result title is a lead, and figures must be retrieved from an opened primary filing before submission. If web_search returns nothing, retry with a non-empty query or use edgar_search. Cite only documents opened and retrieved from. If the as-of date falls after the latest balance-sheet date, say which date the figures come from. Write plain text with no citation markup.
observed: The only contrast is between runs on the unedited harness and agg1. base1 and inv1 (no guidance) each parsed the 10-K and retrieved the Note 9 table (4 turns), and both produced 7,500 with a date caveat. dom1 (no guidance) ended in 2 turns after a null-query web_search. It never parsed the filing, asserted 8,500 / 8,433 from snippets, and listed the unopened Financial_Report.xlsx as a source. agg1 (with guidance) still issued a null-query web_search in turn 2, so the retry rule did not stop that. It then parsed the 10-K, retrieved the debt table, listed only the 10-K, and reported the same 7,500. The guidance may have helped agg1 verify, but base1 and inv1 verified without it. That makes this one run, with an unexplained dom1 shortcut, and no run shows the rule changing behavior. All runs reached 7,500.
verdict: confounded

component: systemprompt.md, skills/, LongTermMEMORY.md, guardrails.md
candidates: none
change: Left unchanged in every candidate. inv1 and dom1 submitted no edits at all (KEEP_BASE).
observed: Nothing to compare. The task was a single-table lookup in one 10-K, and the unedited runs completed it in 2–4 turns.
verdict: no observed effect

## Transferable lesson
- **cue**: A simple lookup of one table figure in a single filing (for example a debt principal total or a subtotal after excluding one line). Unedited runs usually open the filing, but one run answered from search-result titles or snippets and listed a spreadsheet it never opened.
- **lesson**: In tool_guidance.md, state that a figure must be retrieved with retrieve_information from a document opened with parse_html_page before it is submitted. Allow only opened documents as sources, which excludes Financial_Report.xlsx or mirrors seen only in search results. Also state the as-of-date rule: if the question's date is later than the filing's balance-sheet date, name the date the figures come from. Do not add a skill for a one-table lookup.
- **evidence**: tool_guidance.md row (confounded). Among unedited runs, dom1 took 2 turns, never parsed the 10-K and cited an unopened xlsx, while base1 and inv1 parsed and retrieved. agg1, with the rule, parsed, retrieved and listed one source. All four runs gave 7,500, so the contrast concerns sourcing and verification and not the number.
- **confidence**: low. The failure appeared in 1 of 3 unedited runs, agg1 is a single rollout, and agg1 still made the null-query search that the guidance was meant to discourage.
