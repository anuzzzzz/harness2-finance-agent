## Rollout `static1`
- outcome: submitted
- turns: 5; cost: $0.295; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Spirit Airlines 10-K 2024 operating statistics available seat miles load factor") → 0 results: 
- edgar_search({"search_query": "Spirit Airlines annual report 2024 operating statistics", "ciks": ["SAVE"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  ERROR: ValueError: Unknown ticker 'SAVE'. Provide a numeric CIK instead.

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Spirit Airlines, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm>; Spirit Aviation Holdings, Inc. (Form: 10-K, Received: 03/16/2026 17:23:02) <https://www.otcmarkets.com/filing/html?id=19253367&guid=ynC-kpluZfruQOh>; Spirit Airlines 2024 Operating Analysis <https://www.scribd.com/document/867528160/discussion-7-spirit>; Spirit Aviation Holdings, Inc. - 10K - Annual Report - February 9, 2024 <https://fintel.io/doc/sec-spirit-airlines-inc-1498710-10k-2024-february-09-19762-4794>; Spirit Airlines, Inc. <https://www.sec.gov/Archives/edgar/data/1498710/000149871024000192/save-20240630.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm", "key": "save10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: save10k. (635,378 characters)
  The data_storage currently contains the following keys:
  save10k
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Spirit Airlines FY2024 10-K, list every operating KPI / operating statistic the company tracks (e.g., in the \"Comparative Operating Statistics\" table and any \"Key Performance Indicators\" or non-GAAP/operating metrics section). For each, give the FY2024 (twelve months ended December 31, 2024) total value exactly as reported, with units, and the 2023 comparison. Also note the section heading where each appears. Text: {{save10k}}"})
  result: I'll work from the "Comparative Operating Statistics" table in Item 7 (MD&A), plus the other operating metrics the filing defines in its MD&A and Glossary. Values are as reported in the filing.
  
  **Section heading: "Comparative Operating Statistics" (Item 7, MD&A, "Operating Statistics (unaudited)")**
  
  | Metric | FY2024 (12 months ended Dec 31, 2024) | FY2023 | % Change (as reported) |
  |---|---|---|---|
  | Average aircraft | 209.9 | 199.5 | 5.2% |
  | Aircraft at end of period (includes 21 held for sale) | 213 | 205 | 3.9% |
  | Average daily aircraft utilization (hours) | 9.9 | 11.1 | (10.8)% |
  | Departures | 288,180 | 297,900 | (3.3)% |
  | Passenger flight segments (PFSs) (thousands) | 44,180 | 44,105 | 0.2% |
  | Revenue passenger miles, RPMs (thousands) | 43,671,009 | 45,243,787 | (3.5)% |
  | Available seat miles, ASMs (thousands) | 53,017,948 | 55,665,561 | (4.8)% |
  | Load factor (%) | 82.4% | 81.3% | 1.1 pts |
  | Total revenue per passenger flight segment ($) | 111.21 | 121.58 | (8.5)% |
  | Average yield (cents) | 11.25 | 11.85 | (5.1)% |
  | TRASM (cents) | 9.27 | 9.63 | (3.7)% |
  | CASM (cents) | 11.35 | 10.52 | 7.9% |
  | Adjusted CASM (cents) | 10.76 | 10.33 | 4.2% |
  | Adjusted CASM ex-fuel (cents) | 7.97 | 7.06 | 12.9% |
  | Fuel gallons consumed (thousands) | 551,819 | 591,796 | (6.8)% |
  | Average fuel cost per gallon ($) | 2.68 | 3.08 | (13.0)% |
  
  **Other operating metrics disclosed outside that table**
  
  - **Operating Revenues table (Item 7, "Operating Revenues"):** TRASM 9.27 cents (−3.7%) and total revenue per passenger flight segment $111.21 (−8.5%), same values as above.
  - **CASM table (Item 7, "Operating Expenses"):** Per-ASM cost line items for 2024 vs. 2023 (CASM 11.35 vs. 10.52; Salaries, wages and benefits 3.19 vs. 2.90; Aircraft fuel 2.79 vs. 3.27; Aircraft rent 1.0
  …[truncated 1,593 chars]

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "Quote the exact rows of the \"Comparative Operating Statistics\" table and the Operating Revenues / Operating Expenses per-ASM tables for 2024 and 2023 from this text, including any rows for average yield, TRASM, CASM, Adjusted CASM, total revenue per passenger flight segment, fuel gallons, and average fuel cost per gallon. Text: {{save10k}}"})
  result: ## Comparative Operating Statistics (Twelve Months Ended December 31)
  
  | Operating Statistic | 2024 | 2023 | Percent Change |
  |---|---|---|---|
  | Average aircraft | 209.9 | 199.5 | 5.2 % |
  | Aircraft at end of period (B) | 213 | 205 | 3.9 % |
  | Average daily aircraft utilization (hours) | 9.9 | 11.1 | (10.8)% |
  | Departures | 288,180 | 297,900 | (3.3)% |
  | Passenger flight segments (PFSs) (thousands) | 44,180 | 44,105 | 0.2 % |
  | Revenue passenger miles (RPMs) (thousands) | 43,671,009 | 45,243,787 | (3.5)% |
  | Available seat miles (ASMs) (thousands) | 53,017,948 | 55,665,561 | (4.8)% |
  | Load factor (%) | 82.4 % | 81.3 % | 1.1 pts |
  | Total revenue per passenger flight segment ($) | 111.21 | 121.58 | (8.5)% |
  | **Average yield (cents)** | **11.25** | **11.85** | **(5.1)%** |
  | **TRASM (cents)** | **9.27** | **9.63** | **(3.7)%** |
  | **CASM (cents)** | **11.35** | **10.52** | **7.9 %** |
  | **Adjusted CASM (cents)** | **10.76** | **10.33** | **4.2 %** |
  | Adjusted CASM ex-fuel (cents) | 7.97 | 7.06 | 12.9 % |
  | **Fuel gallons consumed (thousands)** | **551,819** | **591,796** | **(6.8)%** |
  | **Average fuel cost per gallon ($)** | **2.68** | **3.08** | **(13.0)%** |
  
  ## Operating Revenues
  
  | Line item | 2024 | % change 2024 vs. 2023 | 2023 |
  |---|---|---|---|
  | Passenger (thousands) | 4,811,752 | (8.7)% | 5,268,161 |
  | Other (thousands) | 101,669 | 7.7% | 94,388 |
  | Total operating revenue (thousands) | $4,913,421 | (8.4)% | $5,362,549 |
  | **Total operating revenue per ASM (TRASM) (cents)** | **9.27** | **(3.7)%** | **9.63** |
  | **Total revenue per passenger flight segment** | **$111.21** | **(8.5)%** | **$121.58** |
  
  The text does not present a separate per-ASM table for average yield in the operating revenues section. Average yield (11.25 cents in 2024, 11.85 cents in 2
  …[truncated 1,588 chars]

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "Spirit Airlines (NYSE: SAVE, CIK 1498710) does not label a separate \"Key Performance Indicators\" section in its FY2024 Form 10-K. Its operating metrics sit in the MD&A \"Comparative Operating Statistics\" table (twelve months ended December 31, 2024 vs. 2023), plus the per-ASM operating revenue and expense tables and the fuel table. The FY2024 totals are below.\n\n**Operating statistics table (Item 7, MD&A)**\n\n| KPI | FY2024 Total | FY2023 | % Change |\n|---|---|---|---|\n| Average aircraft | 209.9 | 199.5 | 5.2% |\n| Aircraft at end of period | 213 | 205 | 3.9% |\n| Average daily aircraft utilization (hours) | 9.9 | 11.1 | (10.8)% |\n| Departures | 288,180 | 297,900 | 
…[truncated 1,958 chars])

### Final answer
Spirit Airlines (NYSE: SAVE, CIK 1498710) does not label a separate "Key Performance Indicators" section in its FY2024 Form 10-K. Its operating metrics sit in the MD&A "Comparative Operating Statistics" table (twelve months ended December 31, 2024 vs. 2023), plus the per-ASM operating revenue and expense tables and the fuel table. The FY2024 totals are below.

**Operating statistics table (Item 7, MD&A)**

| KPI | FY2024 Total | FY2023 | % Change |
|---|---|---|---|
| Average aircraft | 209.9 | 199.5 | 5.2% |
| Aircraft at end of period | 213 | 205 | 3.9% |
| Average daily aircraft utilization (hours) | 9.9 | 11.1 | (10.8)% |
| Departures | 288,180 | 297,900 | (3.3)% |
| Passenger flight segments (thousands) | 44,180 | 44,105 | 0.2% |
| Revenue passenger miles (RPMs, thousands) | 43,671,009 | 45,243,787 | (3.5)% |
| Available seat miles (ASMs, thousands) | 53,017,948 | 55,665,561 | (4.8)% |
| Load factor (%) | 82.4% | 81.3% | 1.1 pts |
| Total revenue per passenger flight segment ($) | 111.21 | 121.58 | (8.5)% |
| Average yield (cents) | 11.25 | 11.85 | (5.1)% |
| TRASM – total operating revenue per ASM (cents) | 9.27 | 9.63 | (3.7)% |
| CASM – operating cost per ASM (cents) | 11.35 | 10.52 | 7.9% |
| Adjusted CASM (cents) | 10.76 | 10.33 | 4.2% |
| Adjusted CASM ex-fuel (cents) | 7.97 | 7.06 | 12.9% |
| Fuel gallons consumed (thousands) | 551,819 | 591,796 | (6.8)% |
| Average fuel cost per gallon ($) | 2.68 | 3.08 | (13.0)% |

**Calculation check:** Load factor is RPMs ÷ ASMs = 43,671,009 ÷ 53,017,948 = 82.37%, which rounds to the reported 82.4%. TRASM is consistent with total operating revenue of $4,913,421 thousand ÷ 53,017,948 thousand ASMs = 9.27 cents.

**Related per-ASM cost detail (Item 7, Operating Expenses), FY2024 cents per ASM:** Salaries, wages and benefits 3.19; aircraft fuel 2.79; aircraft rent 1.02; landing fees and other rentals 0.85; depreciation and amortization 0.61; maintenance, materials and repairs 0.41; distribution 0.37; special charges 0.07; loss on disposal of assets 0.52; other operating expenses 1.52.

**Note:** Average yield and total revenue per passenger flight segment appear only in the statistics table and the revenue section. The filing's operating-revenue table reports passenger revenue of $4,811,752 thousand and total operating revenue of $4,913,421 thousand for 2024.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm",
            "name": "Spirit Airlines, Inc. - Form 10-K - FY2024 (SEC EDGAR)"
        }
    ]
}