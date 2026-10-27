## Rollout `inv1`
- outcome: submitted
- turns: 8; cost: $0.161; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025067220/tko-20250331.htm", "key": "tko_10q"})
  result: SUCCESS: The result has been saved to the data storage under the key: tko_10q. (193,094 characters)
  The data_storage currently contains the following keys:
  tko_10q
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1973266/0001193125-25-040879/d879819d8k.htm", "key": "tko_8k"})
  ERROR: ValueError: HTTP 403 when fetching https://www.sec.gov/Archives/edgar/data/1973266/0001193125-25-040879/d879819d8k.htm

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this TKO 10-Q, find the business combination / acquisition note and any table of consideration transferred for the Endeavor acquisition (closing February 28, 2025). Report the total consideration amount, each component (cash, OpCo units, Class B shares, purchase price adjustment, fair value of equity at closing, any other), the measurement date/share price used, and the units/period. Quote the relevant text. Text: {{tko_10q}}"})
  result: **The 10-Q has no business combination note or consideration-transferred table for the Endeavor acquisition.** The filing describes the transaction only in narrative form, and it does not break the consideration into components.
  
  The filing also covers two different Endeavor transactions, and the one closing February 28, 2025 is not the Silver Lake take-private:
  
  - **Endeavor Asset Acquisition (closed February 28, 2025):** TKO acquired the IMG business, On Location, and PBR from Endeavor affiliates. The filing says it "was accounted for as a common control acquisition," so it was recorded at historical carrying amounts with no fair-value purchase accounting or goodwill step-up.
  - **Endeavor Take-Private (closed March 24, 2025):** Silver Lake acquired Endeavor Group Holdings. TKO is not the acquirer, and the filing gives no consideration figures for it.
  
  ## What the filing does say about the February 28, 2025 transaction
  
  **Note 1, Description of Business:**
  > "the TKO Parties acquired the Acquired Businesses for total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment (based on the volume-weighted average sales price of TKO Class A common stock for the twenty-five trading days ending on October 23, 2024). Endeavor Group Holdings, Inc. received approximately 26.54 million common units of TKO OpCo and subscribed for an equivalent number of corresponding shares of TKO Class B common stock."
  
  **Note 10, Stockholders' Equity:**
  > "On February 28, 2025, as consideration paid in connection with the Endeavor Asset Acquisition, the Company issued approximately 26.54 million Common Units of TKO OpCo and an equivalent number of corresponding shares of TKO Class B common stock to Endeavor OpCo and certain of EGH's other subsidiaries. The equit
  …[truncated 2,570 chars]

### Turn 3  (stop_reason=tool_use)
- edgar_search({"search_query": "TKO Endeavor Asset Acquisition consideration closing", "ciks": ["1973266"], "start_date": "2025-02-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 6, "page": 1, "results": [{"form": "8-K", "file_date": "2025-03-19", "period_ending": "2025-03-19", "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266"], "accession": "0001193125-25-057890", "document": "d803159dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312525057890/d803159dex991.htm"}, {"form": "10-K", "file_date": "2025-02-26", "period_ending": "2024-12-31", "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266"], "accession": "0000950170-25-027778", "document": "tko-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025027778/tko-20241231.htm"}, {"form": "SCHEDULE 13D", "file_date": "2025-02-06", "period_ending": null, "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266", "0001766363"], "accession": "0000950170-25-015735", "document": "primary_doc.xml", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025015735/primary_doc.xml"}, {"form": "SCHEDULE 13D", "file_date": "2025-02-06", "period_ending": null, "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266", "0001868088"], "accession": "0000950170-25-015761", "document": "primary_doc.xml", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025015761/primary_doc.xml"}, {"form": "8-K", "file_date": "2025-02-26", "period_ending": "2025-02-26", "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266"], "accession": "0000950170-25-027743", "document": "tko-ex99_1.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1973266/0000950170
  …[truncated 389 chars]
- retrieve_information({"prompt": "Search this TKO 10-Q for every mention of \"consideration\", \"purchase price\", \"fair value\", \"closing\", \"Closing\" and \"Endeavor Asset Acquisition\" with dollar amounts. Report each passage with its amount and context, especially any amount measured at the closing date (February 28, 2025) such as a value of equity issued or the total purchase price at close. Text: {{tko_10q}}"})
  result: 

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "List every passage in this document that mentions the Endeavor Asset Acquisition with a dollar amount, including total consideration, purchase price, fair value, or value of equity issued at closing. Give the exact amounts and the surrounding sentence. Document: {{tko_10q}}"})
  result: Three passages qualify. Two state the total consideration, and one gives the value of equity issued at closing.
  
  **1. Note 1, Description of Business (p. 11)**
  "In connection with the Endeavor Asset Acquisition Agreement, the TKO Parties acquired the Acquired Businesses for total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment (based on the volume-weighted average sales price of TKO Class A common stock for the twenty-five trading days ending on October 23, 2024)."
  
  **2. Item 2, MD&A, Endeavor Asset Acquisition (p. 32)**
  "In connection with the Endeavor Asset Acquisition Agreement, the TKO Parties acquired the Acquired Businesses for total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment (based on the volume-weighted average sales price of TKO Class A common stock for the twenty five trading days ending on October 23, 2024)."
  
  **3. Note 12, Equity-Based Compensation (p. 21)**
  "Upon the close of the Endeavor Asset Acquisition, the Company issued 160,455 shares of TKO Class A common stock for an aggregate value of $23.5 million to NFL Properties LLC, as set forth in the Endeavor Asset Acquisition Agreement (such shares, the "NFLP Shares")."
  
  Passages that mention the acquisition with a dollar figure but do not fit the requested categories, so I excluded them:
  - Note 10 gives the equity consideration as about 26.54 million units but no dollar amount.
  - Note 10 and Note 11 give the reclassified net parent investment ($1,552.1 million) and AOCI ($67.8 million), which are accounting reclassifications rather than consideration or fair value.
  - Part II, Item 2 reports a $20 million share issuance on March 4, 2025, but it is tied to a contract counterparty and a commercial arrangement, not the End
  …[truncated 241 chars]
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025027778/tko-20241231.htm", "key": "tko_10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: tko_10k. (524,461 characters)
  The data_storage currently contains the following keys:
  tko_10q
  tko_10k
  

