## Rollout `ctl2`
- outcome: submitted
- turns: 4; cost: $0.118; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="KKR Series D mandatory convertible preferred stock offering March 2025") → 0 results: 
- edgar_search({"search_query": "KKR Series D mandatory convertible preferred stock", "start_date": "2025-03-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 232, "page": 1, "results": [{"form": "424B5", "file_date": "2025-03-06", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007426", "document": "ny20042797x2_424b5.htm", "description": "424B5", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm"}, {"form": "8-K", "file_date": "2025-03-07", "period_ending": "2025-03-04", "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007608", "document": "ny20042797x5_8k.htm", "description": "8-K", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_8k.htm"}, {"form": "424B5", "file_date": "2025-03-04", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-006869", "document": "ny20042797x1_424b5.htm", "description": "424B5", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125006869/ny20042797x1_424b5.htm"}, {"form": "8-K", "file_date": "2025-03-07", "period_ending": "2025-03-04", "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007608", "document": "ny20042797x5_ex3-1.htm", "description": "EXHIBIT 3.1", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_ex3-1.htm"}, {"form": "FWP", "file_date": "2025-03-05", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007061", "document": "ny20042797x3_fwp.htm", "description": "FWP", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007061/ny200
  …[truncated 5,265 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 9 results: KKR & Co. Inc. - Form 10-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000140491226000007/kkr-20251231.htm>; KKR & Co. Inc. - Form 424B5 - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm>; KKR & Co. Inc. - Form 10-Q - FY2025 (Quarterly Earnings Tables - quarter ended Mar 2025) <https://www.sec.gov/Archives/edgar/data/1404912/000140491225000022/Financial_Report.xlsx>; KKR & Co. Inc. - Form 10-Q - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000140491225000042/kkr-20250930.htm>; KKR & Co. Inc. - Form 10-Q - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000140491225000032/kkr-20250630.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm", "key": "kkr_424b5"})
  result: SUCCESS: The result has been saved to the data storage under the key: kkr_424b5. (500,749 characters)
  The data_storage currently contains the following keys:
  kkr_424b5
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this prospectus supplement, extract: the final offering size (number of shares and dollar amount), closing/settlement date, public offering price, liquidation preference, dividend rate and payment terms, conversion rates (minimum and maximum), initial price / threshold appreciation price, voting rights of the Series D mandatory convertible preferred stock, and the stated use of proceeds. Quote the relevant sentences briefly. {{kkr_424b5}}"})
  result: **Offering size:** 45,000,000 shares of 6.25% Series D Mandatory Convertible Preferred Stock, or $2,250,000,000 at the public offering price. The underwriters have a 30-day option for 6,750,000 more shares, which would bring the total to $2,587,500,000. The option is not reflected in the base figures.
  - "We are offering 45,000,000 shares of our 6.25% Series D Mandatory Convertible Preferred Stock"
  
  **Settlement date:** March 7, 2025 (T+2)
  - "The underwriters expect to deliver the Mandatory Convertible Preferred Stock to purchasers on or about March 7, 2025"
  
  **Public offering price:** $50.00 per share
  - "Public Offering Price: $50.00 per share of the Mandatory Convertible Preferred Stock."
  
  **Liquidation preference:** $50.00 per share, plus accumulated and unpaid dividends
  - "each holder of the Mandatory Convertible Preferred Stock will be entitled to receive a Liquidation Preference in the amount of $50.00 per share"
  
  **Dividend rate and payment terms:**
  - Rate: 6.25% per year on the $50.00 liquidation preference, or $3.125 per share annually.
  - Cumulative, when, as and if declared by the Board.
  - Payment dates: March 1, June 1, September 1 and December 1, from June 1, 2025 through March 1, 2028.
  - Form: "payable in cash, by delivery of shares of our common stock or through any combination of cash and shares of our common stock, as determined by us in our sole discretion"
  - Expected amounts: about $0.7292 for the first dividend, then $0.78125 per quarter.
  - Common stock used for dividends is valued at 97% of the Average VWAP over five trading days.
  - Share delivery for dividends is capped at the declared dividend divided by a Floor Price of $42.2705.
  
  **Conversion rates:**
  - Minimum Conversion Rate: 0.3312 common shares per preferred share.
  - Maximum Conversion Rate: 0
  …[truncated 2,088 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "\n**KKR & Co. Inc. (NYSE: KKR) Series D Mandatory Convertible Preferred Stock, March 2025**\n\n**Offering size:** The offering was launched at $1.5 billion (30,000,000 shares) on March 4, 2025, <cite index=\"9-1\">and was then priced as a $2.25 billion offering (45,000,000 shares) of 6.25% Series D Mandatory Convertible Preferred Stock</cite>. The underwriters' 30-day option covered up to 6,750,000 more shares. The 10-K reports that <cite index=\"1-5\">on March 7, 2025, KKR & Co. Inc. issued 51,750,000 shares, or $2.59 billion aggregate liquidation preference</cite>, which indicates the option was exercised in full (45,000,000 + 6,750,000 = 51,750,000 shares; 51,750,000 × $
…[truncated 5,360 chars])

### Final answer

**KKR & Co. Inc. (NYSE: KKR) Series D Mandatory Convertible Preferred Stock, March 2025**

**Offering size:** The offering was launched at $1.5 billion (30,000,000 shares) on March 4, 2025, <cite index="9-1">and was then priced as a $2.25 billion offering (45,000,000 shares) of 6.25% Series D Mandatory Convertible Preferred Stock</cite>. The underwriters' 30-day option covered up to 6,750,000 more shares. The 10-K reports that <cite index="1-5">on March 7, 2025, KKR & Co. Inc. issued 51,750,000 shares, or $2.59 billion aggregate liquidation preference</cite>, which indicates the option was exercised in full (45,000,000 + 6,750,000 = 51,750,000 shares; 51,750,000 × $50.00 = $2.5875 billion).

**Closing/settlement date:** <cite index="2-4">The underwriters expected to deliver the Mandatory Convertible Preferred Stock to purchasers on or about March 7, 2025</cite>, on a T+2 cycle. Pricing occurred on March 4, 2025.

**Price:** The public offering price was $50.00 per share, <cite index="9-1">at a price to the public and liquidation preference of $50.00 per share</cite>.

**Liquidation preference:** $50.00 per share. Holders are entitled to that amount plus accumulated and unpaid dividends (per the prospectus supplement). The 10-K describes the aggregate liquidation preference as $2.59 billion for the 51,750,000 shares.

**Dividend rights:** Dividends are <cite index="3-3">payable on a cumulative basis when, as and if declared by KKR & Co. Inc.'s board of directors, or an authorized committee thereof, at an annual rate of 6.25% on the liquidation preference of $50.00 per share</cite>. That equals $3.125 per share per year. Payments are made quarterly on March 1, June 1, September 1 and December 1, starting June 1, 2025 through March 1, 2028. Dividends may be paid in cash, in common stock, or in a combination, at KKR's election and subject to limitations. The prospectus supplement puts the first dividend at about $0.7292 per share and each full quarterly dividend at $0.78125. Shares delivered for dividends are valued at 97% of the average VWAP over five trading days, and the share count is capped using a $42.2705 floor price. Under the 10-K's description, dividends on KKR's common stock are restricted while any Series D shares remain outstanding (subject to exceptions).

**Conversion terms:** Unless converted earlier, each share <cite index="1-6">will automatically convert on the mandatory conversion date, which is expected to be March 1, 2028, into between 0.3312 shares and 0.4140 shares of common stock</cite>. The number of common shares is set by the average VWAP over the 20 trading days beginning with the 21st scheduled trading day before March 1, 2028. Holders may convert early at any time before March 1, 2028 at the minimum rate of 0.3312 shares per preferred share. Key reference prices (my calculation from the stated rates): the initial price is $50.00 ÷ 0.4140 ≈ $120.7729 (equal to the March 4, 2025 closing price), and the threshold appreciation price is $50.00 ÷ 0.3312 ≈ $150.9662, about 25% above the initial price.

**Voting rights:** Generally none. The prospectus supplement states that, <cite index="2-2">except as specifically required by Delaware law or our certificate of incorporation</cite>, holders have no voting rights. The exceptions are: if dividends are unpaid for six or more dividend periods, holders may elect two additional directors; and a two-thirds vote of the Series D holders is required for certain actions, such as creating senior stock, adversely amending the preferred's terms, or certain mergers or share exchanges.

**Purpose / use of proceeds:** Per the prospectus supplement, KKR intends to use the net proceeds (about $2.20 billion, or about $2.53 billion if the option is exercised in full) <cite index="6-4">mainly for the acquisition of additional equity interests in core private equity portfolio companies reported in its Strategic Holdings segment</cite>, along with other general corporate purposes.

**Sources noted:** The prospectus supplement and 10-K/10-Q disclosures are the primary sources. The underwriting figures ($2.25 billion base, 45,000,000 shares) come from the pricing press release. Press reports (RTTNews) give the same use of proceeds. Note: the base offering figure in the prospectus supplement is $2.25 billion (45,000,000 shares), but the final issued amount including the option was 51,750,000 shares.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm",
            "name": "KKR & Co. Inc. Form 424B5 Prospectus Supplement (March 2025)"
        },
        {
            "url": "https://www.nasdaq.com/press-release/kkr-upsizes-and-prices-offering-mandatory-convertible-preferred-stock-2025-03-04",
            "name": "KKR Upsizes and Prices Offering of Mandatory Convertible Preferred Stock (Business Wire via Nasdaq, March 4, 2025)"
        },
        {
            "url": "https://www.businesswire.com/news/home/20250304232380/en/KKR-Announces-Offering-of-Mandatory-Convertible-Preferred-Stock",
            "name": "KKR Announces Offering of Mandatory Convertible Preferred Stock (Business Wire, March 4, 2025)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000140491226000007/kkr-20251231.htm",
            "name": "KKR & Co. Inc. Form 10-K (FY2025)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000140491225000042/kkr-20250930.htm",
            "name": "KKR & Co. Inc. Form 10-Q (quarter ended September 30, 2025)"
        },
        {
            "url": "https://www.nasdaq.com/articles/kkr-co-commences-15-bln-offering-series-d-mandatory-convertible-preferred-stock",
            "name": "KKR & Co. Commences $1.5 Bln Offering Of Series D Mandatory Convertible Preferred Stock (RTTNews via Nasdaq)"
        }
    ]
}
