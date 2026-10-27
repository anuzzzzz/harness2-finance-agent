## Rollout `ctl2`
- outcome: submitted
- turns: 4; cost: $0.153; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Spirit Airlines 2024 annual report 10-K operating statistics") → 0 results: 
- edgar_search({"search_query": "Spirit Airlines operating statistics key performance indicators 2024 ASM CASM", "ciks": ["SAVE"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  ERROR: ValueError: Unknown ticker 'SAVE'. Provide a numeric CIK instead.

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 9 results: Spirit Airlines, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm>; Spirit Aviation Holdings, Inc. - 10K - Annual Report - February 9, 2024 <https://fintel.io/doc/sec-spirit-airlines-inc-1498710-10k-2024-february-09-19762-4794>; Spirit Airlines' AWFUL 2024 Financial Results (Yowzers!!!) - One Mile at a Time <https://onemileatatime.com/news/spirit-airlines-financial-results/>; Spirit Airlines, Inc. SEC 10-K Report — TradingView News <https://www.tradingview.com/news/tradingview:c7e1213098a24:0-spirit-airlines-inc-sec-10-k-report/>; Spirit Airlines Financials: Bankruptcy, Debt & 10-K Data <https://dwuconsulting.com/dwu-ai/spirit-airlines-financial-profile>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm", "key": "spirit_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: spirit_10k_2024. (635,378 characters)
  The data_storage currently contains the following keys:
  spirit_10k_2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Spirit Airlines FY2024 10-K, find the \"Operating Statistics\" table (Comparative Operating Statistics) for the twelve months ended December 31, 2024 and 2023. List every operating KPI row name exactly as shown, with the 2024 total value, the 2023 value, and percent change. Also list the definitions of any KPIs (e.g., ASMs, RPMs, TRASM, CASM, yield, load factor, PFSs, aircraft utilization) if provided. Text: {{spirit_10k_2024}}"})
  result: ## Comparative Operating Statistics: Twelve Months Ended December 31, 2024 and 2023
  
  | Operating Statistics (unaudited) (A) | 2024 | 2023 | Percent Change |
  |---|---|---|---|
  | Average aircraft | 209.9 | 199.5 | 5.2% |
  | Aircraft at end of period (B) | 213 | 205 | 3.9% |
  | Average daily aircraft utilization (hours) | 9.9 | 11.1 | (10.8)% |
  | Departures | 288,180 | 297,900 | (3.3)% |
  | Passenger flight segments (PFSs) (thousands) | 44,180 | 44,105 | 0.2% |
  | Revenue passenger miles (RPMs) (thousands) | 43,671,009 | 45,243,787 | (3.5)% |
  | Available seat miles (ASMs) (thousands) | 53,017,948 | 55,665,561 | (4.8)% |
  | Load factor (%) | 82.4% | 81.3% | 1.1 pts |
  | Total revenue per passenger flight segment ($) | 111.21 | 121.58 | (8.5)% |
  | Average yield (cents) | 11.25 | 11.85 | (5.1)% |
  | TRASM (cents) | 9.27 | 9.63 | (3.7)% |
  | CASM (cents) | 11.35 | 10.52 | 7.9% |
  | Adjusted CASM (cents) | 10.76 | 10.33 | 4.2% |
  | Adjusted CASM ex-fuel (cents) | 7.97 | 7.06 | 12.9% |
  | Fuel gallons consumed (thousands) | 551,819 | 591,796 | (6.8)% |
  | Average fuel cost per gallon ($) | 2.68 | 3.08 | (13.0)% |
  
  Footnotes to the table:
  - (A) Definitions are in the "Glossary of Airline Terms."
  - (B) Includes 21 aircraft recorded as assets held for sale at December 31, 2024.
  
  ## KPI Definitions (from the Glossary of Airline Terms)
  
  - **Adjusted CASM:** Operating expenses, excluding loss (gain) on disposal of assets, special charges (credits), furlough-related expenses, and litigation loss contingency adjustments recorded in the first and third quarters of 2024 and a litigation loss contingency recorded in the second quarter of 2023, divided by ASMs.
  - **Adjusted CASM ex fuel:** Operating expenses excluding aircraft fuel expense, loss (gain) on disposal of assets, special charges (credits), 
  …[truncated 1,747 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Spirit Airlines (NYSE: SAVE) reported the following operating statistics in its FY2024 Form 10-K (\"Comparative Operating Statistics,\" twelve months ended December 31, 2024, unaudited). The 2023 comparatives are included for context.\n\n| KPI | FY 2024 Total | FY 2023 | % Change |\n|---|---|---|---|\n| Average aircraft | 209.9 | 199.5 | 5.2% |\n| Aircraft at end of period (includes 21 aircraft held for sale) | 213 | 205 | 3.9% |\n| Average daily aircraft utilization (hours) | 9.9 | 11.1 | (10.8)% |\n| Departures | 288,180 | 297,900 | (3.3)% |\n| Passenger flight segments (PFSs) (thousands) | 44,180 | 44,105 | 0.2% |\n| Revenue passenger miles (RPMs) (thousands) | 43,671,00
…[truncated 1,586 chars])

### Final answer
Spirit Airlines (NYSE: SAVE) reported the following operating statistics in its FY2024 Form 10-K ("Comparative Operating Statistics," twelve months ended December 31, 2024, unaudited). The 2023 comparatives are included for context.

| KPI | FY 2024 Total | FY 2023 | % Change |
|---|---|---|---|
| Average aircraft | 209.9 | 199.5 | 5.2% |
| Aircraft at end of period (includes 21 aircraft held for sale) | 213 | 205 | 3.9% |
| Average daily aircraft utilization (hours) | 9.9 | 11.1 | (10.8)% |
| Departures | 288,180 | 297,900 | (3.3)% |
| Passenger flight segments (PFSs) (thousands) | 44,180 | 44,105 | 0.2% |
| Revenue passenger miles (RPMs) (thousands) | 43,671,009 | 45,243,787 | (3.5)% |
| Available seat miles (ASMs) (thousands) | 53,017,948 | 55,665,561 | (4.8)% |
| Load factor (%) | 82.4% | 81.3% | 1.1 pts |
| Total revenue per passenger flight segment ($) | 111.21 | 121.58 | (8.5)% |
| Average yield (cents) | 11.25 | 11.85 | (5.1)% |
| TRASM (total revenue per ASM, cents) | 9.27 | 9.63 | (3.7)% |
| CASM (cents) | 11.35 | 10.52 | 7.9% |
| Adjusted CASM (cents) | 10.76 | 10.33 | 4.2% |
| Adjusted CASM ex-fuel (cents) | 7.97 | 7.06 | 12.9% |
| Fuel gallons consumed (thousands) | 551,819 | 591,796 | (6.8)% |
| Average fuel cost per gallon ($) | 2.68 | 3.08 | (13.0)% |

Key definitions from the 10-K glossary:
- ASMs: seats available for passengers multiplied by miles flown (capacity).
- RPMs: revenue passengers multiplied by miles flown (traffic).
- Load factor: RPMs divided by ASMs.
- TRASM: operating revenue divided by ASMs.
- CASM: operating expenses divided by ASMs; Adjusted CASM excludes certain special items.
- Average yield: total revenue divided by RPMs.
- Average daily aircraft utilization: block hours divided by days in the period, divided by average aircraft.

Note: the 10-K glossary does not define Departures, Total revenue per passenger flight segment, or Aircraft at end of period.

Sources: Spirit Airlines FY2024 Form 10-K (SEC EDGAR).

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm",
            "name": "Spirit Airlines, Inc. - Form 10-K - FY2024 (SEC EDGAR)"
        }
    ]
}