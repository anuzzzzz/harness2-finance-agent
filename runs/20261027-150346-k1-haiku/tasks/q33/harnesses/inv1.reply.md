<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with company and date filters. If web_search returns nothing, retry once with a short non-empty query. Never send an empty or null query. Then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document). Then ask retrieve_information one targeted question at a time, using input_character_ranges on long filings. Confirm each figure's period, unit and basis in the retrieved text.
- Before collecting inputs, write down which inputs the requested calculation actually needs. For a what-if on a rate or a price change, the change is the delta times the balance, so a current average rate may not be needed. Do not import a third-party or snippet figure the arithmetic does not need. If an input the filing does not state is needed, say so plainly and label any outside estimate as such.
- When the question's wording allows two readings (for example, "3% higher" as 3 percentage points or as a 3% relative increase), pick the most natural reading, state it, and give the other as a labelled alternate with its figure. Do not hide the choice.
- For an after-tax figure, take the tax line or effective rate from the opened income statement or tax note. Do not use a snippet. When the base is a loss, say what the percentage means (the loss widens or narrows).
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit.
- Cite only documents you opened and retrieved from. Do not list a page seen only in a search result, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State each figure with its period, unit and source, then the calculation unrounded until the end, then the conclusion in the form the question asks for. Before submitting, re-check each figure in the calculation against the retrieved text. Submit with submit_final_result as soon as the figures are verified.

Leads for this task (Boeing FY2024; verified in the opened 10-K in an earlier run, so re-confirm in the text):
- Source: the FY2024 10-K, https://www.sec.gov/Archives/edgar/data/12927/000001292725000015/ba-20241231.htm (about 477K characters; use targeted retrievals).
- Total debt at Dec 31, 2024 is $53,864M ($53.9B in the MD&A, of which about $1.3B is short-term). The debt note (Note 16) gives the detail. Do not confuse this with the $54,369M "long-term debt including current portion" line in the Capital Resources table, which is a different figure.
- 2024 net loss attributable to Boeing shareholders is $(11,817)M. Total net loss is $(11,829)M. Interest and debt expense is $2,725M.
- The 10-K states no weighted-average interest rate, only coupon ranges by debt category. The incremental-interest calculation (debt x 3 points) needs no current rate. A third-party rate (about 5.3%) came from search snippets and was never opened, so it is not a primary figure.
- Get the pre-tax loss and the income tax line from the 10-K income statement for the after-tax version.
</file>

<notes>
Moments from base1:
- It issued a null-query web_search in turn 2.
- It retrieved a 10-K that has no weighted-average rate, then fetched a third-party page (stock-analysis-on.net). Its final answer quoted 5.32% and a 3.10% effective tax rate from FY2024 snippets of a DCF page it never opened. It also listed that page and the Financial_Report.xlsx as sources, and it leaked <cite> markup. The 5.32% figure was not even needed, because the delta is debt x 3 points.
- The agent did not state the reading of "3% higher" (percentage points) as a choice.
- All edits go in tool_guidance.md, following the library pattern of similar tasks. The rules cover: decide the needed inputs first, label ambiguity, take tax from opened statements, cite only opened documents, and leave out citation markup. A leads block carries verified task facts (debt $53,864M, loss $(11,817)M, interest expense $2,725M, no weighted-average rate in the 10-K, the look-alike $54,369M line). No skill is added, since the procedure is short.
</notes>