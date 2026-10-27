## Rollout `base1`
- outcome: submitted
- turns: 4; cost: $0.200; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Zillow Group annual report net cash provided by operating activities capital expenditures", "ciks": ["1617640"], "form_types": ["10-K"], "start_date": "2023-01-01", "end_date": "2025-04-07"})
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
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow 10-K text: {{z2024}} — extract the consolidated statements of cash flows: Net cash provided by operating activities, and Purchases of property and equipment / capitalized software (capex) lines, for fiscal 2024, 2023, and 2022. Also extract total revenue for 2024, 2023, 2022. Give exact numbers in thousands."})
  result: The 10-K reports these figures in **millions**, not thousands, so exact figures in thousands aren't available. Below are the figures as reported, with the thousands equivalent (the reported millions × 1,000).
  
  | Item | 2024 | 2023 | 2022 |
  |---|---|---|---|
  | **Net cash provided by operating activities** | $428M (428,000 thousand) | $354M (354,000 thousand) | $4,504M (4,504,000 thousand) |
  | **Purchases of property and equipment** | $(143)M (143,000 thousand) | $(135)M (135,000 thousand) | $(115)M (115,000 thousand) |
  | **Purchases of intangible assets** | $(28)M (28,000 thousand) | $(30)M (30,000 thousand) | $(25)M (25,000 thousand) |
  | **Total revenue** | $2,236M (2,236,000 thousand) | $1,945M (1,945,000 thousand) | $1,958M (1,958,000 thousand) |
  
  Notes:
  - The cash flow statement has no line labeled "capitalized software." Software and website development spending is split between "Purchases of property and equipment" and "Purchases of intangible assets," so I listed both. Capitalized website development costs were $196M in 2024, $191M in 2023, and $143M in 2022, per Note 5, but those are disclosed in the notes, not the cash flow statement.
  - The 2022 operating cash flow of $4,504M includes discontinued operations (Zillow Offers), which contributed a $3,904M inventory change, so it isn't comparable to 2023 or 2024.
- retrieve_information({"prompt": "From this Zillow 10-K text: {{z2023}} — extract the consolidated statements of cash flows: Net cash provided by operating activities, and Purchases of property and equipment / capitalized software (capex) lines, for fiscal 2023, 2022, and 2021. Also extract total revenue for 2023, 2022, 2021. Give exact numbers in thousands."})
  result: The filing reports these figures in **millions**, not thousands, and does not disclose exact figures in thousands. The values below are the reported millions converted to thousands by appending three zeros.
  
  | Item (USD) | FY2023 | FY2022 | FY2021 |
  |---|---|---|---|
  | **Net cash provided by (used in) operating activities** | 354,000 | 4,504,000 | (3,177,000) |
  | **Purchases of property and equipment** (capex) | (135,000) | (115,000) | (74,000) |
  | *Purchases of intangible assets (separate line)* | *(30,000)* | *(25,000)* | *(31,000)* |
  | **Total revenue** | 1,945,000 | 1,958,000 | 2,132,000 |
  
  The cash flow statement lists "Purchases of property and equipment" and "Purchases of intangible assets" as separate lines. The filing has no line labeled "capitalized software," so I've shown intangibles separately. If you want a combined capex figure, it would be 165,000 (2023), 140,000 (2022), and 105,000 (2021).
  
  The 2022 and 2021 operating cash flows include discontinued Zillow Offers operations, which were not separated in the cash flow statement. The 2022 figure is driven largely by a $3.9 billion decrease in inventory as that wind-down progressed.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Approach:** Free Cash Flow = Net cash provided by operating activities (CFO) − Capex, where Capex = \"Purchases of property and equipment\" from the cash flow statement. FCF margin = FCF / Total revenue. All figures are in USD millions, from Zillow Group's 10-K filings.\n\n**Inputs (as reported):**\n| Item | FY2022 | FY2023 | FY2024 |\n|---|---|---|---|\n| CFO | 4,504 | 354 | 428 |\n| Capex (purchases of property & equipment) | 115 | 135 | 143 |\n| Total revenue | 1,958 | 1,945 | 2,236 |\n\n**Free cash flow (CFO − Capex):**\n- FY2022: 4,504 − 115 = 4,389\n- FY2023: 354 − 135 = 219\n- FY2024: 428 − 143 = 285\n\n**FCF margin:**\n- FY2022: 4,389 / 1,958 = 224.16%\n- FY2023: 
…[truncated 1,688 chars])

### Final answer
**Approach:** Free Cash Flow = Net cash provided by operating activities (CFO) − Capex, where Capex = "Purchases of property and equipment" from the cash flow statement. FCF margin = FCF / Total revenue. All figures are in USD millions, from Zillow Group's 10-K filings.

**Inputs (as reported):**
| Item | FY2022 | FY2023 | FY2024 |
|---|---|---|---|
| CFO | 4,504 | 354 | 428 |
| Capex (purchases of property & equipment) | 115 | 135 | 143 |
| Total revenue | 1,958 | 1,945 | 2,236 |

**Free cash flow (CFO − Capex):**
- FY2022: 4,504 − 115 = 4,389
- FY2023: 354 − 135 = 219
- FY2024: 428 − 143 = 285

**FCF margin:**
- FY2022: 4,389 / 1,958 = 224.16%
- FY2023: 219 / 1,945 = 11.26%
- FY2024: 285 / 2,236 = 12.75%

**Trend:** The FCF margin fell sharply from FY2022 to FY2023 (224.16% → 11.26%), then recovered in FY2024 to 12.75%. The FY2022 figure is not representative: CFO included discontinued Zillow Offers operations, mainly a roughly $3.9 billion inventory decrease as that business wound down. Excluding that distortion, the underlying trend is a modest improvement from FY2023 to FY2024 (about +1.5 percentage points).

**Sensitivity:** Zillow also reports "Purchases of intangible assets" (software/website development) separately. If capex includes these, FCF would be 4,364 / 189 / 257 for FY2022 / FY2023 / FY2024, with margins of about 222.89% / 9.72% / 11.49%. The same pattern holds: a large FY2022 distortion, then a rise from FY2023 to FY2024.

**Caveat:** The source filings report figures in millions. The parsed 10-K tables were read through an automated extraction step, so the figures are approximate and should be checked against the filings.

**Sources:**
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