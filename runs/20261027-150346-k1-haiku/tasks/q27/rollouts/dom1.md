## Rollout `dom1`
- outcome: submitted
- turns: 6; cost: $0.192; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "debt_instrument_terms"})
  result: ---
  name: debt_instrument_terms
  description: Report the terms of a named debt or hybrid security (junior subordinated debentures, subordinated notes, preferred) from a company's 10-K debt note, with each term tied to opened text.
  ---
  ANALYTIC MOVE: trace and classify. The input is a named instrument and a fiscal year. The result is a term sheet for that instrument only, read from the filing's own words.
  
  1. Where the terms live. In a 10-K, the governing text is the debt note in the financial statements (often titled "Capital Structure" or "Debt"). It has a table of principal, rate and maturity by instrument, followed by narrative on call, interest deferral and covenants. MD&A "Capital Resources" and Item 5 or the exhibit index give corroboration. Open the filing itself. A snippet or a prior-year filing is not enough. Terms can change between years, for example a LIBOR replacement.
  2. Keep look-alike instruments apart. "Junior subordinated debentures" are different from "subordinated debentures", "senior notes" and preferred stock. Each has its own principal, rate and maturity. Name the instrument exactly as the table does. If the filing has several lines, report only the one asked about, and note the others in one line.
  3. Term checklist, each tied to the opened text and flagged "not stated" if absent:
     - issuer, series name and the principal outstanding at fiscal year-end, with the prior year for comparison, in the filing's units;
     - coupon, fixed or floating, any switch date, and the floating benchmark plus spread. Check for a LIBOR-to-SOFR fallback and the spread adjustment;
     - scheduled maturity versus final maturity;
     - optional redemption: dates, price and any make-whole;
     - interest deferral: maximum length, compounding, any obligation to issue stock, a
  …[truncated 1,472 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/899051/000089905125000015/all-20241231.htm", "key": "all10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: all10k. (817,347 characters)
  The data_storage currently contains the following keys:
  all10k
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Allstate 10-K text, find all text about the Junior Subordinated Debentures (Series A 6.500% Fixed-to-Floating Rate Junior Subordinated Debentures due 2067). Report: principal outstanding at Dec 31, 2024 and 2023; coupon and reset terms; benchmark and spread adjustment; scheduled maturity and final maturity dates; optional redemption dates and price/make-whole; interest deferral length, compounding, restrictions during deferral; ranking. Also note the separate floating rate subordinated debentures due 2053 in one line. Quote exact dates and the section name. Say 'not stated' where absent. Text: {{all10k}}"})
  result: ## Series A 6.500% Fixed-to-Floating Rate Junior Subordinated Debentures due 2067
  
  | Item | What the filing says | Source section |
  |---|---|---|
  | **Principal outstanding** | $500 million at Dec 31, 2024 and $500 million at Dec 31, 2023 | Note 14, "Total debt outstanding" table ("6.500% Junior Subordinated Debentures, due 2067") |
  | **Coupon (fixed period)** | 6.500% fixed annual rate, payable semi-annually, through May 15, 2037 | Note 14, "Junior Subordinated Debentures" |
  | **Reset / floating terms** | After May 15, 2037, interest is payable quarterly at "an annual rate equal to the three-month LIBOR plus 2.120%, which was replaced with the CME Term SOFR Reference Rate published for a three-month tenor plus a spread adjustment of 0.26161%" | Note 14 |
  | **Benchmark** | Originally three-month LIBOR; now three-month CME Term SOFR Reference Rate | Note 14 |
  | **Spread / spread adjustment** | 2.120% spread over the benchmark; 0.26161% spread adjustment | Note 14 |
  | **Scheduled maturity** | "May 15, 2057" | Note 14 |
  | **Final maturity** | "May 15, 2067" | Note 14 |
  | **Optional redemption** | (i) "in whole or in part, at any time on or after May 15, 2037 at the principal amount plus accrued and unpaid interest to the date of redemption"; (ii) "in certain circumstances, in whole or in part, prior to May 15, 2037 at the principal amount plus accrued and unpaid interest to the date of redemption or, if greater, a make-whole price" | Note 14 |
  | **Make-whole** | Applies only prior to May 15, 2037, in the "certain circumstances" described; the make-whole formula and the triggering circumstances are not stated | Note 14 |
  | **Interest deferral length** | Company may defer for "one or more consecutive interest periods that do not exceed 10 years" | Note 14 |
  | **Compounding du
  …[truncated 2,780 chars]

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "Quote exactly the sentences describing the Junior Subordinated Debentures due 2067: the reset rate after May 15, 2037 (benchmark, spread adjustment, spread), the scheduled and final maturity dates, the redemption terms, and the deferral terms. Also quote the total debt table rows for Junior Subordinated Debentures and Subordinated Debentures due 2053 with amounts at Dec 31, 2024 and 2023. Text: {{all10k}}", "input_character_ranges": [{"key": "all10k", "start": 600000, "end": 817347}]})
  result: **Junior Subordinated Debentures due 2067: sentences from Note 14, Capital Structure**
  
  *Reset rate after May 15, 2037:*
  "Interest on the Junior Subordinated Debentures is payable semi-annually at the stated fixed annual rate to May 15, 2037, and then payable quarterly at an annual rate equal to the three-month LIBOR plus 2.120%, which was replaced with the CME Term SOFR Reference Rate published for a three-month tenor plus a spread adjustment of 0.26161%."
  
  *Scheduled and final maturity dates:*
  "The scheduled maturity date for the Debentures is May 15, 2057 with a final maturity date of May 15, 2067."
  
  *Redemption terms:*
  "The Junior Subordinated Debentures may be redeemed (i) in whole or in part, at any time on or after May 15, 2037 at the principal amount plus accrued and unpaid interest to the date of redemption, or (ii) in certain circumstances, in whole or in part, prior to May 15, 2037 at the principal amount plus accrued and unpaid interest to the date of redemption or, if greater, a make-whole price."
  
  *Deferral terms:*
  "The Company may elect at one or more times to defer payment of interest on the Junior Subordinated Debentures for one or more consecutive interest periods that do not exceed 10 years. Interest compounds during such deferral periods at the rate in effect for each period. The interest deferral feature obligates the Company in certain circumstances to issue common stock or certain other types of securities if it cannot otherwise raise sufficient funds to make the required interest payments. The Company has reserved 75 million shares of its authorized and unissued common stock to satisfy this obligation."
  
  "The terms of the Subordinated Debentures and Junior Subordinated Debentures prohibit the Company from declaring or paying any dividends or dist
  …[truncated 1,100 chars]

