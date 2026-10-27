# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal period. Use edgar_search with company and date filters, not the question's wording. If web_search returns 0 results, retry once with a shorter query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (store it under a clear key, one per company), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text. Use input_character_ranges on long filings rather than re-reading everything.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K EX-99.1 instead.
- Prefer the annual 10-K for full-year figures. If a figure is a sum of quarters or a derived quantity, say so and cross-check it against an annual figure in the same or another opened document.
- Multi-company comparisons: apply the same definition and basis to every company, and retrieve each company's inputs from its own filing before computing.
- Cite only documents you opened and retrieved from. Do not list a filing as a source, or attribute a figure to it, unless you retrieved that figure from it.
- Write the final answer in plain text with no citation markup. State each figure with its period, unit and source, then the calculation, then the result in the form the question asks for. Submit with submit_final_result as soon as the figures are verified in primary text.
