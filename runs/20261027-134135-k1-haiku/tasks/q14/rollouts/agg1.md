## Rollout `agg1`
- outcome: submitted
- turns: 4; cost: $0.208; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Zillow Group annual report 10-K 2024 cash flows", "ciks": ["1617640"], "form_types": ["10-K"], "start_date": "2023-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 5, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-11", "period_ending": "2024-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-25-000016", "document": "z-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm"}, {"form": "10-K", "file_date": "2024-02-15", "period_ending": "2023-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000022", "document": "z-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm"}, {"form": "10-K", "file_date": "2023-02-15", "period_ending": "2022-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-23-000010", "document": "z-20221231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm"}, {"form": "10-K", "file_date": "2024-02-15", "period_ending": "2023-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000022", "document": "a2023form10-kex312.htm", "description": "EX-31.2", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/a2023form10-kex312.htm"}, {"form": "10-K", "file_date": "2024-02-15", "period_ending": "2023-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000022", "document": "a2023form10-kex311.htm", "description": "EX-31.1", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/a2023form10-kex311.htm"
  …[truncated 3 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "key": "z2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: z2024. (467,105 characters)
  The data_storage currently contains the following keys:
  z2024
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm", "key": "z2022"})
  result: SUCCESS: The result has been saved to the data storage under the key: z2022. (527,221 characters)
  The data_storage currently contains the following keys:
  z2024
  z2022
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow 10-K document, extract for fiscal years 2024, 2023, and 2022 (as reported, in millions USD): (1) Net cash provided by operating activities (total, including any continuing operations line); (2) Purchases of property and equipment (capex); (3) Purchases of intangible assets / capitalized software if shown separately; (4) Total revenue. Give exact figures with period, unit and row label. Document: {{z2024}}"})
  result: All figures are from Zillow Group's Consolidated Statements of Cash Flows and Statements of Operations, in millions of USD. Cash outflows are shown as negatives, as reported.
  
  | Item (row label) | FY2024 | FY2023 | FY2022 |
  |---|---|---|---|
  | **(1) Net cash provided by operating activities** (cash flow statement, "Net cash provided by operating activities") | $428 | $354 | $4,504 |
  | **(2) Purchases of property and equipment** (cash flow statement, investing activities) | $(143) | $(135) | $(115) |
  | **(3) Purchases of intangible assets** (cash flow statement, investing activities) | $(28) | $(30) | $(25) |
  | **(4) Total revenue** (statement of operations, "Total revenue") | $2,236 | $1,945 | $1,958 |
  
  **Notes:**
  - **Operating cash flow:** The cash flow statement does not split operating cash flow into continuing and discontinued operations, so the figures above are totals. The FY2022 figure of $4,504 is inflated by the wind-down of Zillow Offers, mainly a $3,904 "Inventory" change in working capital. It is not comparable to FY2023 or FY2024.
  - **Capex and intangibles:** The filing shows no separate capitalized-software line. Capitalized website and software development costs are included within "Purchases of property and equipment" (the filing notes website development capitalized of $196M, $191M and $143M for 2024, 2023 and 2022). Purchases of intangible assets are shown separately above.
  - **Total revenue for FY2022:** $1,958M is continuing operations only. Zillow Offers is presented as discontinued operations, with its FY2022 revenue of $4,249M excluded.
- retrieve_information({"prompt": "From this Zillow 10-K document, extract for fiscal years 2022, 2021, and 2020 (as reported, in millions USD): (1) Net cash provided by operating activities; (2) Purchases of property and equipment; (3) Purchases of intangible assets / capitalized software if shown separately; (4) Total revenue. Give exact figures with period, unit and row label. Document: {{z2022}}"})
  result: All figures are from Zillow Group, Inc.'s FY2022 Form 10-K, in millions of USD. Cash flow figures are from the Consolidated Statements of Cash Flows, and revenue is from the Consolidated Statements of Operations.
  
  | Row label (as reported) | FY2022 | FY2021 | FY2020 |
  |---|---|---|---|
  | **(1) Net cash provided by (used in) operating activities** | $4,504 | $(3,177) | $423 |
  | **(2) Purchases of property and equipment** | $(115) | $(74) | $(85) |
  | **(3) Purchases of intangible assets** (shown as a separate line) | $(25) | $(31) | $(24) |
  | **(4) Revenue** (Consolidated Statements of Operations) | $1,958 | $2,132 | $1,624 |
  
  Notes:
  - Purchases are shown as negative numbers because they are cash outflows, as presented in the filing.
  - The filing does not show a separate line for capitalized software. Website and software development costs are capitalized within property and equipment, and the filing reports $143M, $82M and $53M of website development capitalized in 2022, 2021 and 2020, respectively (Note 8). Those amounts are not included in the purchases line above.
  - The cash flow statement does not separate discontinued operations (Zillow Offers). The operating cash flow figures therefore include both continuing and discontinued operations. The revenue figures are for continuing operations only.
  - The 2021 and 2020 figures are as presented in this FY2022 filing, so they reflect the recast for discontinued operations.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Zillow Group (CIK 1617640): FCF = CFO − purchases of property and equipment (default capex definition). Purchases of intangible assets are shown only as a sensitivity.\n\nInputs (USD millions, as reported):\n- FY2024 (10-K filed 2025-02-11): CFO $428; PP&E purchases $(143) → capex 143; FCF = 428 − 143 = 285; total revenue $2,236. FCF margin = 285 / 2,236 = 12.75% (12.7458%).\n- FY2023 (from FY2024 10-K comparative columns): CFO $354; PP&E purchases $(135) → capex 135; FCF = 354 − 135 = 219; total revenue $1,945. FCF margin = 219 / 1,945 = 11.26% (11.2596%).\n- FY2022 (FY2022 10-K, cross-checked against FY2024 10-K): CFO $4,504; PP&E purchases $(115) → capex 115; FCF = 4,504
…[truncated 2,413 chars])

### Final answer
Zillow Group (CIK 1617640): FCF = CFO − purchases of property and equipment (default capex definition). Purchases of intangible assets are shown only as a sensitivity.

Inputs (USD millions, as reported):
- FY2024 (10-K filed 2025-02-11): CFO $428; PP&E purchases $(143) → capex 143; FCF = 428 − 143 = 285; total revenue $2,236. FCF margin = 285 / 2,236 = 12.75% (12.7458%).
- FY2023 (from FY2024 10-K comparative columns): CFO $354; PP&E purchases $(135) → capex 135; FCF = 354 − 135 = 219; total revenue $1,945. FCF margin = 219 / 1,945 = 11.26% (11.2596%).
- FY2022 (FY2022 10-K, cross-checked against FY2024 10-K): CFO $4,504; PP&E purchases $(115) → capex 115; FCF = 4,504 − 115 = 4,389; continuing-operations revenue $1,958. FCF margin as reported = 4,389 / 1,958 = 224.16% (224.1573%).

Distortion: The FY2022 CFO is inflated by the wind-down of Zillow Offers (discontinued operations). The cash flow statement does not split continuing and discontinued operations, and the filing shows a $3,904M inventory working-capital inflow in 2022. The revenue denominator ($1,958M) excludes Zillow Offers' $4,249M revenue, so the 224% headline is not economically meaningful. Sensitivity only (not a filed figure): removing the $3,904M inventory inflow gives CFO ≈ $600M, FCF ≈ $485M, and a margin of about 24.77%. This is a rough adjustment because the inventory line may also include discontinued-ops effects.

Trend:
- As reported: FY2022 224.16% → FY2023 11.26% → FY2024 12.75%. The FY2022 to FY2023 change is about −212.90 pp (distorted). The FY2023 to FY2024 change is +1.49 pp (up). Across the full span FY2022 to FY2024, the margin fell by about 211.41 pp, which is driven by the 2022 distortion.
- Excluding the 2022 inventory unwind (sensitivity): FY2022 ≈ 24.77% → FY2023 11.26% → FY2024 12.75%. The margin fell about 13.51 pp from 2022 to 2023, then recovered about 1.49 pp in 2024. Net change FY2022 to FY2024 is about −12.02 pp (down).

Conclusion: On a clean, comparable basis the FCF margin declined from roughly 25% in FY2022 to about 11% in FY2023, then edged up to about 12.7% in FY2024. The as-reported 2022 figure is distorted by discontinued operations.

Sensitivity note: Adding purchases of intangible assets to capex (FY2024 $28M, FY2023 $30M, FY2022 $25M) gives FCF of 257 (FY2024, 11.49%), 189 (FY2023, 9.72%), and 4,364 (FY2022, 222.85%). The same direction holds for 2023 to 2024 (up).

Sources:
- Zillow Group FY2024 10-K (filed 2025-02-11): cash flow statement, statement of operations, and capitalized website development note.
- Zillow Group FY2022 10-K (filed 2023-02-15): cash flow statement, statement of operations, and Note 8.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm",
            "name": "Zillow Group FY2024 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm",
            "name": "Zillow Group FY2022 Form 10-K"
        }
    ]
}