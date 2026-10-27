---
name: guidance_vs_actual
description: Measure how far a company's reported result beat or missed its own prior guidance (margin, revenue, EPS), in bps, percent or dollars, using the right pair of earnings releases and keeping GAAP and non-GAAP separate.
---
ANALYTIC MOVE: result minus guidance, where the guidance was issued one quarter before the result.

1. Fix the two documents before searching. The ACTUAL is in the earnings release (8-K EX-99.1) for the target quarter. The GUIDANCE is in the "Outlook" table of the PRIOR quarter's release (issued about three months earlier). A quarter-N release is the wrong place for quarter-N guidance. Use edgar_search with company and date filters, or the URLs in the lead below. Then parse_html_page each release under its own key.
2. With retrieve_information, ask separately: (a) the guided metric for the target quarter, with midpoint, ± band and GAAP/non-GAAP labels as printed; (b) the actual for that quarter on the same basis, in dollars and as a percent of revenue. Confirm that period, basis and unit match on both sides. Never compare a GAAP actual with a non-GAAP guide.
3. Headline = actual minus guidance midpoint (1 percentage point = 100 bps; beat positive, miss negative). Use the company-stated rounded percentage for the headline (e.g. the release's "26.9%"). Also give an unrounded cross-check of dollars / revenue, computed carefully and labelled as a cross-check. Say plainly if the two differ in the last digits.
4. State where the actual sits against the guided range: above, inside or below. Give the distance to the nearest end. If the range is derived from midpoint ± band, say so. If management says "above the high end", check which basis (GAAP or non-GAAP) the statement refers to.
5. Take every figure from retrieved text, not from snippets or memory. Do not cite a document you did not open.
6. Answer with: the sign and size in the requested unit; guidance (midpoint, range, basis, period); actual (basis, dollars, percent, period); the calculation; the position versus the range; and the URLs of both releases.

Task lead (unverified; re-confirm in text): Micron fiscal Q3 2024 (quarter ended May 30, 2024). Actual release: https://www.sec.gov/Archives/edgar/data/723125/000072312524000016/a2024q3ex991-pressrelease.htm. Guidance release (fiscal Q2 2024, issued March 2024): https://www.sec.gov/Archives/edgar/data/723125/000072312524000004/a2024q2ex991-pressrelease.htm. The 10-Q rounds gross margin to a whole percent, so use the release for the actual.
