# Tool use

- A search snippet or result title is a lead, not evidence. Open the primary filing with parse_html_page, then ask retrieve_information one targeted question at a time. Confirm the figure, period and unit in the retrieved text before using it.
- Never call web_search with an empty or null query. If a search returns nothing, retry once with a short non-empty query, or use edgar_search or a known URL.
- Cite only documents you opened and retrieved from. Do not list a filing, PDF or press release seen only in search results.
- Write the final answer in plain text with no citation markup such as <cite> tags.
