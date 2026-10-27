---
name: company_kpi_lookup
description: Retrieve a company-defined operating metric (e.g. average nights per booking, ADR, active users, by region/segment) for a fiscal year from primary filings and report it with period, units and precision.
---
ANALYTIC MOVE: look up (and where possible cross-check) one company-defined KPI for a named period and breakdown (region/segment).

WHERE IT LIVES
- 10-K, Item 7 MD&A "Key Business Metrics" and segment/geography notes (Item 8). Regional splits are often only in the earnings release or shareholder letter, not the 10-K body.
- 8-K Item 2.02 earnings release: Exhibit 99.1 (press release / shareholder letter) with the regional KPI tables and definitions.
- Search edgar_search with the company ticker for the 10-K and the Q4 8-K EX-99.1 filed in the following Feb. Parse the document and retrieve the figure from source text; a search snippet or third-party site (statistics aggregators) is not a primary source -- use it only as a corroboration.

ANSWER CONTRACT
- State the figure exactly as disclosed (same decimals; do not round it further or substitute a third-party's more precise number unless labelled as such), the fiscal period (full year vs Q4), the region/segment, and the unit.
- Name the document (filing type, exhibit, date) the figure came from, and quote the defining sentence/table row.
- Check the metric definition (e.g. whether it excludes a business line like Experiences/Services) and mention it if it affects comparison.
- Check the period: full-year 2024 is not Q4 2024; fiscal year is not necessarily calendar year; confirm comparatives are not restated.
- If the table gives components (e.g. nights and seats booked and bookings), recompute the ratio as a sanity check and show the arithmetic; if the disclosed ratio and recomputed ratio differ, report the disclosed one and note the gap.
- In this task family (Airbnb, FY2024, Asia Pacific average nights per booking), the Q4 2024 shareholder letter (8-K EX-99.1 filed 2025-02-13) is the controlling source; the base run reported 3.3 from it (North America 4.1, EMEA 3.8, Latin America 3.7), but had not opened the filing itself -- verify in the document.
