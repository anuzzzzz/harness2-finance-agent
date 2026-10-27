## Rollout `static1`
- outcome: submitted
- turns: 4; cost: $0.180; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Allstate junior subordinated debentures terms interest rate maturity", "ciks": ["ALL"], "start_date": "2025-01-01", "end_date": "2025-04-07", "form_types": ["10-K"]})
  result: {"total_matching_documents": 1, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-24", "period_ending": "2024-12-31", "company": "ALLSTATE CORP  (ALL, ALL-PB, ALL-PH, ALL-PI, ALL-PJ)  (CIK 0000899051)", "ciks": ["0000899051"], "accession": "0000899051-25-000015", "document": "all-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/899051/000089905125000015/all-20241231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/899051/000089905125000015/all-20241231.htm", "key": "all10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: all10k. (817,347 characters)
  The data_storage currently contains the following keys:
  all10k
  
- retrieve_information({"prompt": "From this Allstate 10-K, find all information about Junior Subordinated Debentures: principal amounts, interest rates (fixed/floating, reset terms), issue dates, maturity dates, redemption terms, call dates, and any deferral features. Quote the relevant figures. Document: {{all10k}}"})
  result: # Junior Subordinated Debentures: Allstate Corporation 2024 Form 10-K
  
  The filing describes one series of junior subordinated debentures: the **Series A 6.500% Fixed-to-Floating Rate Junior Subordinated Debentures due 2067**. The principal terms are in Note 14 (Capital Structure) and the debt table in the same note.
  
  ## Key Terms
  
  | Term | Disclosure in the 10-K |
  |---|---|
  | **Series** | "Series A 6.500% Fixed-to-Floating Rate Junior Subordinated Debentures" |
  | **Principal amount** | "$500 million," shown as "6.500% Junior Subordinated Debentures, due 2067" with $500 million outstanding at both December 31, 2024 and December 31, 2023 |
  | **Issue date** | Not stated in the filing |
  | **Scheduled maturity** | "May 15, 2057" |
  | **Final maturity** | "May 15, 2067" |
  | **Fixed rate period** | 6.500%, "payable semi-annually at the stated fixed annual rate to May 15, 2037" |
  | **Floating rate period** | "payable quarterly at an annual rate equal to the three-month LIBOR plus 2.120%, which was replaced with the CME Term SOFR Reference Rate published for a three-month tenor plus a spread adjustment of 0.26161%" |
  | **Optional redemption** | "in whole or in part, at any time on or after May 15, 2037 at the principal amount plus accrued and unpaid interest to the date of redemption" |
  | **Pre-call redemption** | "in certain circumstances, in whole or in part, prior to May 15, 2037 at the principal amount plus accrued and unpaid interest to the date of redemption or, if greater, a make-whole price" |
  | **Deferral right** | The Company "may elect at one or more times to defer payment of interest… for one or more consecutive interest periods that do not exceed 10 years" |
  | **Compounding** | "Interest compounds during such deferral periods at the rate in effect for each period" |
  
  …[truncated 3,533 chars]

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "Search this Allstate 10-K text for \"Junior Subordinated\" and \"6.125\" and report every passage mentioning them, including the debt table in Note 14 (Capital Structure) with outstanding amounts and any issue dates, and whether any 6.125% junior debentures remain outstanding at Dec 31, 2024. Document: {{all10k}}", "input_character_ranges": [{"key": "all10k", "start": 600000, "end": 817000}]})
  result: ## Search results
  
  **"Junior Subordinated"** appears in Note 14 (Capital Structure) in the debt table and in the narrative that follows it. It does not appear elsewhere in the document.
  
  **"6.125"** appears once, in the Note 14 debt table. It refers to a senior note, not a junior debenture.
  
  ## Note 14 debt table (Total debt outstanding, as of December 31, $ in millions)
  
  | Instrument | 2024 | 2023 |
  |---|---|---|
  | 6.125% Senior Notes, due 2032 (1) | $159 | $159 |
  | 6.500% Junior Subordinated Debentures, due 2067 | $500 | $500 |
  
  The table includes the full debt schedule, from which these two rows are taken:
  - Long-term debt total principal: $8,141 (2024), $7,991 (2023)
  - Total long-term debt: $8,085 (2024), $7,942 (2023)
  - Total debt: $8,085 (2024), $7,942 (2023)
  
  The table gives no issue dates. The only issue date stated in Note 14 is for the 5.05% Senior Notes, issued June 24, 2024.
  
  ## Narrative passages mentioning Junior Subordinated Debentures
  
  1. **Outstanding amount and terms:** "As of December 31, 2024, the Company had outstanding $500 million of Series A 6.500% Fixed-to-Floating Rate Junior Subordinated Debentures ('Junior Subordinated Debentures'). The scheduled maturity date for the Debentures is May 15, 2057 with a final maturity date of May 15, 2067. The Junior Subordinated Debentures may be redeemed (i) in whole or in part, at any time on or after May 15, 2037 at the principal amount plus accrued and unpaid interest to the date of redemption, or (ii) in certain circumstances, in whole or in part, prior to May 15, 2037 at the principal amount plus accrued and unpaid interest to the date of redemption or, if greater, a make-whole price."
  
  2. **Interest:** "Interest on the Junior Subordinated Debentures is payable semi-annually at the stated fixed annual ra
  …[truncated 2,811 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "As of December 31, 2024 (FY2024), Allstate's only junior subordinated debt was a single series of junior subordinated debentures, the Series A 6.500% Fixed-to-Floating Rate Junior Subordinated Debentures due 2067. Terms, per the 2024 Form 10-K (Note 14, Capital Structure):\n\n- **Principal outstanding:** $500 million at both December 31, 2024 and December 31, 2023 (debt table in $ millions: $500 for 2024 and 2023).\n- **Coupon – fixed period:** 6.500% per year, paid semi-annually, through May 15, 2037.\n- **Coupon – floating period:** after May 15, 2037, paid quarterly at three-month LIBOR plus 2.120%. That LIBOR reference was replaced by CME Term SOFR (three-month tenor) p
…[truncated 2,454 chars])

