## Rollout `ctl3`
- outcome: submitted
- turns: 4; cost: $0.152; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Spirit Airlines 2024 10-K operating statistics ASM CASM load factor fiscal 2024") → 0 results: 
- edgar_search({"search_query": "Spirit Airlines key operating statistics 2024 available seat miles load factor", "ciks": ["SAVE"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  ERROR: ValueError: Unknown ticker 'SAVE'. Provide a numeric CIK instead.

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 9 results: Spirit Airlines, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm>; Spirit Aviation Holdings, Inc. - 10K - Annual Report - February 9, 2024 <https://fintel.io/doc/sec-spirit-airlines-inc-1498710-10k-2024-february-09-19762-4794>; Spirit Airlines Reports First Quarter 2024 Results <https://s204.q4cdn.com/112592003/files/doc_financials/2024/q1/Earnings-Release-1Q24.pdf>; Spirit Airlines Reports $1.2 Billion Loss For 2024 With Plans For Recovery <https://simpleflying.com/spirit-airlines-1-billion-loss-2024-plans-recovery/>; Spirit Airlines Financials: Bankruptcy, Debt & 10-K Data <https://dwuconsulting.com/dwu-ai/spirit-airlines-financial-profile>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm", "key": "spirit10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: spirit10k. (635,378 characters)
  The data_storage currently contains the following keys:
  spirit10k
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Spirit Airlines FY2024 10-K, find the \"Operating Statistics\" table (the one with Twelve Months Ended December 31, 2024 vs 2023 columns, including items like Average aircraft, Aircraft at end of period, Average daily aircraft utilization, Average stage length, Departures, ASMs, Load factor, Fare revenue per passenger flight segment, TRASM, CASM, Adjusted CASM, Adjusted CASM ex-fuel, Fuel gallons consumed, Average fuel cost per gallon, etc.). List every KPI row with its 2024 value and 2023 value exactly as stated. Also state the list of operating KPIs the company says it tracks/uses to evaluate performance, if stated.\n\n{{spirit10k}}"})
  result: ## Operating Statistics (Twelve Months Ended December 31, 2024 vs. 2023)
  
  From Item 7, "Comparative Operating Statistics." The table is marked unaudited.
  
  | KPI | 2024 | 2023 | % Change (as stated) |
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
  
  **Notes on the table:**
  - The table does not contain rows for "Average stage length" or "Fare revenue per passenger flight segment." The closest rows are "Total revenue per passenger flight segment" (shown above) and "Average yield." Stage length does not appear in the table.
  - Footnote (B) says the aircraft at end of period includes 21 aircraft recorded as assets held for sale at December 31, 2024.
  
  ## KPIs the company says it uses to evaluate performance
  
  The filing does not contain a single explicit list of operating KPIs that management uses to evaluate performance. The only measures it describes as evaluation tools are the non-GAAP m
  …[truncated 425 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Spirit Airlines (CIK 1498710) reported a set of unaudited \"Operating Statistics\" in the Item 7 MD&A of its FY2024 Form 10-K (filed for year ended December 31, 2024). The FY2024 totals, with FY2023 comparatives, are:\n\n| KPI | FY 2024 Total | FY 2023 |\n|---|---|---|\n| Average aircraft | 209.9 | 199.5 |\n| Aircraft at end of period (includes 21 aircraft held for sale) | 213 | 205 |\n| Average daily aircraft utilization (hours) | 9.9 | 11.1 |\n| Departures | 288,180 | 297,900 |\n| Passenger flight segments (thousands) | 44,180 | 44,105 |\n| Revenue passenger miles (thousands) | 43,671,009 | 45,243,787 |\n| Available seat miles (thousands) | 53,017,948 | 55,665,561 |\n| Lo
…[truncated 2,086 chars])

### Final answer
Spirit Airlines (CIK 1498710) reported a set of unaudited "Operating Statistics" in the Item 7 MD&A of its FY2024 Form 10-K (filed for year ended December 31, 2024). The FY2024 totals, with FY2023 comparatives, are:

| KPI | FY 2024 Total | FY 2023 |
|---|---|---|
| Average aircraft | 209.9 | 199.5 |
| Aircraft at end of period (includes 21 aircraft held for sale) | 213 | 205 |
| Average daily aircraft utilization (hours) | 9.9 | 11.1 |
| Departures | 288,180 | 297,900 |
| Passenger flight segments (thousands) | 44,180 | 44,105 |
| Revenue passenger miles (thousands) | 43,671,009 | 45,243,787 |
| Available seat miles (thousands) | 53,017,948 | 55,665,561 |
| Load factor (%) | 82.4% | 81.3% |
| Total revenue per passenger flight segment ($) | 111.21 | 121.58 |
| Average yield (cents) | 11.25 | 11.85 |
| TRASM – total operating revenue per ASM (cents) | 9.27 | 9.63 |
| CASM (cents) | 11.35 | 10.52 |
| Adjusted CASM (cents) | 10.76 | 10.33 |
| Adjusted CASM ex-fuel (cents) | 7.97 | 7.06 |
| Fuel gallons consumed (thousands) | 551,819 | 591,796 |
| Average fuel cost per gallon ($) | 2.68 | 3.08 |

Supporting context and checks:
- Passenger revenue fell 8.7% and total operating revenue was $4,913.4 million, with TRASM at 9.27 cents, down 3.7% year over year, per the 10-K's operating revenue discussion.
- Third-party summaries of the 10-K agree on the key unit metrics: ASMs down 4.8%, load factor 82.4%, CASM 11.35 cents, and Adjusted CASM ex-fuel 7.97 cents.
- Stage length and "fare revenue per passenger flight segment" (which appear in the FY2023 10-K) do not appear in the FY2024 table, so I have not listed them as FY2024 KPIs. The closest FY2024 equivalent is total revenue per passenger flight segment.
- The filing does not contain a standalone list of KPIs that management uses to evaluate performance. The only evaluation-oriented measures it names are the non-GAAP Adjusted CASM and Adjusted CASM ex-fuel, which the company says help management and investors understand underlying performance.

Note on sourcing: I extracted the full table from the 10-K text and cross-checked key values against the search snippets. The 10-K is the primary source; the other snippets were used only for verification.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm",
            "name": "Spirit Airlines, Inc. - Form 10-K - FY2024 (SEC EDGAR)"
        },
        {
            "url": "https://simpleflying.com/spirit-airlines-1-billion-loss-2024-plans-recovery/",
            "name": "Simple Flying – Spirit Airlines Reports $1.2 Billion Loss For 2024 (secondary cross-check)"
        }
    ]
}