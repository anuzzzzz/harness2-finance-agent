## Rollout `dom1`
- outcome: submitted
- turns: 9; cost: $0.199; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "company_kpi_lookup"})
  result: ---
  name: company_kpi_lookup
  description: Retrieve a company-defined operating metric (e.g. average nights per booking, ADR, active users, by region/segment) for a fiscal year from primary filings and report it with period, units and precision.
  ---
  ANALYTIC MOVE: look up (and where possible cross-check) one company-defined KPI for a named period and breakdown (region/segment).
  
  WHERE IT LIVES
  - 10-K, Item 7 MD&A "Key Business Metrics" and segment/geography notes (Item 8). Regional splits are often only in the earnings release or shareholder letter, not the 10-K body.
  - 8-K Item 2.02 earnings release: Exhibit 99.1 (press release / shareholder letter) with the regional KPI tables and definitions.
  - Search edgar_search with the company ticker for the 10-K and the Q4 8-K EX-99.1 filed in the following Feb. Parse the document and retrieve the figure from source text; a search snippet or third-party site (statistics aggregators) is not a primary source -- use it only as a corroboration.
  
  ANSWER CONTRACT
  - State the figure exactly as disclosed (same decimals; do not round it further or substitute a third-party's more precise number unless labelled as such), the fiscal period (full year vs Q4), the region/segment, and the unit.
  - Name the document (filing type, exhibit, date) the figure came from, and quote the defining sentence/table row.
  - Check the metric definition (e.g. whether it excludes a business line like Experiences/Services) and mention it if it affects comparison.
  - Check the period: full-year 2024 is not Q4 2024; fiscal year is not necessarily calendar year; confirm comparatives are not restated.
  - If the table gives components (e.g. nights and seats booked and bookings), recompute the ratio as a sanity check and show the arithmetic; if the disclosed ratio and rec
  …[truncated 383 chars]

### Turn 2  (stop_reason=tool_use)
- edgar_search({"search_query": "Airbnb shareholder letter fourth quarter 2024 nights and experiences booked Asia Pacific", "ciks": ["ABNB"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 1, "page": 1, "results": [{"form": "8-K", "file_date": "2025-02-13", "period_ending": "2025-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-25-026054", "document": "d915198dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm"}]}

### Turn 3  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm", "key": "abnb_q4_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_q4_2024. (54,854 characters)
  The data_storage currently contains the following keys:
  abnb_q4_2024
  

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb Q4 2024 shareholder letter, find the Average Nights per Booking for Asia Pacific for full year 2024 (and Q4 2024 if present), plus the definition of Average Nights per Booking, and the regional table rows for Nights and Experiences Booked, Nights and Experiences Booked by region, and Average Nights per Booking by region. Quote the defining sentence and table rows exactly. Text: {{abnb_q4_2024}}"})
  result: The letter does not contain an Average Nights per Booking metric for Asia Pacific, for either full-year 2024 or Q4 2024. It also has no definition of that term and no regional table. Asia Pacific is discussed only in narrative text, and the letter's only Nights and Experiences Booked tables are company-wide.
  
  **Definition:** The letter does not define Average Nights per Booking. The closest definition is for Nights and Experiences Booked:
  
  > "Nights and Experiences Booked on our platform in a period represents the sum of the total number of nights booked for stays and the total number of seats booked for experiences, net of cancellations and alterations that occurred in that period."
  
  **Regional table rows:** None exist. The only related rows are company-wide:
  
  - Quarterly Summary: "Nights and 102.1M 103.7M 99.7M 88.2M 121.1M 115.1M 113.2M 98.8M 132.6M 125.1M 122.8M 111.0M Experiences Booked"
  - Key Business Metrics: "Nights and Experiences Booked 98.8M 111.0M 448.2M 491.5M"
  
  **Asia Pacific commentary:** The only regional figure is a growth rate, not a count of nights or an average:
  
  > "In Asia Pacific, we saw low-20s Nights and Experiences Booked growth in Q4 2024 compared to Q4 2023."
  
  Because the letter provides no Asia Pacific nights or booking counts, Average Nights per Booking cannot be calculated for Asia Pacific for either period.

### Turn 5  (stop_reason=tool_use)
- edgar_search({"search_query": "Airbnb average nights per booking Asia Pacific 2024", "ciks": ["ABNB"], "start_date": "2025-01-01", "end_date": "2025-04-07", "form_types": ["10-K"]})
  result: {"total_matching_documents": 1, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}]}
- edgar_search({"search_query": "Airbnb \"Average Nights per Booking\" Asia Pacific", "start_date": "2024-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 2, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}, {"form": "10-K", "file_date": "2024-02-16", "period_ending": "2023-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-24-000006", "document": "abnb-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm"}]}

### Turn 6  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_10k_2024. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb_q4_2024
  abnb_10k_2024
  

### Turn 7  (stop_reason=tool_use)
- retrieve_information({"prompt": "Search this Airbnb 2024 10-K for any Asia Pacific or regional breakdown of Nights and Experiences Booked, Nights Booked, Average Nights per Booking, or Gross Booking Value by region (North America, EMEA, Latin America, Asia Pacific). Quote the definition of Average Nights per Booking if present, and any Asia Pacific figures with their units and period. State clearly if not found. Text: {{abnb_10k_2024}}"})
  result: **Short answer:** The filing does include an Asia Pacific breakdown of Nights and Experiences Booked, Gross Booking Value (GBV), and average nights per booking. It does not contain a formal definition of "Average Nights per Booking."
  
  ## Definition of Average Nights per Booking
  
  No formal definition appears in the filing. The Glossary of Terms (Item 7) covers active booker, active listing, available listings, check-ins, co-hosts, guest arrivals, hosts, and payments to customers, but not average nights per booking. The closest available language is in the Geographic Mix discussion, which says key metrics, including "Nights per Booking," "vary by geography," and in the Average nights per booking sentence:
  
  > "Our total Company average nights per booking, excluding experiences, was 3.8 in 2024 compared to 3.9 in 2023. Average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific."
  
  The forward-looking statements also refer to "our global average nights per booking." The filing does not state how the metric is calculated.
  
  ## Asia Pacific figures
  
  Source: Item 7, "Geographic Mix" table, unless noted. Figures are in millions except percentages.
  
  | Metric | Period | Asia Pacific | % of total | % change |
  |---|---|---|---|---|
  | Nights and Experiences Booked | Year ended Dec 31, 2023 | 51 million | 11% | — |
  | Nights and Experiences Booked | Year ended Dec 31, 2024 | 61 million | 12% | 20% |
  | Gross Booking Value (GBV) | Year ended Dec 31, 2023 | $6,016 million | 8% | — |
  | Gross Booking Value (GBV) | Year ended Dec 31, 2024 | $7,126 million | 9% | 18% |
  | Average nights per booking (excl. experiences) | Year ended Dec 31, 2024 | 3.3 nights | n/a | No 2023 regional figure given |
  
  Additional Asia Pacific context:
  - 
  …[truncated 918 chars]

### Turn 8  (stop_reason=tool_use)
- retrieve_information({"prompt": "Copy verbatim the sentence(s) containing 'average nights per booking' and 'Asia Pacific' from this text, and the Geographic Mix table row for Asia Pacific average nights. Text: {{abnb_10k_2024}}"})
  result: **Sentences containing "average nights per booking" or "Asia Pacific":**
  
  1. •our expectations regarding fluctuations to our global average nights per booking;
  2. Our total Company average nights per booking, excluding experiences, was 3.8 in 2024 compared to 3.9 in 2023.
  3. Average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific.
  4. We expect that our blended global average nights per booking will continue to fluctuate based on our geographic mix and changes in traveler behaviors.
  
  **Geographic Mix table row for Asia Pacific average nights:**
  
  The Geographic Mix table has no average nights per booking row. Its Asia Pacific rows cover only Nights and Experiences Booked, Gross Booking Value, and Revenue:
  
  - Nights and Experiences Booked: Asia Pacific51 11 61 12 20
  - Gross Booking Value: Asia Pacific6,016 8 7,126 9 18
  - Revenue: Asia Pacific840 9 992 9 18
  
  The Asia Pacific average nights figure (3.3 in 2024) appears only in sentence 3 above.

### Turn 9  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: 3.3 nights per booking** for Asia Pacific in fiscal year 2024 (full year, ended December 31, 2024). The figure excludes experiences, since Airbnb's company-wide average is stated on that basis.\n\n**Source and verification**\n- I checked Airbnb's FY2024 Form 10-K (filed 2025-02-13, accession 0001559720-25-000010), Item 7 \"Geographic Mix\" section. It states that average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific. The same section says the company-wide figure, excluding experiences, was 3.8 in 2024 compared with 3.9 in 2023.\n- The 10-K does not give a 2023 regional comparative, so no year-ov
…[truncated 1,420 chars])

### Final answer
**Answer: 3.3 nights per booking** for Asia Pacific in fiscal year 2024 (full year, ended December 31, 2024). The figure excludes experiences, since Airbnb's company-wide average is stated on that basis.

**Source and verification**
- I checked Airbnb's FY2024 Form 10-K (filed 2025-02-13, accession 0001559720-25-000010), Item 7 "Geographic Mix" section. It states that average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific. The same section says the company-wide figure, excluding experiences, was 3.8 in 2024 compared with 3.9 in 2023.
- The 10-K does not give a 2023 regional comparative, so no year-over-year change for Asia Pacific can be calculated from it.
- The Q4 2024 shareholder letter (8-K Exhibit 99.1, filed 2025-02-13) does not contain this regional metric. It gives only company-wide nights and experiences booked and says Asia Pacific nights and experiences booked grew in the low-20s percent in Q4 2024. So the 10-K is the controlling source for this figure.
- The 10-K does not define "average nights per booking" or describe how it is calculated. The only definition available is for the related metric, Nights and Experiences Booked, which is the sum of nights booked for stays and seats booked for experiences, net of cancellations and alterations.
- Context from the same table: Asia Pacific Nights and Experiences Booked were 61 million in 2024 (51 million in 2023). I did not recompute the 3.3 ratio because the 10-K does not disclose Asia Pacific nights booked separately from experiences.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2024 (filed 2025-02-13)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm",
            "name": "Airbnb, Inc. Q4 2024 Shareholder Letter, Form 8-K Exhibit 99.1 (filed 2025-02-13)"
        }
    ]
}