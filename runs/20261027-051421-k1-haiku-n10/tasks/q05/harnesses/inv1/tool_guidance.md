# Tool use

- Before searching, fix the company, the form types (DEF 14A, DEFA14A, 8-K Item 5.02, press release) and the calendar year the question names. Search with those terms, not the question's wording. Always pass a non-empty `query`; a null query returns unrelated results.
- `edgar_search` and `parse_html_page` on sec.gov can return HTTP 403 (edgar_search failed on the company-tickers lookup in this environment). Do not retry after one failure. Use `web_search`; results often give company IR-site URLs (for example ir.bbsi.com/sec-filings/...) that `parse_html_page` can open. `parse_html_page` cannot read PDFs.
- Store each opened document under a clear key, then ask `retrieve_information` one targeted question at a time.
- A search snippet is a lead, not a source. Open the document before relying on a name list or a date taken from a snippet, or else say it came from an excerpt.
- Cite only URLs that appeared in tool output. Once the figures or names are checked, call `submit_final_result` right away.