### Turn 5  (stop_reason=tool_use)
- retrieve_information({"prompt": "Quote exactly any sentences about a replacement capital covenant for the Junior Subordinated Debentures or Subordinated Debentures due 2053 in Note 14 (Capital Structure), and any sentence stating the ranking or seniority of the Junior Subordinated Debentures. Say 'not stated' if absent. Text: {{all10k}}", "input_character_ranges": [{"key": "all10k", "start": 600000, "end": 817347}]})
  result: **Replacement capital covenant sentences (Note 14):**
  
  1. "In connection with the issuance of the Junior Subordinated Debentures, the Company entered into a replacement capital covenant (“RCC”)."
  2. "This covenant was not intended for the benefit of the holders of the Junior Subordinated Debentures and could not be enforced by them."
  3. "Rather, it was for the benefit of holders of one or more other designated series of the Company’s indebtedness (“covered debt”), currently the $800 million Floating Rate Subordinated Debentures due in 2053."
  4. "Pursuant to the RCC, the Company has agreed that it will not repay, redeem, or purchase the Junior Subordinated Debentures on or before May 15, 2067 (or such earlier date on which the RCC terminates by its terms) unless, subject to certain limitations, the Company has received net cash proceeds in specified amounts from the sale of common stock or certain other qualifying securities."
  5. "The promises and covenants contained in the RCC will not apply if (i) S&P upgrades the Company’s issuer credit rating to A or above, (ii) the Company redeems the Junior Subordinated Debentures due to a tax event, (iii) after notice of redemption has been given by the Company and a market disruption event occurs preventing the Company from raising proceeds in accordance with the RCC, or (iv) the Company repurchases or redeems up to 10% of the outstanding principal of the Junior Subordinated Debentures in any one-year period, provided that no more than 25% will be so repurchased, redeemed or purchased in any ten-year period."
  6. "The RCC terminates in 2067."
  7. "The RCC will terminate prior to its scheduled termination date if (i) the Junior Subordinated Debentures are no longer outstanding and the Company has fulfilled its obligations under the 
  …[truncated 826 chars]

