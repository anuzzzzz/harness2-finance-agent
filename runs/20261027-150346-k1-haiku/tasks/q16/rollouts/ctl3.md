## Rollout `ctl3`
- outcome: submitted
- turns: 6; cost: $0.247; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="KKR Series D mandatory convertible preferred stock offering March 2025") → 0 results: 
- edgar_search({"search_query": "KKR Series D Mandatory Convertible Preferred Stock", "start_date": "2025-03-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 232, "page": 1, "results": [{"form": "424B5", "file_date": "2025-03-06", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007426", "document": "ny20042797x2_424b5.htm", "description": "424B5", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm"}, {"form": "8-K", "file_date": "2025-03-07", "period_ending": "2025-03-04", "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007608", "document": "ny20042797x5_8k.htm", "description": "8-K", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_8k.htm"}, {"form": "424B5", "file_date": "2025-03-04", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-006869", "document": "ny20042797x1_424b5.htm", "description": "424B5", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125006869/ny20042797x1_424b5.htm"}, {"form": "8-K", "file_date": "2025-03-07", "period_ending": "2025-03-04", "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007608", "document": "ny20042797x5_ex3-1.htm", "description": "EXHIBIT 3.1", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_ex3-1.htm"}, {"form": "FWP", "file_date": "2025-03-05", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007061", "document": "ny20042797x3_fwp.htm", "description": "FWP", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007061/ny200
  …[truncated 5,265 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 9 results: KKR & Co. Inc. - Form 10-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000140491226000007/kkr-20251231.htm>; KKR & Co. Inc. - Form 424B5 - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm>; KKR & Co. Inc. - Form 10-Q - FY2025 (Quarterly Earnings Tables - quarter ended Mar 2025) <https://www.sec.gov/Archives/edgar/data/1404912/000140491225000022/Financial_Report.xlsx>; KKR & Co. Inc. - Form 10-Q - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000140491225000042/kkr-20250930.htm>; KKR & Co. Inc. - Form 10-Q - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000140491225000032/kkr-20250630.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm", "key": "kkr_424b5"})
  result: SUCCESS: The result has been saved to the data storage under the key: kkr_424b5. (500,749 characters)
  The data_storage currently contains the following keys:
  kkr_424b5
  
- parse_html_page({"url": "https://www.nasdaq.com/press-release/kkr-upsizes-and-prices-offering-mandatory-convertible-preferred-stock-2025-03-04", "key": "kkr_pricing"})
  ERROR: ReadTimeout: HTTPSConnectionPool(host='www.nasdaq.com', port=443): Read timed out. (read timeout=60)

### Turn 3  (stop_reason=tool_use)
- web_search(query="KKR prices 6.25% Series D Mandatory Convertible Preferred Stock $2.25 billion") → 0 results: 
- retrieve_information({"prompt": "From this KKR 424B5 prospectus supplement for its 6.25% Series D Mandatory Convertible Preferred Stock, extract the following with exact figures: (1) total offering size in shares and dollars, including underwriter option; (2) closing/delivery date; (3) public offering price per share and liquidation preference; (4) dividend rate, payment dates, and whether payable in cash or common stock; (5) mandatory conversion date, minimum and maximum conversion rates, settlement period, and early conversion rights/ fundamental change terms; (6) voting rights of holders; (7) stated use of proceeds. Include section names where possible. Document: {{kkr_424b5}}"})
  result: # KKR 6.25% Series D Mandatory Convertible Preferred Stock: Key Terms (424B5, March 4, 2025)
  
  ## 1. Offering Size
  
  **Base offering (Cover Page; Summary, "Securities Offered"; Underwriting):**
  - **45,000,000 shares** of 6.25% Series D Mandatory Convertible Preferred Stock, par value $0.01
  - **$2,250,000,000** total public offering price
  
  **Underwriters' option (Cover Page; Underwriting):**
  - Up to **6,750,000 additional shares**, exercisable within 30 days of the prospectus supplement date, solely to cover over-allotments
  - If exercised in full: total public offering price of **$2,587,500,000**
  
  | | Without Option | With Full Option |
  |---|---|---|
  | Public offering price | $2,250,000,000 | $2,587,500,000 |
  | Underwriting discount ($1.125/sh) | $50,625,000 | $58,218,750 |
  | Proceeds before expenses | $2,199,375,000 | $2,529,281,250 |
  
  ## 2. Closing / Delivery (Settlement) Date
  
  - **March 7, 2025**, which is the second business day after the initial trade date (T+2) (Cover Page; Summary, "Settlement Date"; Summary, "Payment and Settlement")
  - The prospectus is dated **March 4, 2025** (Cover Page)
  
  ## 3. Public Offering Price and Liquidation Preference
  
  - **Public offering price:** $50.00 per share (Cover Page; Summary, "Public Offering Price")
  - **Liquidation preference:** $50.00 per share (Summary, "Liquidation Preference"; Description of Mandatory Convertible Preferred Stock, "Liquidation Preference")
  - Upon liquidation, holders also receive a **Liquidation Dividend Amount**, equal to accumulated and unpaid dividends, whether or not declared
  - Underwriting discount: $1.125 per share; proceeds before expenses: $48.875 per share
  
  ## 4. Dividends
  
  **Rate and form (Summary, "Dividends"; Description, "Dividends"):**
  - **6.25% per annum** on the $50.00 liquidation preference,
  …[truncated 2,882 chars]

### Turn 4  (stop_reason=tool_use)
- web_search(query=null) → 10 results: KKR Upsizes and Prices Offering of Mandatory Convertible Preferred Stock <https://www.nasdaq.com/press-release/kkr-upsizes-and-prices-offering-mandatory-convertible-preferred-stock-2025-03-04>; KKR & Co. Inc. - Form 424B5 - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm>; KKR Upsizes and Prices Offering of Mandatory Convertible Preferred Stock <https://www.marketscreener.com/quote/stock/KKR-CO-INC-44486777/news/KKR-Upsizes-and-Prices-Offering-of-Mandatory-Convertible-Preferred-Stock-49238638/>; KKR Upsizes and Prices Offering of Mandatory Convertible Preferred Stock <https://www.businesswire.com/news/home/20250304161115/en/KKR-Upsizes-and-Prices-Offering-of-Mandatory-Convertible-Preferred-Stock>; KKR-D Search Results - QuantumOnline.com <https://www.quantumonline.com/search.cfm?tickersymbol=KKR-D&sopt=symbol>
- retrieve_information({"prompt": "From this KKR 424B5 prospectus supplement, extract verbatim-free, concise summaries of: (a) the additional conversion amount if accumulated dividends are not declared; (b) the early conversion rate at the holder's option before March 1, 2028 (Minimum Conversion Rate application, Early Conversion Rate and any make-whole/fundamental change terms); (c) voting rights of holders of the Mandatory Convertible Preferred Stock (including any class voting rights upon dividend nonpayment, and what matters require 66 2/3% approval); (d) the use of proceeds and purpose. Include section names. Document: {{kkr_424b5}}"})
  result: ## (a) Additional Conversion Amount (undeclared dividends at mandatory conversion)
  
  **Sections:** Summary, "Mandatory Conversion"; "Description of Mandatory Convertible Preferred Stock," "Mandatory Conversion"
  
  - If, by March 1, 2028, KKR has not declared all accumulated and unpaid dividends, the conversion rate increases so holders receive extra common shares.
  - The extra shares equal the undeclared amount per preferred share, divided by the greater of (x) the Floor Price (initially $42.2705, subject to adjustment) and (y) 97% of the Average Price, calculated using March 1, 2028 as the dividend payment date.
  - If the value of those extra shares falls short of the Additional Conversion Amount, KKR will pay the excess in cash if legally permitted and allowed under its debt agreements. If it cannot, it has no obligation to pay or deliver shares for the shortfall, and that amount is not treated as cumulative dividends.
  
  ## (b) Early Conversion and Fundamental Change Terms
  
  **Sections:** Summary, "Early Conversion at the Option of the Holder" and "Conversion at the Option of the Holder upon Fundamental Change; Fundamental Change Dividend Make-Whole Amount"; "Description of Mandatory Convertible Preferred Stock," "Early Conversion at the Option of the Holder" and the Fundamental Change subsections
  
  **Early conversion (before March 1, 2028, excluding the Fundamental Change Conversion Period):**
  - Holders may convert all or part of their shares (in whole-share increments) at the **Minimum Conversion Rate of 0.3312 common shares per preferred share**, subject to anti-dilution adjustments.
  - If full-period accumulated dividends have not been declared as of the early conversion date, holders receive extra shares equal to the undeclared amount divided by the greater of the Floor P
  …[truncated 3,992 chars]

### Turn 5  (stop_reason=end_turn)
**KKR & Co. Inc. 6.25% Series D Mandatory Convertible Preferred Stock (March 2025): key terms**

The offering was launched on March 4, 2025, upsized during the offering, and priced the same day. Everything below reflects information available as of April 7, 2025.

- **Offering size:** KKR first announced 
an offering of $1.5 billion (30,000,000 shares)
. It then priced 
$2.25 billion (45,000,000 shares)
 of the 6.25% Series D preferred. The underwriters also had a 30-day option for 
up to an additional 6,750,000 shares
, which is about $337.5 million at $50.00 per share. If fully exercised, the total public offering price would be $2,587,500,000.
- **Closing date:** 
The underwriters expected to deliver the shares to purchasers on or about March 7, 2025
, on a T+2 settlement cycle.
- **Price and liquidation preference:** The public offering price and liquidation preference are both $50.00 per share. The underwriting discount was $1.125 per share, so proceeds before expenses were $48.875 per share, or 
$2,199,375,000
 in total. Net proceeds were 
about $2.20 billion, after deducting underwriting discounts and estimated offering expenses.
 Upon liquidation, holders also receive any accumulated and unpaid dividends, whether or not declared.
- **Dividend rights:** Dividends are 
cumulative, payable when, as and if declared by the board, at an annual rate of 6.25% on the $50.00 liquidation preference
. That equals $3.125 per share per year, or $0.78125 per quarter. Payment dates a
…[truncated 3,441 chars]

### Turn 6  (stop_reason=tool_use)
- submit_final_result({"final_result": "**KKR & Co. Inc. 6.25% Series D Mandatory Convertible Preferred Stock (March 2025): key terms**\n\nThis summary reflects information available as of April 7, 2025. It corrects my earlier draft, which had a mis-cited voting-rights sentence (it pointed to Series I preferred stock text) and several passages that stayed too close to their sources. I also removed a note that referred to a later-dated filing.\n\n- **Offering size:** KKR first launched the deal as <cite index=\"8-1\">an offering of $1.5 billion (30,000,000 shares)</cite> and then priced it at <cite index=\"9-1\">$2.25 billion (45,000,000 shares)</cite>. The underwriters received a 30-day option covering <cite inde
…[truncated 4,371 chars])

### Final answer
**KKR & Co. Inc. 6.25% Series D Mandatory Convertible Preferred Stock (March 2025): key terms**

This summary reflects information available as of April 7, 2025. It corrects my earlier draft, which had a mis-cited voting-rights sentence (it pointed to Series I preferred stock text) and several passages that stayed too close to their sources. I also removed a note that referred to a later-dated filing.

- **Offering size:** KKR first launched the deal as <cite index="8-1">an offering of $1.5 billion (30,000,000 shares)</cite> and then priced it at <cite index="9-1">$2.25 billion (45,000,000 shares)</cite>. The underwriters received a 30-day option covering <cite index="2-3">up to an additional 6,750,000 shares</cite>, which equals about $337.5 million at $50.00 per share. Full exercise would bring the total public offering price to $2,587,500,000 (my calculation: 51,750,000 shares × $50.00).

- **Closing date:** Delivery to buyers was set for <cite index="2-2">on or about March 7, 2025</cite>, which was the second business day after the trade date.

- **Price and liquidation preference:** The public offering price and the liquidation preference were both set at $50.00 per share. The underwriting discount was $1.125 per share, which leaves $48.875 per share in proceeds before expenses, or <cite index="2-3">$2,199,375,000</cite> in total for the base deal. Net proceeds were <cite index="15-6">about $2.20 billion, after deducting underwriting discounts and estimated offering expenses.</cite> On liquidation, holders also receive accumulated unpaid dividends, whether or not declared.

- **Dividend rights:** Dividends are cumulative and become payable only when the board declares them. The rate is 6.25% a year on the $50.00 preference, which is $3.125 per share annually (my calculation), or $0.78125 per quarter. Payment dates fall on March 1, June 1, September 1 and December 1, starting June 1, 2025 and running through March 1, 2028. KKR may pay in cash, in common stock, or in a combination. Stock payments are subject to a floor price of $42.2705 per share, and accumulated dividends do not bear interest.

- **Conversion terms:** Unless holders convert earlier, each share converts automatically on or around March 1, 2028 into a variable number of common shares. The conversion ratio ranges from a minimum of 0.3312 to a maximum of 0.4140 shares. The ratio depends on the average VWAP of KKR common stock over 20 trading days beginning on the 21st scheduled trading day before March 1, 2028. Holders may also convert early at the minimum ratio. The reference (initial) price is about $120.77, based on the March 4, 2025 closing price. The maximum ratio applies when the average price is at or below that level, and the minimum ratio applies once the average price exceeds about $150.97 (roughly 25% above the initial price). In between, the ratio equals $50.00 divided by the average price (my reading of the prospectus formula). A fundamental change, such as a merger or change of control, triggers a separate conversion table and a dividend make-whole payment.

- **Voting rights:** Holders generally have no voting rights except as required by Delaware law or KKR's charter. If dividends go unpaid for six or more dividend periods, holders can elect two additional directors. Actions such as authorizing senior stock or materially and adversely amending the charter require approval from at least two-thirds of the preferred voting power. These points come from my review of the 424B5 prospectus supplement, which I did not link to a specific search excerpt.

- **Purpose:** <cite index="15-7">KKR planned to use the net proceeds for the acquisition of additional equity interests in core private equity portfolio companies reported in its Strategic Holdings segment and for other general corporate purposes.</cite>

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm",
            "name": "KKR & Co. Inc. Form 424B5 prospectus supplement (March 2025)"
        },
        {
            "url": "https://www.businesswire.com/news/home/20250304232380/en/KKR-Announces-Offering-of-Mandatory-Convertible-Preferred-Stock",
            "name": "KKR Announces Offering of Mandatory Convertible Preferred Stock (Business Wire, March 4, 2025)"
        },
        {
            "url": "https://www.businesswire.com/news/home/20250304161115/en/KKR-Upsizes-and-Prices-Offering-of-Mandatory-Convertible-Preferred-Stock",
            "name": "KKR Upsizes and Prices Offering of Mandatory Convertible Preferred Stock (Business Wire, March 4, 2025)"
        },
        {
            "url": "https://www.rttnews.com/3518674/kkr-prices-2-25-bln-offering-of-6-25-series-d-mandatory-convertible-preferred-stock-at-50-00-shr.aspx",
            "name": "RTTNews: KKR Prices $2.25 Bln Offering of 6.25% Series D Mandatory Convertible Preferred Stock"
        }
    ]
}