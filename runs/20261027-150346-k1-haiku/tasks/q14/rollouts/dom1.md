## Rollout `dom1`
- outcome: submitted
- turns: 4; cost: $0.099; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "fcf_margin_trend"})
  result: ---
  name: fcf_margin_trend
  description: Compute free cash flow (CFO minus capex) and FCF margin (FCF / revenue) for several fiscal years and describe the trend, with consistent capex definition and flagged distortions.
  ---
  ANALYTIC MOVE: calculate then explain a trend. For each fiscal year: FCF = net cash provided by operating activities - capex; FCF margin = FCF / total revenue. Then state the direction year to year and over the whole span.
  
  1. Inputs, each retrieved from the cash-flow statement and income statement (not from memory), for every year asked: CFO, each investing-line capex item, total revenue. A 10-K carries three years of both statements, so the latest 10-K covers a 3-year window; open the older 10-K too if you need to confirm a year or if figures may have been recast.
  2. Capex definition. Name the lines used. Check the MD&A liquidity section for the company's own stated capex total and reconcile to it. Capitalized software is often inside "purchases of intangible assets" or a "capitalized software" line, not "purchases of property and equipment". Headline capex = PP&E purchases plus capitalized software / intangible purchases (the company-stated total when MD&A gives one). Because "capex" is ambiguous, also show the margin on PP&E-only as a one-line labelled alternate, and say whether the trend direction changes. Do not include acquisitions, investments or purchases of securities.
  3. Basis and period checks. Revenue and CFO must cover the same scope: if a business was moved to discontinued operations, the revenue line may be continuing operations only while the cash-flow statement still includes the discontinued business. Say so. Check units (millions) and that each figure's fiscal year matches the question.
  4. Distortions. A margin above 100% or a swin
  …[truncated 1,944 chars]
