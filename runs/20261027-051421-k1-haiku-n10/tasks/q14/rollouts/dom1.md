## Rollout `dom1`
- outcome: submitted
- turns: 4; cost: $0.036; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "fcf_margin_trend"})
  result: ---
  name: fcf_margin_trend
  description: Approximate free cash flow as operating cash flow minus capex, compute FCF margin over several fiscal years, and describe the trend.
  ---
  
  # FCF margin trend (FCF ≈ CFO − capex, ÷ revenue, multi-year)
  
  **Analytic move:** calculate, then classify the trend. For each fiscal year take CFO, capex and total revenue from the filings, compute FCF and FCF ÷ revenue unrounded, and state the direction year over year.
  
  **Where the figures live**
  - CFO: cash flow statement, "Net cash provided by (used in) operating activities", total-company line.
  - Capex: investing section, "Purchases of property and equipment". For software or internet companies this line usually includes capitalized internal-use software. Purchases of intangibles (for example domain names) and capitalized-software lines are separate. Headline CFO − "purchases of property and equipment" as the question's approximation. Show the alternative that also deducts intangibles only as a labelled sensitivity, and only if the direction is unchanged.
  - Revenue: income statement, total revenue, same fiscal year.
  - Each 10-K carries three years of cash flows and income statement, so FY(N) and FY(N−2) come from one filing. Take FY2022 from the FY2023 or FY2024 10-K comparative columns. Check whether the comparatives were recast.
  
  **Checks that change the answer**
  1. Discontinued operations: if a business was wound down or reclassified (a large inventory unwind, for example), the cash flow statement may include discontinued operations while revenue shows continuing operations only. State that mismatch. A margin well above 100% is a red flag for it, not a result to present without comment. Give the headline on the stated formula, then identify the distorted year and the cause, quoting the w
  …[truncated 1,247 chars]

### Turn 2  (stop_reason=tool_use)
- edgar_search({"search_query": "Zillow Group annual report 10-K cash flows operating activities purchases of property and equipment", "ciks": ["ZG"], "start_date": "2023-01-01", "form_types": ["10-K"]})
  ERROR: HTTPError: 403 Client Error: Forbidden for url: https://www.sec.gov/files/company_tickers.json
- edgar_search({"search_query": "Zillow Group 10-K 2024 annual report revenue", "ciks": ["ZG"], "start_date": "2025-01-01"})
  ERROR: HTTPError: 403 Client Error: Forbidden for url: https://www.sec.gov/files/company_tickers.json

### Turn 3  (stop_reason=tool_use)
- web_search(query="Zillow Group 2024 full year results free cash flow operating cash flow capital expenditures") → 0 results: 
- edgar_search({"search_query": "Zillow Group annual report net cash provided by operating activities", "ciks": ["0001617640"], "start_date": "2023-01-01", "form_types": ["10-K"]})
  ERROR: ValueError: EDGAR full-text search returned HTTP 403: <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
  <html xmlns="http://www.w3.org/1999/xhtml">
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>SEC.gov | Your Request Originates from an Undeclar

