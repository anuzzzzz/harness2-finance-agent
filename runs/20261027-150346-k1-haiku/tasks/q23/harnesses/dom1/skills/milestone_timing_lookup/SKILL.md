---
name: milestone_timing_lookup
description: Answer "when is X expected to start, open or complete" questions (plant, facility, product launch, deal close) from company filings and releases, with the original and latest guidance and the as-of date handled explicitly.
---
ANALYTIC MOVE: trace. Find the company's own stated timing for one named project, in the controlling document, and say how that statement has evolved up to the as-of date.

1. Identify the project exactly as the company names it. The question's wording may be loose. For example, a "distribution center" may be a combined manufacturing and distribution facility. Say which project you matched and why.
2. Controlling sources, in order:
   - the announcement press release (8-K EX-99.1 or the investor-relations news page) for the ORIGINAL timing;
   - the latest 10-K or 10-Q on or before the as-of date (Item 1 / MD&A "Liquidity and capital resources" / capital-expenditure or "Other developments" notes) for the CURRENT timing;
   - a subsequent 8-K or release for any delay, fire, or acceleration.
   Open at least the announcement and the latest periodic filing with parse_html_page, then retrieve_information. Search snippets are leads only.
3. Check the wording and unit of time. "Calendar year 2025" is not "fiscal 2025". Check the company's fiscal year-end and say so if the filing uses fiscal quarters. Report exactly what the text says (a year, a quarter, "no later than"), and do not turn it into a month.
4. Compare filings. If the original and the latest statements differ, report both with their dates and name the latest as the current expectation. If they agree, say they agree. Record any stated risk to the timing (for example a fire or delay) and whether the company says it expects a delay.
5. As-of date. Answer in the "expected" frame the question uses. If a later opening, start or completion is documented in an opened source dated on or before the as-of date, add it as a clearly labelled update after the main answer. Do not substitute it for the expectation.
6. Answer contract: one direct sentence giving the expected timing; the dated statements behind it (original and latest) with the document name and date; any caveat on timing; sources limited to documents actually opened. Plain text, with no citation markup.

Task facts (J.M. Smucker, McCalla, Alabama Uncrustables facility; leads from search snippets in an earlier run, so re-confirm in the opened text): the Nov 2021 announcement described a $1.1B manufacturing facility and distribution center, with construction beginning no later than Jan 2022. Snippets of later 10-K and 10-Q text said construction began in 2022 with production expected to begin in calendar year 2025, and the 10-Q for the quarter ended Jan 31, 2024 said an equipment fire was not expected to cause significant delay. Smucker's fiscal year ends April 30. The ticker is SJM, not SJ. Open the press release and the latest 10-K or 10-Q to confirm the exact wording.
