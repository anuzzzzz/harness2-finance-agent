# Tool use

- A search snippet is a lead, not evidence. Open the primary document (8-K EX-99.1 release or shareholder letter, 10-Q, 10-K) with parse_html_page (one clear key per document), then confirm each figure, period and unit with retrieve_information. This applies to the actual as well as to the guidance. If web_search returns nothing, retry once with a short non-empty query, then use edgar_search or a known primary URL.
- parse_html_page cannot read PDFs. Use the HTML 8-K exhibit instead (edgar_search finds it).
- Do not add up quarterly figures from different documents to build a full-year number if a document states the full-year figure; retrieve the stated figure. If you must sum, say so and label it a derived figure.
- Cite only documents you opened and retrieved from. Do not list a document as a source, or attribute a figure to it, unless you retrieved that figure from it.
- Write the final answer in plain text with no citation markup such as <cite> tags.
