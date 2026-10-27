---
name: kpi_metric_lookup
description: Retrieve a company-reported operating metric (nights per booking, ADR, GBV, MAUs, ARPU, same-store sales and similar) for a named period, region or segment, and report it with its definition.
---
ANALYTIC MOVE: look up one reported operating metric for a specific period and breakdown. No arithmetic is needed unless the question asks for one.

1. Find the controlling source. Operating KPIs are usually not in the financial statements. Look in this order:
   - the 10-K, in MD&A "Key Business Metrics", "Geographic Mix" or the segment and geographic notes;
   - the 8-K earnings release (EX-99.1);
   - the shareholder letter or earnings presentation for the quarter containing fiscal year-end.
   A third-party aggregator (Statista, stats blogs) is only a cross-check, never a replacement for the company document.
2. Read the figure from a fetched or retrieved passage of the company document (parse_html_page then retrieve_information), not from a search snippet or memory.
3. Match the question's period to the metric's period. A full-year metric is not a Q4 metric. Confirm the region label is the company's own.
4. Check the metric definition and any exclusions (e.g. Airbnb's company-wide nights per booking is "excluding experiences") and state which definition the number uses.
5. Give the figure at the precision the company published (e.g. 3.3, not a third party's 3.33); mention the other as a cross-check.
6. Sanity-check against neighbours: regional figures should bracket the company-wide figure; cite the prior-year comparison if the document gives one.
7. The answer states: the figure, period and unit, the company's definition, and the document and URL it came from.

Lead (unverified, re-confirm in text): Airbnb FY2024 average nights per booking was North America 4.1, EMEA 3.8, Latin America 3.7, Asia Pacific 3.3; company-wide 3.8 (3.9 in 2023). One run retrieved this from the FY2024 10-K MD&A "Geographic Mix" (https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm).
