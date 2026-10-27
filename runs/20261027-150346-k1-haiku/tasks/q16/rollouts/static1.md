## Rollout `static1`
- outcome: submitted
- turns: 4; cost: $0.120; submitted: True

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
- retrieve_information({"prompt": "From this KKR 424B5 prospectus supplement, extract: total offering size (shares and dollars, including over-allotment), initial trade/closing/settlement date, public offering price and liquidation preference per share, dividend rate and payment terms, conversion rate range (minimum and maximum), initial price, mandatory conversion date, voting rights of the Series D mandatory convertible preferred stock, and the stated use of proceeds/purpose of the offering. Quote the relevant text briefly. {{kkr_424b5}}"})
  result: # KKR 6.25% Series D Mandatory Convertible Preferred Stock: Key Terms (424B5, March 4, 2025)
  
  **Total offering size**
  - **Base:** 45,000,000 shares, for a public offering price of $2,250,000,000 (cover page: "Public offering price $50.000 $2,250,000,000").
  - **Over-allotment:** "up to an additional 6,750,000 shares." With full exercise, the total would be 51,750,000 shares and $2,587,500,000 in gross proceeds (Underwriting table: "With Option $2,587,500,000").
  
  **Initial trade, closing, and settlement dates**
  - **Initial trade date:** Not stated explicitly. The prospectus says the settlement date is "the second business day after the initial trade date," which implies a trade date of about March 5, 2025.
  - **Settlement/closing:** "March 7, 2025, which is the second business day after the initial trade date" (T+2).
  
  **Public offering price and liquidation preference**
  - **Public offering price:** "$50.00 per share of the Mandatory Convertible Preferred Stock."
  - **Liquidation preference:** "$50.00 per share," plus accumulated and unpaid dividends.
  
  **Dividend rate and payment terms**
  - **Rate:** "6.25% of the liquidation preference of $50.00 per share" ($3.125 per year).
  - **Cumulative:** "payable on a cumulative basis when, as and if declared by our Board of Directors."
  - **Payment dates:** "March 1, June 1, September 1 and December 1 of each year, commencing on June 1, 2025, and ending on, and including, March 1, 2028."
  - **Form of payment:** "We may pay declared dividends in cash or, subject to certain limitations, in shares of our common stock or in any combination," at the company's sole discretion.
  - **Expected amounts:** about $0.7292 for the first dividend and $0.78125 for each subsequent full period.
  - **Common stock dividend valuation:** shares are valued at "9
  …[truncated 2,623 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**KKR & Co. Inc. 6.25% Series D Mandatory Convertible Preferred Stock (March 2025): key terms**\n\n**1. Offering size**\n- The offering was launched at <cite index=\"8-1\">$1.5 billion (30,000,000 shares) of its Series D Mandatory Convertible Preferred Stock, par value $0.01 per share</cite>.\n- It was then upsized. KKR <cite index=\"9-1\">priced its previously announced offering of $2.25 billion of its 6.25% Series D Mandatory Convertible Preferred Stock at a price to the public and liquidation preference of $50.00 per share.</cite> That is 45,000,000 shares.\n- The underwriters had a 30-day option for <cite index=\"2-3\">up to an additional 6,750,000 shares</cite>. KKR's 
…[truncated 5,489 chars])

### Final answer
**KKR & Co. Inc. 6.25% Series D Mandatory Convertible Preferred Stock (March 2025): key terms**

**1. Offering size**
- The offering was launched at <cite index="8-1">$1.5 billion (30,000,000 shares) of its Series D Mandatory Convertible Preferred Stock, par value $0.01 per share</cite>.
- It was then upsized. KKR <cite index="9-1">priced its previously announced offering of $2.25 billion of its 6.25% Series D Mandatory Convertible Preferred Stock at a price to the public and liquidation preference of $50.00 per share.</cite> That is 45,000,000 shares.
- The underwriters had a 30-day option for <cite index="2-3">up to an additional 6,750,000 shares</cite>. KKR's FY2025 10-K states that on March 7, 2025 it <cite index="1-5">issued 51,750,000 shares, or $2.59 billion aggregate liquidation preference</cite>. The 51,750,000 total equals 45,000,000 + 6,750,000, so the option was exercised in full. Gross proceeds are $2,587,500,000 (51,750,000 × $50.00).
- Estimated net proceeds were <cite index="2-3">$2,199,375,000</cite> before the over-allotment option. The prospectus estimates about $2.20 billion, or about $2.53 billion with the option exercised in full.