### Turn 5  (stop_reason=tool_use)
- retrieve_information({"prompt": "In this FY2024 10-K, find the Endeavor Asset Acquisition discussion: total consideration, purchase price, the closing date measurement or value of TKO equity issued at close, and any subsequent events note about the closing on February 28, 2025. Quote amounts and context. Document: {{tko_10k}}"})
  result: **The 10-K does not describe a February 28, 2025 closing.** This annual report was signed February 26, 2025, and it describes the Endeavor Asset Acquisition as still pending. Its subsequent-events disclosures don't mention a closing on that date, so I can't provide a closing-date measurement or a closing-date value for the TKO equity.
  
  **Total consideration and purchase price**
  
  Note 22 (Commitments and Contingencies) states: "Under the terms of the agreement, TKO will acquire the Endeavor assets for total consideration of $3.25 billion, based on the volume-weighted average sales price of TKO's Class A common stock for the twenty five trading days ending on October 23, 2024. Endeavor will receive approximately 26.1 million common units of TKO OpCo and will subscribe for an equal number of shares of TKO's Class B common stock (subject to certain customary purchase price adjustments to be settled at the closing in equity and cash)."
  
  The 10-K gives no per-share or per-unit price. Dividing $3.25 billion by 26.1 million units implies roughly $124 per unit, but that is my arithmetic, not a disclosed figure, and the equity/cash adjustment mechanics are not quantified.
  
  **TKO equity issued at close**
  
  Risk factors say: "the Company expects to issue approximately 26.1 million TKO OpCo Units and corresponding shares of Class B common stock (subject to certain customary purchase price adjustments to be settled at the closing in equity and cash) to the EDR Parties, who beneficially hold approximately 53.9% of the Company's total outstanding shares." They estimate "an approximate 6% reduction of equity ownership and... an approximate 6% reduction in the total voting interests."
  
  Because the deal had not closed, no fair value of the equity issued at close is reported.
  
  **Expected ac
  …[truncated 1,840 chars]

