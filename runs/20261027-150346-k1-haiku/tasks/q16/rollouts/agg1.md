## Rollout `agg1`
- outcome: submitted
- turns: 8; cost: $0.421; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "security_offering_terms"})
  result: ---
  name: security_offering_terms
  description: Summarise the key terms of a registered securities offering (preferred, convertible, notes) from the prospectus supplement, with each term tied to an opened document.
  ---
  ANALYTIC MOVE: extract and summarise terms into one term-by-term summary.
  
  1. Controlling sources. The final 424B5 holds price, share count, discount, liquidation preference, dividend, conversion, voting and use-of-proceeds terms. The 8-K filed at closing holds the certificate of designations (EX-3.1) and the underwriting agreement (EX-1.1). The company's pricing press release is where an upsize from the launched size is stated, and often where option exercise is reported. The final 424B5 itself may not mention the launch size.
  2. A deal can have a launch 424B5, a pricing FWP or release and a final 424B5. Use the final version for terms. Give the launched size and the priced size separately if an opened document shows an upsize.
  3. Keep these apart, each with its own figure:
     - base deal size versus size if the over-allotment option is exercised in full;
     - gross versus net proceeds (after the underwriting discount and expenses);
     - pricing date versus settlement or closing date (T+2).
  4. Over-allotment exercise and upsizing must come from an opened document (press release, 8-K, later filing). Open the pricing press release before concluding either is unconfirmed. If still unconfirmed, write "option for up to X additional shares" and say so.
  5. For a mandatory convertible preferred, cover: price and liquidation preference; dividend rate, dollar amount per share per year, payment dates, first payment date, form of payment and cumulative status; minimum and maximum conversion rates with their price thresholds (initial price x maximum rate = liquidation
  …[truncated 1,017 chars]
- edgar_search({"search_query": "KKR Series D mandatory convertible preferred stock prospectus supplement", "start_date": "2025-03-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 92, "page": 1, "results": [{"form": "424B5", "file_date": "2025-03-06", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007426", "document": "ny20042797x2_424b5.htm", "description": "424B5", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm"}, {"form": "424B5", "file_date": "2025-03-04", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-006869", "document": "ny20042797x1_424b5.htm", "description": "424B5", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125006869/ny20042797x1_424b5.htm"}, {"form": "FWP", "file_date": "2025-03-05", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007061", "document": "ny20042797x3_fwp.htm", "description": "FWP", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007061/ny20042797x3_fwp.htm"}, {"form": "8-A12B", "file_date": "2025-03-07", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007653", "document": "ny20042797x4_8a12b.htm", "description": "8-A12B", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007653/ny20042797x4_8a12b.htm"}, {"form": "8-K", "file_date": "2025-03-07", "period_ending": "2025-03-04", "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007608", "document": "ny20042797x5_ex1-1.htm", "description": "EXHIBIT 1.1", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20
  …[truncated 5,268 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm", "key": "final424b5"})
  result: SUCCESS: The result has been saved to the data storage under the key: final424b5. (500,749 characters)
  The data_storage currently contains the following keys:
  final424b5
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_ex3-1.htm", "key": "ex31"})
  result: SUCCESS: The result has been saved to the data storage under the key: ex31. (158,512 characters)
  The data_storage currently contains the following keys:
  final424b5
  ex31
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this prospectus supplement, state the offering summary: number of shares offered, option to purchase additional shares, public offering price per share, underwriting discount, net proceeds, total offering size, expected closing/settlement date, and the trade date. Quote the exact sentences. Document: {{final424b5}}"})
  result: Here are the offering terms from the prospectus supplement, quoted from the document:
  
  **Number of shares offered:** "We are offering 45,000,000 shares of our 6.25% Series D Mandatory Convertible Preferred Stock, par value $0.01 per share (the "Mandatory Convertible Preferred Stock")."
  
  **Option to purchase additional shares:** "We have granted the underwriters an option, exercisable within 30 days from the date of this prospectus supplement, to purchase up to 6,750,000 additional shares of the Mandatory Convertible Preferred Stock at the public offering price, less the underwriting discount, solely to cover over-allotments, if any."
  
  **Public offering price per share:** "$50.00 per share of the Mandatory Convertible Preferred Stock." (The cover table shows "$50.000" per share.)
  
  **Underwriting discount:** The cover table shows "Underwriting discount $1.125 $50,625,000" (per share and total).
  
  **Net proceeds:** The cover table shows "Proceeds, before expenses, to us $48.875 $2,199,375,000." The Use of Proceeds section states: "We estimate that the net proceeds to us from this offering, after deducting underwriting discounts and estimated offering expenses payable by us, will be approximately $2.20 billion (or approximately $2.53 billion if the underwriters exercise their over-allotment option to purchase additional shares of Mandatory Convertible Preferred Stock in full)."
  
  **Total offering size:** The cover table shows "Total Public offering price $2,250,000,000." The Underwriting section shows $2,587,500,000 if the option is fully exercised.
  
  **Expected closing/settlement date:** "Settlement Date March 7, 2025, which is the second business day after the initial trade date for the Mandatory Convertible Preferred Stock (this settlement cycle being referred to as "T+2").
  …[truncated 463 chars]
- retrieve_information({"prompt": "From this prospectus supplement, state the dividend terms of the 6.25% Series D Mandatory Convertible Preferred Stock: dividend rate, dollar amount per share per year, payment dates, first dividend payment date, whether cumulative, form of payment. Also the liquidation preference per share. Document: {{final424b5}}"})
  result: **6.25% Series D Mandatory Convertible Preferred Stock (KKR & Co. Inc.)**
  
  **Dividend terms**
  
  - **Dividend rate:** 6.25% per annum of the $50.00 liquidation preference per share.
  - **Dollar amount per share per year:** $3.125 per share per annum.
  - **Quarterly amount:** $0.78125 per share for each full dividend period (the rate divided by four).
  - **Payment dates:** March 1, June 1, September 1 and December 1 of each year, commencing June 1, 2025, and ending on and including March 1, 2028. If a payment date is not a Business Day, payment is made on the next Business Day with no interest for the delay.
  - **First dividend payment date:** June 1, 2025. The initial dividend period runs from the Initial Issue Date (assumed to be March 7, 2025) to, but excluding, June 1, 2025. The expected first dividend is approximately $0.7292 per share, payable to holders of record on May 15, 2025.
  - **Cumulative or non-cumulative:** Cumulative. Dividends accumulate from the most recent date to which dividends have been paid (or from the Initial Issue Date if none have been paid), whether or not there are funds legally available or shares legally permitted to be issued for payment. Accumulated dividends do not bear interest.
  - **Form of payment:** Declared dividends may be paid in cash, by delivery of shares of KKR common stock, or through any combination of cash and common stock, at KKR's sole discretion. Common stock used for payment is valued at 97% of the Average VWAP over the five Trading Days beginning on the sixth Scheduled Trading Day before the payment date. Share deliveries are capped by a Floor Price of $42.2705 (about 35% of the Initial Price); any excess over the cap is paid in cash to the extent legally and contractually permitted.
  
  **Liquidation preference**
  
  - **$50.00 per
  …[truncated 170 chars]
- retrieve_information({"prompt": "From this prospectus supplement, state the mandatory conversion date, minimum conversion rate, maximum conversion rate, initial price, threshold appreciation price, early conversion terms and fundamental change terms for the Series D Mandatory Convertible Preferred Stock. Document: {{final424b5}}"})
  result: Here are the key terms of the 6.25% Series D Mandatory Convertible Preferred Stock from the KKR & Co. Inc. prospectus supplement (424B5, March 4, 2025):
  
  - **Mandatory Conversion Date:** The second business day immediately following the last Trading Day of the Settlement Period. It is expected to be **March 1, 2028**.
  
  - **Minimum Conversion Rate:** **0.3312** shares of common stock per share of preferred stock, applying when the Applicable Market Value exceeds the Threshold Appreciation Price.
  
  - **Maximum Conversion Rate:** **0.4140** shares of common stock per share of preferred stock, applying when the Applicable Market Value is below the Initial Price.
  
  - **Initial Price:** Approximately **$120.7729**, which is $50.00 divided by the Maximum Conversion Rate. It equals the closing price of KKR common stock on March 4, 2025.
  
  - **Threshold Appreciation Price:** Approximately **$150.9662**, which is $50.00 divided by the Minimum Conversion Rate. It represents about 25% appreciation over the Initial Price.
  
  - **Early Conversion Terms:** At any time before March 1, 2028, holders may convert all or part of their shares (in increments of at least one share, other than during a Fundamental Change Conversion Period) at the Minimum Conversion Rate of 0.3312 shares per preferred share. If accumulated and unpaid dividends for prior full dividend periods have not been declared and paid, the conversion rate is increased by an Early Conversion Additional Amount, divided by the greater of the Floor Price and the Early Conversion Average Price (the Average VWAP over the 20 Trading Day period beginning on the 21st Scheduled Trading Day before the Early Conversion Date). The Company has no obligation to pay any shortfall in cash or in shares for this adjustment.
  
  - **Fundamental Chang
  …[truncated 919 chars]
- retrieve_information({"prompt": "From this prospectus supplement, state the voting rights of the Series D Mandatory Convertible Preferred Stock, the NYSE listing symbol, and the use of proceeds of the offering. Document: {{final424b5}}"})
  result: **Voting rights of the Series D Mandatory Convertible Preferred Stock**
  
  The holders have no voting rights except as required by Delaware law or KKR's certificate of incorporation, and the following limited circumstances:
  
  - **Board representation on nonpayment:** If dividends have not been declared and paid for the equivalent of six or more dividend periods (whether or not consecutive), the number of directors will increase by two at the next annual or special meeting. The holders, voting together as a single class with any other Voting Preferred Stock, can then elect two additional directors (subject to a limit of two Preferred Stock Directors and NYSE majority-independence requirements). This right ends once all accumulated dividends are paid.
  - **Protective provisions:** Without the affirmative vote or consent of at least two-thirds of the voting power of the outstanding Mandatory Convertible Preferred Stock (and, for the first item only, other affected Voting Preferred Stock), KKR will not:
    1. Create or increase the authorized amount of any Senior Stock;
    2. Amend its certificate of incorporation or the Certificate of Designations in a way that materially and adversely affects the preferred stock's special rights, preferences, or voting powers; or
    3. Complete a binding share exchange, reclassification, merger, or consolidation unless the preferred stock remains outstanding or is converted into preference securities of the successor with terms not materially less favorable to holders.
  
  Certain actions, such as authorizing additional Parity or Junior Stock, increasing authorized preferred shares, or the reorganization adjustments described in the document, are expressly deemed not to adversely affect the preferred stock and do not require a vote.
  
  **NYSE listing
  …[truncated 754 chars]

### Turn 4  (stop_reason=tool_use)
- web_search(query="KKR prices upsized mandatory convertible preferred stock offering March 2025") → 0 results: 
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007061/ny20042797x3_fwp.htm", "key": "fwp"})
  result: SUCCESS: The result has been saved to the data storage under the key: fwp. (12,230 characters)
  The data_storage currently contains the following keys:
  final424b5
  ex31
  fwp
  

### Turn 5  (stop_reason=tool_use)
- web_search(query=null) → 10 results: KKR & Co. Inc. - Form FWP - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000114036125007061/ny20042797x3_fwp.htm>; KKR & Co. Inc. - Form 424B5 - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm>; KKR & Co. Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_ex1-1.htm>; KKR & Co. Inc. - Form 424B5 - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000114036125006869/ny20042797x1_424b5.htm>; KKR & Co. Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_8k.htm>
- parse_html_page({"url": "https://www.nasdaq.com/press-release/kkr-upsizes-and-prices-offering-mandatory-convertible-preferred-stock-2025-03-04", "key": "pricing_pr"})
  ERROR: ReadTimeout: HTTPSConnectionPool(host='www.nasdaq.com', port=443): Read timed out. (read timeout=60)
- retrieve_information({"prompt": "From this FWP, state the trade date, settlement date, public offering price, and the stated purpose or use of proceeds, plus any statement about upsizing from the launched size. Document: {{fwp}}"})
  result: **Trade date:** March 5, 2025
  
  **Settlement date:** March 7, 2025, which is T+2 for the Mandatory Convertible Preferred Stock.
  
  **Public offering price:** $50.00 per share of 6.25% Series D Mandatory Convertible Preferred Stock.
  
  **Stated purpose or use of proceeds:** The Issuer estimates net proceeds of about $2.20 billion (about $2.53 billion if the underwriters exercise the over-allotment option in full). It intends to use the net proceeds to acquire additional equity interests in core private equity portfolio companies reported in its Strategic Holdings segment and for other general corporate purposes.
  
  **Upsizing statement:** The offering size was increased from the previously announced 30,000,000 shares to 45,000,000 shares. The final prospectus supplement will reflect conforming changes for the increase. The underwriters also have an over-allotment option to purchase up to 6,750,000 additional shares.

### Turn 6  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_8k.htm", "key": "8k"})
  result: SUCCESS: The result has been saved to the data storage under the key: 8k. (10,186 characters)
  The data_storage currently contains the following keys:
  final424b5
  ex31
  fwp
  8k
  

### Turn 7  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this 8-K, state the number of shares issued in total, aggregate liquidation preference, whether the over-allotment option was exercised in full (and how many shares), the date of the underwriting agreement, and the closing date. Document: {{8k}}"})
  result: - **Total shares issued:** 51,750,000 shares of 6.25% Series D Mandatory Convertible Preferred Stock.
  - **Aggregate liquidation preference:** $2,587,500,000 ($50.00 per share).
  - **Over-allotment option:** Exercised in full, for 6,750,000 additional shares ($337,500,000 aggregate liquidation preference), included in the 51,750,000 total.
  - **Underwriting agreement date:** March 4, 2025, with Morgan Stanley & Co. LLC and KKR Capital Markets LLC as representatives of the underwriters.
  - **Closing date:** The 8-K does not use the word "closing," but it reports the issuance on March 7, 2025, which is the closing date. The Certificate of Designations was also filed and became effective that day.

### Turn 8  (stop_reason=tool_use)
- submit_final_result({"final_result": "KKR & Co. Inc. (NYSE: KKR) 6.25% Series D Mandatory Convertible Preferred Stock, offered March 2025\n\nOffering size\n- Launched at $1.5 billion (30,000,000 shares). The FWP filed March 5, 2025 states the size was increased to 45,000,000 shares, and says the final prospectus supplement would reflect that increase.\n- Priced at 45,000,000 shares x $50.00 = $2.25 billion (base deal).\n- Underwriters' 30-day option for 6,750,000 more shares ($337.5 million). The 8-K filed March 7, 2025 reports the option was exercised in full, for a total of 51,750,000 shares and $2,587,500,000 aggregate liquidation preference.\n- Underwriting discount: $1.125 per share ($50,625,000 on the bas
…[truncated 4,065 chars])

### Final answer
KKR & Co. Inc. (NYSE: KKR) 6.25% Series D Mandatory Convertible Preferred Stock, offered March 2025

Offering size
- Launched at $1.5 billion (30,000,000 shares). The FWP filed March 5, 2025 states the size was increased to 45,000,000 shares, and says the final prospectus supplement would reflect that increase.
- Priced at 45,000,000 shares x $50.00 = $2.25 billion (base deal).
- Underwriters' 30-day option for 6,750,000 more shares ($337.5 million). The 8-K filed March 7, 2025 reports the option was exercised in full, for a total of 51,750,000 shares and $2,587,500,000 aggregate liquidation preference.
- Underwriting discount: $1.125 per share ($50,625,000 on the base deal). Net proceeds: about $2.20 billion, or about $2.53 billion with the option exercised in full.

Key dates
- Pricing/underwriting agreement: March 4, 2025 (the final 424B5 cover is dated March 4, 2025).
- Trade date: March 5, 2025 (per the FWP). The final prospectus supplement does not state it.
- Settlement/closing: March 7, 2025 (T+2). The 8-K reports the issuance on that date, and the Certificate of Designations was filed with Delaware that day.

Price and liquidation preference
- Public offering price: $50.00 per share.
- Liquidation preference: $50.00 per share, plus accumulated and unpaid dividends (declared or not) up to the liquidation date.

Dividend rights
- Rate: 6.25% per annum of the $50.00 liquidation preference, i.e., $3.125 per share per year ($0.78125 per quarter).
- Payment dates: March 1, June 1, September 1 and December 1, starting June 1, 2025 and ending March 1, 2028. The first dividend (June 1, 2025) is expected to be about $0.7292 per share.
- Cumulative. Undeclared dividends accumulate without interest.
- Form: cash, KKR common stock, or a combination, at KKR's discretion. Stock used for payment is valued at 97% of the average VWAP over a five-day period, with share deliveries capped by a $42.2705 floor price (about 35% of the initial price); any excess is paid in cash where permitted.

Conversion terms
- Mandatory conversion date: expected March 1, 2028, into a variable number of common shares based on the average VWAP over a 20-trading-day settlement period.
- Minimum conversion rate: 0.3312 common shares per preferred share (applies when the applicable market value exceeds the threshold appreciation price of about $150.97, i.e., $50 / 0.3312).
- Maximum conversion rate: 0.4140 common shares per preferred share (applies when the applicable market value is below the initial price of about $120.77, i.e., $50 / 0.4140). The initial price equals KKR's March 4, 2025 closing price.
- Early conversion: holders may convert at any time before March 1, 2028 at the minimum rate of 0.3312. If prior accumulated dividends are unpaid, an additional amount is added to the rate, with no cash or share make-up obligation for any shortfall.
- Fundamental change: holders may convert during a window of 20 calendar days from the effective date, at a reference-table rate capped at 0.4140 and floored at 0.3312. They also receive a dividend make-whole amount (remaining dividends discounted at 4.77% per year) and any accumulated dividend amount.

Voting rights
- Generally none, except as required by Delaware law or the charter. Exceptions: if dividends are unpaid for six or more periods, the holders can elect two additional directors until arrears are paid. Two-thirds of the preferred must consent to create senior stock, adversely amend its special rights, or complete certain mergers or reclassifications.

Listing
- Intended NYSE symbol: "KKR PR D."

Use of proceeds
- Acquiring additional equity interests in core private equity portfolio companies in KKR's Strategic Holdings segment, including the roughly $1.1 billion of increased ownership interests announced February 4, 2025, and other general corporate purposes.

Note: I did not open the pricing press release (the Nasdaq copy timed out). The upsizing and full option exercise are confirmed from the FWP and 8-K.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm",
            "name": "KKR & Co. Inc. Form 424B5 final prospectus supplement (filed 2025-03-06)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007061/ny20042797x3_fwp.htm",
            "name": "KKR & Co. Inc. Form FWP (filed 2025-03-05)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_8k.htm",
            "name": "KKR & Co. Inc. Form 8-K (filed 2025-03-07)"
        }
    ]
}