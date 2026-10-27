---
name: guidance_metrics_inventory
description: Answer "what metrics does company X guide on in its earnings reports" by reading the outlook section of the latest earnings release and supplemental deck, then listing each guided metric with its period, basis and latest range.
---
ANALYTIC MOVE: classify and list. Input: the company's most recent earnings release and any supplemental or investor deck filed as of the question's date. Result: the complete list of metrics the company gives forward ranges or targets for, each with its period, basis and unit.

1. Find the controlling documents.
   - Open the latest earnings release (8-K EX-99.1) for the most recent completed quarter before the as-of date. Open the supplemental or investor-update exhibit (often EX-99.2) if the filing has one.
   - Ignore filings dated after the as-of date. Search results often surface later quarters.
   - Guidance is usually in an "Outlook" or "Guidance" section, a table near the end of the release or deck, or the CFO prepared remarks. Do not infer the list from news snippets or call Q&A, since journalists report only the headline items (usually EPS).
2. Build the list by asking retrieve_information for every guided line: "list every forward-looking metric in the outlook or guidance section, with its period (next quarter or full year), range, and whether it is GAAP or adjusted". Ask a second time about items that may be missing or only qualitative (capacity, unit cost, fuel or input prices, non-operating items, tax rate, capex, free cash flow, leverage).
3. Separate the metrics into groups: next-quarter table; full-year table; longer-term targets (multi-year, investor-day, labelled as not current-year guidance); and narrative-only figures given in management quotes or remarks but not in the table. Label each metric with its group.
4. Record for each metric: the exact name as the company writes it, the unit (percent change versus the prior-year period, cents or dollars per share, $ per gallon, $ billions), the GAAP or adjusted basis, and the range. Keep "year over year growth" separate from "absolute level". Never convert or restate a range.
5. Do not mix periods. A quarter guided in January is not a full year. For a generic question ("what does it guide on"), give the list of metrics first, then the latest ranges as illustrations, labelled with the date of the release they came from.
6. Consistency checks before submitting.
   - Each metric listed was seen in the opened text. If a figure appears in one retrieval but not in the table (for example a narrative EPS level), re-query to confirm it, and report it as narrative-only rather than dropping it or calling it unconfirmed without checking.
   - If the release and a deck disagree on the metric list, report both and say which is more recent. A prior-year deck is not the current set.
   - Do not say a metric is not guided unless the outlook table and the remarks were searched. Say "not found in the opened documents" instead.
7. Answer contract: a headline sentence; the metrics grouped as above, each with unit, basis, and latest range with its period; the release and date; sources limited to documents actually opened and retrieved from. Plain text, no citation markup.

Lead (Delta Air Lines, as of April 7, 2025; from earlier runs, so confirm in the opened text): the December-quarter 2024 release is https://www.sec.gov/Archives/edgar/data/27904/000168316825000182/delta_ex9901.htm. Its tables gave 1Q25 total revenue growth, operating margin and EPS, and FY2025 EPS growth, free cash flow and gross leverage, plus 3-5 year targets. Capacity, fuel price and capex were not guided numerically there. Figures like FY2025 EPS above $7.35, pre-tax income above $6 billion and low-single-digit non-fuel unit cost growth appeared only in narrative.