### Turn 6  (stop_reason=tool_use)
- edgar_search({"search_query": "TKO completion Endeavor Asset Acquisition OpCo units issued February 28, 2025", "start_date": "2025-02-27", "end_date": "2025-03-10"})
  result: {"total_matching_documents": 1, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-27", "period_ending": "2024-12-31", "company": "Endeavor Group Holdings, Inc.  (EDR)  (CIK 0001766363)", "ciks": ["0001766363"], "accession": "0000950170-25-028394", "document": "edr-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1766363/000095017025028394/edr-20241231.htm"}]}

### Turn 7  (stop_reason=tool_use)
- retrieve_information({"prompt": "In this 10-Q, does the document state the final purchase price adjustment amount settled at closing, the final number of OpCo units or Class B shares issued at closing, any closing share price, or any dollar value of the equity issued at closing (other than the 160,455 NFLP shares)? Quote exact text and amounts, or state clearly that none is given. Document: {{tko_10q}}"})
  result: The 10-Q gives no final settled purchase price adjustment, no exact count of units or shares issued at closing, no closing share price, and no dollar value for the closing equity issuance other than the NFLP shares. Its closest statements are below.
  
  **1. Final purchase price adjustment settled at closing: Not stated as a final settled amount.**
  Note 1 says: "the TKO Parties acquired the Acquired Businesses for total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment (based on the volume-weighted average sales price of TKO Class A common stock for the twenty-five trading days ending on October 23, 2024)." The MD&A repeats this language. The $50 million is a stated adjustment, but the filing does not say it was the amount settled at closing.
  
  **2. Final number of OpCo units or Class B shares issued at closing: Only approximate figures.**
  - Note 1: "Endeavor Group Holdings, Inc. received approximately 26.54 million common units of TKO OpCo and subscribed for an equivalent number of corresponding shares of TKO Class B common stock."
  - Note 10: "On February 28, 2025, as consideration paid in connection with the Endeavor Asset Acquisition, the Company issued approximately 26.54 million Common Units of TKO OpCo and an equivalent number of corresponding shares of TKO Class B common stock."
  - The Statement of Stockholders' Equity shows 26,542 (thousand) Class B shares under "Stock issuances and other, net," but that line is not tied to the Endeavor issuance. The balance sheet shows Class B shares rising from 89,616,891 to 116,158,615.
  
  The filing's only explicit count is "approximately 26.54 million."
  
  **3. Closing share price: Not stated.**
  Note 12 says the RSU conversion values were "determined using the closing price of TKO Class A comm
  …[truncated 1,185 chars]

### Turn 8  (stop_reason=tool_use)
- submit_final_result({"final_result": "Answer: The headline total consideration TKO agreed to pay for the Endeavor assets is about $3.30 billion ($3.25 billion plus a $50 million purchase price adjustment). The filings I could open do not give a figure measured at the February 28, 2025 closing, so the $3.30 billion is not a closing-date measurement.\n\nWhat the filings say:\n- TKO's Q1 2025 10-Q (filed for the period ended March 31, 2025, which covers the February 28, 2025 closing) states in Note 1 that the TKO Parties acquired the Acquired Businesses \"for total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment,\" with the adjustment based on the volume-weighted average s
…[truncated 2,732 chars])

### Final answer
Answer: The headline total consideration TKO agreed to pay for the Endeavor assets is about $3.30 billion ($3.25 billion plus a $50 million purchase price adjustment). The filings I could open do not give a figure measured at the February 28, 2025 closing, so the $3.30 billion is not a closing-date measurement.

What the filings say:
- TKO's Q1 2025 10-Q (filed for the period ended March 31, 2025, which covers the February 28, 2025 closing) states in Note 1 that the TKO Parties acquired the Acquired Businesses "for total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment," with the adjustment based on the volume-weighted average sales price of TKO Class A common stock for the 25 trading days ending October 23, 2024. The MD&A repeats this language.
- The same 10-Q says Endeavor received approximately 26.54 million TKO OpCo common units and an equal number of TKO Class B shares. Note 10 says these were issued on February 28, 2025 as consideration for the Endeavor Asset Acquisition, but gives no dollar value for them.
- The 10-Q does not state the final purchase price adjustment settled at closing, a closing share price, or a dollar value for the equity issued at closing. Note 12 says RSU values were set using the closing price on the closing day, but does not disclose that price.
- Separately, 160,455 Class A shares were issued to NFL Properties LLC "for an aggregate value of $23.5 million" upon closing. The 10-Q does not say this is part of the $3.25 billion consideration, so I did not add it.
- The FY2024 10-K (signed February 26, 2025, before closing) gives the same $3.25 billion total consideration and about 26.1 million units, subject to purchase price adjustments to be settled at closing in equity and cash. It has no closing-date measurement.
- Because the transaction was accounted for as a common control acquisition, the 10-Q records the acquired businesses at historical carrying amounts rather than fair value, so no purchase-price allocation or goodwill is recorded.

Calculation: $3,250 million + $50 million = $3,300 million (about $3.30 billion). This is the headline figure. An implied per-unit value of about $122 per unit ($3.25 billion / 26.54 million units) is my own arithmetic, not a disclosed figure.

Limitations: The 8-K filed around February 28, 2025 could not be opened (HTTP 403 error), and I found no other closing-date filing that gives a qualified total. The closing-date figure is therefore not confirmed. Using the 26.54 million units with TKO's February 28, 2025 closing share price would give an estimate, but I did not retrieve that price, so I did not calculate it.

Sources: TKO Group Holdings Q1 2025 Form 10-Q (https://www.sec.gov/Archives/edgar/data/1973266/000095017025067220/tko-20250331.htm); TKO Group Holdings FY2024 Form 10-K (https://www.sec.gov/Archives/edgar/data/1973266/000095017025027778/tko-20241231.htm).

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025067220/tko-20250331.htm",
            "name": "TKO Group Holdings Form 10-Q for quarter ended March 31, 2025"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025027778/tko-20241231.htm",
            "name": "TKO Group Holdings Form 10-K for fiscal year 2024"
        }
    ]
}