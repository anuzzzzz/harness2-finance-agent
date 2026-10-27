## Rollout `agg1`
- outcome: submitted
- turns: 4; cost: $0.306; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "acquisition_strategy_vs_revenue_mix"})
  result: ---
  name: acquisition_strategy_vs_revenue_mix
  description: Explain a company's recent M&A pattern and test whether it lines up with the shift in its revenue mix, using the acquisitions note, cash-flow statement and the revenue-by-category table.
  ---
  ANALYTIC MOVE: trace and compare. List the deals made in the window. Quantify the spend. Map each deal to a revenue line. Then check whether the mix shift came from the deals or from organic growth.
  
  1. Window. Fix the question's window (for example "past 2 years as of Dec 2024" means Dec 2022 to Dec 2024). Say which deals fall outside it, and label post-window events as later developments. Do not call a deal "recent" on memory alone.
  2. Deal list from the controlling sources:
     - the 10-K acquisitions note (target, close date, cash paid net of cash acquired, contingent consideration, goodwill and intangibles);
     - the cash-flow line "cash paid for acquisitions, net" for each year;
     - the risk-factor or Item 1 text, which often names small deals that have no note;
     - the prior-year 10-K (for deals closed early in the window and for the stated rationale) and any 10-Qs or 8-Ks for anything the latest 10-K omits.
     For each deal give the date, price (cash plus contingent, using the filing's wording) and what the target does. If the text and the allocation table disagree (net versus gross of cash acquired, or two filings giving different goodwill), show both numbers and flag it. If the price is undisclosed, say so; do not guess.
  3. Intensity. Compare each year's net cash paid with total revenue. Show which single deal dominates (deal cash / year's net acquisition cash). A year with near-zero spend is a pause, so say that.
  4. Revenue mix. From the 10-K MD&A and Results of Operations table, retrieve revenue by category for 
  …[truncated 2,885 chars]
