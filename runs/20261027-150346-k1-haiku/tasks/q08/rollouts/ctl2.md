## Rollout `ctl2`
- outcome: submitted
- turns: 4; cost: $0.034; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="TKO acquisition Endeavor assets consideration at closing") → 0 results: 
- edgar_search({"search_query": "TKO Group Endeavor acquisition consideration transaction close", "top_n_results": 10})
  result: {"total_matching_documents": 1033, "page": 1, "results": [{"form": "8-K/A", "file_date": "2023-09-18", "period_ending": "2023-09-12", "company": "Endeavor Group Holdings, Inc.  (EDR)  (CIK 0001766363)", "ciks": ["0001766363"], "accession": "0001193125-23-237000", "document": "d526530dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1766363/000119312523237000/d526530dex991.htm"}, {"form": "8-K", "file_date": "2024-11-07", "period_ending": "2024-11-07", "company": "Endeavor Group Holdings, Inc.  (EDR)  (CIK 0001766363)", "ciks": ["0001766363"], "accession": "0001193125-24-252644", "document": "d865891dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1766363/000119312524252644/d865891dex991.htm"}, {"form": "8-K", "file_date": "2024-10-24", "period_ending": "2024-10-23", "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266"], "accession": "0001193125-24-242249", "document": "d875145dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312524242249/d875145dex991.htm"}, {"form": "8-K", "file_date": "2025-02-27", "period_ending": "2025-02-27", "company": "Endeavor Group Holdings, Inc.  (EDR)  (CIK 0001766363)", "ciks": ["0001766363"], "accession": "0001193125-25-037654", "document": "d910583dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1766363/000119312525037654/d910583dex991.htm"}, {"form": "8-K", "file_date": "2025-03-19", "period_ending": "2025-03-19", "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266"], "accession": "0001193125-25-057890", "document": "d803159dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/197
  …[truncated 1,814 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 9 results: TKO Group Holdings, Inc. - Form ARS - FY2024 <https://www.sec.gov/Archives/edgar/data/1973266/000119312525097003/d909805dars.pdf>; 10-Q <https://www.sec.gov/Archives/edgar/data/1973266/000095017025067220/tko-20250331.htm>; TKO Group Holdings, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1973266/000095017025027778/tko-20241231.htm>; TKO Group Holdings, Inc. - Form 424B3 - FY2024 <https://www.sec.gov/Archives/edgar/data/1973266/000095017024122397/424b3_tko_10q_q3_093024.htm>; Endeavor Group Holdings, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1766363/000095017025028394/edr-20241231.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025067220/tko-20250331.htm", "key": "tko_q1_10q"})
  result: SUCCESS: The result has been saved to the data storage under the key: tko_q1_10q. (193,094 characters)
  The data_storage currently contains the following keys:
  tko_q1_10q
  

### Turn 3  (stop_reason=tool_use)
- web_search(query="TKO completes Endeavor Asset Acquisition IMG On Location PBR February 2025") → 0 results: 
- retrieve_information({"prompt": "From this TKO 10-Q, find the total consideration / purchase price of the Endeavor Asset Acquisition as measured at closing (February 28, 2025), including any purchase price adjustments, equity units issued, and cash components. Quote the exact figures and describe the breakdown. Text: {{tko_q1_10q}}"})
  result: The 10-Q does not give a single purchase price measured at closing (February 28, 2025), and it does not split the consideration into exact cash and equity amounts. The figures it does disclose are below.
  
  **Disclosed figures**
  
  - **Headline consideration:** "total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment (based on the volume-weighted average sales price of TKO Class A common stock for the twenty-five trading days ending on October 23, 2024)" (Note 1; MD&A). That is roughly **$3.30 billion** combined. The adjustment is keyed to the October 23, 2024 signing-date VWAP, not the closing-date price.
  - **Equity units issued:** "approximately 26.54 million common units of TKO OpCo" to Endeavor Group Holdings, Inc., with "an equivalent number of corresponding shares of TKO Class B common stock" subscribed (Note 1; Note 10). Note 10 says the equity consideration "increased the nonredeemable non-controlling interest in TKO OpCo, with a corresponding increase to additional paid-in capital."
  - **NFLP Shares:** Note 12 says that "upon the close of the Endeavor Asset Acquisition, the Company issued 160,455 shares of TKO Class A common stock for an aggregate value of $23.5 million to NFL Properties LLC, as set forth in the Endeavor Asset Acquisition Agreement." The 10-Q does not say whether this is inside or outside the $3.25 billion.
  - **Cash component:** The only explicit cash figure tied to the transaction is "contributions of $23.3 million from Endeavor Group Holdings, Inc. in connection with the Endeavor Asset Acquisition" (MD&A, Cash Flows). The cash flow statement also shows a non-cash "Capital contribution from parent" of $49,443 thousand, but the 10-Q does not explicitly link it to the acquisition.
  
  **Breakdown**
  
  | Component | 
  …[truncated 975 chars]

### Turn 4  (stop_reason=tool_use)
- web_search(query=null) → 10 results: TKO Group Holdings, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1973266/000119312525040879/d879819dex991.htm>; TKO Group Holdings, Inc. - Form 10-Q - FY2025 <https://www.sec.gov/Archives/edgar/data/1973266/000095017025067220/tko-20250331.htm>; Endeavor Group Holdings, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1766363/000119312525040892/d105376dex991.htm>; TKO Group Holdings, Inc. - Form 10-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1973266/000119312526071651/tko-20251231.htm>; Endeavor Group Holdings, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1766363/000095017025028394/edr-20241231.htm>
- submit_final_result({"final_result": "**Answer: About $3.30 billion total consideration at close** ($3.25 billion base consideration plus a $50 million purchase price adjustment), paid almost entirely in TKO equity.\n\n**Reasoning and evidence**\n\n1. **Deal terms at signing.** TKO agreed on October 23, 2024 to acquire the Endeavor assets (PBR, On Location, and IMG) <cite index=\"1-3\">for total consideration of $3.25 billion, based on the volume-weighted average sales price of TKO's Class A common stock for the twenty five trading days ending on October 23, 2024.</cite>\n\n2. **Consideration at close.** The later TKO filing that describes the closed deal states that <cite index=\"7-1\">the TKO Parties acquired
…[truncated 2,854 chars])

### Final answer
**Answer: About $3.30 billion total consideration at close** ($3.25 billion base consideration plus a $50 million purchase price adjustment), paid almost entirely in TKO equity.

**Reasoning and evidence**

1. **Deal terms at signing.** TKO agreed on October 23, 2024 to acquire the Endeavor assets (PBR, On Location, and IMG) <cite index="1-3">for total consideration of $3.25 billion, based on the volume-weighted average sales price of TKO's Class A common stock for the twenty five trading days ending on October 23, 2024.</cite>

2. **Consideration at close.** The later TKO filing that describes the closed deal states that <cite index="7-1">the TKO Parties acquired the Businesses for a total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment (based on the volume-weighted average sales price of TKO PubCo Class A Common Stock for the twenty five trading days ending on October 23, 2024).</cite> Adding the two components gives $3.25B + $50M = **$3.30 billion**.

3. **Form of payment.** <cite index="7-2">Endeavor received approximately 26.54 million common units of TKO and subscribed for an equal number of shares of TKO's Class B Common Stock.</cite> The deal was announced as <cite index="9-1">an all-equity transaction valued at $3.25 billion</cite>.

4. **Closing date.** <cite index="11-1">On February 28, 2025, TKO OpCo and TKO Group Holdings, Inc. completed the acquisition</cite> of the IMG business, On Location, and PBR.

**Caveats**
- The $3.30 billion figure is my sum of the disclosed base amount and the $50 million adjustment. TKO does not state a single closing-date total in the sources I reviewed.
- The adjustment is keyed to the October 23, 2024 VWAP, not the closing-date share price, so the 26.54 million units may not reflect $3.25 billion at closing prices.
- The Q1 2025 10-Q also discloses a separate issuance of 160,455 Class A shares to NFL Properties LLC, valued at $23.5 million, and a $23.3 million cash contribution from Endeavor. The filing does not say whether these sit inside or outside the $3.30 billion, so I have not added them.

**Sources**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312525057890/R8.htm",
            "name": "TKO Group Holdings – Description of Business (SEC filing, 2025)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312525097003/d909805dars.pdf",
            "name": "TKO Group Holdings – Form ARS FY2024"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025027778/tko-20241231.htm",
            "name": "TKO Group Holdings – Form 10-K FY2024"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025067220/tko-20250331.htm",
            "name": "TKO Group Holdings – Form 10-Q Q1 2025"
        },
        {
            "url": "https://investor.tkogrp.com/news/news-details/2025/TKO-Completes-Acquisition-of-Sports-Assets-From-Endeavor/default.aspx",
            "name": "TKO Completes Acquisition of Sports Assets From Endeavor (press release, Feb 28, 2025)"
        },
        {
            "url": "https://investor.tkogrp.com/news/news-details/2025/TKO-Reports-Fourth-Quarter-and-Full-Year-2024-Results/default.aspx",
            "name": "TKO Reports Fourth Quarter and Full Year 2024 Results"
        }
    ]
}