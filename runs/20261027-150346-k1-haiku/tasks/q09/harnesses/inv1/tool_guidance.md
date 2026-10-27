# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1 earnings release), fiscal period. Prefer edgar_search with company and date filters over question-worded web_search. If web_search returns 0 results, retry once with a shorter query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Before any figure enters a calculation, open the primary document with parse_html_page (store it under a clear key), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text. Do not say a filing "reports" or "states" a figure you did not retrieve. If a document cannot be fetched, say so and name where the figure came from.
- parse_html_page cannot read PDFs. Use the HTML 8-K EX-99.1 or the 10-K/10-Q instead.
- Use input_character_ranges on long filings rather than re-reading everything.
- When the company states a rounded figure (e.g. "26.9%"), use that stated figure for the comparison, and mention an unrounded recomputation only as a labelled cross-check. Carry full precision otherwise and round only the final result.
- Write the final answer in plain text with no citation markup. State each input with its period, unit and source, then the calculation.
- Reserve budget: once every input is verified in primary text, submit with submit_final_result immediately.
