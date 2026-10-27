## Rollout `ctl2`
- outcome: submitted
- turns: 5; cost: $0.455; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Airbnb gross booking value nights and experiences booked annual report", "ciks": ["1559720"], "form_types": ["10-K"], "start_date": "2023-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 3, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}, {"form": "10-K", "file_date": "2023-02-17", "period_ending": "2022-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-23-000003", "document": "abnb-20221231.htm", "description": "FORM 10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm"}, {"form": "10-K", "file_date": "2024-02-16", "period_ending": "2023-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-24-000006", "document": "abnb-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm"}]}

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
- retrieve_information({"prompt": "From this Airbnb 10-K document, find the \"Gross Booking Value\" and \"Nights and Experiences Booked\" metrics for the fiscal years in the key metrics table (give exact figures in millions for GBV and nights for each year presented). Quote the sentence(s) where these are stated. Document: {{fy2024}}"})
  result: The key business metrics table in Item 7 (MD&A) covers fiscal years 2023 and 2024:
  
  | Metric | 2023 | 2024 | % Change |
  |---|---|---|---|
  | Nights and Experiences Booked | 448 million | 492 million | 10% |
  | Gross Booking Value (GBV) | $73,252 million | $81,784 million | 12% |
  
  **Where the figures are stated:**
  
  - The table introduction reads: "The following table summarizes our key business metrics, for each period presented below (in millions, except percentages):"
  - The table rows read: "Nights and Experiences Booked 448 492 10 %" and "Gross Booking Value $73,252 $81,784 12 %"
  - The 2024 Financial Highlights section adds: "In 2024, revenue increased by 12% to $11.1 billion compared to 2023, primarily due to a 10% increase in Nights and Experiences Booked of 43.3 million combined with higher Average Daily Rate ('ADR') driving a 12% increase in Gross Booking Value of $8.5 billion."
  
  The 43.3 million increase in the highlights section doesn't exactly match the rounded table figures (492 − 448 = 44). The filing's underlying unrounded numbers likely account for the difference.
- retrieve_information({"prompt": "From this Airbnb 10-K document, find the \"Gross Booking Value\" and \"Nights and Experiences Booked\" metrics for the fiscal years in the key metrics table (give exact figures in millions for GBV and nights for each year presented). Quote the sentence(s) where these are stated. Document: {{fy2023}}"})
  result: The key business metrics table covers fiscal 2022 and 2023 (values in millions):
  
  | Metric | 2022 | 2023 | % Change |
  |---|---|---|---|
  | Nights and Experiences Booked | 394 million | 448 million | 14% |
  | Gross Booking Value (GBV) | $63,212 million | $73,252 million | 16% |
  
  The table is in Item 7 (MD&A), under "Key Business Metrics and Non-GAAP Financial Measures." The narrative text gives more precise figures:
  
  **Nights and Experiences Booked:** "In 2023, we had 448.2 million Nights and Experiences Booked, a 14% increase from 393.7 million in 2022."
  
  **Gross Booking Value:** "In 2023, our GBV was $73.3 billion, a 16% increase from $63.2 billion in 2022."
