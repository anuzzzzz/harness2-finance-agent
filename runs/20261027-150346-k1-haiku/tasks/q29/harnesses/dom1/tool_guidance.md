# Tool use

- A search snippet or result title is a lead, not evidence. Open the primary filing with parse_html_page and confirm each figure, period and unit with retrieve_information. Never issue a web_search with an empty or null query. If a search returns nothing, retry once with a short non-empty query, or use edgar_search with a numeric CIK (tickers are rejected) or a known SEC URL.
- Cite only documents you opened and retrieved from. A secondary article seen only in search results is not a source and not a cross-check. Do not describe it as one.
- If a retrieve_information answer is cut off ("truncated"), ask again for the remainder or for the table alone, so the list is complete before you submit.
- Write the final answer in plain text with no citation markup.

Task fact (Spirit Airlines FY2024, verified in the run): the 10-K is https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm (CIK 1498710). The KPI table is "Comparative Operating Statistics" in Item 7 MD&A.
