# Tool use

- A search snippet or result title is a lead, not evidence. Open the primary document (8-K EX-99.1 earnings release, 10-Q, 10-K) with parse_html_page, then confirm each figure, period, unit and GAAP/non-GAAP basis with retrieve_information. This applies to the guidance and to the actual.
- Never send an empty or null query. If web_search returns nothing, retry once with a short non-empty query, then use edgar_search (company, form, date window) or a known primary URL.
- parse_html_page cannot read PDFs. Use the HTML exhibit.
- Guidance-versus-actual questions need two opened documents: the prior quarter's release (guidance) and the target period's release (actual). Compare like with like and carry full precision.
- Cite only documents you opened and retrieved from. Do not list a filing, article or press-release mirror seen only in search results. If a figure came only from a snippet, say so.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags.
