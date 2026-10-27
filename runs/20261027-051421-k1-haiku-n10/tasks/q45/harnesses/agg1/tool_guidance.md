# Tool use

- Before searching, fix the company, form type (10-K / 10-Q / 8-K Exhibit 99.1) and fiscal period. Use the latest filing already published as of the question date. Search with those terms plus the exact line item. Always pass a non-empty `query`; a null query returned unrelated results.
- `edgar_search` and `parse_html_page` on sec.gov often return HTTP 403 here, and `parse_html_page` cannot read PDFs. Do not retry a 403 and do not call `edgar_search` again after one failure. Make one or two targeted `web_search` calls (company, form, year, table name); results often quote the table text and give the sec.gov URL. You may try `parse_html_page` once on a non-sec.gov HTML copy. If it succeeds, ask `retrieve_information` one targeted question at a time.
- Check the line item before using it: name the table it came from, its period, and its units (thousands vs millions).
- Do not give a figure you have not seen in some tool output, and cite only URLs that appeared in tool results.
- Say in the answer whether the figure came from an opened filing or from a search excerpt. Do not write "verified" for a figure seen only in an excerpt.
- Do the arithmetic on unrounded numbers, re-check it once, and round only the final result.
- Write the answer as plain text with no raw citation tags. Once the figure is in hand, call `submit_final_result` right away.
