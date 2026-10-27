# Tool use

- Before searching, fix the company, form type (10-K / 10-Q / 8-K) and fiscal period. As of the question date, use the latest filing already published. Search with those terms plus the exact line item. Always pass a non-empty `query`; a null query returns unrelated results.
- SEC endpoints often return HTTP 403 here. `edgar_search` and `parse_html_page` on sec.gov both failed in the earlier run. Do not retry a 403 and do not call `edgar_search` again after one failure. Make one or two targeted `web_search` calls (company, form, year, table name). Results often quote the table text and give the sec.gov URL. You may try `parse_html_page` once on a non-sec.gov HTML copy. If it works, store it under a clear key and ask `retrieve_information` one targeted question at a time. `parse_html_page` cannot read PDFs.
- Check the line item before using it: name the table, the period and the units (thousands vs millions).
- Cite only URLs that appeared in tool output. Do not give a figure you have not seen in tool output.
- Say in the answer whether the figure came from an opened filing or a search excerpt. Do not call an excerpt-only figure "verified".
- Do the arithmetic on unrounded numbers, re-check it once, and round only the final result. Once the figures are in hand, call `submit_final_result` right away.
