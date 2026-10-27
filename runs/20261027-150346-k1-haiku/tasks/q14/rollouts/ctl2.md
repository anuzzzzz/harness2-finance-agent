## Rollout `ctl2`
- outcome: submitted
- turns: 2; cost: $0.035; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Zillow Group 2024 full year results operating cash flow capital expenditures revenue") → 0 results: 
- edgar_search({"search_query": "Zillow Group annual report net cash provided by operating activities capital expenditures", "ciks": ["1617640"], "form_types": ["10-K"], "start_date": "2024-01-01"})
  result: {"total_matching_documents": 2, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-11", "period_ending": "2024-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-25-000016", "document": "z-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm"}, {"form": "10-K", "file_date": "2024-02-15", "period_ending": "2023-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000022", "document": "z-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000012/exhibit993.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000069/exhibit993.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000012/q42023991.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000125/exhibit993.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000095/exhibit993.htm>
- web_search(query="Zillow Group full year 2022 revenue net cash provided by operating activities 2022 results") → 9 results: ZILLOW GROUP, INC. - Form ARS - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764023000060/zg202210k5a.pdf>; ZILLOW GROUP, INC. - Form 10-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm>; ZILLOW GROUP, INC. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000063/z-20220331.htm>; ZILLOW GROUP, INC. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000081/z-20220630.htm>; ZILLOW GROUP, INC. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000106/z-20220930.htm>
- web_search(query="Zillow 2022 full-year revenue $1,958 million continuing operations") → 10 results: ZILLOW GROUP, INC. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000104/exhibit993.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000104/q32022991.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000011/q42021991.htm>; ZILLOW GROUP, INC. - Form ARS - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764023000060/zg202210k5a.pdf>; ZILLOW GROUP, INC. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000011/exhibit993.htm>
- submit_final_result({"final_result": "**Approximate Zillow Group free cash flow (CFO − capex) and FCF margin, FY2022–FY2024**\n\n**Inputs ($ millions)**\n\n| Fiscal year | Operating cash flow (CFO) | Capex | Approx. FCF | Revenue | FCF margin |\n|---|---|---|---|---|---|\n| FY2022 | 4,504 | 115 | 4,389 | 1,958 | 224.16% |\n| FY2023 | 354 | 135 | 219 | 1,945 | 11.26% |\n| FY2024 | 428 | 143 | 285 | 2,236 | 12.75% |\n\n- **CFO, FY2022:** Zillow reported <cite index=\"12-4\">Net cash provided by (used in) operating activities of $4,504 (2022), $(3,177) (2021) and $423 (2020)</cite>. The 10-K notes that this figure <cite index=\"12-1,12-2\">includes the results of continuing and discontinued operations</cite>, beca
…[truncated 2,987 chars])

### Final answer
**Approximate Zillow Group free cash flow (CFO − capex) and FCF margin, FY2022–FY2024**

**Inputs ($ millions)**

| Fiscal year | Operating cash flow (CFO) | Capex | Approx. FCF | Revenue | FCF margin |
|---|---|---|---|---|---|
| FY2022 | 4,504 | 115 | 4,389 | 1,958 | 224.16% |
| FY2023 | 354 | 135 | 219 | 1,945 | 11.26% |
| FY2024 | 428 | 143 | 285 | 2,236 | 12.75% |

- **CFO, FY2022:** Zillow reported <cite index="12-4">Net cash provided by (used in) operating activities of $4,504 (2022), $(3,177) (2021) and $423 (2020)</cite>. The 10-K notes that this figure <cite index="12-1,12-2">includes the results of continuing and discontinued operations</cite>, because cash flows from discontinued operations were not separated.
- **CFO, FY2023 and FY2024:** Per a third-party aggregator, operating cash flow was 354 in FY2023 and 428 in FY2024 (stockanalysis.com cash flow statement). I did not verify these against the 10-K directly.
- **Capex:** Per the same aggregator, capital expenditures were -115 (FY2022), -135 (FY2023) and -143 (FY2024) (stockanalysis.com). I did not verify these against the filings directly.
- **Revenue, FY2022:** <cite index="26-1">Total revenue $1,958 (2022) vs. $2,132 (2021)</cite>, from the FY2022 10-K. This is revenue from continuing operations, since the iBuying business was presented as discontinued.
- **Revenue, FY2023 and FY2024:** Full-year 2024 revenue was $2,236 million versus $1,945 million in 2023 (per the Q4 2024 earnings release table). <cite index="8-5">Full-year 2024 revenue of $2.2 billion was up 15% year over year.</cite>

**Calculations**
- FY2022: (4,504 − 115) = 4,389; 4,389 / 1,958 = 224.16%
- FY2023: (354 − 135) = 219; 219 / 1,945 = 11.26%
- FY2024: (428 − 143) = 285; 285 / 2,236 = 12.75%

**Trend**
- The FY2022 margin is not comparable. It is inflated because CFO includes the cash from winding down Zillow Offers inventory (the 10-K describes cash received from home sales through Zillow Offers until September 30, 2022), while revenue excludes the discontinued iBuying business. Treat 224% as a distortion, not a sign of underlying cash generation.
- Excluding FY2022, the margin fell from about 11.26% in FY2023 to about 12.75% in FY2024, an increase of roughly 1.49 percentage points. This reflects operating cash flow growing faster than revenue in 2024 (CFO up about 21% against revenue up about 15%).
- Overall: FCF margin was extremely elevated in FY2022 due to the Zillow Offers wind-down, dropped sharply in FY2023, and recovered modestly in FY2024. It is still well below the FY2022 level.

**Caveats:** The CFO and capex figures for FY2023 and FY2024 come from a third-party aggregator and were not checked against the 10-K cash flow statements. Figures are approximate and use company-defined CFO, not an adjusted free cash flow measure.

Sources:
{
    "sources": [
        {"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm", "name": "Zillow Group FY2022 Form 10-K"},
        {"url": "https://stockanalysis.com/stocks/z/financials/cash-flow-statement/", "name": "Stockanalysis - Zillow Group Cash Flow Statement (CFO and capex FY2022–FY2024)"},
        {"url": "https://content.edgar-online.com/ExternalLink/EDGAR/0001617640-25-000015.html?hash=976c7b67b9f0ca8285459d54c98c13b1235a64e6f21ddcb86dd82682aedf6803&dest=z-20250211_htm", "name": "Zillow Group Q4 and FY2024 earnings release (revenue table)"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000015/q42024991.htm", "name": "Zillow Group Q4 and FY2024 press release"}
    ]
}