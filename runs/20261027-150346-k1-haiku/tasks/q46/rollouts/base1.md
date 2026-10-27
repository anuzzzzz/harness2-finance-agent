## Rollout `base1`
- outcome: submitted
- turns: 5; cost: $0.239; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Zillow 2024 annual report acquisitions strategy revenue mix") → 0 results: 
- edgar_search({"search_query": "Zillow Group acquisition strategy revenue mix IMT rentals", "ciks": ["Z"], "start_date": "2022-10-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 3, "page": 1, "results": [{"form": "8-K", "file_date": "2023-02-15", "period_ending": "2023-02-15", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-23-000006", "document": "exhibit993.htm", "description": "EX-99.3", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000006/exhibit993.htm"}, {"form": "ARS", "file_date": "2023-04-26", "period_ending": "2022-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-23-000060", "document": "zg202210k5a.pdf", "description": "ARS", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000060/zg202210k5a.pdf"}, {"form": "10-K", "file_date": "2023-02-15", "period_ending": "2022-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-23-000010", "document": "z-20221231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 9 results: ZILLOW GROUP, INC. - Form 10-K - FY2024 (Annual Financial Statement Tables - full year 2024) <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/Financial_Report.xlsx>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000125/q32024991.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000125/exhibit993.htm>; ZILLOW GROUP, INC. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000012/exhibit993.htm>
- web_search(query="Zillow 10-K 2024 Follow Up Boss acquisition ShowingTime+ revenue by segment Residential Rentals Mortgages percent of total revenue") → 0 results: 
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "key": "z10k2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: z10k2024. (467,105 characters)
  The data_storage currently contains the following keys:
  z10k2024
  

### Turn 3  (stop_reason=tool_use)
- web_search(query=null) → 9 results: ZILLOW GROUP, INC. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm>; ZILLOW GROUP, INC. - Form 10-K - FY2024 (Annual Financial Statement Tables - full year 2024) <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/Financial_Report.xlsx>; ZILLOW GROUP, INC. (Form: 10-K, Received: 02/11/2025 16:21:55) <https://content.edgar-online.com/ExternalLink/EDGAR/0001617640-25-000016.html?hash=0cbc5b58372fd7624126f2551e8e8a884de4b57fe379aaaa014e219af2339afa&dest=z-20241231_htm>; How Does Zillow Make Money? Zillow Business Model (2026) <https://fourweekmba.com/how-does-zillow-make-money/>; exhibit993 <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000015/exhibit993.htm>
- web_search(query="Zillow acquires Aryeo 2024") → 0 results: 
- retrieve_information({"prompt": "From this Zillow 10-K for FY2024, extract: (1) all acquisitions completed in 2023 and 2024 (names, dates, purchase prices, strategic rationale), including Aryeo and Follow Up Boss; (2) revenue by category for 2024 and 2023 (Residential, Mortgages, Rentals, Other, For Sale subtotal) with amounts and percentage of total revenue; (3) any statements about strategy shifts (e.g., Zillow Home Loans, mortgage marketplace, Zillow Offers, software investment, rentals growth). Quote exact figures and cite section context.\n\n{{z10k2024}}"})
  result: # Zillow Group FY2024 10-K: Extracted Data
  
  All figures are in millions of USD unless noted. Section references are to the 10-K.
  
  ## (1) Acquisitions, 2023–2024
  
  | Acquisition | Close Date | Purchase Price (per filing) | Business | Key Allocations |
  |---|---|---|---|---|
  | **Aryeo, Inc.** | July 31, 2023 | ~$15M cash, net of cash acquired, plus 380,259 Class C shares valued at $20M. Text says "total consideration of $35 million, net of cash acquired"; the allocation table totals **$38** (see note below). | Software company serving real estate photographers (Note 6). | Goodwill $26; intangibles $11 (customer relationships $5, 5-yr life; purchased content $4, 3-yr; developed technology $2, 3-yr) |
  | **Spruce Holdings, Inc.** (substantially all assets and liabilities) | September 11, 2023 | ~$19M cash, net of cash acquired; allocation table totals **$24** | "Tech-enabled title and escrow platform" (Note 6) | Goodwill $16 (tax-deductible); intangibles $2 (developed technology, 3-yr) |
  | **Enchant, LLC d/b/a Follow Up Boss** | December 8, 2023 | **$399** cash, net of cash acquired, plus contingent consideration of **up to $100** payable over three years. Total purchase price allocated: **$484** (cash $403 + contingent consideration $81 at fair value). | CRM system for real estate professionals (Item 1, Note 6) | Goodwill $402; intangibles $86 (developed technology $50, 4-yr; customer relationships $34, 7-yr; trade names $2, 7-yr) |
  | **Virtual Staging AI Inc.** | October 2024 | **Not disclosed.** Named only in Item 1A. | Not described | Not disclosed |
  
  **Aggregate 2023 cash paid for acquisitions, net:** $433 (cash flow statement). This reconciles to Follow Up Boss ($399) + Aryeo (~$15) + Spruce (~$19) = $433.
  
  **2024 cash paid for acquisitions, net:** $7 (cash flow statemen
  …[truncated 1,779 chars]

### Turn 4  (stop_reason=tool_use)
- web_search(query=null) → 10 results: ZILLOW GROUP, INC. - Form 10-Q - FY2024 (Quarterly Earnings Tables - quarter ended Sep 2024) <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000126/Financial_Report.xlsx>; ZILLOW GROUP, INC. - Form 10-K - FY2024 (Annual Financial Statement Tables - full year 2024) <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/Financial_Report.xlsx>; ZILLOW GROUP, INC. - Form 10-Q - FY2024 (Quarterly Earnings Tables - quarter ended Jun 2024) <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000094/Financial_Report.xlsx>; ZILLOW GROUP, INC. - Form 10-Q - FY2024 (Quarterly Earnings Tables - quarter ended Mar 2024) <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000070/Financial_Report.xlsx>; ZILLOW GROUP, INC. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm>
- retrieve_information({"prompt": "From this Zillow FY2024 10-K, give the revenue table for years ended Dec 31, 2024 and 2023: Residential, Mortgages, For Sale revenue, Rentals, Other, Total revenue, in millions, and percentage of total for 2024 and 2023 if stated. Also the sentence describing total revenue growth and the Virtual Staging AI acquisition, and any statement on Zillow Home Loans / mortgage strategy and rentals/multifamily strategy.\n\n{{z10k2024}}"})
  result: ## Revenue Table (Years Ended December 31, in millions)
  
  | Revenue Category | 2024 | % of Total 2024 | 2023 | % of Total 2023 |
  |---|---|---|---|---|
  | Residential | $1,594 | 71% | $1,452 | 75% |
  | Mortgages | 145 | 6% | 96 | 5% |
  | **For Sale revenue (subtotal)** | **1,739** | **78%** | **1,548** | **80%** |
  | Rentals | 453 | 20% | 357 | 18% |
  | Other | 44 | 2% | 40 | 2% |
  | **Total revenue** | **$2,236** | **100%** | **$1,945** | **100%** |
  
  *Source: MD&A Results of Operations table (p. 44) and Consolidated Statements of Operations (p. 62). Percentages are as stated in the filing.*
  
  ## Total Revenue Growth
  
  "For the years ended December 31, 2024 and 2023, we generated total revenue of $2.2 billion and $1.9 billion, respectively, representing a year-over-year increase of 15%." The MD&A also states that "Total revenue increased $291 million, or 15%, to $2.2 billion."
  
  ## Virtual Staging AI Acquisition
  
  The 10-K mentions this acquisition only once, in the risk factor on acquisitions: "we acquired ... Virtual Staging AI Inc. in October 2024." The filing gives no purchase price, accounting details, or revenue contribution. Note 6 (Acquisitions) covers only Follow Up Boss, Aryeo and Spruce.
  
  ## Zillow Home Loans / Mortgage Strategy
  
  - **Operations:** Zillow Home Loans is available in 49 states and the District of Columbia. It originates mortgage loans and generally sells them on the secondary market.
  - **Integration with For Sale:** In Enhanced Markets, consumers are supported by Premier Agent partners and Zillow Home Loans loan officers. The company says it sees "higher transaction conversion rates for agent partners working with buyers who choose Zillow Home Loans."
  - **Growth focus:** Mortgages revenue rose $49 million (51%), driven by a $64 million increase in mortgage 
  …[truncated 2,006 chars]

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "\n**Short answer:** Over 2023–2024, Zillow's acquisitions were concentrated in real estate software that feeds its largest segment, Residential. Revenue growth and the mix shift toward Rentals and Mortgages came mostly from organic growth and partnerships, not from M&A. Acquisition spending also slowed sharply in 2024. (Scope note: I used the FY2024 10-K, filed February 2025, and the Q4 2024 results letter. I excluded later data such as 2025 quarterly results, since it postdates April 7, 2025.)\n\n**1. Acquisition strategy (2023–2024)**\n\n- **Software-first M&A.** Zillow's stated approach was to buy tools for agents and sellers. <cite index=\"1-3\">The acquisition is consi
…[truncated 5,063 chars])

### Final answer

**Short answer:** Over 2023–2024, Zillow's acquisitions were concentrated in real estate software that feeds its largest segment, Residential. Revenue growth and the mix shift toward Rentals and Mortgages came mostly from organic growth and partnerships, not from M&A. Acquisition spending also slowed sharply in 2024. (Scope note: I used the FY2024 10-K, filed February 2025, and the Q4 2024 results letter. I excluded later data such as 2025 quarterly results, since it postdates April 7, 2025.)

**1. Acquisition strategy (2023–2024)**

- **Software-first M&A.** Zillow's stated approach was to buy tools for agents and sellers. <cite index="1-3">The acquisition is consistent with our strategy to invest in a more integrated software experience for our customers.</cite> The 10-K describes its software push this way: <cite index="12-4">we acquired Aryeo and Follow Up Boss, which provide real estate professionals tools to manage leads, create listings, and effectuate transactions.</cite>
- **Deals completed (per the FY2024 10-K):**
  - Aryeo (July 31, 2023): software for real estate photographers. Filings state <cite index="19-3">total consideration of $35 million, net of cash acquired</cite>, while the purchase price allocation table totals $38M. I flag this as a reporting inconsistency.
  - Spruce (September 11, 2023): <cite index="19-4">substantially all of the assets and liabilities of Spruce, a tech-enabled title and escrow platform, in exchange for approximately $19 million in cash, net of cash acquired.</cite>
  - Follow Up Boss (December 8, 2023): <cite index="1-1">$399 million in cash, net of cash acquired, and contingent consideration of up to $100 million in cash, payable over a three-year period</cite>. The total purchase price was $484M, including $81M of contingent consideration at fair value.
  - Virtual Staging AI (October 2024): the filing names it only in a risk factor and gives no price or rationale.
- **Scale of spending.** Net cash paid for acquisitions was $433M in 2023, so Follow Up Boss alone accounts for about 92.15% of that figure (399 / 433). In 2024, net cash paid for acquisitions fell to $7M, which shows a clear pause in M&A.
- **Post-period pivot to partnerships.** In February 2025, Zillow <cite index="4-6">entered a rentals partnership with Redfin, making it the exclusive provider of multifamily rental listings</cite> with a $100 million upfront payment to Redfin. This suggests that rentals growth was being pursued through commercial deals rather than acquisitions.

**2. Evolving revenue mix**

| Category | 2024 ($M) | % of total 2024 | 2023 ($M) | % of total 2023 | 2024 YoY growth |
|---|---|---|---|---|---|
| Residential | 1,594 | 71% | 1,452 | 75% | 9.78% |
| Mortgages | 145 | 6% | 96 | 5% | 51.04% |
| Rentals | 453 | 20% | 357 | 18% | 26.89% |
| Other | 44 | 2% | 40 | 2% | 10.00% |
| Total | 2,236 | 100% | 1,945 | 100% | 14.99% |

Source for the table: the FY2024 10-K revenue table. Growth rates are my calculations from those figures, and the percentages match the filing.

Key points:
- Residential, the segment that includes the acquired software (Follow Up Boss, ShowingTime+), still produced most revenue but fell from 75% to 71% of the total.
- Rentals and Mortgages gained share. Rentals rose from 18% to 20%, and Mortgages from 5% to 6%.
- The Residential segment's growth was partly acquisition-driven. The 10-K attributes part of its increase to <cite index="4-2">the inclusion of revenue from Follow Up Boss, which we acquired in December 2023</cite>, along with Premier Agent conversion gains.

**3. How the strategy aligns with the mix shift**

- **Alignment:** The software acquisitions reinforce the Residential franchise, which remains the core of the business, and they support the "integrated transaction" model. Acquired tools such as Follow Up Boss also help Zillow retain agent relationships in its Enhanced Markets.
- **Partial misalignment or limited M&A role:** The mix shift toward Rentals and Mortgages was mostly organic. In Mortgages, the 10-K attributes the growth to <cite index="4-7">our strategic focus on growing Zillow Home Loans purchase loan origination volume</cite>, and total origination volume rose 101%. Rentals grew through multifamily listings and marketing, not through acquisitions.
- **Shift away from mortgage M&A:** Mortgage marketplace revenue declined as Zillow <cite index="7-4">shifted strategic priority as we focus on organic growth of our mortgage origination business.</cite>
- **Net assessment:** Zillow's 2023 acquisitions strengthened its software layer inside Residential, but the faster-growing Rentals and Mortgages lines gained share through organic investment and partnerships. As of the FY2024 10-K, the company was prioritizing organic growth and commercial partnerships in those segments, while acquisition activity was largely paused in 2024.

**Sources**
- Zillow FY2024 10-K (main document): https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm
- Zillow FY2024 10-K financial report tables: https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/Financial_Report.xlsx
- Zillow Q4 2024 shareholder letter exhibit: https://www.sec.gov/Archives/edgar/data/1617640/000161764025000015/exhibit993.htm
- Zillow Q2 2024 shareholder letter exhibit: https://www.sec.gov/Archives/edgar/data/1617640/000161764024000095/exhibit993.htm
- Zillow Q1 2024 shareholder letter exhibit: https://www.sec.gov/Archives/edgar/data/1617640/000161764024000069/exhibit993.htm
- Zillow Q3 2024 10-Q (Aryeo and Spruce acquisitions): https://www.sec.gov/Archives/edgar/data/1617640/000161764024000126/z-20240930.htm
