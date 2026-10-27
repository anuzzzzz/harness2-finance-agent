---
name: guidance_vs_actual
description: Measure how far a company's reported result beat or missed its own prior guidance (margin, revenue, EPS), in basis points or percent, GAAP and non-GAAP kept separate.
---
ANALYTIC MOVE: compare one reported actual with the guidance the company issued for that same period. Inputs: the guided figure and range, the actual figure, and the basis (GAAP or non-GAAP). Result: the signed gap, in the unit the question asks for.

1. Find the guidance in the PRIOR period's earnings release (8-K EX-99.1). It sits in the "Outlook" or "Guidance" table, usually labelled "GAAP" and "Non-GAAP" in separate rows. The guidance for fiscal quarter N is issued with the results for quarter N-1, so a quarter-N release is the wrong place for it.
2. Find the actual in the quarter-N release (8-K EX-99.1) or the 10-Q for that quarter. Use the same basis as the guidance row. Never compare a GAAP actual to a non-GAAP guide.
3. Match the period. Check the fiscal quarter label and its end date (e.g. for Micron, fiscal Q3 2024 ended May 30, 2024). Confirm that the guidance and the actual refer to that same quarter.
4. Guidance is a midpoint plus or minus a range. Report the gap versus the midpoint as the headline "beat or miss". Also state where the actual sits against the low and high ends: above the range, inside it, or below it.
5. Margin gaps are percentage-point differences. Convert with 1 percentage point = 100 bps. Take the actual margin from the company's stated percentage, or compute gross margin $ / revenue $ from the same table. If the two differ in the second decimal, give the headline in bps from the company-stated percentage and the unrounded value as a labelled cross-check, so the reviewer sees both.
6. Retrieve every figure from the filing text (parse_html_page, then retrieve_information). Do not use a search snippet or memory. Name the document for each figure, and do not cite documents you did not open.
7. Answer contract: guidance midpoint and range with basis and period; actual with basis, dollars and percent; the calculation shown; signed result in bps (beat is positive, miss is negative); where the actual sits against the range; sources.

Task lead for Micron fiscal Q3 2024 (unverified here, re-confirm in the filings): the Q2 FY2024 release (https://www.sec.gov/Archives/edgar/data/723125/000072312524000004/a2024q2ex991-pressrelease.htm) guided GAAP gross margin to 25.5% plus or minus 1.5%. The Q3 release (https://www.sec.gov/Archives/edgar/data/723125/000072312524000016/a2024q3ex991-pressrelease.htm) reported GAAP gross margin of $1,832M on revenue of $6,811M, which is about 26.9%. The management claim of "above the high end" refers to non-GAAP, so check which basis a statement refers to.
