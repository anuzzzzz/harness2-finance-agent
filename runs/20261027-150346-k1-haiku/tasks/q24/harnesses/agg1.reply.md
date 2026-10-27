<file path="tool_guidance.md">
# Tool use

- A search snippet or result title is a lead, not evidence. Before submitting, open the primary filing with parse_html_page (one clear key per document) and confirm each figure, period and unit with retrieve_information. Do not submit figures you have not retrieved from an opened document.
- If web_search returns 0 results, retry once with a short non-empty query (never null), or go straight to edgar_search with company and date filters.
- Cite only documents you opened and retrieved from. Do not list a spreadsheet, mirror or filing seen only in search results.
- If the question's as-of date falls between filings or after the latest balance-sheet date, say which date the figures are from and what the filing says about later changes.
- Write the final answer in plain text with no citation markup.
</file>

<notes>
kept -> tool_guidance.md (new, short; no candidate changed anything, so this is my own addition) -> dom1's rollout, with no edit, ran 2 turns, opened no filing and submitted 8,500 / 8,433 figures with no retrieval. It also listed Financial_Report.xlsx as a source without opening it. base1 and inv1 both parsed the 10-K and retrieved Note 9, so the failure showed in 1 of 3 runs on the same unmodified harness. The same pattern recurs in the library entries (q44, q45, q47).
dropped -> inv1 edit (KEEP_BASE) -> base1 and inv1 both took 4 turns and gave $7,500M with a correct date caveat. No moment shows a rule would have changed their behaviour.
dropped -> dom1 edit (KEEP_BASE) -> its unrealised risk, 8-Ks between Jan 31 and Mar 10, was seen in 1 rollout only. I handled it with a single as-of-date line, not a skill.
dropped -> any skill -> this is a single-table lookup and a skill would cost context for no observed gain.
</notes>