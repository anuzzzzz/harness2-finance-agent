## Rollout `inv1`
- outcome: submitted
- turns: 3; cost: $0.306; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "key": "z10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: z10k. (467,105 characters)
  The data_storage currently contains the following keys:
  z10k
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow 10-K, quote the Acquisitions note (Note 6) text describing the Aryeo, Spruce, and Follow Up Boss acquisitions: closing dates, cash consideration, contingent consideration, and total purchase consideration and goodwill/intangibles amounts. Also state any acquisition of Virtual Staging AI. {{z10k}}"})
  result: **Note 6. Acquisitions (verbatim)**
  
  **Acquisition of Follow Up Boss**
  
  > On December 8, 2023, Zillow Group acquired Follow Up Boss, a customer relationship management system for real estate professionals, for $399 million in cash, net of cash acquired, and contingent consideration of up to $100 million in cash, payable over a three-year period upon achievement of certain performance metrics. See Note 4 for additional information regarding the fair value of contingent consideration. The acquisition is consistent with our strategy to invest in a more integrated software experience for our customers. The acquisition of Follow Up Boss has been accounted for as a business combination, and assets acquired and liabilities assumed were generally recorded at their estimated fair values, in accordance with the applicable accounting guidance. Goodwill represents the expected synergies from combining the acquired assets and the operations of the acquirer as well as intangible assets that do not qualify for separate recognition. Goodwill recorded in connection with the acquisition is deductible for tax purposes.
  
  The filing's purchase price table (in millions):
  
  | | |
  |---|---|
  | Cash | $403 |
  | Contingent consideration | 81 |
  | **Total purchase price** | **$484** |
  | Cash and cash equivalents | $4 |
  | **Goodwill** | **402** |
  | **Intangible assets** | **86** |
  | Deferred revenue | (7) |
  | Other liabilities | (1) |
  | Total | $484 |
  
  Intangibles: developed technology $50M (4-year weighted-average life), customer relationships $34M (7 years), trade names and trademarks $2M (7 years), total $86M.
  
  **Acquisitions of Aryeo and Spruce**
  
  > On July 31, 2023, Zillow Group acquired Aryeo, a software company that serves real estate photographers, in exchange for approximately $15 million in 
  …[truncated 2,498 chars]
- retrieve_information({"prompt": "From this Zillow 10-K MD&A, give the revenue explanations for Residential, Mortgages, Rentals and Other for 2024 vs 2023, including the wording on how Follow Up Boss, Aryeo, Spruce or other acquisitions contributed to revenue growth in each line, and whether Mortgages or Rentals growth is attributed to acquisitions or organic factors. {{z10k}}"})
  result: ## Revenue explanations, 2024 vs. 2023 (Form 10-K, MD&A)
  
  | Category | 2024 | 2023 | Change | Acquisition cited? | Stated primary driver |
  |---|---|---|---|---|---|
  | Residential | $1,594M | $1,452M | +$142M (+10%) | Yes: Follow Up Boss | Higher revenue per visit, plus more visits |
  | Mortgages | $145M | $96M | +$49M (+51%) | No | Mortgage originations (loan volume and gain on sale margin) |
  | Rentals | $453M | $357M | +$96M (+27%) | No | Revenue per unique visitor and unique visitor growth |
  | Other | $44M | $40M | +$4M (+10%) | No | Not explained in MD&A |
  
  ### Residential
  
  The MD&A says: "The increase in Residential revenue was partially driven by a 6% increase in Residential revenue per visit to $0.171 for the year ended December 31, 2024 from $0.162 for the year ended December 31, 2024, primarily due to the inclusion of revenue from Follow Up Boss, which we acquired in December 2023, growth in our Premier Agent revenue primarily due to continued improvement in our ability to convert connections into transactions, an increase in ShowingTime+ revenue as we expanded software services available to sellers and listing agents, and continued growth in our new construction revenue."
  
  It adds: "The increase in Residential revenue was also attributable to a 4% increase in the number of visits."
  
  - **Follow Up Boss:** This is the only acquisition named in the Residential explanation. The filing attributes part of the per-visit increase to "the inclusion of revenue from Follow Up Boss," which was acquired December 8, 2023. Because the deal closed only weeks before the 2023 year-end, most of Follow Up Boss's revenue appears as incremental in 2024. The filing does not quantify the amount.
  - **Aryeo and Spruce:** Neither is mentioned in the Residential revenue explanation. Aryeo 
  …[truncated 2,879 chars]
