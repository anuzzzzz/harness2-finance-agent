# Tool use

- A search snippet or result title is a lead, not evidence. Open the primary document (10-K, 10-Q, 8-K exhibit, proxy material) with parse_html_page and confirm each fact and date with retrieve_information.
- Cite only documents you opened and retrieved from. Do not list a filing as a source if you saw it only in search results.
- Do not use or cite documents dated after the question's current date (April 07, 2025), even if search returns them.
- Write the final answer in plain text. Do not paste citation markup such as <cite index=...> tags.
- If web_search returns nothing, retry once with a short non-empty query, then use edgar_search (with CIK and date filters) or a known primary URL.
