---
name: nongaap_addback_lookup
description: Retrieve a full-year add-back or adjustment (stock-based compensation, D&A, restructuring, etc.) from a company's Adjusted EBITDA / non-GAAP reconciliation and report it with period, units and source.
---
ANALYTIC MOVE: look up one line of a non-GAAP reconciliation for a fiscal year. Sum quarters only if no annual column exists, and cross-check against the GAAP footnote.

1. Pick the controlling documents. The annual add-back is in the 10-K MD&A non-GAAP section (Adjusted EBITDA reconciliation) and in the stock-compensation footnote or cash-flow statement. The Q4 8-K EX-99.1 (shareholder letter) often shows only quarterly columns. Find the 10-K or the EX-99.1 through edgar_search with company and date filters.
2. Parse the document yourself and retrieve the line from that text. Ask for the exact label, the amount for the requested year, the prior-year comparative, and the units (millions or thousands). If only quarters are shown, sum the four quarters of the requested fiscal year. Then confirm against a second statement in the same filing, such as the SBC footnote or the cash-flow "stock-based compensation" line. Say which basis each number came from.
3. Match the period. Use the fiscal year the question names, and check that the fiscal year-end is December 31 or otherwise. Do not use a trailing, quarterly or prior-year figure.
4. Keep the add-back (the pre-tax expense added to net income to reach Adjusted EBITDA) separate from other SBC measures such as the amount capitalized, tax effects, or unrecognized compensation cost.
5. Cite only documents you opened and retrieved from in this run. Do not list 10-Qs or the 10-K as sources, and do not attribute a quarterly figure to a filing you did not read. If the 10-K was not opened, say the figure comes from the 8-K exhibit.
6. The answer states: the amount with units and fiscal year, the reconciliation line label, the quarterly components or the annual column used, the cross-check, and the URL of each document actually read.

Lead (verified in one run from the Airbnb Q4 2024 EX-99.1, https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm; re-confirm in the text): Airbnb FY2024 stock-based compensation expense add-back was $1,407M (quarters 295 + 382 + 362 + 368), against $1,120M in FY2023. The letter reconciles quarterly only, and the FY total matches the SBC footnote. The 10-K is at https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm.