- retrieve_information({"prompt": "From this Zillow 10-K, quote the business strategy / overview text describing Zillow's stated strategy, including the \"integrated software experience\", the rationale for acquisitions such as Follow Up Boss, Aryeo, Spruce, and Virtual Staging AI, and any description of its shift toward a more integrated transaction/software business. {{z10k}}"})
  result: Below are the relevant passages from Zillow Group's FY2024 Form 10-K, with section references. Ellipses mark omitted text.
  
  ## 1. Overview and the "integrated" strategy (Part I, Item 1)
  
  > "We are helping renters, buyers, sellers, and real estate professionals across all their residential real estate needs through our 'housing super app' which serves as an ecosystem of connected solutions for the tasks and services related to moving. ... We strive to provide renters, buyers, sellers, real estate professionals, and the industry with the seamless, integrated, and tech-enabled experience they demand and deserve. We are focused on continually improving our consumer funnel, capturing consumer demand and connecting that demand to our partner network. We have made significant advancements in our strategy through growth and investments in the following areas:"
  
  ## 2. For Sale, Industry Software, and Rentals (Item 1)
  
  **For Sale:**
  > "The integrated transaction experience we have been building on Zillow is most fully experienced in our Enhanced Markets. Enhanced Markets are geographies in which consumers can easily navigate the home-buying process digitally and seamlessly. In these markets, consumers benefit from a more streamlined experience from touring to closing, with the support of our agent partners and Zillow Home Loans loan officers. As of December 31, 2024, we are active in 43 Enhanced Markets, which represents 21% of our total connections, or leads delivered to our Premier Agent partners. ..."
  
  **Industry Software:**
  > "We are investing in digital solutions to empower real estate professionals to drive a better consumer experience for movers. Our software solutions are designed to make buying and selling a home easier, more efficient, and more digital, thereby deliveri
  …[truncated 4,210 chars]

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "\nShort answer: Over 2023–2024 Zillow's acquisitions were concentrated in real estate software and transaction tools. Those deals connect mainly to the Residential line, which is the largest revenue line but is losing share. The fastest-growing lines, Mortgages and Rentals, were attributed to organic growth in the FY2024 10-K. So the strategy aligns with the Residential business and only partly with the revenue mix shift. Basis: Zillow's FY2024 Form 10-K (filed 2025-02-11), the most recent annual report available as of April 2025. Its Note 6, MD&A and Item 1 are the primary sources.\n\n1. Acquisition strategy (2023–2024)\n- Follow Up Boss (closed Dec 8, 2023): $399M cash ne
…[truncated 4,661 chars])

### Final answer

Short answer: Over 2023–2024 Zillow's acquisitions were concentrated in real estate software and transaction tools. Those deals connect mainly to the Residential line, which is the largest revenue line but is losing share. The fastest-growing lines, Mortgages and Rentals, were attributed to organic growth in the FY2024 10-K. So the strategy aligns with the Residential business and only partly with the revenue mix shift. Basis: Zillow's FY2024 Form 10-K (filed 2025-02-11), the most recent annual report available as of April 2025. Its Note 6, MD&A and Item 1 are the primary sources.

