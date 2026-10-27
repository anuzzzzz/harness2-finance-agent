## Rollout `ctl3`
- outcome: submitted
- turns: 2; cost: $0.012; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="TKO Endeavor assets acquisition total consideration") → 0 results: 
- edgar_search({"search_query": "TKO acquisition Endeavor assets consideration transaction close", "top_n_results": 10})
  result: {"total_matching_documents": 1033, "page": 1, "results": [{"form": "8-K/A", "file_date": "2023-09-18", "period_ending": "2023-09-12", "company": "Endeavor Group Holdings, Inc.  (EDR)  (CIK 0001766363)", "ciks": ["0001766363"], "accession": "0001193125-23-237000", "document": "d526530dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1766363/000119312523237000/d526530dex991.htm"}, {"form": "8-K", "file_date": "2024-11-07", "period_ending": "2024-11-07", "company": "Endeavor Group Holdings, Inc.  (EDR)  (CIK 0001766363)", "ciks": ["0001766363"], "accession": "0001193125-24-252644", "document": "d865891dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1766363/000119312524252644/d865891dex991.htm"}, {"form": "8-K", "file_date": "2024-10-24", "period_ending": "2024-10-23", "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266"], "accession": "0001193125-24-242249", "document": "d875145dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312524242249/d875145dex991.htm"}, {"form": "8-K", "file_date": "2025-02-27", "period_ending": "2025-02-27", "company": "Endeavor Group Holdings, Inc.  (EDR)  (CIK 0001766363)", "ciks": ["0001766363"], "accession": "0001193125-25-037654", "document": "d910583dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1766363/000119312525037654/d910583dex991.htm"}, {"form": "8-K", "file_date": "2025-03-19", "period_ending": "2025-03-19", "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266"], "accession": "0001193125-25-057890", "document": "d803159dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/197
  …[truncated 1,814 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: TKO Acquires Professional Bull Riders, On Location, and IMG From Endeavor <https://www.sportsvideo.org/2024/10/24/tko-acquires-professional-bull-riders-on-location-and-img-from-endeavor/>; TKO Group Holdings, Inc. - Form 10-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1973266/000119312526071651/tko-20251231.htm>; TKO Group Holdings, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1973266/000095017025067188/tko-ex99_1.htm>; TKO Group Holdings, Inc. - Form 424B3 - FY2024 <https://www.sec.gov/Archives/edgar/data/1973266/000095017024122397/424b3_tko_10q_q3_093024.htm>; Media Man Int on X: "TKO Announces Approval of Capital Return Program; Also Announces Strategic Acquisition of Sports Assets From Endeavor October 24, 2024 TKO Announces Approval of Capital Return Program; Also Announces Strategic Acquisition of Sports Assets From Endeavor Board Authorized $2 Bi… / X <https://x.com/mediamanint/status/1849609615128048067>
- submit_final_result({"final_result": "**Answer: about $3.30 billion** ($3.25 billion base consideration plus a $50 million purchase price adjustment), as reflected in TKO's filings for the close on February 28, 2025.\n\n**Reasoning**\n\n1. **Announced price:** When TKO agreed to buy Professional Bull Riders, On Location, and IMG from Endeavor in October 2024, the deal was pegged at $3.25 billion. The figure was set using the volume-weighted average price of TKO's Class A stock over the 25 trading days ending October 23, 2024 (<cite index=\"1-5\">TKO will acquire the Endeavor assets for a total consideration of $3.25 billion, based on the 25-trading-day volume-weighted average price of TKO's Class A common stock
…[truncated 2,703 chars])

### Final answer
**Answer: about $3.30 billion** ($3.25 billion base consideration plus a $50 million purchase price adjustment), as reflected in TKO's filings for the close on February 28, 2025.

**Reasoning**

1. **Announced price:** When TKO agreed to buy Professional Bull Riders, On Location, and IMG from Endeavor in October 2024, the deal was pegged at $3.25 billion. The figure was set using the volume-weighted average price of TKO's Class A stock over the 25 trading days ending October 23, 2024 (<cite index="1-5">TKO will acquire the Endeavor assets for a total consideration of $3.25 billion, based on the 25-trading-day volume-weighted average price of TKO's Class A common stock for the period ending on October 23, 2024.</cite>). The deal was all-equity.

2. **Price at close:** TKO's March 2025 disclosure on the completed transaction says <cite index="9-1">on February 28, 2025, TKO OpCo and TKO Group Holdings, Inc. completed the acquisition of the Professional Bull Riders, On Location, certain contracts associated with Wimbledon, Soccer and Stadia, SailGP, and Royal & Ancient Golf Club of St. Andrews</cite>. It states that the TKO parties <cite index="9-2">acquired the Businesses for a total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment</cite>.

3. **Calculation:** $3.25 billion + $0.05 billion = $3.30 billion. The earlier SEC filing language on the pre-close terms also flagged that the deal <cite index="7-4">is also subject to purchase price adjustments to be settled in cash and equity.</cite>

4. **Consideration form:** Endeavor received approximately 26.54 million common units of TKO and an equal number of TKO Class B shares (<cite index="9-3">Endeavor received approximately 26.54 million common units of TKO and subscribed for an equal number of shares of TKO's Class B Common Stock.</cite>).

**Caveats**
- The $3.25 billion headline is the base value. Adding the $50 million adjustment gives roughly $3.30 billion, the figure I consider the best measure at close.
- Some earlier announcements and the Endeavor 10-Q cite only $3.25 billion. Those figures predate the close and do not include the adjustment.
- Because the deal was treated as a common-control transaction, the consideration was recorded at historical carrying amounts rather than as a fair-value purchase price.

{
    "sources": [
        {
            "url": "https://www.sportsvideo.org/2024/10/24/tko-acquires-professional-bull-riders-on-location-and-img-from-endeavor/",
            "name": "SportsVideo.org – TKO Acquires Professional Bull Riders, On Location, and IMG From Endeavor"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312525057890/R8.htm",
            "name": "TKO Group Holdings SEC filing (March 2025) – description of business, Endeavor Asset Acquisition"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1766363/000095017024122829/edr-20240930.htm",
            "name": "Endeavor Group Holdings 10-Q for period ended September 30, 2024"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017024122397/424b3_tko_10q_q3_093024.htm",
            "name": "TKO Group Holdings 424B3 – Q3 2024 subsequent events"
        }
    ]
}