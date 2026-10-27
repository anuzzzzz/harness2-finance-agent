## Rollout `agg1`
- outcome: submitted
- turns: 2; cost: $0.047; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "fcf_margin_trend"})
  result: ---
  name: fcf_margin_trend
  description: Approximate free cash flow as operating cash flow minus capex, compute FCF margin over several fiscal years, and describe the trend.
  ---
  
  # FCF margin trend (FCF ≈ CFO − capex, ÷ revenue, multi-year)
  
  **Analytic move:** retrieve three inputs per year (CFO, capex, total revenue), calculate FCF and FCF ÷ revenue unrounded, then state the direction year over year.
  
  **Where the figures live**
  - CFO: cash flow statement, "Net cash provided by (used in) operating activities", total-company line.
  - Capex: investing section, "Purchases of property and equipment" (name the exact line used). Purchases of intangibles (e.g. domain names) are a separate line. Headline CFO − purchases of property and equipment as the question's approximation; show the version that also deducts intangibles only as a labelled one-line sensitivity.
  - Revenue: income statement, total revenue, same fiscal year.
  - A 10-K carries three years of cash flows and income statement, so FY(N−2) to FY(N) come from one filing. If the latest 10-K is unreachable, use the prior 10-K plus the latest Q4 8-K Exhibit 99.1. Check whether comparatives were recast.
  
  **Checks that change the answer**
  1. Discontinued operations: if a business was wound down (e.g. an inventory unwind), the cash flow statement may include it while revenue shows continuing operations only. A margin far above 100% is a red flag for this. Give the headline on the stated formula, then identify the distorted year and cause, quoting the working-capital or discontinued-operations line. Show the change between the later, comparable years separately.
  2. Keep CFO and revenue on the same basis and recast status; say so if they differ.
  3. Prefer figures read from filings. Aggregator pages (stockanalysis, macrotrends, m
  …[truncated 906 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query="Zillow Group 10-K 2024 net cash provided by operating activities purchases of property and equipment") → 9 results: ZILLOW GROUP, INC. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm>; ZILLOW GROUP, INC. (Form: 10-K, Received: 02/11/2025 16:21:55) <https://content.edgar-online.com/ExternalLink/EDGAR/0001617640-25-000016.html?hash=0cbc5b58372fd7624126f2551e8e8a884de4b57fe379aaaa014e219af2339afa&dest=z-20241231_htm>; Zillow Group, Inc. - 10K - Annual Report - February 15, 2024 <https://fintel.io/doc/sec-zillow-group-inc-1617640-10k-2024-february-15-19768-9224>; Zillow Group Reports Third-Quarter 2025 Financial Results <https://www.prnewswire.com/news-releases/zillow-group-reports-third-quarter-2025-financial-results-302600215.html>; Zillow Group Reports Fourth-Quarter and Full-Year 2025 Financial Results <https://www.prnewswire.com/news-releases/zillow-group-reports-fourth-quarter-and-full-year-2025-financial-results-302684089.html>
- web_search(query="Zillow Group fourth quarter full year 2024 results total revenue operating cash flow") → 9 results: ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000012/q42023991.htm>; ZILLOW GROUP, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1617640/000161764024000125/q32024991.htm>; Z Q4-2025 Earnings Call - Alpha Spread <https://www.alphaspread.com/security/nasdaq/z/investor-relations/earnings-call/q4-2025>; NEWS RELEASE Zillow Group Reports Fourth-Quarter and Full-Year <https://s25.q4cdn.com/975009107/files/doc_news/Zillow-Group-Reports-Fourth-Quarter-and-Full-Year-2024-Financial-Results-2025.pdf>; Zillow Group Reports Fourth-Quarter and Full-Year 2024 Financial Results - Feb 11, 2025 <https://zillowgroup.mediaroom.com/2025-02-11-Zillow-Group-Reports-Fourth-Quarter-and-Full-Year-2024-Financial-Results>
- web_search(query="Zillow Group fourth-quarter full-year 2023 results purchases of property and equipment year ended December 31 2023 2022") → 10 results: Zillow Group Reports Fourth-Quarter and Full-Year 2023 Financial Results <https://www.marketscreener.com/quote/stock/ZILLOW-GROUP-INC-20814107/news/Zillow-Group-Reports-Fourth-Quarter-and-Full-Year-2023-Financial-Results-45943388/>; Zillow Group Reports Fourth-Quarter and Full-Year 2023 Financial Results - Feb 13, 2024 <https://zillowgroup.mediaroom.com/2024-02-13-Zillow-Group-Reports-Fourth-Quarter-and-Full-Year-2023-Financial-Results>; UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 <https://d18rn0p25nwr6d.cloudfront.net/CIK-0001617640/843e13f6-5f09-40ec-9d0d-c43e39c38be7.pdf>; Zillow Group, Inc. - Zillow Group Reports Fourth-Quarter and Full-Year 2023 Financial Results <https://investors.zillowgroup.com/investors/news-and-events/news/news-details/2024/Zillow-Group-Reports-Fourth-Quarter-and-Full-Year-2023-Financial-Results/default.aspx>; ZILLOW GROUP, INC. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1617640/000161764025000015/q42024991.htm>
- web_search(query="Zillow 2022 annual report purchases of property and equipment net cash provided by operating activities 4,504 revenue 1,958") → 10 results: ZILLOW GROUP, INC. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000081/z-20220630.htm>; ZILLOW GROUP, INC. - Form 10-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm>; ZILLOW GROUP, INC. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000106/z-20220930.htm>; ZILLOW GROUP, INC. - Form ARS - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764023000060/zg202210k5a.pdf>; ZILLOW GROUP, INC. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1617640/000161764022000063/z-20220331.htm>
- submit_final_result({"final_result": "\nZillow Group (NASDAQ: Z/ZG): FCF ≈ CFO − purchases of property and equipment; FCF margin = FCF ÷ total revenue. Figures in USD millions.\n\nInputs and results (source type: search excerpts from the FY2024 10-K cash flow and income statement tables, plus the FY2023 and FY2022 press-release/10-K excerpts; I did not open the full filings):\n\nFY2022: CFO 4,504; capex 115; FCF = 4,504 − 115 = 4,389; revenue 1,958; margin = 4,389 ÷ 1,958 = 224.16%\nFY2023: CFO 354; capex 135; FCF = 354 − 135 = 219; revenue 1,945; margin = 219 ÷ 1,945 = 11.26%\nFY2024: CFO 428; capex 143; FCF = 428 − 143 = 285; revenue 2,236; margin = 285 ÷ 2,236 = 12.75%\n\nCapex line: \"Purchases of property 
…[truncated 2,953 chars])

### Final answer

Zillow Group (NASDAQ: Z/ZG): FCF ≈ CFO − purchases of property and equipment; FCF margin = FCF ÷ total revenue. Figures in USD millions.

Inputs and results (source type: search excerpts from the FY2024 10-K cash flow and income statement tables, plus the FY2023 and FY2022 press-release/10-K excerpts; I did not open the full filings):

FY2022: CFO 4,504; capex 115; FCF = 4,504 − 115 = 4,389; revenue 1,958; margin = 4,389 ÷ 1,958 = 224.16%
FY2023: CFO 354; capex 135; FCF = 354 − 135 = 219; revenue 1,945; margin = 219 ÷ 1,945 = 11.26%
FY2024: CFO 428; capex 143; FCF = 428 − 143 = 285; revenue 2,236; margin = 285 ÷ 2,236 = 12.75%

Capex line: "Purchases of property and equipment" (2024: 143, 2023: 135, 2022: 115), as shown in the FY2024 10-K table. Purchases of intangible assets (28, 30, 25) are a separate line and were excluded from the headline.

Trend:
- FY2022→FY2023: margin fell by about 212.90 percentage points (224.16% → 11.26%).
- FY2023→FY2024: margin rose by about 1.49 percentage points (11.26% → 12.75%).
- The path is not monotonic. The FY2022 value is an outlier: CFO of 4,504 reflected the wind-down of Zillow Offers, when operating cash flow included cash from home sales and home purchases, while revenue of 1,958 is the reported total. The 2022 margin is therefore not comparable with later years. Excluding 2022, the trend from FY2023 to FY2024 is a modest improvement of about 1.49 pp.

Sensitivity (CFO − property and equipment purchases − intangible asset purchases): FY2022 222.88% (4,364 ÷ 1,958); FY2023 9.72% (189 ÷ 1,945); FY2024 11.49% (257 ÷ 2,236). Change: −213.16 pp, then +1.78 pp. The conclusion is the same.

Conclusion: On the headline formula, Zillow's FCF margin collapsed from about 224% in FY2022 (distorted by the Zillow Offers wind-down) to about 11.26% in FY2023, then recovered modestly to about 12.75% in FY2024.

Sources:
- Zillow FY2024 10-K (EDGAR-hosted, via edgar-online excerpt): cash flow and revenue figures for 2024, 2023, 2022
- Zillow FY2024 10-K (sec.gov z-20241231.htm) excerpts: operating cash flow and revenue for 2024, 2023, 2022
- Zillow FY2023 10-K (sec.gov z-20231231.htm) and FY2023 Q4 press release excerpts: 2023 and 2022 revenue and operating cash flow
- Zillow FY2022 10-K (sec.gov z-20221231.htm) excerpt: 2022 investing activity, purchases of property and equipment and intangibles
- Zillow Q4 2024 press release (prnewswire) excerpts: full-year 2024 revenue

{
    "sources": [
        {
            "url": "https://content.edgar-online.com/ExternalLink/EDGAR/0001617640-25-000016.html?hash=0cbc5b58372fd7624126f2551e8e8a884de4b57fe379aaaa014e219af2339afa&dest=z-20241231_htm",
            "name": "Zillow Group FY2024 Form 10-K (EDGAR Online excerpt)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm",
            "name": "Zillow Group FY2024 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm",
            "name": "Zillow Group FY2023 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm",
            "name": "Zillow Group FY2022 Form 10-K"
        },
        {
            "url": "https://www.nasdaq.com/press-release/zillow-group-reports-fourth-quarter-and-full-year-2022-financial-results-2023-02-15",
            "name": "Zillow Group Q4 and Full-Year 2022 Financial Results press release"
        }
    ]
}