- retrieve_information({"prompt": "From this Airbnb 10-K document, find the \"Gross Booking Value\" and \"Nights and Experiences Booked\" metrics for the fiscal years in the key metrics table (give exact figures in millions for GBV and nights for each year presented). Quote the sentence(s) where these are stated. Document: {{fy2022}}"})
  result: **Key Business Metrics table (in millions):**
  
  | Metric | 2021 | 2022 |
  |---|---|---|
  | Nights and Experiences Booked | 301 | 394 |
  | Gross Booking Value (GBV) | $46,877 | $63,212 |
  
  The table rounds nights to whole millions. The narrative text gives more precise figures: 300.6 million nights and experiences in 2021 and 393.7 million in 2022.
  
  **Where the figures are stated:**
  
  - **Nights and Experiences Booked:** "In 2022, we had 393.7 million Nights and Experiences Booked, a 31% increase from 300.6 million in 2021."
  
  - **Gross Booking Value:** "In 2022, our GBV was $63.2 billion, a 35% increase from $46.9 billion in 2021."
  
  The table is in Item 7 (MD&A), under "Key Business Metrics and Non-GAAP Financial Measures."

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K, quote the exact sentence stating the 2024 Nights and Experiences Booked figure (with decimal, in millions) and the 2024 GBV in billions, and the 2023 comparison. Document: {{fy2024}}"})
  result: The 10-K doesn't state the 2024 Nights and Experiences Booked figure with a decimal. The closest exact sentence is from the 2024 Financial Highlights in Item 7:
  
  > "In 2024, revenue increased by 12% to $11.1 billion compared to 2023, primarily due to a 10% increase in Nights and Experiences Booked of 43.3 million combined with higher Average Daily Rate ("ADR") driving a 12% increase in Gross Booking Value of $8.5 billion."
  
  The key business metrics table (Item 7, in millions) gives the levels:
  
  > "Nights and Experiences Booked 448 492 10 %"
  > "Gross Booking Value $73,252 $81,784 12 %"
  
  So:
  
  - **Nights and Experiences Booked:** 492 million in 2024, compared with 448 million in 2023 (a 10% increase, or 43.3 million more according to the highlights sentence).
  - **Gross Booking Value:** $81,784 million (about $81.8 billion) in 2024, compared with $73,252 million (about $73.3 billion) in 2023 (a 12% increase, or $8.5 billion more).

### Turn 5  (stop_reason=tool_use)
- web_search(query="Airbnb full year 2024 nights and experiences booked million 491.5") → 10 results: Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/abnb-20240930.htm>
- submit_final_result({"final_result": "FY 2022: $160.56\nFY 2023: $163.44\nFY 2024: $166.40\n\nMethod: Gross booking value (GBV) ÷ Nights and Experiences Booked (both for the full fiscal year, from Airbnb's Form 10-K filings).\n\n- FY 2022: GBV $63,212M ÷ 393.7M nights and experiences = $160.5588 → $160.56. The 2022 10-K states that <cite index=\"\">\"In 2022, we had 393.7 million Nights and Experiences Booked\"</cite> and that GBV was $63.2 billion.\n- FY 2023: GBV $73,252M ÷ 448.2M = $163.4360 → $163.44. The 2023 10-K's narrative gives <cite index=\"\">448.2 million Nights and Experiences Booked</cite>, and the key metrics table shows GBV of $73,252M. The Q4 2023 shareholder letter also reports <cite index=\"1
…[truncated 1,549 chars])

### Final answer
FY 2022: $160.56
FY 2023: $163.44
FY 2024: $166.40

Method: Gross booking value (GBV) ÷ Nights and Experiences Booked (both for the full fiscal year, from Airbnb's Form 10-K filings).

- FY 2022: GBV $63,212M ÷ 393.7M nights and experiences = $160.5588 → $160.56. The 2022 10-K states that <cite index="">"In 2022, we had 393.7 million Nights and Experiences Booked"</cite> and that GBV was $63.2 billion.
- FY 2023: GBV $73,252M ÷ 448.2M = $163.4360 → $163.44. The 2023 10-K's narrative gives <cite index="">448.2 million Nights and Experiences Booked</cite>, and the key metrics table shows GBV of $73,252M. The Q4 2023 shareholder letter also reports <cite index="1-5">448.2M</cite> nights for the year.
- FY 2024: GBV $81,784M ÷ 491.5M = $166.3967 → $166.40. The 2024 10-K key metrics table shows GBV of $81,784M and nights of 492M (rounded). The unrounded figure of 491.5M is the 2023 figure of 448.2M plus the 43.3M increase stated in the 10-K highlights. Public reporting of the full-year result also cites <cite index="8-2">491.5M (+10% YoY)</cite>, which confirms it.

Note: Using the rounded table figure of 492M for FY 2024 would give $166.22 instead.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2024"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2023"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2022"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm",
            "name": "Airbnb Q4 2023 Shareholder Letter (Form 8-K)"
        },
        {
            "url": "https://x.com/ColinGardiner/status/1895160218868240615",
            "name": "Colin Gardiner post on Airbnb FY 2024 results"
        }
    ]
}