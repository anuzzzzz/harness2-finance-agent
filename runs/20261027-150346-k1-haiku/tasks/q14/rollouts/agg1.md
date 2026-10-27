## Rollout `agg1`
- outcome: submitted
- turns: 4; cost: $0.100; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "fcf_margin_trend"})
  result: ---
  name: fcf_margin_trend
  description: Compute free cash flow (CFO minus capex) and FCF margin (FCF / revenue) for several fiscal years and describe the trend, with consistent capex definition and flagged distortions.
  ---
  ANALYTIC MOVE: calculate then explain a trend. For each fiscal year: FCF = net cash provided by operating activities - capex; FCF margin = FCF / total revenue. Then state the direction year to year and over the whole span.
  
  1. Inputs, each retrieved from the cash-flow statement and income statement (not from memory), for every year asked: CFO, each investing-line capex item, total revenue. The latest 10-K covers a 3-year window; open an older 10-K only if you need to confirm a year or figures may have been recast.
  2. Capex definition. Name the lines used. Check the MD&A liquidity section for the company's own stated capital-spending total and reconcile to it. Capitalized software is often inside "purchases of intangible assets", not "purchases of property and equipment". Headline capex = PP&E purchases plus capitalized software / intangible purchases (the company-stated total when MD&A gives one). Because "capex" is ambiguous, show the margin on PP&E-only as a one-line labelled alternate and say whether the trend direction changes. Exclude acquisitions, investments and purchases of securities.
  3. Basis checks. If a business was moved to discontinued operations, revenue may be continuing operations only while the cash-flow statement still includes the discontinued business. Say so. Check units and that fiscal years match the question.
  4. Distortions. A margin above 100% or a swing of more than ~10x signals a one-off (inventory liquidation, working-capital release, settlement). Find the cause in the MD&A cash-flow discussion, quantify it, and give the t
  …[truncated 1,515 chars]
