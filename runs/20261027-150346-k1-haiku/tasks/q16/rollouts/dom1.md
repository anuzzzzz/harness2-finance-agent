## Rollout `dom1`
- outcome: submitted
- turns: 7; cost: $0.342; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "security_offering_terms"})
  result: ---
  name: security_offering_terms
  description: Summarise the key terms of a registered securities offering (preferred, convertible, notes) from the prospectus supplement, with each term tied to the opened document.
  ---
  ANALYTIC MOVE: extract and summarise terms. Inputs are the final 424B5 prospectus supplement, the pricing press release or FWP, and the closing 8-K. The result is one term-by-term summary.
  
  1. Controlling sources. The final 424B5 holds the price, share count, discount, liquidation preference, dividend, conversion, voting and use-of-proceeds terms. An 8-K filed after closing holds the certificate of designations (EX-3.1) and the underwriting agreement. The 8-K or press release is the place to confirm closing and over-allotment exercise.
  2. Several 424B5s or FWPs may exist for one deal: a launch version, a pricing version and an upsize. Use the pricing or final version for terms. Say when the deal was upsized, and give the launched size and the priced size separately.
  3. Keep these apart, each with its own figure:
     - base deal size versus size if the over-allotment option is exercised in full;
     - gross proceeds versus net proceeds (after the underwriting discount and expenses);
     - pricing date versus settlement or closing date (T+2 is stated in the supplement).
  4. Do not state that the over-allotment option was exercised, or give a final post-exercise total, unless an opened document (8-K, press release, later filing) says so. Otherwise write "option for up to X additional shares".
  5. For a mandatory convertible preferred, cover: price and liquidation preference per share; dividend rate, the dollar amount per share per year, payment dates, the first payment date, form of payment (cash, stock or both) and the cumulative or non-cumulative status; the mi
  …[truncated 1,674 chars]