1. Acquisition strategy (2023–2024)
- Follow Up Boss (closed Dec 8, 2023): $399M cash net of cash acquired, plus up to $100M contingent consideration over three years. The purchase price table totals $484M (cash $403M, contingent consideration $81M). It allocates $402M to goodwill and $86M to intangibles. The 10-K says the deal is "consistent with our strategy to invest in a more integrated software experience for our customers."
- Aryeo (closed Jul 31, 2023): a software company serving real estate photographers. The text gives about $15M cash plus 380,259 Class C shares worth $20M, for $35M net of cash acquired. The allocation table totals $38M, and the filing does not reconcile the two figures.
- Spruce (closed Sep 11, 2023): a tech-enabled title and escrow platform, for about $19M cash net of cash acquired. The allocation table totals $24M.
- Virtual Staging AI (October 2024): named only in the risk factors. Note 6 gives no price, date or rationale, and the filing does not tie the $7M of 2024 acquisition cash to it.
- Scale: cash paid for acquisitions, net, was about $433M in 2023 (consistent with $399M + $15M + $19M) and $7M in 2024 (cash flow statement, per the earlier extraction).
- Stated purpose: Item 1 describes Aryeo and Follow Up Boss as tools that help agents manage leads, create listings and complete transactions. It says Zillow will keep investing in digital solutions to increase transactions completed on Zillow. The filing describes an "integrated transaction experience" in its 43 Enhanced Markets, which represent 21% of connections. Item 1 also says more than 80% of Enhanced Market connections are managed through Follow Up Boss.

2. Revenue mix, FY2024 vs FY2023 ($M; share of total)
- Residential: 1,594 (71.29%) vs 1,452 (74.65%). Up 142, or 9.78%.
- Mortgages: 145 (6.49%) vs 96 (4.94%). Up 49, or 51.04%.
- Rentals: 453 (20.26%) vs 357 (18.35%). Up 96, or 26.89%.
- Other: 44 (1.97%) vs 40 (2.06%). Up 4, or 10.00%.
- Total: 2,236 vs 1,945. Up 291, or 14.96%.
- Residential's share fell about 3.37 points. Mortgages rose about 1.55 points, and Rentals about 1.90 points.
- Of the $291M increase, Residential supplied about 48.8%, Rentals 33.0%, Mortgages 16.8% and Other 1.4%.

3. How the revenue drivers line up with the acquisitions
- Residential: this is the only line where the MD&A names an acquisition. It cites the "inclusion of revenue from Follow Up Boss" as part of a 6% rise in revenue per visit (to $0.171 from $0.162). Premier Agent conversion, ShowingTime+ and new construction are also cited, along with a 4% rise in visits. The filing does not quantify Follow Up Boss's contribution. Aryeo and Spruce are not mentioned as drivers. The MD&A also contains a typo: it compares 2024 with "2024" where it should read 2023.
- Mortgages: growth is attributed to organic factors. Loan origination volume rose 101% to $3.1B, driven by purchase loans at Zillow Home Loans, and gain-on-sale margin rose 22%. The 10-K ties the drop in Custom Quote and Connect revenue to Zillow's focus on organic growth of its mortgage operations. No acquisition is cited.
- Rentals: growth is attributed to multifamily listings (multifamily revenue up 42%), revenue per unique visitor (up 15% to $3.65) and unique visitors (up 11% to 31M). No acquisition is cited.
- Other: no driver is given. The MD&A does not explain the $4M increase.

4. Assessment
- Alignment: the software deals (Follow Up Boss, Aryeo, Spruce, Virtual Staging AI) support the Residential ecosystem of agent tools, lead management and transaction services. This is where the filing attributes acquired revenue, so the strategy is consistent with the Residential business.
- Misalignment with the mix shift: the mix moved toward Mortgages and Rentals, and the filing credits those gains to organic execution, not to acquisitions. Acquisitions therefore did not drive the fastest-growing lines.
- Limits: the filing does not split out acquired revenue, so the Follow Up Boss effect cannot be separated from organic Residential growth. The "shift toward an integrated software business" is my inference from the "integrated" language; the 10-K does not use the word "shift." Rationale for Spruce, Aryeo and Virtual Staging AI is limited to general "integrated software" language.
- Later development (after December 2024, labeled only): the 10-K notes a Redfin rentals partnership entered February 6, 2025. It did not contribute to 2024 revenue.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm",
            "name": "Zillow Group FY2024 Form 10-K (filed 2025-02-11)"
        }
    ]
}
