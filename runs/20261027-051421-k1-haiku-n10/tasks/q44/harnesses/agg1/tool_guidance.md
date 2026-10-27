# Tool guidance

- Decide the company, form type (10-K, 10-Q, 8-K Ex. 99.1, shareholder letter) and fiscal period before searching. Use those in the query, not the question's wording.
- Chain: find the primary document URL (edgar_search or web_search), then parse_html_page with a clear key, then retrieve_information with one targeted question and the same key. Ask for the exact sentence or table row, including the column header and the period.
- If edgar_search fails (for example a 403 on the ticker lookup), don't repeat the identical call. Switch to web_search with a company, form and year query to find the document URL.
- If parse_html_page returns 403 for a sec.gov URL, try another HTML copy of the same disclosure, such as an 8-K Ex. 99.1 or an IR-site page. parse_html_page cannot read PDFs, so look for an HTML version.
- Before submitting, check that the figure matches the requested metric label, region or segment, fiscal year (not the prior-year column) and units. If the figure rests only on a search excerpt because the primary document could not be opened, say so in the answer. Submit before the budget runs low.
