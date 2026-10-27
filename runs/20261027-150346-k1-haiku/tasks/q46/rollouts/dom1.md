## Rollout `dom1`
- outcome: submitted
- turns: 5; cost: $0.517; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "acquisition_strategy_vs_revenue_mix"})
  result: ---
  name: acquisition_strategy_vs_revenue_mix
  description: Explain a company's recent M&A pattern and test whether it lines up with the shift in its revenue mix, using the acquisitions note, cash-flow statement and the revenue-by-category table.
  ---
  ANALYTIC MOVE: trace and compare. List the deals made in the window. Quantify the spend. Map each deal to a revenue line. Then check whether the mix shift came from the deals or from organic growth.
  
  1. Window. Fix the question's window (for example "past 2 years as of Dec 2024" means Dec 2022 to Dec 2024). Say which deals fall outside it. Do not call a deal "recent" on memory alone.
  2. Deal list from the controlling sources:
     - the 10-K acquisitions note (target, close date, cash paid net of cash acquired, contingent consideration, goodwill and intangibles);
     - the cash-flow line "cash paid for acquisitions, net" for each year;
     - the risk-factor or Item 1 text, which often names small deals that have no note;
     - the 10-Qs and 8-Ks of the window for anything the 10-K omits.
     For each deal give the date, price (cash plus contingent, using the filing's wording) and what the target does. If the text and the allocation table disagree, show both numbers and flag it. If the price is undisclosed, say so; do not guess.
  3. Intensity. Compare each year's net cash paid with total revenue. Show which single deal dominates (deal cash / year's net acquisition cash). A year with near-zero spend is a pause, so say that.
  4. Revenue mix. From the 10-K MD&A and Results of Operations table, retrieve both years of revenue by category: dollars, percent of total, and YoY growth. Check that the categories sum to total revenue. Note any re-labelled or re-segmented categories between years, and compare only like with like.
  5. Mapping and a
  …[truncated 2,605 chars]
