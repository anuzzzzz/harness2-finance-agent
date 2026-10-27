## Rollout `ctl3`
- outcome: submitted
- turns: 4; cost: $0.130; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Zillow acquisitions 2023 2024 strategy") → 9 results: ZILLOW GROUP, INC. - Form 10-K - FY2024 (Annual Financial Statement Tables - full year 2024) <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/Financial_Report.xlsx>; ZILLOW GROUP, INC. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000094/z-20240630.htm>; ZILLOW GROUP, INC. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000070/z-20240331.htm>; ZILLOW GROUP, INC. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000126/z-20240930.htm>; ZILLOW GROUP, INC. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm>
- web_search(query="Zillow 2024 annual report revenue mix IMT Mortgages Homes segment") → 10 results: ZILLOW GROUP, INC. - Form 10-K - FY2024 (Annual Financial Statement Tables - full year 2024) <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/Financial_Report.xlsx>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000069/exhibit993.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000125/exhibit993.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000095/exhibit993.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000069/q12024991.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "key": "zg10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: zg10k. (467,105 characters)
  The data_storage currently contains the following keys:
  zg10k
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow 10-K for FY2024: {{zg10k}} Extract verbatim-short facts about (1) acquisitions made in 2023 and 2024 (Aryeo, Spruce, Follow Up Boss, any others, dates, consideration), (2) the company's stated strategy for acquisitions/software integration/\"housing super app\"/financing, (3) revenue by category and percentage of total for 2024, 2023, 2022 (Residential, Mortgages, Rentals, Other), and (4) any statements about mortgage marketplace or Zillow Home Loans strategy shift. Include the section text where possible."})
  result: # Zillow Group FY2024 10-K: Extracts
  
  ## 1. Acquisitions (2023–2024)
  
  **Aryeo (July 31, 2023)** (Note 6)
  > "On July 31, 2023, Zillow Group acquired Aryeo, a software company that serves real estate photographers, in exchange for approximately $15 million in cash, net of cash acquired, and 380,259 shares of our Class C capital stock with a value of $20 million, for total consideration of $35 million, net of cash acquired."
  
  **Spruce (September 11, 2023)** (Note 6)
  > "On September 11, 2023, Zillow Group acquired substantially all of the assets and liabilities of Spruce, a tech-enabled title and escrow platform, in exchange for approximately $19 million in cash, net of cash acquired."
  
  **Follow Up Boss (December 8, 2023)** (Note 6)
  > "On December 8, 2023, Zillow Group acquired Follow Up Boss, a customer relationship management system for real estate professionals, for $399 million in cash, net of cash acquired, and contingent consideration of up to $100 million in cash, payable over a three-year period upon achievement of certain performance metrics."
  - Expected first earn-out payment: "an expected payment of $33 million in February 2025" (MD&A, Contractual Obligations).
  
  **Other acquisitions**
  - Virtual Staging AI Inc., October 2024 (Risk Factors: "Virtual Staging AI Inc. in October 2024"). No consideration is disclosed in the document.
  - VRX Media Group LLC, December 2022 (Risk Factors). Outside the requested period.
  
  **Subsequent event (not an acquisition):** Redfin rentals partnership, February 6, 2025 (Note 19): "Zillow will make a $100 million upfront payment to Redfin and will pay Redfin for leads generated through the Redfin Rental Network..."
  
  ## 2. Stated Strategy
  
  **Overall / "housing super app"** (Item 1)
  > "We are reimagining residential real estate to make ho
  …[truncated 2,436 chars]

### Turn 3  (stop_reason=end_turn)
<br>

**Short answer:** Over 2023–2024, Zillow's acquisitions were small, software-focused bolt-ons plus one large customer-software purchase (Follow Up Boss). They were aimed at its agent-facing and transaction-service businesses. Over the same period, the revenue mix shifted toward Rentals and away from Residential, so the deals fit a broader push to become an end-to-end "housing super app," although the acquisitions themselves were too small to drive the mix change, which came mostly from organic growth.

**1. Acquisition strategy (2023–2024)**

- **Aryeo (July 2023):** A software company serving real estate photographers. Total consideration was $35 million, net of cash acquired, including roughly $15 million in cash and shares worth about $20 million. 
On July 31, 2023, we acquired Aryeo, Inc. ("Aryeo"), a software company that serves real estate photographers, in exchange for total consideration of $35 million, net of cash acquired.

- **Spruce (September 2023):** A tech-enabled title and escrow platform. 
On September 11, 2023, we acquired substantially all of the assets and liabilities of Spruce Holdings, Inc. and certain affiliated entities (collectively referred to as "Spruce"), a tech-enabled title and escrow platform, in exchange for total consideration of $19 million, net of cash acquired.
 This moved Zillow into the transaction-services layer beyond advertising.
- **Follow Up Boss (December 2023):** The largest deal, a customer relationship management system for
…[truncated 5,603 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Short answer:** Over 2023–2024, Zillow's acquisitions were small, software-focused deals plus one large customer-software purchase (Follow Up Boss). They target agent-facing tools and transaction services. Over the same period, revenue shifted toward Rentals and away from Residential. The deals fit the broader goal of becoming an end-to-end \"housing super app,\" but organic growth, not acquisitions, drove most of the mix change.\n\n**1. Acquisition strategy (2023–2024)**\n\n- **Aryeo (July 2023):** A software company serving real estate photographers. <cite index=\"9-1\">On July 31, 2023, we acquired Aryeo, Inc. (\"Aryeo\"), a software company that serves real estate pho
…[truncated 5,329 chars])

