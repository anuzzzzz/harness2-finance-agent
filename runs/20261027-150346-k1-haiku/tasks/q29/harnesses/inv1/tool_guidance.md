# Tool use

- Decide the filing and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. edgar_search takes a numeric CIK, not a ticker (a ticker such as 'SAVE' raises "Unknown ticker"). Retry once with the CIK. Never send an empty or null query to web_search. If web_search returns nothing, retry once with a short non-empty query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Use input_character_ranges on long filings.
- "List the KPIs / metrics" questions: find the filing's own table of operating statistics (usually in MD&A) and copy its rows in the filing's order, with unit and period. Retrieval output can truncate. If the answer ends mid-table or mid-sentence, ask again for just the table, or for the rows after the last one shown. Confirm the row count against the table before submitting. Do not pad the list with metrics from elsewhere in the filing unless you label them as outside the table.
- Before submitting, re-check each figure against the retrieved text (period, unit, GAAP vs non-GAAP). A successful retrieval does not make a figure correct.
- Cite only documents you opened and retrieved from. Do not list an article or filing seen only in search results, and do not use unopened secondary pages as "cross-checks". If a figure came only from a snippet, say so.
- Write the final answer in plain text. Never paste citation markup such as <cite> tags. State each figure with its period, unit and source. Submit with submit_final_result as soon as the figures are verified.

Task facts (Spirit Airlines FY2024 KPIs; verified in the base run, so re-confirm in the opened text):
- Spirit Airlines CIK is 1498710. The FY2024 10-K is https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm (about 635k characters when parsed).
- The KPIs are in Item 7 MD&A, in the "Comparative Operating Statistics" table (twelve months ended Dec 31, 2024 vs 2023, unaudited). The rows are:
  - Average aircraft (209.9)
  - Aircraft at end of period (213, including 21 held for sale)
  - Average daily aircraft utilization in hours (9.9)
  - Departures (288,180)
  - Passenger flight segments in thousands (44,180)
  - Revenue passenger miles in thousands (43,671,009)
  - Available seat miles in thousands (53,017,948)
  - Load factor (82.4%)
  - Total revenue per passenger flight segment ($111.21)
  - Average yield in cents (11.25)
  - TRASM in cents (9.27)
  - CASM in cents (11.35)
  - Adjusted CASM in cents (10.76)
  - Adjusted CASM ex-fuel in cents (7.97)
  - Fuel gallons consumed in thousands (551,819)
  - Average fuel cost per gallon ($2.68)
