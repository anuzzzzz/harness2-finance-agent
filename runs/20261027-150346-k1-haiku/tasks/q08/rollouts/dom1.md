## Rollout `dom1`
- outcome: submitted
- turns: 7; cost: $0.049; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="TKO acquisition Endeavor assets closing consideration") → 0 results: 
- load_skill({"name": "deal_consideration_at_close"})
  result: ---
  name: deal_consideration_at_close
  description: Determine the total consideration an acquirer paid for acquired businesses as measured at closing (headline price vs. closing-date value, cash vs. equity, adjustments), from the closing 8-K and the acquirer's periodic filings.
  ---
  ANALYTIC MOVE: reconcile. Inputs: the headline price in the agreement, the closing-date settlement (cash, equity units issued, assumed debt, purchase-price adjustments), and the accounting basis. Result: one consideration figure at close, plus the bridge from the headline.
  
  1. Separate three numbers and never blur them: (a) headline price at signing; (b) adjustments settled at closing (working capital, volume-weighted-price true-ups); (c) consideration measured at close, meaning cash plus the value of equity issued at the closing-date price, plus any assumed debt or contingent items. Say which one the question asks for.
  2. Controlling sources, in order: the closing 8-K (Item 2.01 completion of acquisition, Item 3.02 unregistered share issuance, and any EX-99); the acquirer's next 10-Q or 10-K acquisition or business-combination note (consideration table, purchase price allocation); the subsequent-events note in the 10-K if the close came after year-end. Open at least the closing 8-K and the note, not only the MD&A summary.
  3. Equity component: units or shares issued x the price the filing states at close (or the closing-date market price in the note). Show the multiplication. Do not substitute the signing-date price.
  4. Check the accounting basis. If the deal was between entities under common control, the filing may record it at historical carrying amounts. Then state both the contractual consideration and the recorded amount, and say which the question's wording points to.
  5. If a filing give
  …[truncated 1,455 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: TKO Group Holdings, Inc. - Form ARS - FY2024 <https://www.sec.gov/Archives/edgar/data/1973266/000119312525097003/d909805dars.pdf>; 10-Q <https://www.sec.gov/Archives/edgar/data/1973266/000095017025067220/tko-20250331.htm>; TKO Acquires Professional Bull Riders, On Location, and IMG From Endeavor <https://www.sportsvideo.org/2024/10/24/tko-acquires-professional-bull-riders-on-location-and-img-from-endeavor/>; TKO Group Holdings, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1973266/000095017024122364/tko-20240930.htm>; TKO Group Holdings - TKO Announces Approval of Capital Return Program; Also Announces Strategic Acquisition of Sports Assets From Endeavor <https://investor.tkogrp.com/news/news-details/2024/TKO-Announces-Approval-of-Capital-Return-Program-Also-Announces-Strategic-Acquisition-of-Sports-Assets-From-Endeavor/default.aspx>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025067220/tko-20250331.htm", "key": "tko10q"})
  result: SUCCESS: The result has been saved to the data storage under the key: tko10q. (193,094 characters)
  The data_storage currently contains the following keys:
  tko10q
  
- edgar_search({"search_query": "TKO Endeavor Asset Acquisition completion closing units issued fair value", "ciks": ["1973266"], "start_date": "2025-02-01"})
  result: {"total_matching_documents": 3, "page": 1, "results": [{"form": "8-K", "file_date": "2025-03-19", "period_ending": "2025-03-19", "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266"], "accession": "0001193125-25-057890", "document": "d803159dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312525057890/d803159dex991.htm"}, {"form": "10-K", "file_date": "2025-02-26", "period_ending": "2024-12-31", "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266"], "accession": "0000950170-25-027778", "document": "tko-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025027778/tko-20241231.htm"}, {"form": "8-K", "file_date": "2025-02-26", "period_ending": "2025-02-26", "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266"], "accession": "0000950170-25-027743", "document": "tko-ex99_1.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025027743/tko-ex99_1.htm"}]}

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this TKO 10-Q text, find all statements about the Endeavor Asset Acquisition's total consideration, purchase price adjustment, number of common units/Class B shares issued, closing date, and any fair value or purchase consideration measured at closing (including per-unit prices). Quote the relevant passages with exact figures. Text: {{tko10q}}"})
  result: ## Endeavor Asset Acquisition: Consideration, Adjustments, Units/Shares, and Closing Date
  
  ### Total consideration and purchase price adjustment
  
  **Note 1, Description of Business:**
  > "In connection with the Endeavor Asset Acquisition Agreement, the TKO Parties acquired the Acquired Businesses for total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment (based on the volume-weighted average sales price of TKO Class A common stock for the twenty-five trading days ending on October 23, 2024)."
  
  **MD&A, Overview, Endeavor Asset Acquisition:**
  > "In connection with the Endeavor Asset Acquisition Agreement, the TKO Parties acquired the Acquired Businesses for total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment (based on the volume-weighted average sales price of TKO Class A common stock for the twenty five trading days ending on October 23, 2024)."
  
  The two passages differ slightly in punctuation ("twenty-five" vs. "twenty five"), but the figures are identical.
  
  ### Number of common units and Class B shares issued
  
  **Note 1, Description of Business:**
  > "Endeavor Group Holdings, Inc. received approximately 26.54 million common units of TKO OpCo and subscribed for an equivalent number of corresponding shares of TKO Class B common stock."
  
  **MD&A, Overview:**
  > "Endeavor Group Holdings, Inc. received approximately 26.54 million common units of TKO OpCo and subscribed for an equivalent number of corresponding shares of TKO's Class B common stock."
  
  **Note 10, Stockholders' Equity:**
  > "On February 28, 2025, as consideration paid in connection with the Endeavor Asset Acquisition, the Company issued approximately 26.54 million Common Units of TKO OpCo and an equivalent number of corresponding shar
  …[truncated 3,185 chars]
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312525057890/R8.htm", "key": "r8"})
  result: SUCCESS: The result has been saved to the data storage under the key: r8. (6,814 characters)
  The data_storage currently contains the following keys:
  tko10q
  r8
  

