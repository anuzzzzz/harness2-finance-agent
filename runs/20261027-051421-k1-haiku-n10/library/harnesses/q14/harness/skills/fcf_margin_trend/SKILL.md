---
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
3. Prefer figures read from filings. Aggregator pages (stockanalysis, macrotrends, marketbeat) are leads or cross-checks only: do not take their precomputed FCF or margin as inputs, and name any year whose input came only from an aggregator or was derived (e.g. backed out from a percentage).
4. Confirm units (millions vs thousands). Report changes between years in percentage points.
5. Trend wording: for each step say rises or falls with the pp change; say whether the whole path is monotonic; if one year is an outlier, state the trend excluding it.
6. Recheck: FCF = CFO − capex each year, margin = FCF ÷ revenue, and the stated direction matches the numbers.

**Answer contract:** a per-year table (CFO, capex, FCF, revenue, margin to two decimals, units, period), formula and arithmetic, pp change per step, one-sentence trend conclusion, any outlier explanation, and each figure's source type (opened filing, search excerpt, or third-party page). Plain text, no raw citation tags.
