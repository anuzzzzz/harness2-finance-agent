# Tool use

- A search snippet is a lead, not evidence. Open the primary filing with parse_html_page (one key per document), then use retrieve_information to confirm each figure, period and unit.
- Cite only documents you opened and retrieved from. Do not list a filing seen only in search results, such as an earlier-year 10-K you never parsed.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags.
- Do not run web_search with an empty query. If web_search returns nothing, use edgar_search.
