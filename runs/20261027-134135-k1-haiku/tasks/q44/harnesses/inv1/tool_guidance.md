# Tool guidance

Before searching, decide the document and period the question needs: company, form type (10-K, 10-Q, 8-K exhibit 99.1 or shareholder letter) and fiscal period. Then search with those filters, not the question's wording.

- `edgar_search`: pass the ticker or CIK, a date range, and the form type. If it returns 0 results, change the filters once. If it still returns nothing, use `web_search` for the company's investor-relations PDF.
- `web_search`: use it to find primary documents. A snippet or third-party page (statistics aggregators, blogs) is a lead, not evidence. If `web_search` returns 0 results, rephrase it once and then move to `edgar_search`.
- `parse_html_page`: store each primary document under a clear key (for example `abnb_10k_2024`).
- `retrieve_information`: ask one targeted question at a time. On long filings, use `input_character_ranges`. Ask for the exact figure with its period, unit and definition.

Enough evidence means the figure was read from the text of a primary document that was actually opened with `parse_html_page` and `retrieve_information`, and the period, unit and definition match the question. A figure that only appeared in a search result is not yet verified. Open its source, or the filed 10-K or 8-K, and confirm it. If the primary document cannot be opened, say so in the answer and name the secondary source.

Before `submit_final_result`, re-check each figure you will submit against the retrieved text: period, region or segment, units, and rounding as reported. If the company reports a rounded figure and a source gives more precision, give the company's figure and note the other. Submit while budget remains.

In this task (Airbnb, FY2024, average nights per booking by region):
- A search excerpt of the Q4 2024 shareholder letter (https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf) gave 2024 averages of North America 4.1, EMEA 3.8, Latin America 3.7 and Asia Pacific 3.3. The company-wide figure, excluding experiences, was 3.8.
- Radical Storage cited 3.33 for Asia Pacific.
- The earlier run never opened the primary document. Treat these as leads to confirm.
- The FY2024 10-K is https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm. The 8-K ex-99.1 is https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm.
- Open the 10-K and the 8-K ex-99.1, or the shareholder letter. Confirm the Asia Pacific row and the year column (2024, not 2023), and check whether the filing shows more than one decimal.
