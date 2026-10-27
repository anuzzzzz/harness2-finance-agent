# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal period. Use edgar_search with company and date filters. If web_search returns 0 results or errors, retry once with a short, non-empty query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (store it under a clear key), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and basis in the retrieved text. Use input_character_ranges on long filings rather than re-reading everything.
- If a retrieval answer is truncated, or says a number was derived rather than disclosed, run a second targeted retrieval (the exact table row or the note's own sentence) before relying on it. When you derive a figure from components, reconcile it to any disclosed total and say which figures are disclosed and which are derived.
- Cite only documents you opened and retrieved from. Do not list a filing (e.g. a press release) that you only saw in search results or used as background.
- Write the final answer in plain text with no citation markup: the figure, period and unit, how it was derived, and the source of each figure. Submit with submit_final_result as soon as the figure is verified.
