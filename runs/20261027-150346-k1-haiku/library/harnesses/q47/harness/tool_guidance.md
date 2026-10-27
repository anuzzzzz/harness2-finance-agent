# Tool use

- A search snippet is a lead, not evidence. Open the primary document (8-K EX-99.1 release or letter, 10-Q or 10-K) with parse_html_page (one clear key per document) and confirm each figure, period and unit with retrieve_information. This applies to the actual as well as the guidance. If web_search returns nothing, retry once with a short non-empty query, then use edgar_search or a known primary URL.
- parse_html_page cannot read PDFs; use the HTML exhibits.
- If a parsed document shows draft markers or two places in it disagree, cross-check in a second opened source if one is available, otherwise say so plainly.
- Cite only documents you opened and retrieved from. Do not cite, or lean on figures from, filings, articles or transcripts you saw only in search results.
- Write the final answer in plain text with no citation markup such as <cite> tags.
