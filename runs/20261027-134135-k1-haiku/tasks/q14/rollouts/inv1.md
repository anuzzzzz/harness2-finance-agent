## Rollout `inv1`
- outcome: submitted
- turns: 2; cost: $0.024; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Zillow Group 2024 annual results operating cash flow capital expenditures revenue") → 0 results: 
- edgar_search({"search_query": "Zillow Group annual report net cash provided by operating activities capital expenditures", "ciks": ["1617640"], "form_types": ["10-K"], "start_date": "2024-01-01"})
  result: {"total_matching_documents": 2, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-11", "period_ending": "2024-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-25-000016", "document": "z-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm"}, {"form": "10-K", "file_date": "2024-02-15", "period_ending": "2023-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000022", "document": "z-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm"}]}

### Turn 2  (stop_reason=tool_use)
**Approach:** Free cash flow ≈ net cash provided by operating activities (CFO) minus capital expenditures. FCF margin = FCF ÷ total revenue.

**Inputs**

- **CFO:** 2022 was $4,504M, 2023 was $354M, and 2024 was $428M. The 2022 figure includes discontinued operations (Zillow Offers) and the wind-down of its inventory. 
Net cash provided by (used in) operating activities was $4,504 (2022), $(3,177) (2021) and $423 (2020)
, and 
the cash flows related to discontinued operations have not been separated. Accordingly, the consolidated statements of cash flows and the following discussions include the results of continuing and discontinued operations.
 The 2023 and 2024 CFO figures appear in the FY2024 10-K's cash flow table, which shows 
$428 for 2024 and $354 for 2023
.
- **Capex:** Stockanalysis reports capital expenditures of $115M (FY2022), $135M (FY2023) and $143M (FY2024). 
Capital Expenditures -115 (FY 2022), -135 (FY 2023), -143 (FY 2024)
, per the table in the cash flow statement source.
- **Revenue:** FY2022 total revenue from continuing operations was $1,958M. The FY2022 results release shows 
$1,958 (full year 2022)
. FY2023 and FY2024 revenue comes from the Q4 2024 release, which shows 
$2,236 for full-year 2024 and $1,945 for full-year 2023
. (MarketBeat shows different 2023 and 2024 revenue totals, $2,061M and $2,326M, which I did not use because they conflict with the company's own releases.)

**Calculations**

| Year | CFO ($M) | Capex ($M) | FCF ($M) | Revenue ($
…[truncated 960 chars]
- web_search(query=null) → 9 results: ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000012/exhibit993.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000012/q42023991.htm>; ZILLOW GROUP, INC. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000125/exhibit993.htm>; ZILLOW GROUP, INC. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000094/z-20240630.htm>
- web_search(query="Zillow Group full year 2022 total revenue net cash provided by operating activities 2022") → 9 results: ZILLOW GROUP, INC. - Form ARS - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764023000060/zg202210k5a.pdf>; ZILLOW GROUP, INC. - Form 10-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm>; ZILLOW GROUP, INC. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000063/z-20220331.htm>; ZILLOW GROUP, INC. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000081/z-20220630.htm>; ZILLOW GROUP, INC. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000106/z-20220930.htm>
- submit_final_result({"final_result": "Approximate Zillow Group free cash flow (FCF = CFO − capex) and FCF margin (FCF ÷ total revenue):\n\nFY2022: CFO $4,504M − capex $115M = FCF $4,389M; revenue $1,958M; FCF margin 224.16% (distorted by the one-time release of Zillow Offers inventory during the wind-down, and CFO includes discontinued operations).\nFY2023: CFO $354M − capex $135M = FCF $219M; revenue $1,945M; FCF margin 11.26%.\nFY2024: CFO $428M − capex $143M = FCF $285M; revenue $2,236M; FCF margin 12.75%.\n\nTrend: The FCF margin was not meaningful in FY2022 because of the inventory unwind. Excluding that, it fell from 11.26% in FY2023 to 12.75% in FY2024, a recovery. The overall trend is a sharp drop from 
…[truncated 1,504 chars])

### Final answer
Approximate Zillow Group free cash flow (FCF = CFO − capex) and FCF margin (FCF ÷ total revenue):

FY2022: CFO $4,504M − capex $115M = FCF $4,389M; revenue $1,958M; FCF margin 224.16% (distorted by the one-time release of Zillow Offers inventory during the wind-down, and CFO includes discontinued operations).
FY2023: CFO $354M − capex $135M = FCF $219M; revenue $1,945M; FCF margin 11.26%.
FY2024: CFO $428M − capex $143M = FCF $285M; revenue $2,236M; FCF margin 12.75%.

Trend: The FCF margin was not meaningful in FY2022 because of the inventory unwind. Excluding that, it fell from 11.26% in FY2023 to 12.75% in FY2024, a recovery. The overall trend is a sharp drop from FY2022 to FY2023, then improvement in FY2024, still below the FY2022 level.

Caveats: This is an approximation using CFO less capex, with no working-capital or company "adjusted free cash flow" adjustments. MarketBeat's revenue figures for 2023 and 2024 conflict with company releases and were not used.

Sources:
{
    "sources": [
        {"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm", "name": "Zillow Group FY2022 Form 10-K (cash flow data)"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "name": "Zillow Group FY2024 Form 10-K (cash flow data)"},
        {"url": "https://stockanalysis.com/stocks/z/financials/cash-flow-statement/", "name": "StockAnalysis - Zillow Group cash flow statement (capex)"},
        {"url": "https://investors.zillowgroup.com/investors/news-and-events/news/news-details/2023/Zillow-Group-Reports-Fourth-Quarter-and-Full-Year-2022-Financial-Results/default.aspx", "name": "Zillow Group Q4 and FY2022 financial results release"},
        {"url": "https://www.prnewswire.com/news-releases/zillow-group-reports-fourth-quarter-and-full-year-2024-financial-results-302373842.html", "name": "Zillow Group Q4 and FY2024 financial results release (PR Newswire)"},
        {"url": "https://www.marketbeat.com/stocks/NASDAQ/Z/financials/", "name": "MarketBeat - Zillow Group financials (cross-check only)"}
    ]
}