- edgar_search({"search_query": "KKR Series D mandatory convertible preferred stock prospectus supplement", "start_date": "2025-03-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 92, "page": 1, "results": [{"form": "424B5", "file_date": "2025-03-06", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007426", "document": "ny20042797x2_424b5.htm", "description": "424B5", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm"}, {"form": "424B5", "file_date": "2025-03-04", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-006869", "document": "ny20042797x1_424b5.htm", "description": "424B5", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125006869/ny20042797x1_424b5.htm"}, {"form": "FWP", "file_date": "2025-03-05", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007061", "document": "ny20042797x3_fwp.htm", "description": "FWP", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007061/ny20042797x3_fwp.htm"}, {"form": "8-A12B", "file_date": "2025-03-07", "period_ending": null, "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007653", "document": "ny20042797x4_8a12b.htm", "description": "8-A12B", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007653/ny20042797x4_8a12b.htm"}, {"form": "8-K", "file_date": "2025-03-07", "period_ending": "2025-03-04", "company": "KKR & Co. Inc.  (KKR, KKRS)  (CIK 0001404912)", "ciks": ["0001404912"], "accession": "0001140361-25-007608", "document": "ny20042797x5_ex1-1.htm", "description": "EXHIBIT 1.1", "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20
  …[truncated 5,268 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm", "key": "final_424b5"})
  result: SUCCESS: The result has been saved to the data storage under the key: final_424b5. (500,749 characters)
  The data_storage currently contains the following keys:
  final_424b5
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_ex3-1.htm", "key": "cert_designations"})
  result: SUCCESS: The result has been saved to the data storage under the key: cert_designations. (158,512 characters)
  The data_storage currently contains the following keys:
  final_424b5
  cert_designations
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this KKR 424B5 prospectus supplement, extract the key terms of the 6.25% Series D Mandatory Convertible Preferred Stock: number of shares offered and base deal size in dollars, option for additional shares, public offering price per share, underwriting discount, gross and net proceeds, pricing date, settlement/closing date, liquidation preference, dividend rate and per-share annual amount, dividend payment dates, cumulative status, minimum and maximum conversion rates, initial price, threshold appreciation price, mandatory conversion date, early conversion terms, voting rights, NYSE listing symbol, and use of proceeds. Quote exact figures and state the section each comes fro
…[truncated 30 chars])
  result: # KKR & Co. Inc. 6.25% Series D Mandatory Convertible Preferred Stock: Key Terms from the 424B5 Prospectus Supplement (dated March 4, 2025)
  
  | Term | Exact Figure / Language from Document | Source Section (page) |
  |---|---|---|
  | **Shares offered (base)** | "45,000,000 shares of our 6.25% Series D Mandatory Convertible Preferred Stock, par value $0.01 per share" | Cover page; The Offering – Securities Offered (S-6) |
  | **Base deal size** | Total public offering price "$2,250,000,000" | Cover page pricing table; Underwriting – offering table (S-80) |
  | **Underwriters' option** | "up to an additional 6,750,000 shares," exercisable "within 30 days from the date of this prospectus supplement," "solely to cover over-allotments, if any" | Cover page; The Offering – Underwriters' Option (S-6); Underwriting (S-79)
- retrieve_information({"prompt": "From this KKR certificate of designations (Exhibit 3.1 to 8-K), extract for the Series D Mandatory Convertible Preferred Stock: liquidation preference, dividend rate and payment dates, cumulative status, conversion rate minimum and maximum, initial price, threshold appreciation price, mandatory conversion date, early conversion/fundamental change terms, and voting rights (general and protective provisions). Document: {{cert_designations}}"})
  result: # KKR & Co. Inc. 6.25% Series D Mandatory Convertible Preferred Stock: Key Terms
  
  **Source:** Certificate of Designations (Exhibit 3.1), dated March 7, 2025. Section references are to that document.
  
  ## Core Terms
  
  | Term | Provision |
  |---|---|
  | **Shares authorized** | 51,750,000 (Sec. 1) |
  | **Par value** | $0.01 (Charter/Sec. 1) |
  | **Initial Issue Date** | March 7, 2025 (Sec. 3) |
  | **Liquidation Preference** | $50.00 per share (Sec. 3, Sec. 5(a)) |
  | **Liquidation Dividend Amount** | Plus accumulated and unpaid dividends, whether or not declared, to but excluding the liquidation date (Sec. 5(a)) |
  | **Ranking** | Senior to Junior Stock (including Common Stock and Existing Series I Preferred); on parity with Parity Stock; junior to Senior Stock and to all indebtedness and liabilities; structurally subordinated to subsidiary liabilities (Sec. 2) |
  | **Redemption / sinking fund** | None. Company may repurchase or exchange in the open market or by tender without holder consent (Sec. 6) |
  
  ## Dividends
  
  - **Rate:** 6.25% per annum of the $50.00 Liquidation Preference, equal to $3.125 per share per year (Sec. 4(a)).
  - **Quarterly amount:** $3.125 ÷ 4 = $0.78125 per share for each full Dividend Period (Sec. 4(a)).
  - **Payment dates:** March 1, June 1, September 1, and December 1 of each year, through and including March 1, 2028, beginning June 1, 2025 (Sec. 3). Initial Dividend Period runs from the Initial Issue Date to June 1, 2025.
  - **Regular Record Dates:** February 15, May 15, August 15, and November 15 (Sec. 3).
  - **Day-count:** Initial and partial periods use actual days over a 360-day year of twelve 30-day months. If a payment date is not a Business Day, payment is made the next Business Day with no interest (Sec. 4(a)).
  - **Cumulative status:** Cumulative. Divid
  …[truncated 2,645 chars]

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this KKR 424B5 prospectus supplement, extract: pricing date, closing/settlement date, underwriting discount per share and total, estimated net proceeds, net proceeds if option exercised, NYSE ticker symbol for the Series D preferred, early conversion (holder) terms and fundamental change conversion rate, voting rights, and use of proceeds. Quote exact figures and state the section. Document: {{final_424b5}}"})
  result: # KKR 424B5 Extraction (Prospectus Supplement dated March 4, 2025)
  
  **Offering:** 45,000,000 shares of 6.25% Series D Mandatory Convertible Preferred Stock, par value $0.01, at $50.00 per share.
  
  | Item | Extracted Terms | Section / Location |
  |---|---|---|
  | **Pricing date** | No "pricing date" is labeled. The supplement is dated **March 4, 2025**, and the Initial Price is based on the **March 4, 2025** closing price of common stock. | Cover page; "Summary—The Offering" (Dividends; Conversion Rate), S-6 to S-9 |
  | **Closing / settlement date** | **March 7, 2025** ("on or about March 7, 2025," T+2) | Cover page; "The Offering—Settlement Date" (S-6); "Payment and Settlement" (S-14) |
  | **Underwriting discount, per share** | **$1.125** | Cover page table; "Underwriting (Conflicts of Interest)," S-79 |
  | **Underwriting discount, total** | **$50,625,000** (without option); **$58,218,750** (with full option) | Cover page table; "Underwriting," S-79 |
  | **Estimated net proceeds** | Proceeds before expenses: **$48.875** per share, **$2,199,375,000** total. Summary and Use of Proceeds state **approximately $2.20 billion**. Estimated offering expenses are about **$2.3 million**. | Cover page; "Summary—Use of Proceeds" (S-14); "Use of Proceeds" (S-32); "Underwriting," S-79; Capitalization fn. (3), S-33 |
  | **Net proceeds if option exercised** | **Approximately $2.53 billion**. Total proceeds before expenses are **$2,529,281,250**, on a gross offering of $2,587,500,000 with the underwriters' option of 6,750,000 additional shares. | "Summary—Use of Proceeds" (S-14); "Use of Proceeds" (S-32); "Underwriting," S-79 |
  | **NYSE ticker, Series D preferred** | **"KKR PR D"** (proposed; the company "intends to apply" to list, and trading is expected within 30 days of first issuance) | Cove
  …[truncated 3,335 chars]
- retrieve_information({"prompt": "From this KKR certificate of designations, extract the Voting Rights section (general voting rights, dividend-nonpayment voting rights, protective provisions/consent requirements), the early conversion at holder's option terms and fundamental change make-whole terms (Sections 9 and 10). Document: {{cert_designations}}"})
  result: # Extracted Provisions: KKR 6.25% Series D Mandatory Convertible Preferred Stock Certificate of Designations (EX-3.1)
  
  The Voting Rights provisions are in **Section 7**, not Sections 9 and 10. Sections 9 and 10 cover early conversion and fundamental change conversion. The text below is reproduced from the document, with headings added for navigation.
  
  ---
  
  ## Part I: Voting Rights (Section 7)
  
  ### 7(a) General
  Holders shall not have any voting rights or powers other than those set forth in this Section 7, except as specifically required by Delaware law or by the Charter from time to time.
  
  ### 7(b) Right to Elect Two Directors Upon Nonpayment
  
  **(i)** Whenever dividends on any shares of the Mandatory Convertible Preferred Stock have not been declared and paid for the equivalent of six or more Dividend Periods, whether or not for consecutive Dividend Periods (a "Nonpayment"), the authorized number of directors on the Board of Directors shall, at the Corporation's next annual meeting of the stockholders or at a special meeting of stockholders as provided below, automatically be increased by two and Holders, voting together as a single class with holders of any and all other series of Voting Preferred Stock then outstanding, shall be entitled, at the Corporation's next annual meeting of stockholders or at a special meeting of stockholders, if any, as provided below, to vote for the election of a total of two additional members of the Board of Directors (the "Preferred Stock Directors"); provided, however, that the election of any such Preferred Stock Directors will not cause the Corporation to violate the corporate governance requirements of NYSE (or any other exchange or automated quotation system on which the Corporation's securities may be listed or quoted) that require
  …[truncated 8,125 chars]

### Turn 5  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this KKR 424B5 prospectus supplement, quote the Use of Proceeds section describing what KKR will do with the net proceeds of the Series D mandatory convertible preferred offering. Also state whether the offering size was described as increased or upsized from an earlier amount, and any earlier launched size. Document: {{final_424b5}}"})
  result: **Use of Proceeds (S-32), verbatim:**
  
  "We estimate that the net proceeds to us from this offering, after deducting underwriting discounts and estimated offering expenses payable by us, will be approximately $2.20 billion (or approximately $2.53 billion if the underwriters exercise their over-allotment option to purchase additional shares of Mandatory Convertible Preferred Stock in full). We intend to use the net proceeds from this offering for the acquisition of additional equity interests in core private equity portfolio companies reported in our Strategic Holdings segment and for other general corporate purposes."
  
  **Upsizing:** The document does not describe the offering as increased or upsized, and it does not mention any earlier launched size. It states the offering as 45,000,000 shares of 6.25% Series D Mandatory Convertible Preferred Stock, with an underwriters' option for up to 6,750,000 additional shares to cover over-allotments. The only size-related language is that option, which is not described as an increase.

### Turn 6  (stop_reason=end_turn)
Summary of the KKR & Co. Inc. 6.25% Series D Mandatory Convertible Preferred Stock offering (March 2025). I confirmed the terms in the final prospectus supplement and the certificate of designations, and I note where a term could not be confirmed.

**Offering size**
- Base offering: 45,000,000 shares at $50.00 per share, or $2,250,000,000 total public offering price.
- Underwriters' option: up to 6,750,000 additional shares to cover over-allotments, exercisable within 30 days of the prospectus supplement. If fully exercised, gross proceeds would be $2,587,500,000. I did not find confirmation that the option was exercised.
- Upsizing: the prior-run notes said the deal was upsized from $1.5 billion. The final prospectus supplement does not describe an upsize or mention an earlier launched size, so I could not confirm this.

**Pricing and closing**
- Pricing: the prospectus supplement is dated March 4, 2025, and the initial price is tied to the March 4, 2025 closing price of KKR common stock. No separate "pricing date" is labelled.
- Closing/settlement: on or about March 7, 2025 (T+2). The certificate of designations also gives March 7, 2025 as the Initial Issue Date.
- Underwriting discount: $1.125 per share, or $50,625,000 in total without the option.
- Net proceeds: $48.875 per share, or $2,199,375,000 before about $2.3 million of expenses. The filing rounds this to approximately $2.20 billion. With the full option, net proceeds are approximately $2.53 billion.

**Price and l
…[truncated 3,729 chars]

### Turn 7  (stop_reason=tool_use)
- submit_final_result({"final_result": "KKR & Co. Inc. 6.25% Series D Mandatory Convertible Preferred Stock (March 2025): key terms\n\nOFFERING SIZE\n- Base offering: 45,000,000 shares at $50.00 per share, or $2,250,000,000 total public offering price (final 424B5 prospectus supplement dated March 4, 2025; filed March 6, 2025).\n- Underwriters' option: up to 6,750,000 additional shares to cover over-allotments, exercisable within 30 days of the prospectus supplement. If fully exercised, gross proceeds would be $2,587,500,000. I did not find confirmation that the option was exercised.\n- Upsizing: prior notes said the deal was upsized from $1.5 billion. The final prospectus supplement does not describe an upsize o
…[truncated 4,564 chars])

### Final answer
KKR & Co. Inc. 6.25% Series D Mandatory Convertible Preferred Stock (March 2025): key terms

OFFERING SIZE
- Base offering: 45,000,000 shares at $50.00 per share, or $2,250,000,000 total public offering price (final 424B5 prospectus supplement dated March 4, 2025; filed March 6, 2025).
- Underwriters' option: up to 6,750,000 additional shares to cover over-allotments, exercisable within 30 days of the prospectus supplement. If fully exercised, gross proceeds would be $2,587,500,000. I did not find confirmation that the option was exercised.
- Upsizing: prior notes said the deal was upsized from $1.5 billion. The final prospectus supplement does not describe an upsize or mention an earlier launched size, so this is unconfirmed.

PRICING AND CLOSING
- Pricing: the prospectus supplement is dated March 4, 2025, and the initial price is tied to the March 4, 2025 closing price of KKR common stock. No separate pricing date is labelled.
- Closing/settlement: on or about March 7, 2025 (T+2). The certificate of designations also gives March 7, 2025 as the Initial Issue Date.
- Underwriting discount: $1.125 per share, or $50,625,000 in total without the option.
- Net proceeds: $48.875 per share, or $2,199,375,000 before about $2.3 million of estimated offering expenses. The filing rounds this to approximately $2.20 billion. With the full option, net proceeds are approximately $2.53 billion.

LIQUIDATION PREFERENCE
- $50.00 per share plus accumulated and unpaid dividends to the liquidation date.

DIVIDEND RIGHTS
- Rate: 6.25% per year on the $50.00 liquidation preference, or $3.125 per share per year ($0.78125 per quarter).
- Payment dates: March 1, June 1, September 1 and December 1, beginning June 1, 2025 and running through March 1, 2028. Regular record dates are February 15, May 15, August 15 and November 15.
- Cumulative: yes. Accumulated dividends do not bear interest.
- Declaration: payable only when, as and if declared. No dividend may be declared on junior stock unless all accumulated Series D dividends have been paid or set aside.
- Form of payment: KKR chooses cash, common stock, or a combination. Stock payments are valued at 97% of the average VWAP over a 5-trading-day period. Shares are capped at the dividend divided by a floor price of $42.2705, subject to anti-dilution adjustment.

CONVERSION TERMS
- Minimum conversion rate: 0.3312 common shares per preferred share, applying when the applicable market value is above the threshold appreciation price of about $150.97 (= $50.00 / 0.3312).
- Maximum conversion rate: 0.4140 common shares per preferred share, applying when the applicable market value is below the initial price of about $120.77 (= $50.00 / 0.4140).
- Between those prices the rate equals $50.00 divided by the applicable market value.
- Share count at the extremes: 45,000,000 x 0.3312 = 14,904,000 shares; 45,000,000 x 0.4140 = 18,630,000 shares.
- Mandatory conversion date: expected to be March 1, 2028. The applicable market value is the average VWAP over a 20-trading-day settlement period.
- Early conversion at holder's option: permitted at any time before March 1, 2028, at the minimum rate of 0.3312, outside the fundamental change period. Holders may receive extra shares if accumulated dividends are unpaid.
- Fundamental change: holders may convert at a rate set by a table that depends on the effective date and the stock price. The rate is 0.4140 at the low end and 0.3312 above $300.00. Holders also receive a make-whole dividend amount.

VOTING RIGHTS
- General: no voting rights except as required by Delaware law or the charter.
- Dividend nonpayment: if dividends are unpaid for six or more dividend periods, the board increases by two and holders elect two directors. Holders of at least 25% can request a special meeting.
- Protective provisions: two-thirds of the outstanding preferred must consent to creating or increasing senior stock, materially adverse amendments to the preferred's rights, or certain mergers or share exchanges.

LISTING
- Proposed NYSE ticker "KKR PR D." The company intends to apply for listing, with trading expected within 30 days of first issuance. Listing has not been confirmed as completed.

USE OF PROCEEDS
- Net proceeds are to be used to acquire additional equity interests in core private equity portfolio companies in the Strategic Holdings segment, and for other general corporate purposes.

SOURCES OPENED
- Final 424B5 prospectus supplement (filed March 6, 2025, dated March 4, 2025).
- Certificate of designations (Exhibit 3.1 to the 8-K filed March 7, 2025).

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm",
            "name": "KKR & Co. Inc. Prospectus Supplement (Form 424B5) for 6.25% Series D Mandatory Convertible Preferred Stock"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1404912/000114036125007608/ny20042797x5_ex3-1.htm",
            "name": "KKR & Co. Inc. Certificate of Designations for Series D Mandatory Convertible Preferred Stock (Exhibit 3.1 to Form 8-K filed March 7, 2025)"
        }
    ]
}