### Turn 4  (stop_reason=tool_use)
- web_search(query=null) → 9 results: Zillow Group (Z) Cash Flow Statement <https://stockanalysis.com/stocks/z/financials/cash-flow-statement/>; Zillow Group (FRA:0ZG) Cash Flow Statement <https://stockanalysis.com/quote/fra/0ZG/financials/cash-flow-statement/>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000012/q42023991.htm>; Zillow Group, Inc. - 10K - Annual Report - February 15, 2024 <https://fintel.io/doc/sec-zillow-group-inc-1617640-10k-2024-february-15-19768-9224>; Zillow Group (ZG) Cash Flow Statement <https://stockanalysis.com/stocks/zg/financials/cash-flow-statement/>
- web_search(query="Zillow Group full year 2024 total revenue 2023 revenue 2022 revenue results") → 9 results: ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000012/exhibit993.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000012/q42023991.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1617640/000161764023000006/q42022991.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000125/q32024991.htm>; Document <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000015/q42024991.htm>
- web_search(query="Zillow 2022 net cash provided by operating activities Zillow Offers inventory wind down working capital") → 9 results: ZILLOW GROUP, INC. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000106/z-20220930.htm>; ZILLOW GROUP, INC. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000081/z-20220630.htm>; ZILLOW GROUP, INC. - Form ARS - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764023000060/zg202210k5a.pdf>; ZILLOW GROUP, INC. - Form 10-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm>; z-20211102 <https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm>
- submit_final_result({"final_result": "**Answer:** Zillow's FCF margin (CFO − capex, ÷ total revenue) was about 224.16% in FY2022, then fell to about 11.26% in FY2023 and rose to about 12.75% in FY2024. The FY2022 figure is distorted by the Zillow Offers wind-down, so the underlying trend is a rise of about 1.49 percentage points from FY2023 to FY2024, not a monotonic path.\n\n**Inputs (USD millions; FY2024 and FY2023 CFO from the FY2024 10-K; FY2022 CFO from the FY2022 10-K / FY2023 comparatives)**\n\n| Item | FY2022 | FY2023 | FY2024 |\n|---|---|---|---|\n| CFO (net cash from operations) | 4,504 | 354 | 428 |\n| Capex (purchases of PP&E, aggregator) | 115 | 135 | 143 |\n| FCF = CFO − capex | 4,389 | 219 | 285 
…[truncated 4,136 chars])

### Final answer
**Answer:** Zillow's FCF margin (CFO − capex, ÷ total revenue) was about 224.16% in FY2022, then fell to about 11.26% in FY2023 and rose to about 12.75% in FY2024. The FY2022 figure is distorted by the Zillow Offers wind-down, so the underlying trend is a rise of about 1.49 percentage points from FY2023 to FY2024, not a monotonic path.

**Inputs (USD millions; FY2024 and FY2023 CFO from the FY2024 10-K; FY2022 CFO from the FY2022 10-K / FY2023 comparatives)**

| Item | FY2022 | FY2023 | FY2024 |
|---|---|---|---|
| CFO (net cash from operations) | 4,504 | 354 | 428 |
| Capex (purchases of PP&E, aggregator) | 115 | 135 | 143 |
| FCF = CFO − capex | 4,389 | 219 | 285 |
| Total revenue | ~1,958 (derived) | 1,945 | 2,236 |
| FCF margin | ~224.16% | 11.26% | 12.75% |

- **Operating cash flow:** The FY2024 10-K reports <cite index="6-5">Net cash provided by operating activities · $ · 428 · $ · 354</cite> for 2024 and 2023. For 2022, the 2023 comparative shows <cite index="25-3">Net cash provided by operating activities 354 4,504</cite>.
- **Capex:** Only aggregator figures were available: <cite index="5-3">Capital Expenditures | -130 | -133 | -143 | -135 | -115 | -74</cite> (stockanalysis, FY2024 through FY2022 columns). I did not open the 10-K cash flow statement to confirm the line item, so treat capex as an aggregator-sourced figure.
- **Revenue:** FY2024 revenue was <cite index="14-7">Full-year 2024 revenue of $2.2 billion was up 15% year over year.</cite> The FY2024 earnings table shows <cite index="14-10">Total revenue · $ · 554 · $ · 474 · 17% · $ · 2,236 · $ · 1,945 · 15%</cite>, so FY2024 = 2,236 and FY2023 = 1,945. For FY2022, the company said <cite index="12-4">full-year 2022 revenue from continuing operations was $2.0 billion.</cite> An aggregator lists 2023 as <cite index="17-4">Zillow annual revenue for 2023 was $1.945B, a 0.66% decline from 2022.</cite> Backing out 2022 from that gives 1,945 / (1 − 0.0066) ≈ 1,958, which is an approximation.

**Arithmetic**
- FY2022: (4,504 − 115) / 1,958 ≈ 224.16%
- FY2023: (354 − 135) / 1,945 = 219 / 1,945 ≈ 11.26%
- FY2024: (428 − 143) / 2,236 = 285 / 2,236 ≈ 12.75%

**Year-over-year steps (percentage points)**
- FY2022 → FY2023: falls by about 212.90 pp.
- FY2023 → FY2024: rises by about 1.49 pp.

**Distortion in FY2022:** The 2022 CFO is inflated by the wind-down of Zillow Offers, which was a discontinued-operations-type unwind of inventory. The company's annual report states that <cite index="21-3">a $3.9 billion decrease in inventory and an $82 million decrease in accounts receivable as we wound down Zillow Offers operations</cite> drove the working-capital change. Revenue is continuing operations only, so the 2022 margin is not comparable. Excluding 2022, the trend is a modest rise of about 1.49 pp from FY2023 to FY2024.

**Trend conclusion:** The FY2022 → FY2024 path is not monotonic. It collapses from the wind-down-inflated 224.16% to 11.26% in FY2023, then recovers to 12.75% in FY2024. On a like-for-like basis (FY2023 → FY2024), the FCF margin improved by about 1.49 pp.

**Caveats:** The FCF figures are approximations (CFO − capex as defined). The capex figures and the FY2022 revenue are from aggregator or derived sources.

**Sources:**
{
    "sources": [
        {"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "name": "Zillow Group FY2024 Form 10-K"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm", "name": "Zillow Group FY2022 Form 10-K"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000060/zg202210k5a.pdf", "name": "Zillow Group FY2022 Form ARS"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000015/q42024991.htm", "name": "Zillow Q4 and FY2024 earnings release (8-K)"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000006/q42022991.htm", "name": "Zillow Q4 and FY2022 earnings release (8-K)"},
        {"url": "https://d18rn0p25nwr6d.cloudfront.net/CIK-0001617640/843e13f6-5f09-40ec-9d0d-c43e39c38be7.pdf", "name": "Zillow FY2023 earnings release with cash flow statement"},
        {"url": "https://stockanalysis.com/stocks/zg/financials/cash-flow-statement/", "name": "StockAnalysis Zillow cash flow statement (aggregator, capex)"},
        {"url": "https://stockanalysis.com/stocks/z/financials/cash-flow-statement/", "name": "StockAnalysis Zillow cash flow statement (aggregator, cross-check)"},
        {"url": "https://www.macrotrends.net/stocks/charts/ZG/zillow/revenue", "name": "Macrotrends Zillow revenue (aggregator, FY2023 and FY2022 derivation)"}
    ]
}