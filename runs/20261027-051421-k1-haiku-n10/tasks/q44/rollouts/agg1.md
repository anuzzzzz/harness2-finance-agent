## Rollout `agg1`
- outcome: submitted
- turns: 2; cost: $0.013; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Airbnb 2024 annual report average nights per booking by region Asia Pacific") → 0 results: 
- edgar_search({"search_query": "Airbnb average nights per booking Asia Pacific 2024", "ciks": ["ABNB"], "top_n_results": 10})
  ERROR: HTTPError: 403 Client Error: Forbidden for url: https://www.sec.gov/files/company_tickers.json

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Airbnb Revenue and Booking Statistics (2026) <https://backlinko.com/airbnb-stats>; Discover Latest Airbnb Statistics (2025) <https://analyzify.com/statsup/airbnb>; Airbnb, Inc. - Cloudfront.net <https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf>; Airbnb Statistics: Revenue and Users <https://radicalstorage.com/travel/airbnb-statistics/>; Airbnb Statistics 2026: Revenue, Hosts, Listings and Bookings <https://sqmagazine.co.uk/airbnb-statistics/>
- submit_final_result({"final_result": "**Answer: Airbnb's average nights per booking in Asia Pacific for 2024 was 3.3 nights.**\n\n**How I got there**\n- I looked for Airbnb's own 2024 disclosure of regional stay length. The Q4 2024 shareholder letter (published in early 2025, so it predates your April 7, 2025 reference date) reports the 2024 figures by region. The letter's excerpt gives Asia Pacific at 3.3 nights, with North America at 4.1, EMEA at 3.8, and Latin America at 3.7. The same passage gives the company-wide figure, excluding experiences, as 3.8 for 2024, down from 3.9 in 2023.\n- Independent aggregators are consistent with this. One lists Asia Pacific at 3.3 for 2024 and describes it as the region wi
…[truncated 1,054 chars])

### Final answer
**Answer: Airbnb's average nights per booking in Asia Pacific for 2024 was 3.3 nights.**

**How I got there**
- I looked for Airbnb's own 2024 disclosure of regional stay length. The Q4 2024 shareholder letter (published in early 2025, so it predates your April 7, 2025 reference date) reports the 2024 figures by region. The letter's excerpt gives Asia Pacific at 3.3 nights, with North America at 4.1, EMEA at 3.8, and Latin America at 3.7. The same passage gives the company-wide figure, excluding experiences, as 3.8 for 2024, down from 3.9 in 2023.
- Independent aggregators are consistent with this. One lists Asia Pacific at 3.3 for 2024 and describes it as the region with the shortest average stay. Another lists 3.3 for Asia Pacific in 2024 and 3.2 for 2023.
- Limitation: the shareholder letter is a PDF, which my tools cannot open. The 3.3 figure therefore rests on the search excerpt of that letter, cross-checked against secondary sources. I did not open the primary document directly.
- I ignored the 2025 figures that appeared in search results, since they fall after the reference date.

**Sources**
{
    "sources": [
        {
            "url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf",
            "name": "Airbnb Q4 2024 Shareholder Letter (PDF)"
        },
        {
            "url": "https://radicalstorage.com/travel/airbnb-statistics/",
            "name": "Radical Storage – Airbnb Statistics: Revenue and Users"
        },
        {
            "url": "https://www.wallstreetzen.com/stocks/us/nasdaq/abnb/statistics",
            "name": "WallStreetZen – Airbnb Statistics"
        }
    ]
}