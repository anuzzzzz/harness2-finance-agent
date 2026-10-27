---
name: non_gaap_adjustment_lookup
description: Retrieve a company's full-year non-GAAP reconciling adjustment (e.g. stock-based compensation in Adjusted EBITDA) from the 10-K and cross-check it.
---

# Non-GAAP adjustment for a fiscal year

ANALYTIC MOVE: read one line item of the company's non-GAAP reconciliation (Adjusted EBITDA, adjusted net income, free cash flow) for the full fiscal year the question names.

WHERE THE FULL-YEAR FIGURE LIVES
1. Governing source: the 10-K for that fiscal year. The reconciliation is in MD&A under "Non-GAAP Financial Measures" or "Key Business Metrics and Non-GAAP", with an annual column. Use `edgar_search` with form 10-K and the ticker to get the URL.
2. Cross-checks, all from the same 10-K:
   - Cash flow statement (operating section) shows the stock-based compensation add-back.
   - The equity note or the income statement footnote gives SBC by function.
   - The MD&A line item should equal these, unless the reconciliation excludes some items. If they differ, report the reconciliation line as the answer, say why they differ, and give both.
3. The Q4 8-K Exhibit 99.1 shareholder letter often shows only quarterly columns. Do not build a full-year figure by adding four quarters when one quarter has not been read from the table. A derived sum is a fallback only. If you use it, label it as derived and read every quarter from a document.

ANSWER CONTRACT
- The figure with fiscal year, units (millions or thousands) and the exact row label from the reconciliation.
- The prior-year comparative from the same table.
- The document and table it came from, and the cross-check result.
- If asked for the "adjustment", state the sign. An add-back is positive in the reconciliation.

CHECKS BEFORE SUBMIT
- The column is the full fiscal year, not a quarter or nine months.
- Units match the table header.
- The figure agrees across the reconciliation, the cash flow statement and the SBC footnote, or the difference is explained.
- Name the `retrieve_information` call that produced the figure and quote the row.

IN THIS TASK (Airbnb, FY2024; verified only as locations, not values)
- The 10-K is https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm (accession 0001559720-25-000010). The Q4 letter is https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm.
- The earlier run parsed only the letter. The letter's reconciliation is quarterly, and its extraction was garbled. The run never opened the 10-K. It summed the quarters (295, 382, 362 and an unconfirmed Q4 of 368 = 1,407), which it flagged as least verified.
- Treat 1,407 as a lead. Confirm the annual figure in the 10-K reconciliation and the cash flow statement. Use `input_character_ranges` or a targeted prompt on the 10-K for "Stock-based compensation expense" in the Adjusted EBITDA table. If the Q4 quarter is below the nine-month-to-year difference, resolve it.
