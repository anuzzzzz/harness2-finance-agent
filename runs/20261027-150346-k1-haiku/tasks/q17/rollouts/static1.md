## Rollout `static1`
- outcome: submitted
- turns: 4; cost: $0.354; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Airbnb 10-K gross booking value total revenue annual", "ciks": ["0001559720"], "form_types": ["10-K"], "start_date": "2023-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 4, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}, {"form": "10-K", "file_date": "2023-02-17", "period_ending": "2022-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-23-000003", "document": "abnb-20221231.htm", "description": "FORM 10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm"}, {"form": "10-K", "file_date": "2024-02-16", "period_ending": "2023-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-24-000006", "document": "abnb-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm"}, {"form": "10-K", "file_date": "2023-02-17", "period_ending": "2022-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-23-000003", "document": "exh1031airbnbrevolvingcred.htm", "description": "EX-10.31", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/exh1031airbnbrevolvingcred.htm"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "fy2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2024. (452,800 characters)
  The data_storage currently contains the following keys:
  fy2024
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm", "key": "fy2023"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2023. (624,096 characters)
  The data_storage currently contains the following keys:
  fy2024
  fy2023
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm", "key": "fy2022"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2022. (637,988 characters)
  The data_storage currently contains the following keys:
  fy2024
  fy2023
  fy2022
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K, extract the exact fiscal year Gross Booking Value (in billions) and Total Revenue (in millions) for the fiscal years stated in the key metrics/MD&A section, for the current year and prior years. Also give the take rate if stated. Quote the sentences where GBV and revenue for the year are stated. Document: {{fy2024}}"})
  result: ## Key Metrics: Airbnb FY2024 10-K
  
  | Fiscal Year | Gross Booking Value | Total Revenue |
  |---|---|---|
  | **FY2024** (current) | **$81.8 billion** ($81,784 million) | **$11,102 million** ($11.1 billion) |
  | **FY2023** (prior) | **$73.3 billion** ($73,252 million) | **$9,917 million** ($9.9 billion) |
  
  The MD&A key metrics cover only 2023 and 2024. The income statement also reports 2022 revenue of $8,399 million, but the filing does not give 2022 GBV.
  
  **Take rate:** The filing does not state a take rate. Dividing revenue by GBV gives an implied rate of about 13.6% for 2024 ($11,102M ÷ $81,784M) and about 13.5% for 2023 ($9,917M ÷ $73,252M). This is my calculation, not a figure from the 10-K.
  
  ## Supporting Quotes
  
  **GBV and revenue for 2024 (narrative, Financial Highlights):**
  > "In 2024, revenue increased by 12% to $11.1 billion compared to 2023, primarily due to a 10% increase in Nights and Experiences Booked of 43.3 million combined with higher Average Daily Rate ("ADR") driving a 12% increase in Gross Booking Value of $8.5 billion."
  
  **GBV table (Key Business Metrics):**
  > "Gross Booking Value $73,252 $81,784 12 %" (in millions; columns are 2023, 2024, % change)
  
  **Revenue table (Key Business Metrics):**
  > "Revenue $9,917 $11,102 12 %" (in millions; columns are 2023, 2024, % change)
  
  **Revenue change (Comparison of the Years):**
  > "Revenue increased $1.2 billion, or 12%, in 2024 compared to 2023, primarily due to an increase in the number of check-ins relating to Nights and Experiences Booked and a modest increase in ADR driven by our North America and EMEA regions."
- retrieve_information({"prompt": "From this Airbnb 10-K, extract the exact fiscal year Gross Booking Value (in billions) and Total Revenue (in millions) for the fiscal years stated in the key metrics/MD&A section, for the current year and prior years. Also give the take rate if stated. Quote the sentences where GBV and revenue for the year are stated. Document: {{fy2023}}"})
  result: ## Airbnb FY2023 10-K: GBV, Revenue, and Take Rate
  
  **Fiscal year 2023 is the current year.** The key metrics table and MD&A give GBV for 2022 and 2023. Revenue for 2021 appears only in the income statement.
  
  | Fiscal Year | Gross Booking Value (GBV) | Total Revenue | Take Rate |
  |---|---|---|---|
  | 2023 (current) | $73.3 billion ($73,252 million) | $9.9 billion ($9,917 million) | Not stated; ~13.5% derived |
  | 2022 (prior) | $63.2 billion ($63,212 million) | $8.4 billion ($8,399 million) | Not stated; ~13.3% derived |
  | 2021 (prior) | Not disclosed in this filing | $6.0 billion ($5,992 million) | Not stated |
  
  **Take rate:** The filing does not state a take rate. The figures above are my calculation (Revenue ÷ GBV), not a company disclosure. Airbnb's revenue is net of incentives and refunds, so this ratio is only an approximation of its service-fee rate.
  
  ### Supporting quotes
  
  **GBV, 2023 vs. 2022 (MD&A, Gross Booking Value):**
  > "In 2023, our GBV was $73.3 billion, a 16% increase from $63.2 billion in 2022."
  
  **Key metrics table (MD&A, in millions):**
  > "Gross Booking Value $63,212 $73,252 16 %"
  
  **Revenue, 2023 vs. 2022 (2023 Financial Highlights):**
  > "In 2023, revenue increased by 18% to $9.9 billion compared to 2022, primarily due to a 14% increase in Nights and Experiences Booked of 54.5 million combined with higher average daily rates driving a 16% increase in Gross Booking Value of $10.0 billion."
  
  **Revenue, 2023 vs. 2022 (Revenue section, in millions):**
  > "Revenue increased $1.5 billion, or 18%, in 2023 compared to 2022, primarily due to a 14% increase in Nights and Experiences Booked combined with higher ADRs."
  
  **Revenue, 2021 (Consolidated Statements of Operations, in millions):**
  > "Revenue $5,992 $8,399 $9,917"
  
  ### Notes
  - The "$10.0 billion" in the F
  …[truncated 256 chars]
- retrieve_information({"prompt": "From this Airbnb 10-K, extract the exact fiscal year Gross Booking Value (in billions) and Total Revenue (in millions) for the fiscal years stated in the key metrics/MD&A section, for the current year and prior years. Also give the take rate if stated. Quote the sentences where GBV and revenue for the year are stated. Document: {{fy2022}}"})
  result: ## Gross Booking Value and Revenue, Airbnb FY2022 10-K
  
  | Fiscal Year | GBV (billions) | Total Revenue (millions) | Source |
  |---|---|---|---|
  | 2022 (current) | $63.2 | $8,399 | Key Business Metrics table; Results of Operations |
  | 2021 (prior) | $46.9 | $5,992 | Key Business Metrics table; Results of Operations |
  | 2020 (prior) | Not stated in the document | $3,378 | Consolidated Statements of Operations only (not in MD&A key metrics) |
  
  The key metrics table reports GBV in millions ($46,877 for 2021 and $63,212 for 2022), so the billions figures are conversions of those values.
  
  ## Supporting quotes
  
  **GBV:**
  - "In 2022, our GBV was $63.2 billion, a 35% increase from $46.9 billion in 2021."
  - "for the year ended December 31, 2022, Gross Booking Value ("GBV") and revenue were $63.2 billion and $8.4 billion, respectively, which were both higher compared to the same periods in 2021, 2020, and pre-COVID-19."
  
  **Revenue:**
  - "In 2022, revenue grew by 40% to $8.4 billion compared to 2021, primarily due to a 31% increase in Nights and Experiences Booked of 93.0 million combined with higher average daily rates driving a 35% increase in Gross Booking Value of $16.3 billion."
  - "Revenue increased $2.4 billion, or 40%, in 2022 compared to 2021, primarily due to a 31% increase in Nights and Experiences Booked combined with higher ADRs."
  
  ## Take rate
  
  The filing does not state a take rate. Derived from the figures above (revenue ÷ GBV), it would be about 13.3% for 2022 and 12.8% for 2021. This is my calculation, not a company-reported metric.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Airbnb does not report a \"take rate\" in its 10-Ks, so I derived it as Total Revenue ÷ Gross Booking Value (GBV) using the figures in its annual filings.\n\nInputs (fiscal years ended December 31):\n- FY2022: Revenue $8,399M; GBV $63,212M\n- FY2023: Revenue $9,917M; GBV $73,252M\n- FY2024: Revenue $11,102M; GBV $81,784M\n\nCalculations (unrounded, then rounded to two decimals):\n- FY2022: 8,399 ÷ 63,212 = 0.132870… → **13.29%**\n- FY2023: 9,917 ÷ 73,252 = 0.135382… → **13.54%**\n- FY2024: 11,102 ÷ 81,784 = 0.135748… → **13.57%**\n\nTrend comment: The take rate has risen modestly and steadily, by about 0.25 percentage points from FY2022 to FY2023 and about 0.03 points in FY
…[truncated 983 chars])

### Final answer
Airbnb does not report a "take rate" in its 10-Ks, so I derived it as Total Revenue ÷ Gross Booking Value (GBV) using the figures in its annual filings.

Inputs (fiscal years ended December 31):
- FY2022: Revenue $8,399M; GBV $63,212M
- FY2023: Revenue $9,917M; GBV $73,252M
- FY2024: Revenue $11,102M; GBV $81,784M

Calculations (unrounded, then rounded to two decimals):
- FY2022: 8,399 ÷ 63,212 = 0.132870… → **13.29%**
- FY2023: 9,917 ÷ 73,252 = 0.135382… → **13.54%**
- FY2024: 11,102 ÷ 81,784 = 0.135748… → **13.57%**

Trend comment: The take rate has risen modestly and steadily, by about 0.25 percentage points from FY2022 to FY2023 and about 0.03 points in FY2024, so it has been broadly stable with a slight upward drift as revenue grew a bit faster than GBV.

Caveat: Airbnb's revenue is recognized net of incentives and refunds, so this ratio approximates its service-fee rate rather than a company-disclosed metric.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2022 (filed 2023-02-17)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2023 (filed 2024-02-16)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2024 (filed 2025-02-13)"
        }
    ]
}