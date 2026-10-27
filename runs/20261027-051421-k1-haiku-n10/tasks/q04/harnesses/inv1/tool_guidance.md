# Tool use

- Before searching, fix the company, document type and fiscal period for each figure. Always pass a non-empty `query`. Search by company, form (8-K Exhibit 99.1 / 10-Q / 10-K), fiscal quarter and line item.
- `edgar_search` and `parse_html_page` on sec.gov often return HTTP 403, and `parse_html_page` cannot read PDFs. Do not retry a 403 and do not call `edgar_search` again after one failure. Make one targeted `web_search` per period (company, release, quarter, "outlook") and read the figure from the excerpt. You may try `parse_html_page` once on a non-sec.gov HTML copy (e.g. the company's IR press release); if it works, ask `retrieve_information` one specific question.
- A search listing (title and URL only) is not evidence of a figure. Use a figure only if its text appeared in tool output for that period; if one period's figure is unseen, run one more targeted search for it before submitting.
- Cite only URLs that appeared in tool output. Say in the answer whether figures came from an opened document or from search excerpts.
- Do arithmetic on unrounded numbers, re-check each result once, and round only the final figures, in the format the question prescribes.
- Write plain text with no raw citation tags. Once all figures are confirmed, call `submit_final_result` right away.
