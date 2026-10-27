---
name: kpi_metric_lookup
description: Retrieve a company-reported operating metric (nights per booking, ADR, GBV, MAUs, ARPU, same-store sales and similar) for a named period, region or segment, and report it with its definition.
---
ANALYTIC MOVE: look up one reported operating metric for a specific period and breakdown. No arithmetic is needed unless the question asks for one.

1. Find the controlling source. Operating KPIs are usually not in the financial statements. Look in this order:
   - the 10-K, in MD&A "Key Business Metrics" or the segment and geographic notes;
   - the 8-K earnings release (EX-99.1);
   - the shareholder letter or earnings presentation for the quarter containing fiscal year-end. It often holds regional splits that the 10-K lacks.
   A third-party aggregator (Statista, stats blogs) is only a cross-check. It never replaces the company document.
2. Read the figure from a fetched or retrieved passage of the company document, not from a search snippet or memory. If only a snippet was seen, run `retrieve_information` or `parse_html_page` on the document before submitting.
3. Match the question's period against the metric's period. A full-year metric is not a Q4 metric. Calendar and fiscal years can differ. Confirm that the regional definition (for example "Asia Pacific") is the company's own region label.
4. Check the metric definition and any exclusions. Example: Airbnb's company-wide nights per booking is stated "excluding experiences". Say which definition the number uses.
5. Give the figure at the precision the company published. If a third party shows a more precise number, such as 3.33 against a company-reported 3.3, give the company figure as the answer and mention the other as a cross-check.
6. Sanity-check against neighbours. The regional figures should bracket the company-wide figure, and the prior-year value should be plausible. Cite the year-over-year comparison if the document gives one.
7. The answer states: the figure, its period and unit, the company's definition, and the document it came from, with the URL.

Task fact (Airbnb, FY2024, verified only from a search snippet of the Q4 2024 shareholder letter and not from the 10-K): average nights per booking was North America 4.1, EMEA 3.8, Latin America 3.7 and Asia Pacific 3.3. The company-wide figure excluding experiences was 3.8 (3.9 in 2023). The shareholder letter is at s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf. Re-confirm these against the document if the question is asked again.
