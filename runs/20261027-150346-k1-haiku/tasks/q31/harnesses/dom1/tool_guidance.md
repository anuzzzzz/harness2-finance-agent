# Tool use

- A search snippet or result title is a lead, not evidence. Open the primary document (10-K, or 8-K EX-99.1 release) with parse_html_page and confirm each figure, period and unit with retrieve_information. If web_search returns nothing, use edgar_search with company and date filters instead of an empty query.
- Cite only documents you opened and retrieved from. A page that failed to load (for example an HTTP 403) or that you saw only in search results must not be listed as a source.
- Write the final answer in plain text with no citation markup.