### Final answer
As of December 31, 2024 (FY2024), Allstate's only junior subordinated debt was a single series of junior subordinated debentures, the Series A 6.500% Fixed-to-Floating Rate Junior Subordinated Debentures due 2067. Terms, per the 2024 Form 10-K (Note 14, Capital Structure):

- **Principal outstanding:** $500 million at both December 31, 2024 and December 31, 2023 (debt table in $ millions: $500 for 2024 and 2023).
- **Coupon – fixed period:** 6.500% per year, paid semi-annually, through May 15, 2037.
- **Coupon – floating period:** after May 15, 2037, paid quarterly at three-month LIBOR plus 2.120%. That LIBOR reference was replaced by CME Term SOFR (three-month tenor) plus a 0.26161% spread adjustment. The all-in floating formula is not written out in the filing; the reading of Term SOFR + 2.120% + 0.26161% is my inference.
- **Maturity:** scheduled maturity May 15, 2057; final maturity May 15, 2067.
- **Optional redemption:** callable in whole or part at any time on or after May 15, 2037, at principal plus accrued and unpaid interest.
- **Pre-2037 redemption:** only in certain circumstances, in whole or part, at principal plus accrued interest or, if greater, a make-whole price.
- **Interest deferral:** Allstate may defer interest for one or more consecutive periods not exceeding 10 years; deferred interest compounds at the applicable rate. Deferral can oblige Allstate, in certain circumstances, to issue common stock or other qualifying securities if it cannot otherwise raise the funds, and it has reserved 75 million authorized but unissued common shares for this. No interest was deferred in 2024.
- **Restrictions while deferring:** dividends/distributions on common or preferred stock and repurchases or liquidation payments on those stocks are prohibited while interest is deferred (limited exceptions apply).
- **Replacement capital covenant:** Allstate agreed not to repay, redeem or purchase the debentures on or before May 15, 2067, except under limited conditions involving net proceeds from qualifying equity-type issuances. The covenant benefits holders of the $800 million Floating Rate Subordinated Debentures due 2053 (the "covered debt") and not the debenture holders themselves. It does not apply in listed circumstances (e.g., an S&P upgrade to A or higher, a tax-event redemption, a market disruption, or limited annual/ten-year repurchase allowances) and terminates in 2067 or earlier under listed conditions.
- **Rating treatment:** rating agencies give the debentures partial equity credit, reflecting the deferral feature.

Not disclosed: the issue date. The 10-K XBRL includes a 6.125% junior debenture member label, but the narrative and debt table show no 6.125% junior debentures outstanding; the 6.125% instrument in the debt table is a $159 million Senior Note due 2032.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/899051/000089905125000015/all-20241231.htm",
            "name": "Allstate Corporation Form 10-K for fiscal year ended December 31, 2024 (filed 2025-02-24)"
        }
    ]
}