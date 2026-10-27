## Rollout `base1`
- outcome: submitted
- turns: 5; cost: $0.230; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="KKR Series D mandatory convertible preferred stock offering March 2025") → 0 results: 
- edgar_search({"search_query": "KKR Series D Mandatory Convertible Preferred Stock", "start_date": "2025-03-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 232, "page": 1, "results": [{"form": "424B5", "file_date": "2025-03-06", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007426", "document": "ny20042797x2_424b5.htm", "description": "424B5", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm"}, {"form": "8-K", "file_date": "2025-03-07", "period_ending": "2025-03-04", "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007608", "document": "ny20042797x5_8k.htm", "description": "8-K", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_8k.htm"}, {"form": "424B5", "file_date": "2025-03-04", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-006869", "document": "ny20042797x1_424b5.htm", "description": "424B5", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125006869/ny20042797x1_424b5.htm"}, {"form": "8-K", "file_date": "2025-03-07", "period_ending": "2025-03-04", "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007608", "document": "ny20042797x5_ex3-1.htm", "description": "EXHIBIT 3.1", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_ex3-1.htm"}, {"form": "FWP", "file_date": "2025-03-05", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007061", "document": "ny20042797x3_fwp.htm", "description": "FWP", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007061/ny200
  …[truncated 5,265 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: KKR & Co. Inc. - Form 10-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000140491226000007/kkr-20251231.htm>; KKR & Co. Inc. - Form 424B5 - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm>; KKR & Co. Inc. - Form 10-Q - FY2025 (Quarterly Earnings Tables - quarter ended Mar 2025) <https://www.sec.gov/Archives/edgar/data/1404912/000140491225000022/Financial_Report.xlsx>; KKR & Co. Inc. - Form 10-Q - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000140491225000042/kkr-20250930.htm>; KKR & Co. Inc. - Form 10-Q - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000140491225000032/kkr-20250630.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm", "key": "kkr_424b5"})
  result: SUCCESS: The result has been saved to the data storage under the key: kkr_424b5. (500,749 characters)
  The data_storage currently contains the following keys:
  kkr_424b5
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this KKR 424B5 prospectus supplement for the 6.25% Series D Mandatory Convertible Preferred Stock, extract the following with exact figures and short quotes where possible: (1) number of shares and gross/net proceeds, underwriting discount, public offering price; (2) closing/settlement date; (3) liquidation preference and rights on liquidation; (4) dividend rate, payment dates, payment forms, junior-stock restrictions; (5) conversion: minimum and maximum conversion rates, early conversion terms, fundamental change terms, mandatory conversion date, settlement period; (6) voting rights; (7) use of proceeds and purpose; (8) listing/ticker. Text: {{kkr_424b5}}"})
  result: # KKR 6.25% Series D Mandatory Convertible Preferred Stock: Key Terms from the 424B5
  
  ## 1. Offering Size and Proceeds
  
  | | Per Share | Without Option | With Full Option |
  |---|---|---|---|
  | Shares | | 45,000,000 | 51,750,000 (45,000,000 + 6,750,000) |
  | Public offering price | $50.000 | $2,250,000,000 | $2,587,500,000 |
  | Underwriting discount | $1.125 | $50,625,000 | $58,218,750 |
  | Proceeds, before expenses, to KKR | $48.875 | $2,199,375,000 | $2,529,281,250 |
  
  - Over-allotment: "up to an additional 6,750,000 shares," exercisable "within 30 days from the date of this prospectus supplement."
  - Estimated offering expenses (excluding the discount): "approximately $2.3 million."
  - Net proceeds: "approximately $2.20 billion (or approximately $2.53 billion if the underwriters exercise their over-allotment option... in full)."
  
  ## 2. Pricing and Settlement Dates
  
  - Prospectus supplement and pricing date: March 4, 2025.
  - Settlement: "March 7, 2025, which is the second business day after the initial trade date... (this settlement cycle being referred to as 'T+2')."
  
  ## 3. Liquidation Preference and Rights on Liquidation
  
  - Liquidation Preference: "$50.00 per share."
  - Plus a "Liquidation Dividend Amount" equal to "accumulated and unpaid dividends on such shares, whether or not declared, to, but excluding, the date fixed for liquidation."
  - Priority: paid "after satisfaction of debt and other liabilities owed to our creditors and holders of shares of any Senior Stock and before any payment or distribution is made to holders of Junior Stock (including our common stock)."
  - Parity Stock: shortfalls are shared "ratably... in proportion to their respective liquidation preferences."
  - Holders have no further claim after receiving the full amount.
  - A sale, lease, or merger is not
  …[truncated 597 chars]

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this KKR 424B5 prospectus supplement text, extract with exact figures and short quotes: (a) conversion terms: minimum conversion rate, maximum conversion rate, early conversion rights by holders, fundamental change make-whole, mandatory conversion date, settlement period and how shares are settled; (b) voting rights of the Mandatory Convertible Preferred Stock; (c) use of proceeds and purpose of the offering; (d) NYSE listing symbol. Text: {{kkr_424b5}}"})
  result: # KKR 6.25% Series D Mandatory Convertible Preferred Stock: Key Terms (424B5, March 4, 2025)
  
  ## (a) Conversion Terms
  
  - **Minimum Conversion Rate:** 0.3312 shares of common stock per preferred share. The prospectus describes it as "not less than 0.3312 shares of our common stock (the 'Minimum Conversion Rate')."
  - **Maximum Conversion Rate:** 0.4140 shares per preferred share. The prospectus describes it as "not more than 0.4140 shares of our common stock (the 'Maximum Conversion Rate')."
  - **Early conversion at holder's option:** Holders may convert "at any time prior to March 1, 2028 (an 'Early Conversion'), into shares of our common stock at the Minimum Conversion Rate of 0.3312 shares," in whole or in part, but not in increments of less than one share. This right does not apply during a Fundamental Change Conversion Period. If declared dividends are unpaid, the rate is increased by an Early Conversion Additional Amount, with no obligation to pay any shortfall in cash or shares.
  - **Fundamental change make-whole:**
    - Holders may convert during the "Fundamental Change Conversion Period," which begins on the Fundamental Change Effective Date and ends "20 calendar days after the Fundamental Change Effective Date," but no later than March 1, 2028.
    - The Fundamental Change Conversion Rate is set by a table keyed to the effective date and the Fundamental Change Stock Price. Per the table, the rate is 0.4140 at the lowest stock prices and 0.3312 when the stock price exceeds $300.00 (or at the 0.3312 level for the March 1, 2028 row above $150.97).
    - The Fundamental Change Dividend Make-Whole Amount is "the present value (calculated using a discount rate of 4.77% per annum)" of remaining dividends through March 1, 2028, payable in cash or shares.
    - Holders also recei
  …[truncated 3,041 chars]

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "**KKR & Co. Inc. (NYSE: KKR) 6.25% Series D Mandatory Convertible Preferred Stock – March 2025 offering (as of April 7, 2025)**\n\n**1. Offering size and proceeds**\n- The deal launched at $1.5 billion, <cite index=\"6-1\">with each share having a liquidation preference of $50.00 per share.</cite>\n- It was then upsized. KKR <cite index=\"8-1\">priced its previously announced offering of $2.25 billion (45,000,000 shares) of its 6.25% Series D Mandatory Convertible Preferred Stock at a price to the public and liquidation preference of $50.00 per share.</cite>\n- The underwriters had an over-allotment option for 6,750,000 more shares. <cite index=\"9-2\">The offering, which i
…[truncated 6,000 chars])

### Final answer
**KKR & Co. Inc. (NYSE: KKR) 6.25% Series D Mandatory Convertible Preferred Stock – March 2025 offering (as of April 7, 2025)**

**1. Offering size and proceeds**
- The deal launched at $1.5 billion, <cite index="6-1">with each share having a liquidation preference of $50.00 per share.</cite>
- It was then upsized. KKR <cite index="8-1">priced its previously announced offering of $2.25 billion (45,000,000 shares) of its 6.25% Series D Mandatory Convertible Preferred Stock at a price to the public and liquidation preference of $50.00 per share.</cite>
- The underwriters had an over-allotment option for 6,750,000 more shares. <cite index="9-2">The offering, which included the full exercise of the underwriters' over-allotment option</cite>, brought the total to 51,750,000 shares. Gross proceeds were <cite index="10-2">approximately $2.6 billion</cite>.
- Calculations: 51,750,000 × $50.00 = $2,587,500,000 public offering price. The underwriting discount was $1.125 per share, or $58,218,750 with the option. Proceeds before expenses were $48.875 per share, or $2,529,281,250. Estimated offering expenses were approximately $2.3 million.

**2. Pricing and closing date**
- Pricing was March 4, 2025, per the prospectus supplement.
- Settlement/closing was <cite index="2-4">on or about March 7, 2025, which will be the second business day after the initial trade date</cite>.
- The certificate of designations was filed with Delaware on March 7, 2025 (per the investing.com report).

**3. Liquidation preference**
- The liquidation preference is $50.00 per share. Holders also receive accumulated and unpaid dividends up to the liquidation date, whether or not declared.
- Priority: these shares rank after creditors and any senior stock, and ahead of junior stock including common stock. Parity stock shares shortfalls pro rata.
- The preferred is structurally subordinated to the liabilities of KKR's subsidiaries.
- The full aggregate liquidation preference is about $2.59 billion (51,750,000 × $50).

**4. Dividend rights**
- Dividends are <cite index="3-3">payable on a cumulative basis when, as and if declared by KKR & Co. Inc.'s board of directors</cite> at 6.25% of the $50.00 liquidation preference, i.e., $3.125 per share per year. Total annual dividends on all shares would be about $161,718,750 (51,750,000 × $3.125).
- Payment dates are <cite index="3-4">quarterly on March 1, June 1, September 1 and December 1 of each year to, and including, March 1, 2028, commencing on June 1, 2025.</cite>
- Dividends may be paid in cash, in common stock, or in a combination, subject to limits.
- While the preferred is outstanding, no dividends or distributions may be paid on common or other junior stock unless accumulated preferred dividends are paid or set aside.

**5. Conversion terms**
- Mandatory conversion date: expected to be March 1, 2028.
- Settlement period: the 20 consecutive trading days beginning on the 21st scheduled trading day before March 1, 2028. The conversion rate is based on the average VWAP over that period.
- Minimum conversion rate: 0.3312 common shares per preferred share (about 17,139,600 shares in total for all 51,750,000 preferred shares).
- Maximum conversion rate: 0.4140 common shares per preferred share (about 21,424,500 shares in total).
- Settlement mechanics: the rate is 0.3312 if the average price is above about $150.97, $50.00 divided by the average price if it is between about $120.77 and $150.97, and 0.4140 if it is below about $120.77.
- Early conversion: holders may convert at any time before March 1, 2028, at the minimum rate of 0.3312 shares, subject to adjustments.
- Fundamental change: holders may convert during a fundamental change period at a rate set by a table, with a dividend make-whole amount computed using a 4.77% discount rate.

**6. Voting rights**
- Holders generally have <cite index="3-1">no voting rights</cite> except as required by Delaware law or the certificate of incorporation. The prospectus states that holders will have no voting rights or powers except as specifically required by Delaware law or the certificate of incorporation.
- If dividends go unpaid for six or more dividend periods, the board expands by two seats and holders may elect two additional directors.
- Protective provisions require approval from holders of at least two-thirds of the preferred voting power for certain actions, such as creating senior stock, adversely changing the preferred's rights, or certain mergers or share exchanges.

**7. Purpose / use of proceeds**
- Net proceeds were approximately $2.20 billion (about $2.53 billion with the over-allotment option).
- KKR <cite index="6-4">intends to use the proceeds mainly for the acquisition of additional equity interests in core private equity portfolio companies reported in its Strategic Holdings segment.</cite> The prospectus also cites general corporate purposes. This follows KKR's February 2025 plan to increase its stakes in core private equity businesses by about $1.1 billion, expected to close in the first half of 2025.

**8. Listing**
- The preferred was proposed for NYSE listing under the symbol "KKR PR D." The common stock trades as "KKR."

**Sources**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm",
            "name": "KKR & Co. Inc. Form 424B5 prospectus supplement (March 2025)"
        },
        {
            "url": "https://www.nasdaq.com/press-release/kkr-upsizes-and-prices-offering-mandatory-convertible-preferred-stock-2025-03-04",
            "name": "KKR Upsizes and Prices Offering of Mandatory Convertible Preferred Stock (Business Wire via Nasdaq)"
        },
        {
            "url": "https://www.nasdaq.com/articles/kkr-co-commences-15-bln-offering-series-d-mandatory-convertible-preferred-stock",
            "name": "KKR & Co. Commences $1.5 Bln Offering Of Series D Mandatory Convertible Preferred Stock (RTTNews via Nasdaq)"
        },
        {
            "url": "https://www.investing.com/news/sec-filings/kkr-issues-26-billion-in-convertible-preferred-stock-93CH-3916004",
            "name": "KKR issues $2.6 billion in convertible preferred stock (Investing.com)"
        },
        {
            "url": "https://www.stblaw.com/about-us/news/view/2025/03/10/kkr-completes-$2.6-billion-mandatory-convertible-preferred-stock-offering",
            "name": "KKR Completes $2.6 Billion Mandatory Convertible Preferred Stock Offering (Simpson Thacher)"
        }
    ]
}