## Rollout `dom1`
- outcome: submitted
- turns: 4; cost: $0.036; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "multi_year_kpi_trend"})
  result: ---
  name: multi_year_kpi_trend
  description: Trace how a company-reported operating KPI (ARM/ARPU, subscribers, margin, volume) changed across several fiscal years, chaining each 10-K's comparative columns and giving change, percent change, CAGR and per-year path.
  ---
  ANALYTIC MOVE: trace and calculate. Inputs: the KPI's annual value for every fiscal year in the window, as the company defines it. Result: start value, end value, absolute change, % change, CAGR, and the year-by-year path with the drivers the company gives.
  
  1. Name the company's own term for the KPI. "ARPU" or "revenue per paying user" is often reported under another name (Netflix: "average monthly revenue per paying membership", ARM). Say in the answer that the question's term maps to this metric. Confirm the definition in the filing (numerator, denominator, monthly or annual, taxes excluded).
  2. Locate the figure. It is in the 10-K MD&A (Results of Operations or Streaming Revenues table), which carries three fiscal years side by side. For a 2019-2024 window you need at least the FY2024 10-K (2024, 2023, 2022), the FY2021 or FY2022 10-K (2021, 2020, and 2022), and the FY2019 10-K (2019, 2018, 2017). Open each of these and retrieve the value from it. Do not fill a year from memory or a snippet.
  3. Match period and basis. Use the full fiscal-year figure, not a quarter (Q4) or a regional row. A multi-region table has global and per-region rows, and only the global row answers a company-level question. If a later 10-K restates an earlier year, use the latest filing's number and say so. Note the currency basis: reported vs constant-currency (FX-neutral) change are different figures, so label which one each percentage is.
  4. Calculation, unrounded until the end: change = end - start. % change = (end / start - 1
  …[truncated 1,525 chars]
- edgar_search({"search_query": "Netflix average monthly revenue per paying membership", "ciks": ["NFLX"], "form_types": ["10-K"], "start_date": "2020-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 6, "page": 1, "results": [{"form": "10-K", "file_date": "2024-01-26", "period_ending": "2023-12-31", "company": "NETFLIX INC  (NFLX)  (CIK 0001065280)", "ciks": ["0001065280"], "accession": "0001065280-24-000030", "document": "nflx-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528024000030/nflx-20231231.htm"}, {"form": "10-K", "file_date": "2021-01-28", "period_ending": "2020-12-31", "company": "NETFLIX INC  (NFLX)  (CIK 0001065280)", "ciks": ["0001065280"], "accession": "0001065280-21-000040", "document": "nflx-20201231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528021000040/nflx-20201231.htm"}, {"form": "10-K", "file_date": "2022-01-27", "period_ending": "2021-12-31", "company": "NETFLIX INC  (NFLX)  (CIK 0001065280)", "ciks": ["0001065280"], "accession": "0001065280-22-000036", "document": "nflx-20211231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528022000036/nflx-20211231.htm"}, {"form": "10-K", "file_date": "2023-01-26", "period_ending": "2022-12-31", "company": "NETFLIX INC  (NFLX)  (CIK 0001065280)", "ciks": ["0001065280"], "accession": "0001065280-23-000035", "document": "nflx-20221231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528023000035/nflx-20221231.htm"}, {"form": "10-K", "file_date": "2020-01-29", "period_ending": "2019-12-31", "company": "NETFLIX INC  (NFLX)  (CIK 0001065280)", "ciks": ["0001065280"], "accession": "0001065280-20-000040", "document": "form10kq419.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528020000040/form10kq419.htm"}, {"form": "10-K", "file_date": "2025-01-27", "peri
  …[truncated 291 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528025000044/nflx-20241231.htm", "key": "fy2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2024. (275,605 characters)
  The data_storage currently contains the following keys:
  fy2024
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528023000035/nflx-20221231.htm", "key": "fy2022"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2022. (228,304 characters)
  The data_storage currently contains the following keys:
  fy2024
  fy2022
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528020000040/form10kq419.htm", "key": "fy2019"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2019. (226,208 characters)
  The data_storage currently contains the following keys:
  fy2024
  fy2022
  fy2019
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Netflix 10-K text: {{fy2024}}. Find the average monthly revenue per paying membership (ARM) for the full years 2024, 2023 and 2022 (global, in $). Also give the constant-currency change for 2024 vs 2023 if stated, and the MD&A drivers of ARM change (price changes, plan mix, FX). Quote the exact table row text."})
  result: **Global ARM (average monthly revenue per paying membership):**
  
  | Year | ARM |
  |---|---|
  | 2024 | $11.70 |
  | 2023 | $11.64 |
  | 2022 | $11.76 |
  
  The exact table row from Item 7 reads: "Average monthly revenue per paying membership $11.70 $11.64 $11.76 1 %"
  
  **Constant-currency change, 2024 vs. 2023:** The filing states "Constant currency change (3) 4%." Footnote (3) says the figure is calculated by assuming foreign exchange rates stayed at prior-year levels, and it excludes hedging gains or losses from both periods. The reported change is +1%, so the 4% constant-currency growth is about three points higher than the reported figure, which reflects unfavorable FX.
  
  **MD&A drivers:**
  
  - **Foreign exchange (negative):** Footnote (3) says revenues would have been about $1,424 million higher for 2024 at constant 2023 exchange rates. It attributes the unfavorable impact "primarily" to "the devaluation of the Argentine peso relative to the U.S. dollar coupled with significant price increases in the local currency in this jurisdiction." Item 7A repeats this.
  - **Pricing (positive):** Streaming revenue growth is attributed to "growth in average paying memberships and price increases, partially offset by unfavorable changes in foreign exchange rates." The filing does not separately quantify the price contribution to ARM.
  - **Hedging:** Streaming revenues include $124 million of hedging gains in 2024. These are excluded from the ARM calculation, and there were none in 2023 or 2022.
  - **Plan mix:** The filing does not quantify plan-mix effects on ARM. It mentions the ad-supported plan and extra member sub-accounts only qualitatively.
  
  **Regional ARM, for context:**
  
  | Region | 2024 | 2023 | 2022 | Change (reported) | Constant currency |
  |---|---|---|---|---|---|
  | UCAN | $17.20 | $1
  …[truncated 281 chars]
- retrieve_information({"prompt": "From this Netflix 10-K text: {{fy2022}}. Find the average monthly revenue per paying membership (ARM) for the full years 2022, 2021 and 2020 (global, in $). Quote the exact table row text and state the drivers given for ARM changes."})
  result: **Global average monthly revenue per paying membership (ARM):**
  
  | Year | ARM |
  |---|---|
  | 2022 | $11.76 |
  | 2021 | $11.67 |
  | 2020 | $10.91 |
  
  The exact row from the consolidated performance highlights table reads:
  
  "Average monthly revenue per paying membership $11.76 $11.67 $10.91 1 %"
  
  The 1% change is 2022 vs. 2021. The filing does not state the 2021 vs. 2020 change; it appears only in the prior-year 10-K. By my calculation, it was about 7%.
  
  **Drivers given for the 2022 change:**
  
  - **Price changes** increased ARM. The filing says the increase "resulted from our price changes."
  - **Foreign exchange** partially offset that increase. The filing cites "the strengthening of the U.S. dollar relative to certain foreign currencies." Had exchange rates stayed constant with 2021, revenues would have been about $1,773 million higher.
  
  The filing gives no specific drivers for the 2021 vs. 2020 change in this document.
- retrieve_information({"prompt": "From this Netflix 10-K text: {{fy2019}}. Find the average monthly revenue per paying membership (ARM) for the full years 2019, 2018 and 2017 (global, in $). Quote the exact table row text and state the drivers given for ARM changes."})
  result: **Global average monthly revenue per paying membership (ARM):**
  
  - **2019: $10.82**
  - **2018: $10.31**
  - **2017: $9.43**
  
  **Exact table row (Results of Operations, consolidated highlights):**
  "Average monthly revenue per paying membership $10.82 $10.31 $9.43 5 % 9 %"
  
  The 5% and 9% figures are the year-over-year changes for 2019 vs. 2018 and 2018 vs. 2017.
  
  **Drivers given in this filing:**
  - For 2019 vs. 2018, the filing says the increase "resulted from our price changes and plan mix, partially offset by unfavorable fluctuations in foreign exchange rates."
  - The filing does not give a separate driver explanation for the 2018 vs. 2017 change in global ARM. That discussion is in the FY2018 10-K, which this document references but does not include.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Answer: Netflix's \"average revenue per paying user\" maps to the company's own KPI, \"average monthly revenue per paying membership\" (ARM), a global monthly figure in US dollars. On that basis, ARM rose from $10.82 in 2019 to $11.70 in 2024, an increase of $0.88, or 8.13%. The compound annual growth rate over the five years is about 1.58%. The path was not steady: it rose in 2021, slipped in 2023, and recovered slightly in 2024.\n\nYear-by-year (global ARM, USD per month, full fiscal year):\n- 2019: $10.82 (FY2019 10-K, Results of Operations highlights table)\n- 2020: $10.91 (FY2022 10-K performance highlights table, prior-year column)\n- 2021: $11.67 (FY2022 10-K perform
…[truncated 2,299 chars])

### Final answer
Answer: Netflix's "average revenue per paying user" maps to the company's own KPI, "average monthly revenue per paying membership" (ARM), a global monthly figure in US dollars. On that basis, ARM rose from $10.82 in 2019 to $11.70 in 2024, an increase of $0.88, or 8.13%. The compound annual growth rate over the five years is about 1.58%. The path was not steady: it rose in 2021, slipped in 2023, and recovered slightly in 2024.

Year-by-year (global ARM, USD per month, full fiscal year):
- 2019: $10.82 (FY2019 10-K, Results of Operations highlights table)
- 2020: $10.91 (FY2022 10-K performance highlights table, prior-year column)
- 2021: $11.67 (FY2022 10-K performance highlights table, prior-year column)
- 2022: $11.76 (FY2022 10-K and FY2024 10-K comparative column)
- 2023: $11.64 (FY2024 10-K)
- 2024: $11.70 (FY2024 10-K)

Calculations (unrounded until the end):
- Absolute change 2019 to 2024: 11.70 - 10.82 = 0.88
- Percent change: (11.70 / 10.82 - 1) x 100 = 8.13%
- CAGR over 5 years: (11.70 / 10.82)^(1/5) - 1 = about 1.58%
- Year-over-year changes: 2020 +$0.09 (+0.83%); 2021 +$0.76 (+6.97%); 2022 +$0.09 (+0.77%); 2023 -$0.12 (-1.02%); 2024 +$0.06 (+0.52%). The five changes sum to the $0.88 total.
- About 96.6% of the net gain (0.85 of 0.88) came in 2019 to 2021, before ARM flattened.

Drivers given in the filings:
- 2019 vs 2018: the 10-K says ARM rose on price changes and plan mix, partly offset by unfavorable foreign exchange.
- 2022 vs 2021 (+1% reported): the 10-K attributes the increase to price changes, partly offset by a stronger US dollar against certain currencies.
- 2024 vs 2023 (+1% reported, +4% constant currency): the largest drag was the devaluation of the Argentine peso, and the 10-K cites price increases and paying membership growth as positives. Streaming revenue also included $124 million of hedging gains in 2024, which are excluded from ARM.
- The 2021 and 2023 drivers were not retrieved from the filings I opened, so they are not stated here. The 2021 to 2020 move is my own calculation from the figures above, not a filing statement.

Caveats: ARM is a reported-currency figure, so the reported changes include currency effects. Netflix excludes hedging gains and losses from ARM. The 2020 and 2021 values come from the FY2022 10-K's comparative columns rather than from the FY2020 or FY2021 filings.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528025000044/nflx-20241231.htm",
            "name": "Netflix FY2024 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528023000035/nflx-20221231.htm",
            "name": "Netflix FY2022 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528020000040/form10kq419.htm",
            "name": "Netflix FY2019 Form 10-K"
        }
    ]
}