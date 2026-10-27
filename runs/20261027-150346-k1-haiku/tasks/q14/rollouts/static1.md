## Rollout `static1`
- outcome: submitted
- turns: 4; cost: $0.312; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Zillow Group annual report net cash provided by operating activities purchases of property and equipment", "ciks": ["1617640"], "form_types": ["10-K"], "start_date": "2023-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 3, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-11", "period_ending": "2024-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-25-000016", "document": "z-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm"}, {"form": "10-K", "file_date": "2023-02-15", "period_ending": "2022-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-23-000010", "document": "z-20221231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm"}, {"form": "10-K", "file_date": "2024-02-15", "period_ending": "2023-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000022", "document": "z-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "key": "z2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: z2024. (467,105 characters)
  The data_storage currently contains the following keys:
  z2024
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm", "key": "z2023"})
  result: SUCCESS: The result has been saved to the data storage under the key: z2023. (503,493 characters)
  The data_storage currently contains the following keys:
  z2024
  z2023
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm", "key": "z2022"})
  result: SUCCESS: The result has been saved to the data storage under the key: z2022. (527,221 characters)
  The data_storage currently contains the following keys:
  z2024
  z2023
  z2022
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow 10-K, extract from the consolidated statements of cash flows: net cash provided by operating activities for each year presented, and purchases of property and equipment, and capitalized software development costs (internal-use software) for each year. Also extract total revenue for each year presented in the consolidated statements of operations. Give exact figures in thousands with the fiscal year labels. Text: {{z2024}}"})
  result: All figures below are from the consolidated statements of cash flows and operations. The filing reports them in millions, so I've converted them to thousands by appending three zeros. Each value is exact to the million as reported.
  
  | Line item (in thousands) | FY2024 | FY2023 | FY2022 |
  |---|---|---|---|
  | Net cash provided by operating activities | $428,000 | $354,000 | $4,504,000 |
  | Purchases of property and equipment | $(143,000) | $(135,000) | $(115,000) |
  | Purchases of intangible assets (internal-use software and purchased content) | $(28,000) | $(30,000) | $(25,000) |
  | Total revenue (statement of operations) | $2,236,000 | $1,945,000 | $1,958,000 |
  
  **Note on capitalized software:** The cash flow statement has no line labeled "capitalized software development costs." The closest line is "Purchases of intangible assets," which Note 2 says includes capitalized internal-use software but also purchased content, so it overstates the software-only figure. Note 5 separately reports capitalized website development costs of $196,000 thousand (2024), $191,000 thousand (2023), and $143,000 thousand (2022). These are part of property and equipment and are not shown as a separate cash flow line. The filing does not break out internal-use software on its own.
- retrieve_information({"prompt": "From this Zillow 10-K, extract from the consolidated statements of cash flows: net cash provided by operating activities for each year presented, and purchases of property and equipment, and capitalized software development costs (internal-use software) for each year. Also extract total revenue for each year presented in the consolidated statements of operations. Give exact figures in thousands with the fiscal year labels. Text: {{z2023}}"})
  result: The filing reports these figures in **millions**, so the values below are the reported amounts multiplied by 1,000. The filing has no more precision than that.
  
  | Item (in thousands) | 2023 | 2022 | 2021 |
  |---|---|---|---|
  | **Net cash provided by (used in) operating activities** | $354,000 | $4,504,000 | $(3,177,000) |
  | **Purchases of property and equipment** | $(135,000) | $(115,000) | $(74,000) |
  | **Purchases of intangible assets (closest line to capitalized internal-use software)** | $(30,000) | $(25,000) | $(31,000) |
  | **Total revenue** | $1,945,000 | $1,958,000 | $2,132,000 |
  
  **Notes:**
  - **Capitalized software development costs:** The cash flow statement has no separate line for these. The "Purchases of intangible assets" line is the closest match. Per Note 2, it includes capitalized internal-use software and enterprise cloud computing development costs, but also purchased data content and third-party software licenses, so it is not a pure software figure. Website development costs are capitalized within property and equipment, so they are already in the "Purchases of property and equipment" line. Note 6 separately discloses $191 million (2023), $143 million (2022) and $82 million (2021) of capitalized website development costs.
  - **2022 operating cash flow:** This figure includes discontinued operations (Zillow Offers), which were not separated in the cash flow statement. The large inflow is mainly from a $3.9 billion decrease in inventory during the wind-down.
