## Rollout `inv1`
- outcome: submitted
- turns: 3; cost: $0.218; submitted: True

### Turn 1  (stop_reason=tool_use)
I'll re-confirm the figures against the two 10-K filings before calculating.
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "fy2024_10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2024_10k. (452,800 characters)
  The data_storage currently contains the following keys:
  fy2024_10k
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm", "key": "fy2023_10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2023_10k. (624,096 characters)
  The data_storage currently contains the following keys:
  fy2024_10k
  fy2023_10k
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this document, find the Gross Booking Value (GBV) for full years 2024, 2023 and 2022 as reported in the Key Business Metrics table (in $ millions), and total revenue for 2024, 2023 and 2022 from the consolidated statement of operations (in $ millions). State the period and units for each. Document: {{fy2024_10k}}"})
  result: **Gross Booking Value (GBV), from the Key Business Metrics table**
  
  | Fiscal year ended December 31 | GBV (USD millions) |
  |---|---|
  | 2024 | $81,784 |
  | 2023 | $73,252 |
  | 2022 | Not reported in this document |
  
  The table covers only 2023 and 2024. The document does not give 2022 GBV, so I can't provide that figure from this filing.
  
  **Total revenue, from the Consolidated Statements of Operations**
  
  | Fiscal year ended December 31 | Revenue (USD millions) |
  |---|---|
  | 2024 | $11,102 |
  | 2023 | $9,917 |
  | 2022 | $8,399 |
  
  Both sets of figures are in millions of U.S. dollars and cover full fiscal years ending December 31.
- retrieve_information({"prompt": "From this document, find the Gross Booking Value (GBV) for full years 2023 and 2022 as reported in the Key Business Metrics table (in $ millions), and total revenue for 2023 and 2022 from the consolidated statement of operations (in $ millions). State the period and units for each. Document: {{fy2023_10k}}"})
  result: **Gross Booking Value (Key Business Metrics table)**
  - **Full year 2023:** $73,252 million (about $73.3 billion)
  - **Full year 2022:** $63,212 million (about $63.2 billion)
  
  Both figures are for the fiscal years ended December 31, in millions of U.S. dollars.
  
  **Total revenue (Consolidated Statements of Operations)**
  - **Full year 2023:** $9,917 million (about $9.9 billion)
  - **Full year 2022:** $8,399 million (about $8.4 billion)
  
  Both figures are for the fiscal years ended December 31, in millions of U.S. dollars.

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "Airbnb annual take rate (revenue / Gross Booking Value), FY2022 to FY2024. All figures in $ millions, fiscal years ended December 31.\n\nInputs (re-confirmed from the filings):\n- FY2022: revenue 8,399; GBV 63,212 (GBV from the FY2023 10-K Key Business Metrics table; revenue from the FY2023 10-K consolidated statement of operations)\n- FY2023: revenue 9,917; GBV 73,252 (both in the FY2023 10-K; revenue also matches the FY2024 10-K)\n- FY2024: revenue 11,102; GBV 81,784 (both in the FY2024 10-K)\n\nCalculations:\n- FY2022: 8,399 / 63,212 = 13.29%\n- FY2023: 9,917 / 73,252 = 13.54%\n- FY2024: 11,102 / 81,784 = 13.57%\n\nTake rate by fiscal year:\n- FY2022: 13.29%\n- FY2023: 1
…[truncated 699 chars])

### Final answer
Airbnb annual take rate (revenue / Gross Booking Value), FY2022 to FY2024. All figures in $ millions, fiscal years ended December 31.

Inputs (re-confirmed from the filings):
- FY2022: revenue 8,399; GBV 63,212 (GBV from the FY2023 10-K Key Business Metrics table; revenue from the FY2023 10-K consolidated statement of operations)
- FY2023: revenue 9,917; GBV 73,252 (both in the FY2023 10-K; revenue also matches the FY2024 10-K)
- FY2024: revenue 11,102; GBV 81,784 (both in the FY2024 10-K)

Calculations:
- FY2022: 8,399 / 63,212 = 13.29%
- FY2023: 9,917 / 73,252 = 13.54%
- FY2024: 11,102 / 81,784 = 13.57%

Take rate by fiscal year:
- FY2022: 13.29%
- FY2023: 13.54%
- FY2024: 13.57%

Trend comment: The take rate has been essentially flat, edging up about 0.25 percentage points in 2023 and then only about 0.03 points in 2024.

Note: The FY2022 GBV was taken from the comparative column in the FY2023 10-K; the FY2022 10-K itself was not opened.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb FY2024 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm",
            "name": "Airbnb FY2023 Form 10-K"
        }
    ]
}