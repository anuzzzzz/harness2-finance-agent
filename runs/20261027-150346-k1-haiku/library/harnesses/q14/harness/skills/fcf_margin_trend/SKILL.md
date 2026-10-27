---
name: fcf_margin_trend
description: Compute free cash flow (CFO minus capex) and FCF margin (FCF / revenue) for several fiscal years and describe the trend, with consistent capex definition and flagged distortions.
---
ANALYTIC MOVE: calculate then explain a trend. For each fiscal year: FCF = net cash provided by operating activities - capex; FCF margin = FCF / total revenue. Then state the direction year to year and over the whole span.

1. Inputs, each retrieved from the cash-flow statement and income statement (not from memory), for every year asked: CFO, each investing-line capex item, total revenue. The latest 10-K covers a 3-year window; open an older 10-K only if you need to confirm a year or figures may have been recast.
2. Capex definition. Name the lines used. Check the MD&A liquidity section for the company's own stated capital-spending total and reconcile to it. Capitalized software is often inside "purchases of intangible assets", not "purchases of property and equipment". Headline capex = PP&E purchases plus capitalized software / intangible purchases (the company-stated total when MD&A gives one). Because "capex" is ambiguous, show the margin on PP&E-only as a one-line labelled alternate and say whether the trend direction changes. Exclude acquisitions, investments and purchases of securities.
3. Basis checks. If a business was moved to discontinued operations, revenue may be continuing operations only while the cash-flow statement still includes the discontinued business. Say so. Check units and that fiscal years match the question.
4. Distortions. A margin above 100% or a swing of more than ~10x signals a one-off (inventory liquidation, working-capital release, settlement). Find the cause in the MD&A cash-flow discussion, quantify it, and give the trend as reported with the distorted year flagged. Do not drop or smooth the year silently.
5. Compute with unrounded inputs; round only final margins to two decimals. Recompute each division. Give FCF and margin for every year, plus the change in percentage points between years.
6. Answer contract: per-year table of CFO, capex lines, FCF, revenue, margin; the arithmetic; the trend (year over year and end to end); distortion note; capex-definition note; sources limited to documents actually opened.

Task facts (Zillow Group, CIK 1617640; retrieved in prior runs from the FY2024 and FY2023 10-Ks; re-confirm in the text), $ millions, FY2022 / FY2023 / FY2024:
- CFO 4,504 / 354 / 428. Purchases of property and equipment 115 / 135 / 143. Purchases of intangible assets (incl. capitalized internal-use software) 25 / 30 / 28. MD&A cites 171 for 2024 and 165 for 2023 (PP&E + intangibles).
- Total revenue 1,958 / 1,945 / 2,236 (continuing operations). FY2022 CFO is inflated by a 3,904 inventory decrease from the Zillow Offers wind-down.
- Headline margins (capex 140 / 165 / 171): about 222.88% / 9.72% / 11.49%. PP&E-only alternates: about 224.16% / 11.26% / 12.75%.
- FY2024 10-K: https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm . FY2023 10-K: https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm . FY2022 10-K: https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm . List a filing as a source only if you opened it.
