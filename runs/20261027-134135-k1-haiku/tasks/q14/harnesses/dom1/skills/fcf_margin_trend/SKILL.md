---
name: fcf_margin_trend
description: Free cash flow / FCF margin (CFO minus capex, over revenue) across several fiscal years, including cases with discontinued operations or working-capital distortions.
---

# FCF and FCF margin trend

Analytic move: CALCULATE FCF = CFO - capex for each year, divide by that year's revenue, then COMPARE the years and name the trend.

## Inputs (all from the consolidated statements of cash flows / income statement)
- CFO: "Net cash provided by (used in) operating activities", as reported. Note whether it is total or continuing operations.
- Capex: use the investing-section purchase lines. Default is "Purchases of property and equipment". Check the notes to see whether capitalized software or website development sits inside that line (it usually does). Treat separate "Purchases of intangible assets" as a labelled sensitivity, not the headline. State which definition you used.
- Revenue: total revenue from the income statement, taken from the latest filing that presents the year (restated for discontinued operations). Check that the original and the restated figure match.
- Years: read each year from a filing that presents it. Open the 10-K of the OLDEST year too, and confirm its CFO and capex against the later filings' comparative columns. If they differ (restatement or recast), say which you used.

## Checks before submitting
1. Units are the same for CFO, capex and revenue (millions vs thousands).
2. Show for each year: CFO, capex, FCF, revenue, margin (unrounded until the end).
3. Look for one-off swings in CFO (wind-down of a discontinued business, inventory liquidation, large settlements). Find the line in the cash flow statement or MD&A that drives them. State the as-reported margin series, then say how much of any outlier the swing explains, and give the underlying trend direction for the years that are comparable. Do not drop the as-reported figure.
4. The conclusion must state the direction year by year (up, down, magnitude in percentage points) and the overall FY-start to FY-end change.

## Task fact (Zillow, as read in an earlier run; re-verify from the filings before use)
- Zillow Group (CIK 1617640) 10-Ks list CFO of 4,504 / 354 / 428 ($M) for FY2022 / FY2023 / FY2024, purchases of property and equipment of 115 / 135 / 143, purchases of intangible assets of 25 / 30 / 28, and revenue of 1,958 / 1,945 / 2,236. The FY2022 CFO includes about $3.9B of inventory run-off from the discontinued Zillow Offers business.
