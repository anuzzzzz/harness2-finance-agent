# Tool use

- A search snippet or result title is a lead, not evidence. Before submitting, open the primary filing with parse_html_page (one clear key per document) and confirm each figure, period and unit with retrieve_information. Do not submit figures you have not retrieved from an opened document.
- If web_search returns 0 results, retry once with a short non-empty query (never null), or go straight to edgar_search with company and date filters.
- Cite only documents you opened and retrieved from. Do not list a spreadsheet, mirror or filing seen only in search results.
- If the question's as-of date falls between filings or after the latest balance-sheet date, say which date the figures are from and what the filing says about later changes.
- Write the final answer in plain text with no citation markup.