- edgar_search({"search_query": "Zillow annual report acquisitions revenue by category", "ciks": ["Z"], "start_date": "2023-01-01", "end_date": "2025-04-07", "form_types": ["10-K"]})
  result: {"total_matching_documents": 3, "page": 1, "results": [{"form": "10-K", "file_date": "2024-02-15", "period_ending": "2023-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000022", "document": "z-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm"}, {"form": "10-K", "file_date": "2025-02-11", "period_ending": "2024-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-25-000016", "document": "z-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm"}, {"form": "10-K", "file_date": "2023-02-15", "period_ending": "2022-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-23-000010", "document": "z-20221231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "key": "fy24"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy24. (467,105 characters)
  The data_storage currently contains the following keys:
  fy24
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm", "key": "fy23"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy23. (503,493 characters)
  The data_storage currently contains the following keys:
  fy24
  fy23
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow FY2024 10-K text, find the Business Acquisitions note (Note 6). List each acquisition with close date, consideration (cash net of cash acquired, contingent consideration), total purchase price allocation, goodwill and intangibles, and the target's business. Also state the text on Aryeo's net cash figure and any Virtual Staging AI mention. Text: {{fy24}}"})
  result: ## Note 6 (Acquisitions): Zillow FY2024 10-K
  
  Three acquisitions are described in Note 6. All are accounted for as business combinations. The filing says the aggregate effects were not material and gives no pro forma information.
  
  | | **Follow Up Boss** | **Aryeo** | **Spruce** |
  |---|---|---|---|
  | **Close date** | Dec 8, 2023 | Jul 31, 2023 | Sep 11, 2023 |
  | **Target's business** | Customer relationship management (CRM) system for real estate professionals (agents, teams, brokerages) | Software company serving real estate photographers | Tech-enabled title and escrow platform (acquired substantially all assets and liabilities) |
  | **Cash consideration, net of cash acquired** | $399M ($403M gross less $4M cash acquired) | ~$15M | ~$19M |
  | **Other consideration** | Contingent consideration up to $100M in cash, payable over 3 years on performance metrics | 380,259 Class C shares valued at $20M | None disclosed |
  | **Total purchase price (gross)** | $484M ($403M cash + $81M contingent fair value) | $38M | $24M |
  | **Purchase price allocation** | Cash $4M; goodwill $402M; intangibles $86M; deferred revenue $(7)M; other liabilities $(1)M | Cash $3M; goodwill $26M; intangibles $11M; other assets $0; liabilities $(2)M | Cash $5M; goodwill $16M; intangibles $2M; other assets $2M; liabilities $(1)M |
  | **Goodwill** | $402M, tax-deductible | $26M, not tax-deductible | $16M, tax-deductible |
  | **Intangibles** | Developed technology $50M (4 yrs); customer relationships $34M (7 yrs); trade names/trademarks $2M (7 yrs) | Customer relationships $5M (5 yrs); purchased content $4M (3 yrs); developed technology $2M (3 yrs) | Developed technology $2M (3 yrs) |
  
  Each allocation sums to its total purchase price. For Follow Up Boss, the $403M gross cash less $4M cash acquired gives the $3
  …[truncated 1,793 chars]
- retrieve_information({"prompt": "From this Zillow FY2023 10-K text, find the Business Acquisitions note. List each acquisition with close date, consideration (cash net of cash acquired, contingent consideration), total purchase price allocation, goodwill and intangibles, and target business. Also find any description of strategic rationale for Follow Up Boss, Aryeo, Spruce, and any divestiture or wind-down (e.g., Zillow Offers) in 2022-2023. Text: {{fy23}}"})
  result: # Zillow Group FY2023 10-K: Business Acquisitions and Divestitures
  
  The Business Acquisitions note is **Note 7, "Acquisitions"** (10-K p. 88-90). Figures are in millions unless noted. All three 2023 purchase price allocations are **preliminary**, and each measurement period remained open at 12/31/2023.
  
  ## 1. Acquisition Summary
  
  | | **Follow Up Boss** | **Aryeo** | **Spruce** |
  |---|---|---|---|
  | **Target** | Enchant, LLC d/b/a Follow Up Boss: CRM for real estate professionals | Aryeo, Inc.: software for real estate photographers | Spruce Holdings, Inc. and affiliates: tech-enabled title and escrow platform (acquired substantially all assets and liabilities) |
  | **Close date** | December 8, 2023 | July 31, 2023 | September 11, 2023 |
  | **Cash consideration, net of cash acquired** | $399 ($403 gross less $4 cash acquired) | ~$15 | ~$19 |
  | **Stock consideration** | None | ~$20 (380,259 Class C shares) | None |
  | **Contingent consideration** | Up to $100 cash over 3 years, tied to performance metrics; preliminary fair value $81 at acquisition | None disclosed | None disclosed |
  | **Total consideration (as reported)** | $484 preliminary purchase price ($403 cash gross + $81 contingent) | $35 net of cash acquired (per Note 7 text) | $19 net of cash acquired (per Note 7 text) |
  | **Total preliminary purchase price (allocation table)** | $484 | $38 | $24 |
  | **Goodwill** | $401 | $26 | $16 |
  | **Identifiable intangibles** | $86 | $11 | $2 |
  | **Tax-deductible goodwill?** | Yes | No | Yes |
  
  **Note on the Aryeo and Spruce figures:** The allocation tables total $38 and $24, which are gross of cash acquired ($3 for Aryeo, $5 for Spruce). The net consideration figures ($35 and $19) are net of that cash. The $3 and $5 amounts reconcile the two presentations, so the figures are n
  …[truncated 3,681 chars]
- retrieve_information({"prompt": "From this Zillow FY2024 10-K text, find the cash flow statement line \"Cash paid for acquisitions, net of cash acquired\" (or similar) for 2024, 2023, and 2022, and the total revenue for 2024, 2023, 2022. Give exact figures and units. Text: {{fy24}}"})
  result: **Cash paid for acquisitions, net** (Consolidated Statements of Cash Flows, investing activities, in millions of USD):
  
  | Year | Amount |
  |---|---|
  | 2024 | $(7) million |
  | 2023 | $(433) million |
  | 2022 | $(4) million |
  
  The line is labeled "Cash paid for acquisitions, net" in the statement. The MD&A describes the 2023 figure as "cash paid for acquisitions, net of cash acquired." Parentheses denote cash outflows.
  
  **Total revenue** (Consolidated Statements of Operations, in millions of USD):
  
  | Year | Amount |
  |---|---|
  | 2024 | $2,236 million |
  | 2023 | $1,945 million |
  | 2022 | $1,958 million |
  
  The 2022 figure excludes Zillow Offers, which was presented as discontinued operations.

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow FY2024 10-K text, find the revenue by category table in the MD&A / Results of Operations (Residential, Mortgages, Rentals, Other, Total revenue) for 2024 and 2023 with dollars in millions and percent of total. Also quote the MD&A sentences explaining drivers of Residential, Mortgages, and Rentals revenue growth, including any mention of Follow Up Boss or acquisitions. Text: {{fy24}}"})
  result: ## Revenue by Category (MD&A, Results of Operations)
  
  Dollars in millions; years ended December 31.
  
  | Category | 2024 | 2023 | $ Change | % Change | % of Total 2024 | % of Total 2023 |
  |---|---|---|---|---|---|---|
  | **For Sale revenue:** | | | | | | |
  | Residential | $1,594 | $1,452 | $142 | 10% | 71% | 75% |
  | Mortgages | 145 | 96 | 49 | 51% | 6% | 5% |
  | **Total For Sale revenue** | **1,739** | **1,548** | **191** | **12%** | **78%** | **80%** |
  | Rentals | 453 | 357 | 96 | 27% | 20% | 18% |
  | Other | 44 | 40 | 4 | 10% | 2% | 2% |
  | **Total revenue** | **$2,236** | **$1,945** | **$291** | **15%** | **100%** | **100%** |
  
  ## MD&A Sentences on Revenue Drivers
  
  **Residential**
  
  > "The increase in Residential revenue was partially driven by a 6% increase in Residential revenue per visit to $0.171 for the year ended December 31, 2024 from $0.162 for the year ended December 31, 2024, primarily due to the inclusion of revenue from Follow Up Boss, which we acquired in December 2023, growth in our Premier Agent revenue primarily due to continued improvement in our ability to convert connections into transactions, an increase in ShowingTime+ revenue as we expanded software services available to sellers and listing agents, and continued growth in our new construction revenue."
  
  > "The increase in Residential revenue was also attributable to a 4% increase in the number of visits for the year ended December 31, 2024, as compared to the year ended December 31, 2023."
  
  Note: The comparative period in the first sentence is labeled "December 31, 2024" in the filing text. It should read 2023, which is how the figure is used here.
  
  **Mortgages**
  
  > "This increase was driven by a $64 million increase in mortgage originations revenue, partially offset by a $12 million decrease in Custom
  …[truncated 1,759 chars]
- retrieve_information({"prompt": "From this Zillow FY2023 10-K text, find (a) the Item 1 or MD&A description of Zillow's strategy around software, marketing solutions, and Premier Agent / seller services, and (b) any 2022 acquisitions or investments, the Zillow Offers wind-down status and inventory sales in 2022, and the 2022 revenue by category if disclosed. Text: {{fy23}}"})
  result: ## (a) Strategy around software, marketing solutions, and Premier Agent / seller services
  
  - **"Housing super app" vision.** Item 1 describes the goal of helping customers with "all their real estate needs" as one connected ecosystem. Execution runs through six growth pillars, two of which bear directly on this question:
    - *Expanding seller services*: "Invest in tech-enabled solutions and services to make selling homes easier for sellers and listing agents."
    - *Enhancing our partner network*: "Help the best agents to better serve more customers and grow their businesses."
  - **Marketing software and technology suite.** Zillow describes itself as offering "a comprehensive suite of marketing software and technology solutions for the real estate industry, including Spruce, Mortech, New Home Feed, ShowingTime+ and Follow Up Boss" (Item 1 and MD&A Overview).
  - **Software investment.** Item 1 (Total Addressable Market) says Zillow has "invested in software services, including the acquisition of Follow Up Boss and the expansion of offerings through our ShowingTime+ suite," to better facilitate transactions with buyers and sellers. Note 7 says the Follow Up Boss acquisition "is consistent with our strategy to invest in a more integrated software experience for our customers."
  - **Seller services.** Zillow cites its exclusive multi-year partnership with Opendoor, which offers sellers a cash offer in 45 markets. It also cites the Listing Showcase product under ShowingTime+, which gives sellers and listing agents premium listing presentation.
  - **Premier Agent.** Premier Agent sells advertising and marketing/technology products to agents and brokers. It is offered on a market-based "share of voice" basis and a pay-for-performance "Flex" model, in which agents get validated lead
  …[truncated 2,715 chars]

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "\nHEADLINE\nBetween December 2022 and December 2024, Zillow's acquisitions were concentrated in 2023 and were small software, CRM and title/escrow tuck-ins. The largest deal, Follow Up Boss, feeds Residential, the largest revenue category. However, Residential's share of revenue fell from about 78% in 2022 to 71% in 2024, and that shift came mainly from organic growth in Mortgages and Rentals, not from acquisitions. So the acquisitions reinforce the core Residential business, but they do not explain the mix change.\n\nWINDOW AND SCOPE\nWindow: December 2022 to December 2024. Documents opened: the FY2024 10-K (filed Feb 11, 2025) and the FY2023 10-K (filed Feb 15, 2024). I d
…[truncated 6,521 chars])

### Final answer

HEADLINE
Between December 2022 and December 2024, Zillow's acquisitions were concentrated in 2023 and were small software, CRM and title/escrow tuck-ins. The largest deal, Follow Up Boss, feeds Residential, the largest revenue category. However, Residential's share of revenue fell from about 78% in 2022 to 71% in 2024, and that shift came mainly from organic growth in Mortgages and Rentals, not from acquisitions. So the acquisitions reinforce the core Residential business, but they do not explain the mix change.

WINDOW AND SCOPE
Window: December 2022 to December 2024. Documents opened: the FY2024 10-K (filed Feb 11, 2025) and the FY2023 10-K (filed Feb 15, 2024). I did not open the FY2022 10-K, so 2022 revenue figures come from the recast figures in the FY2024 10-K (continuing operations, four-category presentation). The FY2023 10-K also notes that 2022 Zillow Offers results are in discontinued operations.

1) DEAL LIST (dated, priced, from the filings)
- Aryeo (software for real estate photographers), closed July 31, 2023. Cash of about $15M net of cash acquired, plus 380,259 Class C shares valued at $20M. Total $35M net of cash acquired. The allocation table totals $38M, which is gross of $3M cash acquired. Goodwill $26M (not tax-deductible); intangibles $11M.
- Spruce (tech-enabled title and escrow platform; substantially all assets and liabilities), closed September 11, 2023. About $19M net cash. Allocation table totals $24M gross of $5M cash. Goodwill $16M (tax-deductible); intangibles $2M.
- Follow Up Boss (CRM for real estate agents, teams and brokerages), closed December 8, 2023. $399M net cash ($403M gross less $4M cash acquired), plus up to $100M contingent consideration over three years. Preliminary purchase price $484M ($403M cash + $81M contingent fair value). Goodwill is $402M in the FY2024 10-K but $401M in the FY2023 10-K (a discrepancy I flag; the filings do not reconcile it). Intangibles $86M.
- Virtual Staging AI, acquired October 2024 (after the window, a subsequent event). Named only in a risk factor in the FY2024 10-K. No price, target description or allocation is disclosed, so I do not estimate it. The filing does not tie the $7M 2024 cash outflow to this deal; that link is my inference only.
- VRX Media Group, acquired December 2022 (inside the window). Named only in a risk factor; no price or accounting detail is disclosed.
- Outside the window: none of the above is pre-2022. Zillow Offers (iBuying) was wound down in 2022 (decision November 2021; wind-down completed Q3 2022). This is a divestiture-type exit, not an acquisition, but it shaped the 2022 base.

2) ACQUISITION INTENSITY (cash paid for acquisitions, net, from cash flow statement)
- 2022: $4M (total revenue $1,958M; deal cash is 0.20% of revenue)
- 2023: $433M (total revenue $1,945M; deal cash is 22.26% of revenue). Follow Up Boss's $399M is 92.15% of the year's net acquisition cash (399 / 433).
- 2024: $7M (total revenue $2,236M; 0.31% of revenue). This is a clear pause.