### Turn 4  (stop_reason=tool_use)
- edgar_search({"search_query": "TKO completion of acquisition Endeavor Asset Acquisition February 28, 2025", "ciks": ["1973266"], "start_date": "2025-02-27", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 1, "page": 1, "results": [{"form": "8-K", "file_date": "2025-03-19", "period_ending": "2025-03-19", "company": "TKO Group Holdings, Inc.  (TKO)  (CIK 0001973266)", "ciks": ["0001973266"], "accession": "0001193125-25-057890", "document": "d803159dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312525057890/d803159dex991.htm"}]}

### Turn 5  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312525057890/d803159dex991.htm", "key": "ex991"})
  result: SUCCESS: The result has been saved to the data storage under the key: ex991. (269,820 characters)
  The data_storage currently contains the following keys:
  tko10q
  r8
  ex991
  
- retrieve_information({"prompt": "From this TKO 10-Q text, find any statement of the purchase consideration for the Endeavor Asset Acquisition in a purchase price allocation or business combination/common control note, and any closing-date fair value of the equity issued (units x price). Also find the \"Liquidity\" passage on contributions from Endeavor. Text: {{tko10q}}"})
  result: ## 1. Purchase consideration for the Endeavor Asset Acquisition
  
  The 10-Q does not contain a purchase price allocation. It describes the transaction as a **common control** acquisition, so the Acquired Businesses were recorded at historical carrying amounts rather than fair values.
  
  The consideration statement appears in **Note 1, Description of Business**:
  
  > "the TKO Parties acquired the Acquired Businesses for total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment (based on the volume-weighted average sales price of TKO Class A common stock for the twenty-five trading days ending on October 23, 2024). Endeavor Group Holdings, Inc. received approximately 26.54 million common units of TKO OpCo and subscribed for an equivalent number of corresponding shares of TKO Class B common stock."
  
  Note 10, Stockholders' Equity, adds:
  
  > "On February 28, 2025, as consideration paid in connection with the Endeavor Asset Acquisition, the Company issued approximately 26.54 million Common Units of TKO OpCo and an equivalent number of corresponding shares of TKO Class B common stock to Endeavor OpCo and certain of EGH's other subsidiaries. The equity consideration increased the nonredeemable non-controlling interest in TKO OpCo, with a corresponding increase to additional paid-in capital."
  
  The MD&A repeats the $3.25 billion plus $50 million figure.
  
  ## 2. Closing-date fair value of equity issued (units × price)
  
  The text does not provide this. It gives the share count (about 26.54 million TKO OpCo Common Units and equivalent Class B shares) but no closing-date share price. The $3.25 billion plus $50 million figure is priced off a VWAP ending October 23, 2024, not the February 28, 2025 closing date, so it is not a closing-date fair value of the 
  …[truncated 1,327 chars]

### Turn 6  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this TKO 8-K exhibit, find all statements about the Endeavor Asset Acquisition consideration, purchase price adjustment, closing date, units issued, and any value of equity consideration at closing (e.g., closing share price or fair value). Quote exact figures. Text: {{ex991}}"})
  result: ## Endeavor Asset Acquisition: Consideration, Adjustment, Closing Date, and Units
  
  **Consideration and purchase price adjustment**
  
  - MD&A, "Endeavor Asset Acquisition": "TKO acquired the Businesses for a total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment (based on the volume-weighted average sales price of TKO PubCo Class A Common Stock for the twenty five trading days ending on October 23, 2024)."
  - Note 1, "Endeavor Asset Acquisition": "In connection with the Endeavor Asset Acquisition Agreement the TKO Parties acquired the Businesses for a total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment (based on the volume-weighted average sales price of TKO PubCo Class A Common Stock for the twenty five trading days ending on October 23, 2024)."
  
  **Closing date**
  
  - MD&A: "On February 28, 2025, TKO Operating Company, LLC ... and TKO Group Holdings, Inc. ... completed the acquisition of the Professional Bull Riders ... pursuant to the Transaction Agreement, dated as of October 23, 2024 (as amended, the 'Endeavor Asset Acquisition Agreement')."
  - Note 1: "On February 28, 2025, TKO OpCo and TKO Group Holdings, Inc. ... completed the acquisition ..."
  - Note 1 also states: "On February 28, 2025, prior to the close of the Endeavor Asset Acquisition, Endeavor through its subsidiaries, had controlled approximately 54% of the voting interests in TKO ... Upon the consummation of the close of the Endeavor Asset Acquisition, Endeavor through its subsidiaries, controlled approximately 61% of the voting interest in TKO."
  - Auditor's report: the Businesses were acquired "in a common control acquisition on February 28, 2025."
  - Note 19: the three-segment structure was identified "effective February 28, 20
  …[truncated 1,370 chars]

### Turn 7  (stop_reason=tool_use)
- submit_final_result({"final_result": "Short answer: TKO's filings give a total consideration of about $3.30 billion for the Endeavor assets (approximately $3.25 billion plus a $50 million purchase price adjustment). None of the filings I opened states a closing-date fair value for that consideration, so $3.30 billion is the contractual figure measured against the October 2024 price, not a figure measured at close.\n\nBridge and reasoning:\n1. Headline price at signing: The agreement was signed October 23, 2024. TKO stated that <cite index=\"6-5\">TKO will acquire the Endeavor assets for total consideration of $ 3.25 billion, based on the volume-weighted average sales price of TKO's Class A common stock for the 
…[truncated 3,618 chars])

### Final answer
Short answer: TKO's filings give a total consideration of about $3.30 billion for the Endeavor assets (approximately $3.25 billion plus a $50 million purchase price adjustment). None of the filings I opened states a closing-date fair value for that consideration, so $3.30 billion is the contractual figure measured against the October 2024 price, not a figure measured at close.

Bridge and reasoning:
1. Headline price at signing: The agreement was signed October 23, 2024. TKO stated that <cite index="6-5">TKO will acquire the Endeavor assets for total consideration of $ 3.25 billion, based on the volume-weighted average sales price of TKO's Class A common stock for the twenty five trading days ending on October 23, 2024.</cite>
2. Adjustment: The Q1 2025 10-Q states the businesses were acquired <cite index="10-1">for a total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment</cite>. The adjustment was described in the 10-K as <cite index="6-6">subject to certain customary purchase price adjustments to be settled at the closing in equity and cash</cite>, but the filings do not split the $50 million between cash and equity.
3. Closing date: The 10-Q states the acquisition <cite index="2-4">was accounted for as a common control acquisition and was consummated on February 28, 2025.</cite>
4. Equity issued at close: <cite index="10-2">Endeavor received approximately 26.54 million common units of TKO and subscribed for an equal number of shares of TKO Class B common stock.</cite> The filings give no closing-date share price or per-unit value for these units. The 10-Q's Note 10 says the units were issued <cite index="2-6">as consideration paid in connection with the Endeavor Asset Acquisition</cite>, again without a dollar value at close.
5. Other closing-date items: The 10-Q gives a $23.5 million aggregate value for 160,455 Class A shares issued to NFL Properties LLC <cite index="2-7">as set forth in the Endeavor Asset Acquisition Agreement</cite>. This is a separate item, and I have not added it to the total because the filings do not say it is part of the consideration.

Calculation: $3.25 billion + $50 million = $3.30 billion (contractual total, before any closing-date revaluation of the equity). Implied price per unit on the $3.25 billion base: $3,250 million ÷ 26.54 million units ≈ $122.46 (my derived figure, not a disclosed price).

Accounting caveat: Because this was a transaction between entities under common control, the assets were recorded at historical carrying amounts rather than fair value, so no purchase price allocation at fair value exists. The 10-Q says the equity consideration <cite index="2-6">increased the nonredeemable non-controlling interest in TKO OpCo, with a corresponding increase to additional paid-in capital.</cite>

Conclusion: The best-supported answer is about $3.30 billion ($3.25 billion plus a $50 million adjustment), with the caveat that the filings do not disclose a closing-date measurement of the equity consideration. I could not locate the separate closing 8-K (accession 0001193125-25-040879) in the search index, so a closing-date value could exist there.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025067220/tko-20250331.htm",
            "name": "TKO Group Holdings Form 10-Q for quarter ended March 31, 2025"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000095017025027778/tko-20241231.htm",
            "name": "TKO Group Holdings Form 10-K for FY2024"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312525057890/d803159dex991.htm",
            "name": "TKO Group Holdings 8-K Exhibit 99.1 (filed 2025-03-19)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312525057890/R8.htm",
            "name": "TKO Group Holdings description of business (SEC R8 page)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1973266/000119312525097003/d909805dars.pdf",
            "name": "TKO Group Holdings Form ARS FY2024"
        }
    ]
}