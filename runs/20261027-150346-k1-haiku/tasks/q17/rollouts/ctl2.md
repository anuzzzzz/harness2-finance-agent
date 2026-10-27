## Rollout `ctl2`
- outcome: submitted
- turns: 1; cost: $0.046; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Airbnb full year 2024 results gross booking value revenue") → 10 results: Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm>; Airbnb, Inc. - Form DEF 14A - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524102960/d636281ddef14a.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm>; Airbnb, Inc. - Form PRE 14A - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524080883/d636281dpre14a.htm>
- web_search(query="Airbnb full year 2023 results gross booking value revenue") → 10 results: Airbnb, Inc. - Form DEF 14A - FY2023 <https://www.sec.gov/Archives/edgar/data/1559720/000119312523109099/d406835ddef14a.htm>; Airbnb, Inc. - Form 8-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1559720/000119312523268164/d481318dex991.htm>; Airbnb, Inc. - Form 10-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm>; Airbnb, Inc. - Form 8-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1559720/000119312523039008/d451233dex991.htm>; Airbnb, Inc. - Form 8-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1559720/000119312523202832/d446942dex991.htm>
- web_search(query="Airbnb full year 2022 results gross booking value revenue") → 10 results: Airbnb, Inc. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000119312522210001/d353427dex991.htm>; Airbnb, Inc. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000119312522274904/d408297dex991.htm>; Airbnb, Inc. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000119312522138654/d711122dex991.htm>; Airbnb, Inc. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000155972022000009/abnb-20220331.htm>; Airbnb, Inc. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000155972022000012/abnb-20220630.htm>
- web_search(query="Airbnb 2024 10-K key business metrics Gross Booking Value table 2023 2024 millions") → 9 results: Airbnb, Inc. - Form 10-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm>; Airbnb, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm>; Airbnb, Inc. - Form 10-K - FY2024 (Annual Financial Statement Tables - full year 2024) <https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/Financial_Report.xlsx>; Q3 2024 Shareholder Letter <https://s26.q4cdn.com/656283129/files/doc_financials/2024/q3/Airbnb_Q3-2024-Shareholder-Letter_Final.pdf>; Airbnb Revenue and Booking Statistics (2026) <https://backlinko.com/airbnb-stats>
- submit_final_result({"final_result": "Airbnb's implied take rate (revenue ÷ Gross Booking Value), calculated from company-reported figures:\n\n**FY2022:** 13.29% (Revenue ≈ $8,399M ÷ GBV $63,212M)\n**FY2023:** 13.54% (Revenue $9,917M ÷ GBV $73,252M)\n**FY2024:** 13.57% (Revenue $11,102M ÷ GBV $81,784M)\n\n**Trend comment:** The take rate rose modestly from about 13.29% in 2022 to 13.54% in 2023, then edged up only about 3 basis points to 13.57% in 2024, so the gains are leveling off.\n\n**Inputs and reasoning:**\n- GBV: The FY2023 10-K table shows <cite index=\"13-3\">Gross Booking Value | $63,212 | $73,252</cite> for 2022 and 2023. The FY2024 10-K shows <cite index=\"32-4\">Gross Booking Value | $73,252 | $81,
…[truncated 1,865 chars])

### Final answer
Airbnb's implied take rate (revenue ÷ Gross Booking Value), calculated from company-reported figures:

**FY2022:** 13.29% (Revenue ≈ $8,399M ÷ GBV $63,212M)
**FY2023:** 13.54% (Revenue $9,917M ÷ GBV $73,252M)
**FY2024:** 13.57% (Revenue $11,102M ÷ GBV $81,784M)

**Trend comment:** The take rate rose modestly from about 13.29% in 2022 to 13.54% in 2023, then edged up only about 3 basis points to 13.57% in 2024, so the gains are leveling off.

**Inputs and reasoning:**
- GBV: The FY2023 10-K table shows <cite index="13-3">Gross Booking Value | $63,212 | $73,252</cite> for 2022 and 2023. The FY2024 10-K shows <cite index="32-4">Gross Booking Value | $73,252 | $81,784</cite> for 2023 and 2024.
- Revenue: <cite index="39-5">2023 | 9,917; 2024 | 11,102</cite> ($ millions). For 2022, the company reported <cite index="27-8">revenue of $8.4 billion grew 40% year over year (46% ex-FX).</cite> The exact figure of $8,399M is consistent with the 2022 U.S. ($3,890M) plus International ($4,509M) revenue split reported in the same data set. A third-party analysis also cites an <cite index="28-14">implied take rate (revenue divided by GBV) was 13.3%</cite> for 2022, which matches.
- Calculations: 8,399 ÷ 63,212 = 13.29%; 9,917 ÷ 73,252 = 13.54%; 11,102 ÷ 81,784 = 13.57% (rounded to two decimals at the final step).

Note: Airbnb does not report a take rate directly; the figures above are implied from revenue and GBV, as the company itself defines it in shareholder materials.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm",
            "name": "Airbnb, Inc. Form 10-K FY2023"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K FY2024"
        },
        {
            "url": "https://s26.q4cdn.com/656283129/files/doc_financials/2022/q4/Airbnb_Q4-2022-Shareholder-Letter_Final.pdf",
            "name": "Airbnb Q4 2022 Shareholder Letter"
        },
        {
            "url": "https://sqmagazine.co.uk/airbnb-statistics/",
            "name": "SQ Magazine - Airbnb Statistics 2026 (revenue and GBV tables)"
        },
        {
            "url": "https://www.thewolfofharcourtstreet.com/p/airbnb-headcount-down-5-revenue-up",
            "name": "The Wolf of Harcourt Street - Airbnb Full Year 2022 Earnings Analysis"
        }
    ]
}