### Final answer
**Short answer:** Over 2023–2024, Zillow's acquisitions were small, software-focused deals plus one large customer-software purchase (Follow Up Boss). They target agent-facing tools and transaction services. Over the same period, revenue shifted toward Rentals and away from Residential. The deals fit the broader goal of becoming an end-to-end "housing super app," but organic growth, not acquisitions, drove most of the mix change.

**1. Acquisition strategy (2023–2024)**

- **Aryeo (July 2023):** A software company serving real estate photographers. <cite index="9-1">On July 31, 2023, we acquired Aryeo, Inc. ("Aryeo"), a software company that serves real estate photographers, in exchange for total consideration of $35 million, net of cash acquired.</cite>
- **Spruce (September 2023):** A tech-enabled title and escrow platform, <cite index="9-2">in exchange for total consideration of $19 million, net of cash acquired.</cite> This extends Zillow into transaction services beyond advertising.
- **Follow Up Boss (December 2023):** The largest deal, a CRM for real estate agents. <cite index="1-1">On December 8, 2023, Zillow Group acquired Follow Up Boss, a customer relationship management system for real estate professionals, for $399 million in cash, net of cash acquired, and contingent consideration of up to $100 million in cash, payable over a three-year period upon achievement of certain performance metrics.</cite> Management tied the deal to <cite index="1-3">a more integrated software experience for our customers.</cite> The total purchase price was $484 million, including $81 million of contingent consideration at fair value, with about $402 million allocated to goodwill.
- **Virtual Staging AI (October 2024):** A small tuck-in. The FY2024 10-K does not disclose its consideration.

Combined purchase-price value for Aryeo, Spruce and Follow Up Boss was about $538 million ($35M + $19M + $484M). Upfront cash was about $453 million ($15M + $19M + $399M), plus up to $100 million in contingent payments. The FY2024 10-K also notes an expected $33 million Follow Up Boss earn-out payment in February 2025.

**2. Revenue mix (continuing operations, FY2024 10-K)**

| Category | 2022 ($M / share) | 2023 ($M / share) | 2024 ($M / share) |
|---|---|---|---|
| Residential | 1,522 / 77.73% | 1,452 / 74.65% | 1,594 / 71.28% |
| Mortgages | 119 / 6.08% | 96 / 4.94% | 145 / 6.48% |
| Rentals | 274 / 13.99% | 357 / 18.35% | 453 / 20.26% |
| Other | 43 / 2.20% | 40 / 2.06% | 44 / 1.97% |
| Total | 1,958 | 1,945 | 2,236 |

Shares are category revenue divided by total revenue. Growth rates in 2024 were: total revenue about 14.96%, Residential about 9.78%, Rentals about 26.89%, and Mortgages about 51.04%.

Mortgage growth came with a strategic change. Zillow reported that <cite index="13-9">the year-over-year increase in mortgage origination revenue was partially offset by a decrease in mortgage marketplace revenue driven by a shift in strategic priority as we focus on organic growth of our mortgage origination business.</cite> In Q3 2024, it attributed growth to <cite index="12-11">our ongoing strategy to provide more customers with our integrated financing experience</cite>.

**3. How this aligns with the revenue mix**

- **Rentals is the fastest-growing line, driven mainly by organic marketplace growth.** Its share rose from about 14% in 2022 to about 20% in 2024. Zillow's rentals results were driven by multifamily advertising growth, not by acquisitions.
- **Residential remains the core, and the software deals support it.** Its share fell from about 78% to about 71%. Follow Up Boss and related software are meant to deepen agent relationships and conversion within Residential, which is consistent with the stated goal of capturing more of each transaction.
- **Mortgages and title/escrow are being built as integrated services.** Spruce and the financing push add transaction-services revenue, but Mortgages is still only about 6% of revenue, so these bets are early.
- **Scale:** The Follow Up Boss purchase price of $484 million equals about 24.88% of 2023 total revenue ($1,945 million). The $399 million cash payment alone equals about 20.51%. Relative to the revenue base, the acquisitions were meaningful for software capabilities but not large enough to reshape the mix on their own.

**Caveats**
- The FY2024 10-K was filed after December 2024. I used its year-end figures as the best available data for "as of December 2024." Post-period events are excluded from the analysis, except to note that the 10-K describes a February 6, 2025 Redfin rentals arrangement with a $100 million upfront payment, which suggests rentals remains a priority.
- Percentages and growth rates are my calculations from reported figures, rounded to two decimals. The revenue table is drawn from the 10-K's disaggregation of revenue.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm",
            "name": "Zillow Group FY2024 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/Financial_Report.xlsx",
            "name": "Zillow Group FY2024 10-K Financial Report (Acquisitions and Revenue tables)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000110/z-20230930.htm",
            "name": "Zillow Group Q3 2023 Form 10-Q"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000125/exhibit993.htm",
            "name": "Zillow Group Q3 2024 Shareholder Letter (8-K Exhibit 99.3)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000095/exhibit993.htm",
            "name": "Zillow Group Q2 2024 Shareholder Letter (8-K Exhibit 99.3)"
        }
    ]
}