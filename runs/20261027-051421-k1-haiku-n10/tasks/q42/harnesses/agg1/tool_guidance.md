# Tool use

- Fix the companies, form type (10-K) and fiscal year before searching. Search with company, form, year and the statement or line item (for example "PepsiCo 10-K 2024 consolidated statement of cash flows dividends paid"), not the question's wording. Always pass a non-empty `query`.
- Several companies can be searched in one turn, but search results are only leads. Each figure that enters a calculation must be seen as text for the right company and period, not as a title or URL.
- `edgar_search` and `parse_html_page` on sec.gov often return HTTP 403 here, and `parse_html_page` cannot read PDFs. Start with `web_search`. Do not call `edgar_search` repeatedly after a failure. Make one targeted `web_search` per missing figure and read the statement from the excerpt. You may try `parse_html_page` once on a non-sec.gov HTML copy; if it works, store it under a clear key and ask `retrieve_information` one targeted question at a time.
- Cite only URLs that appeared in tool output. Say whether each figure came from an opened filing or a search excerpt.
- Do arithmetic on unrounded numbers, re-check it once, and round only the final result.
- Write the answer as plain text with no raw citation tags. Once the figures are in hand and re-checked, call `submit_final_result` right away.
