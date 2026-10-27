# Tool use

- A search snippet or result title is a lead, not evidence. Open the primary document (8-K exhibit, Form 425, S-4, 10-K or 10-Q) with parse_html_page, then confirm each figure, period and unit with retrieve_information. parse_html_page cannot read PDFs. Use the HTML exhibit instead.
- Never use an empty search query. If web_search returns nothing, use a short non-empty query or edgar_search with company and date filters.
- Cite only documents you opened and retrieved from. Do not list an article, PDF or filing seen only in search results.
- Write the final answer in plain text with no citation markup such as <cite> tags.