- edgar_search({"search_query": "Zillow Group annual report 10-K cash flows", "ciks": ["Z"], "form_types": ["10-K"], "start_date": "2024-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 6, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-11", "period_ending": "2024-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-25-000016", "document": "z-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm"}, {"form": "10-K", "file_date": "2024-02-15", "period_ending": "2023-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000022", "document": "z-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm"}, {"form": "10-K", "file_date": "2025-02-11", "period_ending": "2024-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-25-000016", "document": "a2024form10-kex312.htm", "description": "EX-31.2", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/a2024form10-kex312.htm"}, {"form": "10-K", "file_date": "2024-02-15", "period_ending": "2023-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000022", "document": "a2023form10-kex312.htm", "description": "EX-31.2", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/a2023form10-kex312.htm"}, {"form": "10-K", "file_date": "2025-02-11", "period_ending": "2024-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-25-000016", "document": "a2024form10-kex311.htm", "description": "EX-31.1", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/a202
  …[truncated 383 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "key": "z2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: z2024. (467,105 characters)
  The data_storage currently contains the following keys:
  z2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow 10-K text: {{z2024}}. Give exact figures in $ millions for FY2024, FY2023, FY2022: net cash provided by operating activities; purchases of property and equipment; purchases of intangible assets (including capitalized internal-use software); total revenue; and the MD&A statement of capital spending total (PP&E plus intangibles) if given. Also explain the FY2022 operating cash flow driver (inventory decrease amount)."})
  result: **Figures in $ millions (fiscal years ended December 31)**
  
  | Item | FY2024 | FY2023 | FY2022 |
  |---|---|---|---|
  | Net cash provided by operating activities | 428 | 354 | 4,504 |
  | Purchases of property and equipment | (143) | (135) | (115) |
  | Purchases of intangible assets | (28) | (30) | (25) |
  | Total revenue | 2,236 | 1,945 | 1,958 |
  | Capital spending (PP&E + intangibles) | 171 | 165 | 140* |
  
  *The FY2022 total is my sum of the two cash flow lines (115 + 25). The 10-K's MD&A gives the total only for 2024 and 2023.
  
  **Notes on the capital spending figures**
  
  - The MD&A liquidity section states that 2024 investing activities included "$171 million of purchases of property and equipment and intangible assets," and 2023 included "$165 million." Both match the sums above.
  - The cash flow statement shows "Purchases of intangible assets" separately from PP&E. The intangible asset note includes a "Software" category, which is consistent with capitalized internal-use software sitting in that line. The 10-K does not explicitly say the line is only software, though.
  - Website development costs are reported within property and equipment (Note 5), not intangibles. Capitalized website development was $196M (2024), $191M (2023) and $143M (2022). These capitalized amounts differ from the cash purchases line, partly because of non-cash items such as capitalized share-based compensation ($72M in 2024, $73M in 2023, $51M in 2022).
  - Total revenue for 2022 is from continuing operations, excluding Zillow Offers, which is presented as discontinued.
  
  **FY2022 operating cash flow driver**
  
  FY2022 operating cash flow of $4,504M was driven mainly by a **$3,904M decrease in inventory** in the changes in operating assets and liabilities. This was the wind-down of Zillow Offers, the iBuying 
  …[truncated 596 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Zillow Group (CIK 1617640): approximate FCF (CFO minus capex) and FCF margin, FY2022 to FY2024\n\nInputs ($ millions; FY2024 10-K, including comparative columns for FY2023 and FY2022)\n- Net cash provided by operating activities (CFO): FY2022 4,504; FY2023 354; FY2024 428\n- Purchases of property and equipment: FY2022 115; FY2023 135; FY2024 143\n- Purchases of intangible assets (incl. capitalized internal-use software): FY2022 25; FY2023 30; FY2024 28\n- Headline capex = PP&E + intangibles: FY2022 140; FY2023 165; FY2024 171 (the MD&A states 165 for 2023 and 171 for 2024; FY2022 is my sum of the two cash-flow lines)\n- Total revenue (continuing operations): FY2022 1,958; F
…[truncated 2,017 chars])

### Final answer
Zillow Group (CIK 1617640): approximate FCF (CFO minus capex) and FCF margin, FY2022 to FY2024

Inputs ($ millions; FY2024 10-K, including comparative columns for FY2023 and FY2022)
- Net cash provided by operating activities (CFO): FY2022 4,504; FY2023 354; FY2024 428
- Purchases of property and equipment: FY2022 115; FY2023 135; FY2024 143
- Purchases of intangible assets (incl. capitalized internal-use software): FY2022 25; FY2023 30; FY2024 28
- Headline capex = PP&E + intangibles: FY2022 140; FY2023 165; FY2024 171 (the MD&A states 165 for 2023 and 171 for 2024; FY2022 is my sum of the two cash-flow lines)
- Total revenue (continuing operations): FY2022 1,958; FY2023 1,945; FY2024 2,236

Headline calculation (CFO minus PP&E plus intangibles)
- FY2022: FCF = 4,504 - 140 = 4,364; margin = 4,364 / 1,958 = 222.88%
- FY2023: FCF = 354 - 165 = 189; margin = 189 / 1,945 = 9.72%
- FY2024: FCF = 428 - 171 = 257; margin = 257 / 2,236 = 11.49%

Alternate (PP&E purchases only, cross-check)
- FY2022: 4,389 / 1,958 = 224.16%
- FY2023: 219 / 1,945 = 11.26%
- FY2024: 285 / 2,236 = 12.75%

Trend
- Year over year: FY2022 to FY2023 the headline margin fell by about 213.16 percentage points (222.88% to 9.72%). FY2023 to FY2024 it rose by about 1.78 points (9.72% to 11.49%). The PP&E-only series shows the same pattern: a large drop, then a rise of about 1.49 points (11.26% to 12.75%).
- End to end: FY2022 to FY2024 the headline margin fell by about 211.39 points (222.88% to 11.49%). Direction is downward over the full span, but this reflects the FY2022 distortion.

Distortion flag
- FY2022 is a one-off. Operating cash flow of 4,504 includes a 3,904 decrease in inventory from the Zillow Offers wind-down, so the 222.88% margin is not a run-rate figure. Excluding that release, the underlying trend from FY2023 to FY2024 is a modest improvement in FCF margin, from about 9.72% to 11.49%.
- Basis mismatch: FY2022 revenue is continuing operations only, while the cash-flow statement still includes discontinued Zillow Offers cash flows, which are not separated out.

Capex-definition note
- The headline definition uses both the PP&E purchases line and the purchases of intangible assets line, which the MD&A's stated 165 and 171 totals reconcile to for 2023 and 2024. Capitalized website development sits in PP&E and is not in the intangibles line. The PP&E-only alternate gives the same direction of trend.

Sources
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm",
            "name": "Zillow Group FY2024 Form 10-K (filed 2025-02-11)"
        }
    ]
}