- edgar_search({"search_query": "Zillow Group annual report 10-K cash flows from operating activities", "ciks": ["ZG"], "form_types": ["10-K"], "start_date": "2025-01-01"})
  result: {"total_matching_documents": 1, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-11", "period_ending": "2024-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-25-000016", "document": "z-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "key": "zg_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: zg_10k_2024. (467,105 characters)
  The data_storage currently contains the following keys:
  zg_10k_2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow 10-K, extract: net cash provided by operating activities for 2024, 2023, 2022; purchases of property and equipment for each year; purchases of intangible assets (including capitalized internal-use software) for each year; total revenue for 2024, 2023, 2022; the decrease in inventory amounts for 2022; and any MD&A statement of total capital expenditures for 2024. Give exact figures in millions and note the table/section. Document: {{zg_10k_2024}}"})
  result: # Zillow Group, Inc. FY2024 Form 10-K: Extracted Figures (in millions, USD)
  
  | Item | 2024 | 2023 | 2022 | Source |
  |---|---|---|---|---|
  | Net cash provided by operating activities | $428 | $354 | $4,504 | Item 8, Consolidated Statements of Cash Flows; also MD&A, "Summarized Cash Flow Information" (2024 and 2023) |
  | Purchases of property and equipment | $(143) | $(135) | $(115) | Item 8, Consolidated Statements of Cash Flows, Investing activities |
  | Purchases of intangible assets (incl. capitalized internal-use software) | $(28) | $(30) | $(25) | Item 8, Consolidated Statements of Cash Flows, Investing activities |
  | Total revenue | $2,236 | $1,945 | $1,958 | Item 8, Consolidated Statements of Operations; also MD&A Results of Operations |
  
  **Additional items**
  
  - **Decrease in inventory, 2022:** $3,904. This is the "Inventory" line under Changes in operating assets and liabilities in the 2022 Consolidated Statements of Cash Flows (Item 8). It is a positive adjustment, so it represents a cash inflow from a reduction in inventory. It reflects the wind-down of Zillow Offers, which was completed in Q3 2022 (see Note 3). The 2022 operating cash flow of $4,504 is largely driven by this inventory liquidation. The 2024 and 2023 inventory lines are zero.
  - **MD&A capital expenditure statement, 2024:** Under Item 7, "Liquidity and Capital Resources," in "Cash Flows Provided By Investing Activities," the filing states: "For the year ended December 31, 2024, net cash provided by investing activities was $395 million. This was primarily the result of $573 million of net proceeds from maturities and sales of investments and $171 million of purchases of property and equipment and intangible assets." The MD&A does not use the phrase "total capital expenditures." The $171 million equ
  …[truncated 168 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Zillow Group (FY ends Dec 31), FCF = net cash provided by operating activities (CFO) minus capex. Figures in $ millions, verified against the FY2024 10-K (Item 8 cash flow statement and income statement; MD&A liquidity section).\n\nInputs and results\n- FY2022: CFO 4,504; PP&E purchases 115; intangible assets incl. capitalized internal-use software 25; headline capex 140; FCF 4,364; total revenue 1,958; FCF margin 4,364 / 1,958 = 222.88%.\n- FY2023: CFO 354; PP&E 135; intangibles 30; headline capex 165; FCF 189; revenue 1,945; FCF margin 189 / 1,945 = 9.72%.\n- FY2024: CFO 428; PP&E 143; intangibles 28; headline capex 171; FCF 257; revenue 2,236; FCF margin 257 / 2,236 = 11
…[truncated 2,075 chars])

### Final answer
Zillow Group (FY ends Dec 31), FCF = net cash provided by operating activities (CFO) minus capex. Figures in $ millions, verified against the FY2024 10-K (Item 8 cash flow statement and income statement; MD&A liquidity section).

Inputs and results
- FY2022: CFO 4,504; PP&E purchases 115; intangible assets incl. capitalized internal-use software 25; headline capex 140; FCF 4,364; total revenue 1,958; FCF margin 4,364 / 1,958 = 222.88%.
- FY2023: CFO 354; PP&E 135; intangibles 30; headline capex 165; FCF 189; revenue 1,945; FCF margin 189 / 1,945 = 9.72%.
- FY2024: CFO 428; PP&E 143; intangibles 28; headline capex 171; FCF 257; revenue 2,236; FCF margin 257 / 2,236 = 11.49%.

Capex definition: headline capex = purchases of property and equipment + purchases of intangible assets (capitalized software). The FY2024 MD&A states $171 million of purchases of property and equipment and intangible assets for 2024, which reconciles to this definition (143 + 28). The MD&A figure for 2023 is $165 million, which also matches. Acquisitions, investments and securities purchases are excluded.

PP&E-only alternate (labelled): FY2022 (4,504 - 115) / 1,958 = 224.16%; FY2023 (354 - 135) / 1,945 = 11.26%; FY2024 (428 - 143) / 2,236 = 12.75%. On this basis the FY2023 to FY2024 direction is also up, so the trend direction does not change.

Trend
- FY2022 to FY2023: margin fell by about 213.16 percentage points (222.88% to 9.72%).
- FY2023 to FY2024: margin rose by about 1.78 percentage points (9.72% to 11.49%).
- End to end (FY2022 to FY2024): margin fell by about 211.39 percentage points, but this is not a meaningful comparison.

Distortion flag: FY2022 CFO is inflated by a 3,904 million inventory decrease (a cash inflow) from the wind-down of the Zillow Offers home-buying business, completed in Q3 2022. The FY2022 margin of about 223% is a one-off and is not comparable to later years. Excluding it, the underlying FCF margin trend from FY2023 to FY2024 is an improvement of roughly 1.78 percentage points, from about 9.7% to about 11.5%, with FCF rising from 189 to 257 million.

Basis note: revenue is continuing operations only (Zillow Offers is discontinued), but the cash flow statement still includes the discontinued business's cash flows. This mismatch affects all years, most strongly FY2022.

Sources: Zillow Group FY2024 Form 10-K (filed 2025-02-11). I did not open the FY2023 or FY2022 10-Ks; the prior-year figures come from the comparative columns of the FY2024 10-K.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm",
            "name": "Zillow Group, Inc. Form 10-K for fiscal year 2024"
        }
    ]
}