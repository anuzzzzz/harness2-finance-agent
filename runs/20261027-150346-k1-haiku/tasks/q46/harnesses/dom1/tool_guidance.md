# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with company and date filters. If web_search returns nothing, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- A search snippet is a lead, not evidence. Open the primary document with parse_html_page, then ask retrieve_information one targeted question at a time. Confirm each figure's period, unit and basis in the retrieved text. For a multi-part question, retrieve each part (for example the acquisitions note, the cash-flow line and the revenue table) separately and check that the output was not cut off.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit.
- Cite only documents you opened and retrieved from. Do not list a filing, shareholder letter or 10-Q seen only in search results. Do not attribute a claim to a document you did not retrieve it from. Do not state a fact (for example about a product or deal) that no retrieved text supports.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State each figure with its period, unit and source, then the calculation, then the conclusion.