3) STRATEGIC RATIONALE (as stated in the filings)
- The FY2023 10-K says Follow Up Boss is consistent with a strategy to invest in a more integrated software experience for customers. It describes Zillow as offering a marketing software and technology suite that includes Spruce, Mortech, New Home Feed, ShowingTime+ and Follow Up Boss.
- The FY2023 10-K gives no explicit strategic rationale for Aryeo or Spruce. Linking them to the seller-services and integrated-experience pillars is my inference.
- The FY2023 10-K lists six growth pillars, including expanding seller services and enhancing the partner network.
- Pattern: the deals are tuck-in software and workflow assets (CRM, photography software, title/escrow tech) that sit next to the Premier Agent and ShowingTime+ products. They are not transformational. The company stated no quantified software revenue figure.

4) REVENUE MIX (continuing operations, $M; share of total)
Category | 2022 | 2023 | 2024
Residential | 1,522 (77.73%) | 1,452 (74.65%) | 1,594 (71.29%)
Mortgages | 119 (6.08%) | 96 (4.94%) | 145 (6.48%)
Rentals | 274 (13.99%) | 357 (18.35%) | 453 (20.26%)
Other | 43 (2.20%) | 40 (2.06%) | 44 (1.97%)
Total | 1,958 | 1,945 | 2,236
YoY growth: 2023 total -0.66%; 2024 total +14.96% (291 / 1,945). Residential 2024 +9.78% (142 / 1,452); Mortgages 2024 +51.04% (49 / 96); Rentals 2024 +26.89% (96 / 357).
"For Sale" (Residential plus Mortgages) was 78% of 2024 revenue versus 80% in 2023. Note: the 2023 and 2024 figures are from the MD&A and sum to total revenue. The 2022 figures come from the FY2024 10-K recast.

