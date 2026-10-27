---
name: marketplace_take_rate
description: Compute a marketplace or platform take rate (revenue / gross booking value, GMV or similar volume) for several fiscal years from 10-K figures and present it in the format the question asks for.
---
ANALYTIC MOVE: calculate a ratio per fiscal year, then compare the years. Inputs: reported revenue and the reported gross volume metric (GBV, GMV, TPV) for each year. Result: one ratio per year and a one-sentence trend.

1. Locate the inputs.
   - Volume metric: 10-K MD&A "Key Business Metrics". Revenue: the income statement or the Results of Operations table. Both are in $ millions.
   - The latest 10-K carries three years of revenue but often only two years of the volume metric. Check the older 10-K for the earliest year and say which filing each figure came from. Use the latest filing's figure if a later 10-K restated an earlier year.
2. Match the periods. Revenue and volume must be for the same fiscal year, and "FY" means the company's own fiscal year. Check that the units agree ($ millions against $ billions).
3. Use total reported revenue over the reported volume metric unless the question says otherwise. State this definition. Do not substitute a segment revenue or an adjusted measure. A take rate is an analyst ratio the company does not report, so say it is computed.
4. Calculate with unrounded inputs, round only the final ratio to two decimals (13.29%, not 13%). Show the formula and the arithmetic for each year. Compute the year-on-year change in percentage points from the unrounded ratios.
5. Answer contract. Follow the shape the question asks for. If it asks for each year on a separate line plus a one-sentence comment, give exactly that: one line per year (e.g. "FY2022: 13.29% (revenue $8,399M / GBV $63,212M)") and one sentence for the trend, stating the direction and the size in points. Put the inputs and sources after it. Do not add extra commentary paragraphs.
6. Sources. List only the filings you opened and retrieved the figures from. Write plain text with no citation markup.

Task facts (Airbnb, verified from the FY2023 and FY2024 10-Ks; re-confirm in the text). GBV is defined as the dollar value of bookings, including host earnings, service fees, cleaning fees and taxes, net of cancellations and alterations. In $ millions:
- FY2022: revenue 8,399, GBV 63,212, giving 13.29%
- FY2023: revenue 9,917, GBV 73,252, giving 13.54%
- FY2024: revenue 11,102, GBV 81,784, giving 13.57%
So the rate is up about 0.25 points in 2023 and 0.03 points in 2024, a modest rise that is nearly flat in 2024. URLs: FY2024 10-K https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm; FY2023 10-K https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm.