**2. Pricing and closing date**
- Price to the public and liquidation preference: $50.00 per share.
- Settlement/closing: <cite index="2-4">on or about March 7, 2025, which will be the second business day after the initial trade date</cite>. The 10-K confirms the issuance date as March 7, 2025.

**3. Liquidation preference**
- Each share has <cite index="8-3">a liquidation preference of $50.00 per share</cite>, plus accumulated and unpaid dividends per the prospectus.

**4. Dividend rights**
- Dividends accrue at <cite index="3-3">an annual rate of 6.25% on the liquidation preference of $50.00 per share</cite>, which is $3.125 per share per year, or $0.78125 per quarter.
- They are cumulative and <cite index="3-3">payable on a cumulative basis when, as and if declared by KKR & Co. Inc.'s board of directors</cite>. The prospectus states that declared dividends may be paid in cash, in common stock, or in a combination, subject to certain limitations.
- Payment dates: <cite index="3-4">quarterly on March 1, June 1, September 1 and December 1 of each year to, and including, March 1, 2028, commencing on June 1, 2025.</cite>
- Dividends are influenced by distributions KKR receives from KKR Group Partnership on its mirrored preferred units.

**5. Conversion terms**
- Mandatory conversion date: <cite index="1-6">expected to be March 1, 2028</cite>, when each share converts into <cite index="1-6">between 0.3312 shares and 0.4140 shares of common stock</cite>, subject to anti-dilution adjustments.
- Conversion is based on <cite index="1-7">the average volume weighted average price per share of common stock over the 20 consecutive trading day period beginning on, and including, the 21st scheduled trading day immediately prior to March 1, 2028.</cite>
- Per the prospectus, the Initial Price is about $120.77 (= $50.00 / 0.4140), the March 4, 2025 closing price. The Threshold Appreciation Price is about $150.97 (= $50.00 / 0.3312). Holders may also convert early at the minimum rate of 0.3312 shares per preferred share.
- Share count at the mandatory conversion (51,750,000 preferred shares): minimum 17,139,600 common shares (51,750,000 × 0.3312) and maximum 21,424,500 (51,750,000 × 0.4140).

**6. Voting rights**
- Holders generally have no voting rights, except as described below or as required by Delaware law or the certificate of incorporation.
- If dividends are unpaid for six or more dividend periods, the board is increased by two and the holders may elect two additional directors.
- Certain actions, such as creating senior stock, adversely amending the preferred's rights, or certain mergers, require at least two-thirds of the preferred's voting power.

**7. Purpose of the offering**
- <cite index="6-4">The company intends to use the proceeds mainly for the acquisition of additional equity interests in core private equity portfolio companies reported in its Strategic Holdings segment.</cite>
- The prospectus says the proceeds are also for general corporate purposes. It links this to KKR's February 4, 2025 plan to increase its ownership in certain core private equity businesses by about $1.1 billion.

**Note on sources:** The March 4 launch release referenced a $1.5 billion deal, but the final pricing was upsized to $2.25 billion base, with the option exercised in full, for $2.5875 billion total.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm",
            "name": "KKR & Co. Inc. Form 424B5 prospectus supplement (March 6, 2025)"
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
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000140491225000042/kkr-20250930.htm",
            "name": "KKR & Co. Inc. Form 10-Q for quarter ended September 30, 2025"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000140491226000007/kkr-20251231.htm",
            "name": "KKR & Co. Inc. Form 10-K FY2025"
        },
        {
            "url": "https://www.nasdaq.com/articles/kkr-co-commences-15-bln-offering-series-d-mandatory-convertible-preferred-stock",
            "name": "RTTNews: KKR & Co. Commences $1.5 Bln Offering of Series D Mandatory Convertible Preferred Stock (March 4, 2025)"
        }
    ]
}