5) ATTRIBUTION: DEALS VERSUS ORGANIC DRIVERS
- Residential: the FY2024 MD&A credits part of the growth to "inclusion of revenue from Follow Up Boss," along with Premier Agent conversion, ShowingTime+ and new construction. The filing does not quantify the Follow Up Boss share, so I cannot split Residential's $142M increase between the deal and organic drivers.
- Mortgages: the MD&A ties growth to a 101% rise in loan origination volume, driven by a strategic focus on Zillow Home Loans purchase-loan origination. No acquisition is cited. Treat as organic.
- Rentals: the MD&A attributes growth to multifamily listings (multifamily rentals revenue +42%) and higher visitors. No acquisition is cited. Treat as organic.
- Conclusion on mix: the decline in Residential's share from 77.73% (2022) to 71.29% (2024) (about 6.44 percentage points) came from faster growth in Rentals (+6.27 points) and Mortgages (+0.40 points). Acquisitions are not credited with that shift. Follow Up Boss supports Residential's growth but is not a driver of the share change.

6) ALIGNMENT ASSESSMENT
- The 2023 deals (Aryeo, Spruce, Follow Up Boss) target software and transaction workflow for agents, sellers and closings. This aligns with the company's stated aim to deepen the Residential and seller-services business. Follow Up Boss feeds the largest category.
- The mix shift toward Rentals and Mortgages was organic (multifamily growth, Zillow Home Loans origination focus). It is not an acquisition outcome, so the M&A strategy and the mix change are only loosely aligned.
- Pause: 2024 net acquisition spend was $7M, so the program slowed after the 2023 deals. The small Virtual Staging AI deal (October 2024) fits the same tuck-in pattern, but no price is disclosed.
- Build versus buy: the strategy looks like buy-to-integrate software for an existing marketplace and partner network, plus organic investment in mortgages and rentals, rather than transformational M&A.

SOURCES
- Zillow Group FY2024 Form 10-K (filed 2025-02-11): https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm
- Zillow Group FY2023 Form 10-K (filed 2024-02-15): https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm

{"sources": [{"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "name": "Zillow Group FY2024 Form 10-K"}, {"url": "h
…[truncated 126 chars]