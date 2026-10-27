I made two small always-on edits and added no skill, because the base run's only process problems were one tool failure and an unverified figure.

<file path="tool_guidance.md">
# Tool use

- Before searching, decide the form type (10-K / 10-Q), the company and the fiscal period the question needs. As of the question date, use the latest filing already published.
- Preferred chain: `edgar_search` (with company, form type and date filters) -> `parse_html_page` (store the filing under a clear key) -> `retrieve_information` (one targeted question at a time; use `input_character_ranges` on long filings).
- If `edgar_search` returns an HTTP 403 or another error, do not retry it. Make one fallback: `web_search` for the company, form and fiscal year, then take the sec.gov filing URL from the results and pass it to `parse_html_page`. If that also fails, work from the search-result text and say in the answer that the figures came from a search excerpt.
- A figure seen only in a search snippet is a lead, not a verified figure. Before submitting, confirm it in the parsed filing text with `retrieve_information`, checking period, units (thousands vs millions) and whether the figure is discounted or undiscounted. If the parse fails, state the limitation and submit anyway.
- Do the arithmetic with unrounded numbers, re-add the components once before submitting, and round only the final result.
- Submit with `submit_final_result` as soon as the figures are verified. Do not spend the remaining budget on extra searching.
</file>

<file path="LongTermMEMORY.md">
# Task facts (verify against the filing before use)

- MSCI Inc., CIK 1408198. The FY2024 10-K is at https://www.sec.gov/Archives/edgar/data/1408198/000140819825000053/msci-20241231.htm. It is the latest annual filing as of April 07, 2025.
- In the base run, a web_search excerpt of that 10-K's lease note showed the operating lease maturity schedule at Dec 31, 2024, in $ thousands:
  - 2025: 30,220
  - 2026: 30,361
  - 2027: 24,421
  - 2028: 23,931
  - 2029: 16,573
  - Thereafter: 40,099
  - Total lease payments: 165,605
  - Less interest: (19,601)
  - Present value of lease liabilities: 146,004
- The base run never opened the filing, so these figures are unconfirmed. Re-check them in the 10-K text.
- For "maturing in the next three years", use 2025-2027 and show the percentage against total undiscounted lease payments. Mention the share of the present-value liability only as a secondary reference.
</file>

<notes>
- Turn 1-2 of base1: edgar_search failed twice with 403 (SEC blocking). The agent had no stated fallback. tool_guidance.md now gives one bounded fallback (web_search, then parse_html_page on the sec.gov URL) and tells the agent not to retry edgar_search.
- Turn 3 of base1: the agent submitted from a search snippet without parsing the filing. The guidance now says to confirm snippet figures in the filing text, covering units, period and discounted vs undiscounted. If the parse fails, it should state the limitation and still submit.
- LongTermMEMORY.md records the verified-by-snippet task facts (the 10-K URL and the lease schedule), labelled as unconfirmed, plus the denominator choice the run made. This lets a rerun go straight to the filing and check the figures.
</notes>