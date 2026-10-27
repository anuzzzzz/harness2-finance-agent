# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with company and date filters. If web_search returns nothing, retry once with a short non-empty query (never null or empty), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary filing with parse_html_page (one clear key), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and line-item name in the retrieved text.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K exhibit.
- Cite only documents you opened and retrieved from. Do not list a press release, article or PDF seen only in search results.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State each figure with its period, unit and source, then the calculation, then the conclusion. Submit with submit_final_result once the figures are verified in the primary text.
