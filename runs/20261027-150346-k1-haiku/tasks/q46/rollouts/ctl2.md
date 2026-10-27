## Rollout `ctl2`
- outcome: submitted
- turns: 5; cost: $0.219; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Zillow acquisitions 2024 2025 strategy") → 0 results: 
- edgar_search({"search_query": "Zillow acquisition 2024 annual report revenue mix", "ciks": ["Z"], "start_date": "2024-01-01", "end_date": "2025-04-07", "top_n_results": 10})
  result: {"total_matching_documents": 7, "page": 1, "results": [{"form": "10-Q", "file_date": "2024-05-01", "period_ending": "2024-03-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000070", "document": "z-20240331.htm", "description": "10-Q", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000070/z-20240331.htm"}, {"form": "10-Q", "file_date": "2024-11-06", "period_ending": "2024-09-30", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000126", "document": "z-20240930.htm", "description": "10-Q", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000126/z-20240930.htm"}, {"form": "10-Q", "file_date": "2024-08-07", "period_ending": "2024-06-30", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000094", "document": "z-20240630.htm", "description": "10-Q", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000094/z-20240630.htm"}, {"form": "10-K", "file_date": "2025-02-11", "period_ending": "2024-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-25-000016", "document": "z-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm"}, {"form": "ARS", "file_date": "2024-04-16", "period_ending": "2023-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000063", "document": "a2023ars.pdf", "description": "ARS", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000063/a2023ars.pdf"}, {"form": "10-K", "file_date": "2024-02-15
  …[truncated 649 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 9 results: ZILLOW GROUP, INC. - Form 10-Q - FY2024 (Quarterly Earnings Tables - quarter ended Sep 2024) <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000126/Financial_Report.xlsx>; ZILLOW GROUP, INC. - Form 10-K - FY2024 (Annual Financial Statement Tables - full year 2024) <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/Financial_Report.xlsx>; ZILLOW GROUP, INC. - Form 10-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000015/exhibit993.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000093/exhibit993.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "key": "z10k2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: z10k2024. (467,105 characters)
  The data_storage currently contains the following keys:
  z10k2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow 10-K for FY2024: {{z10k2024}}. Provide (1) every acquisition described in the Acquisitions note and in Business/MD&A (names, dates, prices, rationale, e.g., Aryeo, Spruce, Follow Up Boss, Terra, ShowingTime, etc.), (2) the revenue breakdown by segment/category for 2024, 2023, 2022 (Premier Agent, Mortgages, Rentals, IMT, New Construction, Showcase, Other, etc.) in dollars and percentages, and (3) any statements linking acquisitions to revenue mix or the software/SaaS strategy. Quote figures exactly."})
  result: # Zillow Group FY2024 10-K: Acquisitions, Revenue Mix, and Software/SaaS Strategy
  
  **Scope note:** The filing does not contain Terra or a ShowingTime acquisition. It also does not break out revenue into Premier Agent, IMT, New Construction, or Showcase in dollars. Those gaps are flagged below.
  
  ## 1. Acquisitions
  
  ### Follow Up Boss (Enchant, LLC, d/b/a Follow Up Boss)
  - **Date:** December 8, 2023 (Note 6; Note 1 "acquired on December 8, 2023")
  - **Price:** "$399 million in cash, net of cash acquired, and contingent consideration of up to $100 million in cash, payable over a three-year period upon achievement of certain performance metrics"
  - **Purchase price allocation:** Cash $403M; contingent consideration $81M; total purchase price $484M. Net assets: cash and equivalents $4M, goodwill $402M, intangible assets $86M, deferred revenue $(7)M, other liabilities $(1)M.
  - **Intangibles:** Developed technology $50M (4-year weighted-average life); customer relationships $34M (7 years); trade names and trademarks $2M (7 years).
  - **Contingent consideration status:** "As of December 31, 2024, the first earn out period passed resulting in an expected payment of $33 million in February 2025." Fair value at 12/31/24: $33M current and $58M long-term. Inputs: discount rate 5.70%–5.87% (weighted average 5.81%); probability of achieving performance metrics 92%–100% (weighted average 96%).
  - **Rationale (Note 6):** "The acquisition is consistent with our strategy to invest in a more integrated software experience for our customers."
  - **Business description:** Follow Up Boss is "a customer relationship management system for real estate professionals."
  
  ### Aryeo, Inc.
  - **Date:** July 31, 2023
  - **Price (text):** "approximately $15 million in cash, net of cash acquired, and 380,259 sh
  …[truncated 1,707 chars]

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow 10-K for FY2024: {{z10k2024}}. Give the exact revenue table by revenue category/segment for years 2024, 2023, 2022 (Premier Agent, Mortgages, Rentals, IMT, New Construction, Other, Total; also Residential vs Mortgages segment revenue), with dollar amounts in millions and % of total. Also give cash paid for acquisitions, net for 2024, 2023, 2022, and the 2024 Business section statement on Zillow Home Loans/Mortgages and Rentals growth and the revenue-per-transaction or software/SaaS commentary."})
  result: ## 1. Revenue by Category (in $ millions)
  
  The 10-K reports four revenue categories: Residential, Mortgages, Rentals, and Other. It does not break out Premier Agent, IMT, or New Construction as separate revenue lines, so those rows are marked "not disclosed." Zillow also reports one operating and reportable segment, so "Residential" and "Mortgages" are revenue categories, not segments.
  
  | Category | 2024 | % of Total | 2023 | % of Total | 2022 | % of Total |
  |---|---|---|---|---|---|---|
  | Premier Agent | Not disclosed | – | Not disclosed | – | Not disclosed | – |
  | Mortgages | 145 | 6.5% | 96 | 4.9% | 119 | 6.1% |
  | Rentals | 453 | 20.3% | 357 | 18.4% | 274 | 14.0% |
  | IMT | Not disclosed | – | Not disclosed | – | Not disclosed | – |
  | New Construction | Not disclosed | – | Not disclosed | – | Not disclosed | – |
  | Other | 44 | 2.0% | 40 | 2.1% | 43 | 2.2% |
  | **Total Revenue** | **2,236** | **100.0%** | **1,945** | **100.0%** | **1,958** | **100.0%** |
  
  **Residential vs. Mortgages (For Sale subtotal):**
  
  | Category | 2024 | % of Total | 2023 | % of Total | 2022 | % of Total |
  |---|---|---|---|---|---|---|
  | Residential | 1,594 | 71.3% | 1,452 | 74.6% | 1,522 | 77.7% |
  | Mortgages | 145 | 6.5% | 96 | 4.9% | 119 | 6.1% |
  | **For Sale revenue** | **1,739** | **77.8%** | **1,548** | **79.6%** | **1,641** | **83.8%** |
  
  **Year-over-year changes:**
  - 2024 vs. 2023: Residential +$142M (+10%); Mortgages +$49M (+51%); Rentals +$96M (+27%); Other +$4M (+10%); Total +$291M (+15%).
  - 2023 vs. 2022: Residential −$70M (−4.6%); Mortgages −$23M (−19%); Rentals +$83M (+30%); Other −$3M; Total −$13M (−0.7%).
  
  Percentages are my calculations from the reported dollar figures and are rounded, so the 2024 column sums to 100.1%.
  
  ## 2. Cash Paid for Acquisitions, Net (Cash Flow Statement, $
  …[truncated 2,635 chars]

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "\n**Short answer:** Over 2023–2024, Zillow's acquisitions were concentrated in agent-facing software and transaction technology, and cash spending on deals was front-loaded in 2023. In 2024 the company grew mainly through organic expansion of Mortgages and Rentals. Revenue mix shifted toward those two categories and away from Residential. The software deals fit the agent-side strategy, but the filings don't break out software revenue, so the link to the revenue shift is inferred rather than reported.\n\n**1. Acquisition strategy (2023–2024)**\n\n- **Follow Up Boss (Dec 8, 2023):** The largest deal. Zillow paid $399 million in cash, net of cash acquired, plus up to $100 mill
…[truncated 3,459 chars])

### Final answer

**Short answer:** Over 2023–2024, Zillow's acquisitions were concentrated in agent-facing software and transaction technology, and cash spending on deals was front-loaded in 2023. In 2024 the company grew mainly through organic expansion of Mortgages and Rentals. Revenue mix shifted toward those two categories and away from Residential. The software deals fit the agent-side strategy, but the filings don't break out software revenue, so the link to the revenue shift is inferred rather than reported.

**1. Acquisition strategy (2023–2024)**

- **Follow Up Boss (Dec 8, 2023):** The largest deal. Zillow paid $399 million in cash, net of cash acquired, plus up to $100 million of contingent consideration over three years. The FY2024 10-K says the deal <cite index="2-3">is consistent with our strategy to invest in a more integrated software experience for our customers.</cite> The first earn-out period passed, with an expected $33 million payment in February 2025.
- **Aryeo (Jul 31, 2023):** Described as <cite index="2-10">a software company that serves real estate photographers</cite>. Consideration was about $15 million cash plus Class C stock worth about $20 million, per the 10-K text. The 10-K's purchase-price table shows $38 million total, and the filing does not reconcile that with the $35 million text figure.
- **Spruce (Sep 11, 2023):** Substantially all assets of a tech-enabled title and escrow platform, for about $19 million cash, net of cash acquired.
- **Smaller tuck-ins:** VRX Media Group (December 2022) and Virtual Staging AI (October 2024) are mentioned only in the risk factors, with no price or rationale given.

Cash paid for acquisitions, net, per the cash flow statement: $4 million in 2022, $433 million in 2023, and $7 million in 2024. This shows the strategy was concentrated in 2023 and largely paused in 2024.

**2. Revenue mix (in $ millions, % of total)**

| Category | 2022 | 2023 | 2024 |
|---|---|---|---|
| Residential | 1,522 (77.7%) | 1,452 (74.6%) | 1,594 (71.3%) |
| Mortgages | 119 (6.1%) | 96 (4.9%) | 145 (6.5%) |
| Rentals | 274 (14.0%) | 357 (18.4%) | 453 (20.3%) |
| Other | 43 (2.2%) | 40 (2.1%) | 44 (2.0%) |
| Total | 1,958 | 1,945 | 2,236 |

Percentages are my calculations from the reported dollars. Total revenue grew 15% in 2024. Mortgages rose 51% and Rentals rose 27%, while Residential rose 10%. Residential's share fell from 77.7% to 71.3%, and Rentals plus Mortgages rose from about 20.1% to about 26.8% of revenue (my calculation).

**3. How the two fit together**

- **Software deals support the Residential/agent side.** Follow Up Boss, ShowingTime+, and Spruce target agents and the transaction workflow. The 10-K credits Follow Up Boss, Premier Agent conversion gains, ShowingTime+ and new construction for the rise in Residential revenue per visit. It also says more than 80% of Enhanced Market connections ran through Follow Up Boss at year-end. Residential still fell as a share of revenue, though, because Rentals and Mortgages grew faster.
- **The fastest growth came from organic businesses, not acquisitions.** Mortgages growth reflected higher origination volume (total loan origination volume rose 101% to $3.1 billion), not an acquired business. Rentals growth reflected traffic and multifamily listing growth, plus a partnership with Realtor.com.
- **Revenue per transaction is not a reported metric.** The closest disclosed figure is For Sale revenue per total transaction value, which rose to 10.1 basis points from 9.6. Software revenue is not reported as a separate line.
- **Subsequent event (after December 2024):** On February 6, 2025, Zillow agreed to a rentals partnership with Redfin that includes a $100 million upfront payment. This is a partnership rather than an acquisition, and it is outside the December 2024 snapshot.

**Caveats:** The 10-K does not disclose Premier Agent, IMT, or New Construction revenue separately, and it does not mention a Terra or ShowingTime acquisition. The figures above come from the FY2024 10-K, filed February 11, 2025, which was available as of the April 2025 date.
