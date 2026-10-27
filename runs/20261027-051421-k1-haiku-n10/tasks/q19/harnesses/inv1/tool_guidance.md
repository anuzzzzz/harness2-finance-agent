# Tool use

- Before searching, decide the form type (10-K / 10-Q), the company and the fiscal period the question needs. As of the question date, use the latest filing already published.
- Preferred chain: `edgar_search` (with company, form type and date filters) -> `parse_html_page` (store the filing under a clear key) -> `retrieve_information` (one targeted question at a time; use `input_character_ranges` on long filings).
- If `edgar_search` returns an HTTP 403 or another error, do not retry it. Make one fallback: `web_search` for the company, form and fiscal year, then take the sec.gov filing URL from the results and pass it to `parse_html_page`. If that also fails, work from the search-result text and say in the answer that the figures came from a search excerpt.
- A figure seen only in a search snippet is a lead, not a verified figure. Before submitting, confirm it in the parsed filing text with `retrieve_information`, checking period, units (thousands vs millions) and whether the figure is discounted or undiscounted. If the parse fails, state the limitation and submit anyway.
- Do the arithmetic with unrounded numbers, re-add the components once before submitting, and round only the final result.
- Submit with `submit_final_result` as soon as the figures are verified. Do not spend the remaining budget on extra searching.
