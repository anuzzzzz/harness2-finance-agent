## Rollout `base1`
- outcome: submitted
- turns: 4; cost: $0.158; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Spirit Airlines full year 2024 operating statistics ASM load factor CASM") → 0 results: 
- edgar_search({"search_query": "Spirit Airlines 10-K 2024 operating statistics available seat miles load factor", "ciks": ["SAVE"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  ERROR: ValueError: Unknown ticker 'SAVE'. Provide a numeric CIK instead.

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Spirit Airlines, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm>; Spirit Airlines, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1498710/000149871024000103/earningsrelease4q23.htm>; Spirit Airlines, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1498710/000149871024000165/earningsrelease1q24.htm>; Spirit Airlines, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1498710/000149871024000195/earningsrelease2q24.htm>; JETBLUE AIRWAYS CORP - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1158463/000115846325000005/jblu-20241231.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm", "key": "spirit_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: spirit_10k_2024. (635,378 characters)
  The data_storage currently contains the following keys:
  spirit_10k_2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Spirit Airlines FY2024 10-K text: {{spirit_10k_2024}}. List every operating key performance indicator (KPI) the company identifies or tracks (e.g., in a section titled 'Key Performance Indicators', 'Operating Statistics', or in Item 7 MD&A metrics). For each, give the FY2024 total/value as stated (and the 2023 comparative if shown). Quote exact figures and units. Also note the section name where each appears."})
  result: # Operating KPIs in the Spirit Airlines FY2024 10-K
  
  The primary KPI source is the **"Comparative Operating Statistics"** table in Item 7 (MD&A). Other metrics appear in the MD&A "2024 Year in Review," "Operating Revenues," "Operating Expenses," and "Liquidity" sections, in Item 1 (Business), and in the Risk Factors.
  
  ## 1. Comparative Operating Statistics (Item 7, MD&A)
  
  Source: "Comparative Operating Statistics," twelve months ended December 31, 2024 vs. 2023 (unaudited).
  
  | Metric | FY2024 | FY2023 | Change (as stated) |
  |---|---|---|---|
  | Average aircraft | 209.9 | 199.5 | 5.2% |
  | Aircraft at end of period | 213 | 205 | 3.9% (includes 21 aircraft held for sale) |
  | Average daily aircraft utilization (hours) | 9.9 | 11.1 | (10.8)% |
  | Departures | 288,180 | 297,900 | (3.3)% |
  | Passenger flight segments (PFSs) (thousands) | 44,180 | 44,105 | 0.2% |
  | Revenue passenger miles (RPMs) (thousands) | 43,671,009 | 45,243,787 | (3.5)% |
  | Available seat miles (ASMs) (thousands) | 53,017,948 | 55,665,561 | (4.8)% |
  | Load factor (%) | 82.4% | 81.3% | 1.1 pts |
  | Total revenue per passenger flight segment ($) | 111.21 | 121.58 | (8.5)% |
  | Average yield (cents) | 11.25 | 11.85 | (5.1)% |
  | TRASM, total operating revenue per ASM (cents) | 9.27 | 9.63 | (3.7)% |
  | CASM, operating expenses per ASM (cents) | 11.35 | 10.52 | 7.9% |
  | Adjusted CASM (cents) | 10.76 | 10.33 | 4.2% |
  | Adjusted CASM ex-fuel (cents) | 7.97 | 7.06 | 12.9% |
  | Fuel gallons consumed (thousands) | 551,819 | 591,796 | (6.8)% |
  | Average fuel cost per gallon ($) | 2.68 | 3.08 | (13.0)% |
  
  ## 2. Other KPIs and Metrics Tracked in MD&A and Elsewhere
  
  **Revenue and margin (MD&A, "2024 Year in Review" and "Operating Revenues")**
  - Operating margin: negative 22.5% (2024) vs. negative 9.2% (2023).
  - Total operatin
  …[truncated 2,167 chars]

### Turn 4  (stop_reason=tool_use)
**Spirit Airlines' FY2024 operating KPIs (from its FY2024 Form 10-K)**

The main KPI set is the "Comparative Operating Statistics" table in Item 7 (MD&A) of the 10-K. It covers twelve months ended December 31, 2024, and is marked unaudited. 
The tables set forth our operating statistics for the twelve month periods ended December 31, 2024 and 2023
. I pulled the full 10-K to confirm the remaining rows, so the table below is complete, though the search snippets only show part of it.

| KPI | FY 2024 Total | FY 2023 (comparative) |
|---|---|---|
| Average aircraft | 209.9 | 199.5 |
| Aircraft at end of period | 213 | 205 |
| Average daily aircraft utilization (hours) | 9.9 | 11.1 |
| Departures | 288,180 | 297,900 |
| Passenger flight segments (thousands) | 44,180 | 44,105 |
| Revenue passenger miles (thousands) | 43,671,009 | 45,243,787 |
| Available seat miles (thousands) | 53,017,948 | 55,665,561 |
| Load factor (%) | 82.4% | 81.3% |
| Total revenue per passenger flight segment ($) | 111.21 | 121.58 |
| Average yield (cents) | 11.25 | 11.85 |
| TRASM (total operating revenue per ASM, cents) | 9.27 | 9.63 |
| CASM (operating expenses per ASM, cents) | 11.35 | 10.52 |
| Adjusted CASM (cents) | 10.76 | 10.33 |
| Adjusted CASM ex-fuel (cents) | 7.97 | 7.06 |
| Fuel gallons consumed (thousands) | 551,819 | 591,796 |
| Average fuel cost per gallon ($) | 2.68 | 3.08 |

**Cross-checks on selected figures:**
- Load factor: 
the average load factor improved by 1.1% to 82.4%
.
- TRASM 
…[truncated 1,201 chars]
- submit_final_result({"final_result": "Spirit Airlines (NYSE: SAVE) FY2024 operating KPIs, from the \"Comparative Operating Statistics\" table in Item 7 (MD&A) of its FY2024 Form 10-K (twelve months ended December 31, 2024, unaudited):\n\n| KPI | FY 2024 Total | FY 2023 (comparative) |\n|---|---|---|\n| Average aircraft | 209.9 | 199.5 |\n| Aircraft at end of period | 213 | 205 |\n| Average daily aircraft utilization (hours) | 9.9 | 11.1 |\n| Departures | 288,180 | 297,900 |\n| Passenger flight segments (thousands) | 44,180 | 44,105 |\n| Revenue passenger miles (thousands) | 43,671,009 | 45,243,787 |\n| Available seat miles (thousands) | 53,017,948 | 55,665,561 |\n| Load factor (%) | 82.4% | 81.3% |\n| Total rev
…[truncated 1,199 chars])

### Final answer
Spirit Airlines (NYSE: SAVE) FY2024 operating KPIs, from the "Comparative Operating Statistics" table in Item 7 (MD&A) of its FY2024 Form 10-K (twelve months ended December 31, 2024, unaudited):

| KPI | FY 2024 Total | FY 2023 (comparative) |
|---|---|---|
| Average aircraft | 209.9 | 199.5 |
| Aircraft at end of period | 213 | 205 |
| Average daily aircraft utilization (hours) | 9.9 | 11.1 |
| Departures | 288,180 | 297,900 |
| Passenger flight segments (thousands) | 44,180 | 44,105 |
| Revenue passenger miles (thousands) | 43,671,009 | 45,243,787 |
| Available seat miles (thousands) | 53,017,948 | 55,665,561 |
| Load factor (%) | 82.4% | 81.3% |
| Total revenue per passenger flight segment ($) | 111.21 | 121.58 |
| Average yield (cents) | 11.25 | 11.85 |
| TRASM (total operating revenue per ASM, cents) | 9.27 | 9.63 |
| CASM (operating expenses per ASM, cents) | 11.35 | 10.52 |
| Adjusted CASM (cents) | 10.76 | 10.33 |
| Adjusted CASM ex-fuel (cents) | 7.97 | 7.06 |
| Fuel gallons consumed (thousands) | 551,819 | 591,796 |
| Average fuel cost per gallon ($) | 2.68 | 3.08 |

Cross-checks: load factor of 82.4% and TRASM of 9.27 cents and CASM of 11.35 cents match secondary coverage of the 10-K (Simple Flying). Other metrics the 10-K reports outside the table include operating margin (negative 22.5% in 2024) and unit costs in cents per ASM.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm",
            "name": "Spirit Airlines, Inc. - Form 10-K - FY2024"
        },
        {
            "url": "https://simpleflying.com/spirit-airlines-1-billion-loss-2024-plans-recovery/",
            "name": "Simple Flying - Spirit Airlines Reports $1.2 Billion Loss For 2024 With Plans For Recovery"
        }
    ]
}