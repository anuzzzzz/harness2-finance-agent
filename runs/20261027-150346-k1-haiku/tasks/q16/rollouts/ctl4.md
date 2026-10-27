## Rollout `ctl4`
- outcome: submitted
- turns: 4; cost: $0.122; submitted: True

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
- retrieve_information({"prompt": "From this KKR 424B5 prospectus supplement, extract the following for the 6.25% Series D Mandatory Convertible Preferred Stock: (1) aggregate offering size, number of shares, base and over-allotment; (2) closing/delivery date; (3) public offering price and liquidation preference; (4) dividend rate, payment dates, payment form, priority/ranking; (5) mandatory conversion date, minimum and maximum conversion rates, settlement period, early conversion rights, fundamental change terms; (6) voting rights; (7) use of proceeds. Quote the key sentences briefly. Document: {{kkr_424b5}}"})
  result: # KKR 6.25% Series D Mandatory Convertible Preferred Stock: Key Terms (424B5, March 4, 2025)
  
  ## 1. Offering Size, Shares, Base and Over-Allotment
  - **Base offering:** "We are offering 45,000,000 shares of our 6.25% Series D Mandatory Convertible Preferred Stock." Gross proceeds are $2,250,000,000 and the underwriting discount is $50,625,000.
  - **Over-allotment:** "We have granted the underwriters the option, exercisable within 30 days from the date of this prospectus supplement, to purchase up to an additional 6,750,000 shares." If fully exercised, the total is $2,587,500,000 gross.
  
  ## 2. Closing/Delivery Date
  - "The underwriters expect to deliver the Mandatory Convertible Preferred Stock to purchasers on or about March 7, 2025, which will be the second business day after the initial trade date... (T+2)."
  
  ## 3. Public Offering Price and Liquidation Preference
  - **Public offering price:** "$50.00 per share."
  - **Liquidation preference:** "$50.00 per share," plus a "Liquidation Dividend Amount" equal to accumulated and unpaid dividends, whether or not declared.
  
  ## 4. Dividends
  - **Rate:** "6.25% of the liquidation preference of $50.00 per share... per annum" ($3.125 per year).
  - **Cumulative:** Dividends are "payable on a cumulative basis when, as and if declared by our Board of Directors."
  - **Payment dates:** "March 1, June 1, September 1 and December 1 of each year, commencing on June 1, 2025, and ending on, and including, March 1, 2028." Record dates are February 15, May 15, August 15 and November 15.
  - **Amounts:** The first dividend is expected to be "approximately $0.7292 per share," and each later dividend "$0.78125 per share."
  - **Payment form:** "We may pay declared dividends in cash or, subject to certain limitations, in shares of our common stock or in any
  …[truncated 4,389 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**KKR & Co. Inc. (NYSE: KKR) 6.25% Series D Mandatory Convertible Preferred Stock, March 2025: key terms**\n\nNote: the offering was launched on March 4, 2025 as a $1.5 billion deal, then upsized and priced the same evening. Terms below come from the final prospectus supplement (424B5, filed March 6, 2025), the pricing press release, and the launch release. Where the launch release and the final prospectus differ, the final terms govern.\n\n1. **Offering size:** KKR launched the deal at $1.5 billion (30,000,000 shares). <cite index=\"9-1\">KKR & Co. Inc. today announced that it has priced its previously announced offering of $2.25 billion of its 6.25% Series D Mandatory Con
…[truncated 4,911 chars])

### Final answer
**KKR & Co. Inc. (NYSE: KKR) 6.25% Series D Mandatory Convertible Preferred Stock, March 2025: key terms**

Note: the offering was launched on March 4, 2025 as a $1.5 billion deal, then upsized and priced the same evening. Terms below come from the final prospectus supplement (424B5, filed March 6, 2025), the pricing press release, and the launch release. Where the launch release and the final prospectus differ, the final terms govern.

1. **Offering size:** KKR launched the deal at $1.5 billion (30,000,000 shares). <cite index="9-1">KKR & Co. Inc. today announced that it has priced its previously announced offering of $2.25 billion of its 6.25% Series D Mandatory Convertible Preferred Stock</cite>, which is 45,000,000 shares. The underwriters also received a 30-day option for up to 6,750,000 more shares (about $337.5 million at $50.00) solely to cover over-allotments. The 424B5 gives a $2,199,375,000 figure for proceeds before expenses, after the underwriting discount.

2. **Closing date:** The underwriters <cite index="2-4">expect to deliver the Mandatory Convertible Preferred Stock to purchasers on or about March 7, 2025, which will be the second business day after the initial trade date</cite>.

3. **Price and liquidation preference:** The public offering price was $50.00 per share, which matched the liquidation preference. Under the prospectus, a holder's dissolution payment also includes accumulated and unpaid dividends, whether or not declared.

4. **Dividend rights:** The stock carries a 6.25% annual rate on the $50.00 liquidation preference, or $3.125 per share per year. Dividends are cumulative and payable only when, as, and if the board declares them. They are scheduled quarterly on March 1, June 1, September 1 and December 1, starting June 1, 2025 and running through March 1, 2028. KKR may pay in cash, in common stock (subject to limits), or in a mix. Stock payments are valued at 97% of the average VWAP over five trading days and are subject to a floor price of $42.2705. The preferred ranks senior to common stock and to the existing Series I preferred. It is junior to all of KKR's indebtedness and liabilities. No dividends may be paid on junior stock, including common stock, until accumulated preferred dividends are paid.

5. **Conversion terms:** Unless converted earlier, each share automatically converts on or around March 1, 2028 into between 0.3312 and 0.4140 shares of common stock. The exact ratio depends on KKR's average VWAP over the 20-trading-day settlement period that begins with the 21st scheduled trading day before March 1, 2028. Per the prospectus, the rate is 0.3312 when the stock trades above roughly $150.97, 0.4140 when it trades below roughly $120.77 (the initial price), and $50.00 divided by the market value in between. Holders may also convert early at any time before March 1, 2028 at the minimum rate of 0.3312 shares, plus an extra-share amount if dividends are in arrears. If a fundamental change occurs (such as a merger, asset sale, a >50% voting-power acquisition, or delisting), holders get a make-whole conversion window and a dividend make-whole amount. Conversion rates are subject to customary anti-dilution adjustments.

6. **Voting rights:** The holders have no voting rights except as required by Delaware law or KKR's charter. If dividends are unpaid for six or more dividend periods, the board increases by two seats and the holders may elect two directors. Certain actions also need approval from two-thirds of the outstanding preferred. These include creating or increasing senior stock, adversely changing the preferred's special rights, and certain mergers or share exchanges.

7. **Purpose:** KKR <cite index="6-4">intends to use the proceeds mainly for the acquisition of additional equity interests in core private equity portfolio companies reported in its Strategic Holdings segment.</cite> The prospectus also states that net proceeds were estimated at about $2.20 billion (about $2.53 billion if the over-allotment option were fully exercised), and that proceeds may fund general corporate purposes too.

**Source notes:** The pricing press release and the 424B5 are consistent on the base size, price, closing date, and conversion range. The initial launch release listed a 4,500,000-share over-allotment, which was superseded by the 6,750,000-share option in the final prospectus.

Sources:
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
            "url": "https://www.nasdaq.com/articles/kkr-co-commences-15-bln-offering-series-d-mandatory-convertible-preferred-stock",
            "name": "KKR & Co. Commences $1.5 Bln Offering Of Series D Mandatory Convertible Preferred Stock (RTTNews via Nasdaq)"
        }
    ]
}