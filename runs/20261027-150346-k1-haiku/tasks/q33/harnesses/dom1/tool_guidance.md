# Tool use

- A search snippet or result title is a lead, not evidence. Open the primary document (10-K, 10-Q, 8-K exhibit) with parse_html_page, then confirm each figure, period and unit with retrieve_information. Never send an empty or null query to web_search; use edgar_search with company and date filters.
- Prefer filing figures to third-party aggregator pages. If a third-party figure is used, label it as such.
- Cite only documents you opened and retrieved from. Do not list a page or spreadsheet seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags.
