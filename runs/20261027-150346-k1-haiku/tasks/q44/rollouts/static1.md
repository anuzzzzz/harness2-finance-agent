## Rollout `static1`
- outcome: submitted
- turns: 4; cost: $0.107; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Airbnb 2024 annual report average nights per booking by region Asia Pacific") → 0 results: 
- edgar_search({"search_query": "Airbnb 10-K 2024 average nights per booking Asia Pacific", "ciks": ["ABNB"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 2, "page": 1, "results": [{"form": "8-K", "file_date": "2025-02-13", "period_ending": "2025-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-25-026054", "document": "d915198dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm"}, {"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Airbnb Statistics - Airbnb Facts, Stats, Trends & Data (2026) <https://www.wallstreetzen.com/stocks/us/nasdaq/abnb/statistics>; Airbnb, Inc. - Cloudfront.net <https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf>; Discover Latest Airbnb Statistics (2025) <https://analyzify.com/statsup/airbnb>; Airbnb: The Next Chapter - The Wolf of Harcourt Street <https://www.thewolfofharcourtstreet.com/p/airbnb-the-next-chapter>; Airbnb Statistics: Revenue and Users <https://radicalstorage.com/travel/airbnb-statistics/>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_10k_2024. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb_10k_2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 2024 10-K, find the average nights per booking for Asia Pacific for 2024 (and 2023 for comparison), including the table of Nights per Booking by region and any explanatory text. Quote the exact figures and the table labels. Document: {{abnb_10k_2024}}"})
  result: **Asia Pacific average nights per booking: 3.3 in 2024.** This 10-K does not give a 2023 Asia Pacific figure, so I can't provide a year-over-year comparison from this document.
  
  **What the filing says**
  
  The figures appear in prose in the "Geographic Mix" section of Item 7 (MD&A), not in a dedicated "Nights per Booking" table:
  
  > "Our total Company average nights per booking, excluding experiences, was 3.8 in 2024 compared to 3.9 in 2023. Average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific. We expect that our blended global average nights per booking will continue to fluctuate based on our geographic mix and changes in traveler behaviors."
  
  **The closest table: "Geographic Mix"**
  
  The table in that section is headed "Nights and Experiences Booked" and has the columns 2023, % of Total, 2024, % of Total, and % Change (in millions, except percentages). The Asia Pacific row reads:
  
  | Region | 2023 | % of Total | 2024 | % of Total | % Change |
  |---|---|---|---|---|---|
  | Asia Pacific | 51 | 11 | 61 | 12 | 20 |
  
  This table reports Nights and Experiences Booked, which include experiences, and it does not show nights per booking. It also doesn't disclose booking counts, so the 3.3 figure can't be recalculated from it.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: Airbnb's Asia Pacific average nights per booking in 2024 was 3.3 nights.**\n\n**How I got it**\n- The FY2024 Form 10-K (filed February 13, 2025) is the primary source. I parsed it and checked the \"Geographic Mix\" section of MD&A. It states the company-wide figure (excluding experiences) and the regional figures in prose, not in a table.\n- The 10-K reports the company-wide average at 3.8 nights for 2024, versus 3.9 in 2023. The Asia Pacific figure for 2024 is 3.3 nights, and the same section gives 4.1 for North America, 3.8 for EMEA and 3.7 for Latin America.\n- The 10-K does not give a 2023 Asia Pacific nights-per-booking figure, so no year-over-year comparison
…[truncated 1,231 chars])

### Final answer
**Answer: Airbnb's Asia Pacific average nights per booking in 2024 was 3.3 nights.**

**How I got it**
- The FY2024 Form 10-K (filed February 13, 2025) is the primary source. I parsed it and checked the "Geographic Mix" section of MD&A. It states the company-wide figure (excluding experiences) and the regional figures in prose, not in a table.
- The 10-K reports the company-wide average at 3.8 nights for 2024, versus 3.9 in 2023. The Asia Pacific figure for 2024 is 3.3 nights, and the same section gives 4.1 for North America, 3.8 for EMEA and 3.7 for Latin America.
- The 10-K does not give a 2023 Asia Pacific nights-per-booking figure, so no year-over-year comparison for this region is possible from that filing.
- The 10-K's Asia Pacific table covers Nights and Experiences Booked, not nights per booking. It shows 51 million in 2023 and 61 million in 2024 (up 20%). Those counts include experiences, so they cannot be used to recompute the 3.3 figure.
- Airbnb's Q4 2024 shareholder letter, which carries the same regional metrics, corroborates the 3.3 figure. It reports that <cite index="2-7">average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific.</cite>

**Note on third-party data:** Third-party aggregators show Asia Pacific at 3.3 nights for 2023 and 2024, which is consistent with the company figure. I did not use them as evidence.

**Sources**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2024 (SEC EDGAR)"
        },
        {
            "url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf",
            "name": "Airbnb Q4 2024 shareholder letter"
        }
    ]
}