### Turn 6  (stop_reason=tool_use)
- submit_final_result({"final_result": "Allstate's Junior Subordinated Debentures are the Series A 6.500% Fixed-to-Floating Rate Junior Subordinated Debentures due 2067, with $500 million principal outstanding at December 31, 2024 (and $500 million at December 31, 2023). They pay 6.500% fixed until May 15, 2037, then float at three-month CME Term SOFR plus a 0.26161% spread adjustment plus 2.120%.\n\nTerm list (all from the FY2024 Form 10-K, Note 14 \"Capital Structure\" unless noted):\n\n1. Principal outstanding: $500 million at Dec 31, 2024 and $500 million at Dec 31, 2023, per the \"Total debt outstanding\" table (\"6.500% Junior Subordinated Debentures, due 2067\").\n2. Fixed coupon: 6.500% annual rate, paid 
…[truncated 3,316 chars])

### Final answer
Allstate's Junior Subordinated Debentures are the Series A 6.500% Fixed-to-Floating Rate Junior Subordinated Debentures due 2067, with $500 million principal outstanding at December 31, 2024 (and $500 million at December 31, 2023). They pay 6.500% fixed until May 15, 2037, then float at three-month CME Term SOFR plus a 0.26161% spread adjustment plus 2.120%.

Term list (all from the FY2024 Form 10-K, Note 14 "Capital Structure" unless noted):

1. Principal outstanding: $500 million at Dec 31, 2024 and $500 million at Dec 31, 2023, per the "Total debt outstanding" table ("6.500% Junior Subordinated Debentures, due 2067").
2. Fixed coupon: 6.500% annual rate, paid semi-annually through May 15, 2037.
3. Floating coupon: from May 15, 2037, interest is paid quarterly at three-month LIBOR plus 2.120%, which was replaced with the three-month CME Term SOFR Reference Rate plus a 0.26161% spread adjustment. So the post-2037 rate is three-month CME Term SOFR + 0.26161% + 2.120%. This is the LIBOR-to-SOFR fallback. The filing does not state the quarterly reset dates.
4. Scheduled maturity: May 15, 2057. Final maturity: May 15, 2067.
5. Optional redemption: (i) in whole or in part, at any time on or after May 15, 2037, at par (principal plus accrued and unpaid interest); (ii) in certain circumstances, in whole or in part, before May 15, 2037, at the greater of par or a make-whole price. The make-whole formula and the triggering circumstances are not stated.
6. Interest deferral: the company may defer interest for one or more consecutive interest periods not exceeding 10 years. Deferred interest compounds at the rate in effect for each period. The company may in certain circumstances have to issue common stock or other qualifying securities if it cannot otherwise raise the funds; 75 million shares are reserved for this.
7. Deferral restrictions: while interest is deferred, the company may not declare or pay dividends or distributions on common or preferred stock, or redeem, purchase, acquire or make liquidation payments on common or preferred stock, subject to certain limited exceptions. The MD&A "Capital Resources and Liquidity" section states that no interest was deferred on the subordinated debentures in 2024.
8. Replacement capital covenant (RCC): the company agreed not to repay, redeem or purchase the debentures on or before May 15, 2067, unless it receives specified net cash proceeds from common stock or other qualifying securities, subject to limits. The covenant benefits holders of the $800 million Floating Rate Subordinated Debentures due 2053 (the "covered debt"), not the Junior Subordinated Debenture holders, who cannot enforce it. Exceptions include an S&P upgrade to A or above, a redemption due to a tax event, a market disruption event after notice of redemption, and repurchases or redemptions of up to 10% of principal in any one-year period (no more than 25% in any ten-year period). The RCC terminates in 2067, or earlier under the conditions listed in the note.
9. Ranking: the filing does not state the debentures' ranking against senior or other subordinated debt beyond the "junior subordinated" designation.

Related instrument (not the subject of the question): the Floating Rate Subordinated Debentures due 2053 are separate. $500 million and $800 million tranches were outstanding at both year-ends. They became floating rate in 2023. The cover page lists the 5.100% Fixed-to-Floating Rate Subordinated Debentures due 2053 on the NYSE.

Note on sourcing: the 10-K text was long, so I read it in two parts. The Note 14 terms above were confirmed directly in the retrieved text.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/899051/000089905125000015/all-20241231.htm",
            "name": "Allstate Corporation Form 10-K for fiscal year 2024 (Note 14 Capital Structure; MD&A Capital Resources and Liquidity; Item 1A)"
        }
    ]
}