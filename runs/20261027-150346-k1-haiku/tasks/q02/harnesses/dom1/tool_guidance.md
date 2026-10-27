# Tool use

- A search snippet or result title is a lead, not evidence. Open the primary filing (10-K, 10-Q, 8-K EX-99.1) with parse_html_page, then ask retrieve_information one targeted question per figure. Confirm period, unit and basis in the retrieved text. Use edgar_search with company and date filters to find filings. Never send an empty or null query to web_search.
- parse_html_page cannot read PDFs. Use the HTML filing.
- Cite only documents you opened and retrieved from. Do not list a filing seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags.
