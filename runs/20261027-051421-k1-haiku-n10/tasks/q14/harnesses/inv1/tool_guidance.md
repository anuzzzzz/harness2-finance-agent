# Tool use

- Before searching, fix the company, form (10-K / 8-K Exhibit 99.1), and fiscal years. Search with company, form, year and the line item name. Always pass a non-empty `query`; a null query returned unrelated results.
- `edgar_search` and `parse_html_page` on sec.gov returned HTTP 403 in this environment (the Zillow run hit both). Do not retry a 403 and do not call `edgar_search` again after one failure. Use `web_search` with company, form, year and table name; excerpts often quote the table and give the sec.gov URL. `parse_html_page` cannot read PDFs.
- If a non-sec.gov HTML page carries the statements (in this task, `https://stockanalysis.com/stocks/zg/financials/cash-flow-statement/` parsed successfully), store it under a clear key and ask `retrieve_information` one targeted question at a time. Treat such a page as a lead: say it is a third-party data set, and confirm each key figure (period, units, continuing vs total operations) against a filing excerpt when one is reachable.
- Cite only URLs that appeared in tool output. State in the answer whether each figure came from an opened filing, a search excerpt, or a third-party data page. Do not call a figure "verified" unless you saw it in filing text.
- Do arithmetic on unrounded numbers, re-check it once, and round only the final result. Once the figures are in hand, call `submit_final_result` right away.
- Write the answer as plain text with no raw citation tags.