- edgar_search({"search_query": "Zillow acquisitions annual report 10-K", "ciks": ["Z"], "start_date": "2025-01-01", "end_date": "2025-04-07", "form_types": ["10-K"]})
  result: {"total_matching_documents": 1, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-11", "period_ending": "2024-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-25-000016", "document": "z-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "key": "fy2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2024. (467,105 characters)
  The data_storage currently contains the following keys:
  fy2024
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm", "key": "fy2023"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2023. (503,493 characters)
  The data_storage currently contains the following keys:
  fy2024
  fy2023
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow 10-K text, find the Acquisitions note: list each acquisition with close date, consideration (cash paid, net of cash acquired, contingent consideration), and what the target does. Also quote the sentence on Follow Up Boss, Aryeo, Spruce, and any mention of Virtual Staging AI or VRX. Text: {{fy2024}}"})
  result: ## Acquisitions (Note 6), Zillow Group FY2024 10-K
  
  | Target | Close date | Cash consideration (net of cash acquired) | Contingent consideration | Target business |
  |---|---|---|---|---|
  | **Follow Up Boss** (Enchant, LLC, d/b/a) | Dec 8, 2023 | $399M (gross cash $403M in the allocation table) | Up to $100M cash over three years, tied to performance metrics. Fair value at acquisition was $81M. At 12/31/24 the liability was $91M ($33M current, $58M long-term). | CRM system for real estate professionals |
  | **Aryeo, Inc.** | Jul 31, 2023 | ~$15M, plus 380,259 Class C shares valued at $20M | None disclosed | Software company serving real estate photographers |
  | **Spruce Holdings, Inc.** (substantially all assets and liabilities) | Sep 11, 2023 | ~$19M | None disclosed | Tech-enabled title and escrow platform |
  
  **Discrepancies in the filing:**
  - Aryeo: the text says "total consideration of $35 million, net of cash acquired," but the purchase price allocation totals $38M.
  - Spruce: the text says ~$19M cash, but the allocation totals $24M.
  - The filing does not reconcile these differences.
  
  **Quoted sentences:**
  
  - **Follow Up Boss:** "On December 8, 2023, Zillow Group acquired Follow Up Boss, a customer relationship management system for real estate professionals, for $399 million in cash, net of cash acquired, and contingent consideration of up to $100 million in cash, payable over a three-year period upon achievement of certain performance metrics."
  
  - **Aryeo:** "On July 31, 2023, Zillow Group acquired Aryeo, a software company that serves real estate photographers, in exchange for approximately $15 million in cash, net of cash acquired, and 380,259 shares of our Class C capital stock with a value of $20 million, for total consideration of $35 million, net of cash acqui
  …[truncated 886 chars]
- retrieve_information({"prompt": "From this Zillow 10-K text, find the revenue by category table in the Results of Operations / MD&A for 2024, 2023 and 2022: Residential, Mortgages, Rentals, Other, Total revenue, with dollar amounts, percent of total, and the MD&A explanation of Residential growth (including any mention of Follow Up Boss revenue inclusion) and of Mortgages and Rentals growth. Text: {{fy2024}}"})
  result: ## Revenue by Category (in millions, except percentages)
  
  | Category | 2024 | % of Total | 2023 | % of Total | 2022 | % of Total |
  |---|---|---|---|---|---|---|
  | **For Sale revenue:** | | | | | | |
  | Residential | $1,594 | 71% | $1,452 | 75% | $1,522 | 78% |
  | Mortgages | 145 | 6% | 96 | 5% | 119 | 6% |
  | **Total For Sale revenue** | **1,739** | **78%** | **1,548** | **80%** | **1,641** | **84%** |
  | Rentals | 453 | 20% | 357 | 18% | 274 | 14% |
  | Other | 44 | 2% | 40 | 2% | 43 | 2% |
  | **Total revenue** | **$2,236** | **100%** | **$1,945** | **100%** | **$1,958** | **100%** |
  
  **2024 vs. 2023 change:** Residential +$142M (+10%); Mortgages +$49M (+51%); Rentals +$96M (+27%); Other +$4M (+10%); Total +$291M (+15%).
  
  The 2024 and 2023 figures and percentages come from the MD&A table. The 2022 figures come from the Consolidated Statements of Operations and Note 17. The 2022 percentages are my calculations. This 10-K does not include a 2023 vs. 2022 MD&A discussion; it refers readers to the prior year's 10-K.
  
  ## MD&A Explanations
  
  **Residential (+$142M, +10%)**
  - Residential revenue per visit rose 6% to $0.171 (the filing's text reads "from $0.162 for the year ended December 31, 2024," which is a typo; the comparison period is 2023).
  - Drivers cited:
    - **Follow Up Boss inclusion:** The MD&A says the increase was "primarily due to the inclusion of revenue from Follow Up Boss, which we acquired in December 2023." The filing does not quantify Follow Up Boss's revenue contribution.
    - Growth in Premier Agent revenue from better conversion of connections into transactions.
    - Increased ShowingTime+ revenue as software services expanded to sellers and listing agents.
    - Continued growth in new construction revenue.
  - Visits increased 4%.
  
  **Mortgages (+$49M, +51%)**
  - Mort
  …[truncated 748 chars]
- retrieve_information({"prompt": "From this Zillow 10-K FY2023 text, find the Business/Acquisitions description: Aryeo, Spruce, Follow Up Boss — close dates, purchase consideration, targets' businesses, and the stated strategic rationale. Also the cash flow line 'cash paid for acquisitions, net' for 2023, 2022. Text: {{fy2023}}"})
  result: ## Acquisitions (FY2023 10-K)
  
  | | Follow Up Boss | Spruce | Aryeo |
  |---|---|---|---|
  | **Close date** | December 8, 2023 | September 11, 2023 | July 31, 2023 |
  | **Legal form** | Enchant, LLC, d/b/a Follow Up Boss | Substantially all assets and liabilities of Spruce Holdings, Inc. and affiliated entities | Aryeo, Inc. |
  | **Purchase consideration** | $399M cash, net of cash acquired, plus contingent consideration of up to $100M cash over three years | ~$19M cash, net of cash acquired | ~$15M cash, net of cash acquired, plus 380,259 shares of Class C capital stock valued at ~$20M; total ~$35M net of cash acquired |
  | **Total preliminary purchase price (Note 7)** | $484M ($403M cash + $81M contingent consideration fair value) | $24M | $38M |
  | **Goodwill / intangibles (preliminary)** | $401M / $86M | $16M / $2M | $26M / $11M |
  
  **Targets' businesses**
  - **Follow Up Boss:** A customer relationship management (CRM) system for real estate professionals that gives them a central hub to organize and engage customers, close deals, and build their teams. The 10-K says it had been a key integration partner for several years and is widely used across the industry and by many Premier Agent partners.
  - **Spruce:** A tech-enabled title and escrow platform.
  - **Aryeo:** A software company that serves real estate photographers.
  
  **Stated strategic rationale**
  - **Follow Up Boss:** The 10-K says the acquisition "is consistent with our strategy to invest in a more integrated software experience for our customers." Management also describes it as a tech-enabled product that the company is actively integrating into its suite of partner offerings. Elsewhere, the company cites software services, including Follow Up Boss, as a way to enhance its ability to facilitate real estate transaction
  …[truncated 1,230 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Headline: As of December 2024, Zillow's acquisition activity over the prior two years (Dec 2022 to Dec 2024) was concentrated in 2023, when it bought three software and fintech businesses, led by the roughly $399M cash Follow Up Boss CRM deal. Spending then stopped almost entirely in 2024. The revenue mix shifted toward Rentals and Mortgages, which the filings attribute mainly to organic drivers. Only Residential, which carries the Follow Up Boss contribution, is tied to an acquisition, and the filing does not quantify that contribution. So the alignment is partial: the largest acquisition feeds the largest category, but the faster-growing categories grew organically.\n\n1.
…[truncated 4,678 chars])

### Final answer
Headline: As of December 2024, Zillow's acquisition activity over the prior two years (Dec 2022 to Dec 2024) was concentrated in 2023, when it bought three software and fintech businesses, led by the roughly $399M cash Follow Up Boss CRM deal. Spending then stopped almost entirely in 2024. The revenue mix shifted toward Rentals and Mortgages, which the filings attribute mainly to organic drivers. Only Residential, which carries the Follow Up Boss contribution, is tied to an acquisition, and the filing does not quantify that contribution. So the alignment is partial: the largest acquisition feeds the largest category, but the faster-growing categories grew organically.

1. Deal table (dated, from the FY2023 and FY2024 10-Ks)
- Follow Up Boss (Enchant, LLC), closed Dec 8, 2023: a CRM for real estate professionals. Price was $399M cash net of cash acquired, plus up to $100M contingent cash over three years. Total preliminary purchase price was $484M ($403M cash plus $81M contingent fair value). At 12/31/24 the contingent liability was $91M. Goodwill was about $401M (FY2023 10-K preliminary) and $402M (FY2024 10-K).
- Aryeo, closed Jul 31, 2023: software for real estate photographers. Price was about $15M cash plus 380,259 Class C shares valued at $20M, described as $35M total net of cash acquired. The purchase price allocation totals $38M, and the filing does not reconcile the two figures.
- Spruce Holdings (substantially all assets), closed Sep 11, 2023: a tech-enabled title and escrow platform. Price was about $19M cash net of cash acquired. The allocation totals $24M, again unreconciled.
- VRX Media Group (Dec 2022) and Virtual Staging AI (Oct 2024) are named only in the FY2024 risk factors. No price or business description is disclosed. Virtual Staging AI's October 2024 date falls inside the window, but the filing that discloses it was issued after December 2024, so treat it as a later-disclosed item.

2. Spend intensity (cash paid for acquisitions, net, from the cash flow statement)
- 2022: $4M, against total revenue of $1,958M (0.20%). The filing does not tie this to a named deal.
- 2023: $433M, against total revenue of $1,945M (22.26%). Follow Up Boss was $399M of this, or 92.15% of the year's net acquisition cash (399/433). The three 2023 components sum to $433M.
- 2024: $7M, against total revenue of $2,236M (0.31%). This is effectively a pause in acquisitions.

3. Revenue mix (MD&A, $ millions; share of total)
- Residential: 2022 $1,522 (78%); 2023 $1,452 (75%); 2024 $1,594 (71%). 2024 growth +9.78% (142/1,452).
- Mortgages: 2022 $119 (6%); 2023 $96 (5%); 2024 $145 (6%). 2024 growth +51.04%.
- Rentals: 2022 $274 (14%); 2023 $357 (18%); 2024 $453 (20%). 2024 growth +26.89%.
- Other: 2022 $43 (2%); 2023 $40 (2%); 2024 $44 (2%).
- Total: 2022 $1,958 (100%); 2023 $1,945 (100%); 2024 $2,236 (100%). 2024 growth +14.96% (291/1,945).
- Categories sum to totals in each year. The FY2024 10-K does not include a 2023 vs 2022 MD&A discussion, so the 2022 figures come from the consolidated statements and note; Zillow Offers is discontinued and not in these figures.
- For Sale (Residential plus Mortgages) fell from 84% of revenue in 2022 to 80% in 2023 and 78% in 2024. Rentals rose from 14% to 20% over the same period.

4. Attribution and alignment
- Residential: the FY2024 MD&A says growth was "primarily due to the inclusion of revenue from Follow Up Boss," which Zillow acquired in December 2023. This is the only filing-stated acquisition contribution in the revenue table, and the filing does not quantify it. Other Residential drivers cited are Premier Agent conversion, ShowingTime+ expansion and new construction.
- Mortgages: growth is attributed to organic drivers, namely Zillow Home Loans purchase originations (loan origination volume up 101% to $3.1B). No acquisition is credited.
- Rentals: growth is attributed to multifamily listings and traffic (multifamily rentals revenue up 42%). No acquisition is credited.
- Inference: the deals did not drive the mix shift toward Rentals or Mortgages. The shift away from For Sale was mainly organic growth in the other categories, so the Follow Up Boss deal reinforces the largest category (Residential) without changing the overall mix much. The 2023 deals were tuck-ins in software and transaction services, with no large transformational deal. Zillow's build-and-partner approach (for example, Mortgages built organically) is consistent with that pattern.

Bottom line: Zillow's acquisition strategy over the two years was a single large 2023 push into agent software (Follow Up Boss), supported by smaller software and title/escrow buys (Aryeo, Spruce), followed by a near-halt in 2024. Its revenue mix moved toward Rentals and Mortgages, which the filings credit to organic growth. Only the Residential category has an acquisition tie, and the filing does not quantify it.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm",
            "name": "Zillow Group FY2024 Form 10-K (filed 2025-02-11)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm",
            "name": "Zillow Group FY2023 Form 10-K"
        }
    ]
}