- retrieve_information({"prompt": "From this Zillow 10-K, extract from the consolidated statements of cash flows: net cash provided by operating activities for each year presented, and purchases of property and equipment, and capitalized software development costs (internal-use software) for each year. Also extract total revenue for each year presented in the consolidated statements of operations. Give exact figures in thousands with the fiscal year labels. Text: {{z2022}}"})
  result: **Zillow Group, Inc.: Selected Cash Flow and Revenue Figures (in thousands)**
  
  The filing reports these amounts in millions, so each figure below is the reported millions amount multiplied by 1,000. The exact dollar amounts are not disclosed.
  
  | Line Item | FY2022 | FY2021 | FY2020 |
  |---|---|---|---|
  | Net cash provided by (used in) operating activities | $4,504,000 | $(3,177,000) | $423,000 |
  | Purchases of property and equipment | $(115,000) | $(74,000) | $(85,000) |
  | Purchases of intangible assets (internal-use software)* | $(25,000) | $(31,000) | $(24,000) |
  | Total revenue | $1,958,000 | $2,132,000 | $1,624,000 |
  
  *The cash flow statement has no separate line for capitalized software development costs. The closest line is "Purchases of intangible assets," which Note 2 says includes capitalized internal-use software and cloud computing costs. Website development costs are capitalized within property and equipment; the notes report $143 million (2022), $82 million (2021) and $53 million (2020) of those, but the cash flow statement does not break them out.
  
  Sources: Consolidated Statements of Cash Flows and Consolidated Statements of Operations, Item 8.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Zillow Group (CIK 1617640) – Approximate FCF (CFO – Capex) and FCF margin, FY2022–FY2024**\n\nInputs (from the FY2022, FY2023 and FY2024 Form 10-K consolidated statements of cash flows and operations; the filings report in millions, shown here in $ millions):\n\n| Item | FY2022 | FY2023 | FY2024 |\n|---|---|---|---|\n| Net cash provided by operating activities (CFO) | 4,504 | 354 | 428 |\n| Purchases of property and equipment (capex) | (115) | (135) | (143) |\n| Purchases of intangible assets (internal-use software + purchased content) | (25) | (30) | (28) |\n| Total revenue | 1,958 | 1,945 | 2,236 |\n\nBase case: FCF = CFO – purchases of property and equipment (the only 
…[truncated 2,197 chars])

### Final answer
**Zillow Group (CIK 1617640) – Approximate FCF (CFO – Capex) and FCF margin, FY2022–FY2024**

Inputs (from the FY2022, FY2023 and FY2024 Form 10-K consolidated statements of cash flows and operations; the filings report in millions, shown here in $ millions):

| Item | FY2022 | FY2023 | FY2024 |
|---|---|---|---|
| Net cash provided by operating activities (CFO) | 4,504 | 354 | 428 |
| Purchases of property and equipment (capex) | (115) | (135) | (143) |
| Purchases of intangible assets (internal-use software + purchased content) | (25) | (30) | (28) |
| Total revenue | 1,958 | 1,945 | 2,236 |

Base case: FCF = CFO – purchases of property and equipment (the only capex line that is clearly a capex item on the cash flow statement).
- FY2022: 4,504 – 115 = 4,389; margin = 4,389 / 1,958 = 224.16%
- FY2023: 354 – 135 = 219; margin = 219 / 1,945 = 11.26%
- FY2024: 428 – 143 = 285; margin = 285 / 2,236 = 12.75%

Broader sensitivity (also deducting purchases of intangible assets, which include capitalized internal-use software but also purchased content):
- FY2022: 4,504 – 115 – 25 = 4,364; margin = 222.88%
- FY2023: 354 – 135 – 30 = 189; margin = 9.72%
- FY2024: 428 – 143 – 28 = 257; margin = 11.49%

Caveats:
- The cash flow statement has no separate "capitalized software" line; website development costs sit inside property and equipment.
- FY2022 CFO (~$4.5bn) is inflated by the wind-down of Zillow Offers (inventory decrease of roughly $3.9bn), and the cash flow statement does not separate discontinued operations. The FY2022 margin of ~224% is therefore not representative and should be treated as an outlier.

Trend:
- Reported FCF margin fell from about 224% in FY2022 to about 11.26% in FY2023, then rose to about 12.75% in FY2024. Measured from FY2022 to FY2024, the margin declined sharply, but this is driven by the one-off FY2022 inventory liquidation.
- Excluding FY2022, the trend is a modest recovery: margin improved from about 11.26% (FY2023) to about 12.75% (FY2024), with revenue up about 14.9% and CFO up about 21% over the same period. On the broader definition the margin moved from about 9.72% to about 11.49%, which shows the same direction.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm",
            "name": "Zillow Group FY2024 Form 10-K (filed 2025-02-11)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm",
            "name": "Zillow Group FY2023 Form 10-K (filed 2024-02-15)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm",
            "name": "Zillow Group FY2022 Form 10-K (filed 2023-02-15)"
        }
    ]
}