## Rollout `agg1`
- outcome: submitted
- turns: 4; cost: $0.097; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "kpi_metric_lookup"})
  result: ---
  name: kpi_metric_lookup
  description: Retrieve a company-reported operating metric (nights per booking, ADR, GBV, MAUs, ARPU, same-store sales and similar) for a named period, region or segment, and report it with its definition.
  ---
  ANALYTIC MOVE: look up one reported operating metric for a specific period and breakdown. No arithmetic is needed unless the question asks for one.
  
  1. Find the controlling source. Operating KPIs are usually not in the financial statements. Look in this order:
     - the 10-K, in MD&A "Key Business Metrics", "Geographic Mix" or the segment and geographic notes;
     - the 8-K earnings release (EX-99.1);
     - the shareholder letter or earnings presentation for the quarter containing fiscal year-end.
     A third-party aggregator (Statista, stats blogs) is only a cross-check, never a replacement for the company document.
  2. Read the figure from a fetched or retrieved passage of the company document (parse_html_page then retrieve_information), not from a search snippet or memory.
  3. Match the question's period to the metric's period. A full-year metric is not a Q4 metric. Confirm the region label is the company's own.
  4. Check the metric definition and any exclusions (e.g. Airbnb's company-wide nights per booking is "excluding experiences") and state which definition the number uses.
  5. Give the figure at the precision the company published (e.g. 3.3, not a third party's 3.33); mention the other as a cross-check.
  6. Sanity-check against neighbours: regional figures should bracket the company-wide figure; cite the prior-year comparison if the document gives one.
  7. The answer states: the figure, period and unit, the company's definition, and the document and URL it came from.
  
  Lead (unverified, re-confirm in text): Airbnb FY2024 average nights per
  …[truncated 265 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb10k. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb10k
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K, find the Average Nights per Booking by geographic region (Asia Pacific, North America, EMEA, Latin America) for the year ended December 31, 2024 and 2023, and the company-wide figure, plus the definition of Nights and Experiences Booked / average nights per booking and any exclusions. Quote the exact table values. {{abnb10k}}"})
  result: The 10-K gives the company-wide figures for both years, but it reports regional average nights per booking only for 2024 and does not provide a 2023 regional breakdown.
  
  | Region | 2023 | 2024 |
  |---|---|---|
  | North America | Not disclosed | 4.1 |
  | EMEA | Not disclosed | 3.8 |
  | Latin America | Not disclosed | 3.7 |
  | Asia Pacific | Not disclosed | 3.3 |
  | **Total Company** | **3.9** | **3.8** |
  
  **Exact source language (Item 7, Geographic Mix):**
  > "Our total Company average nights per booking, excluding experiences, was 3.8 in 2024 compared to 3.9 in 2023. Average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific. We expect that our blended global average nights per booking will continue to fluctuate based on our geographic mix and changes in traveler behaviors."
  
  **Definition of Nights and Experiences Booked (Item 7, Key Business Metrics):**
  > "Nights and Experiences Booked on our platform in a period represents the sum of the total number of nights booked for stays and the total number of seats booked for experiences, net of cancellations and alterations that occurred in that period. … A night can include one or more guests and can be for a listing with one or more bedrooms. … A seat is booked for each participant in an experience. Substantially all of the bookings on our platform to date have come from nights."
  
  The 10-K does not give a separate formal definition of "average nights per booking." Its only stated exclusion is that the company-wide figure is "excluding experiences." The regional figures are described only as "average nights per booking in 2024," with no further qualification.
  
  **Other relevant context:**
  - Regional Nights and Experiences Booked are measured "based on the location of t
  …[truncated 339 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Answer: Airbnb's average nights per booking in the Asia Pacific region for full-year 2024 was 3.3 nights.\n\nDefinition and basis: Airbnb's 10-K describes the company-wide version of this metric as excluding experiences. The 10-K defines Nights and Experiences Booked as the sum of nights booked for stays plus seats booked for experiences, net of cancellations and alterations in the period. Regional figures are measured by the location of the listing. The 10-K does not give a separate formal definition for \"average nights per booking,\" and it does not add a qualification to the regional figures beyond the 2024 period.\n\nContext from the same filing: the company-wide figur
…[truncated 699 chars])

### Final answer
Answer: Airbnb's average nights per booking in the Asia Pacific region for full-year 2024 was 3.3 nights.

Definition and basis: Airbnb's 10-K describes the company-wide version of this metric as excluding experiences. The 10-K defines Nights and Experiences Booked as the sum of nights booked for stays plus seats booked for experiences, net of cancellations and alterations in the period. Regional figures are measured by the location of the listing. The 10-K does not give a separate formal definition for "average nights per booking," and it does not add a qualification to the regional figures beyond the 2024 period.

Context from the same filing: the company-wide figure was 3.8 in 2024, down from 3.9 in 2023. The other 2024 regional figures were North America 4.1, EMEA 3.8, and Latin America 3.7, so Asia Pacific is the lowest of the four regions. The 10-K does not give a 2023 regional breakdown.

Source: Airbnb, Inc. Form 10-K for fiscal year ended December 31, 2024, MD&A "Geographic Mix" section (retrieved and verified in the filing text). No third-party cross-check was used.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for FY2024 (MD&A Geographic Mix and Key Business Metrics)"
        }
    ]
}