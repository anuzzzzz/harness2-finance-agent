# Tool use

- A search snippet or result title is a lead, not evidence. Open the primary document (press release, 8-K exhibit, 10-K, 10-Q) with parse_html_page and confirm the figure or statement, its period and its wording with retrieve_information before relying on it. If web_search returns nothing, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- Cite only documents you opened and retrieved from. Do not list or lean on pages seen only in search results.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags or truncated quotes. Give the direct answer first, then the supporting statement with its date and source.
