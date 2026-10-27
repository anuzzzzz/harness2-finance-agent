---
name: guidance_vs_actual
description: Compare a company's reported result with its own earlier guidance (beat or miss, in bps, percent or dollars) using the right pair of earnings releases.
---
ANALYTIC MOVE: result minus guidance, where guidance was issued one quarter earlier than the result.

1. Fix the two documents before searching. The ACTUAL is in the earnings release (8-K EX-99.1) for the target quarter. The GUIDANCE is in the "Outlook" section of the PRIOR quarter's release (the one issued about three months earlier). Use edgar_search with the company and filing-date filters, then parse_html_page each release under its own key.
2. With retrieve_information, ask separately: (a) the guided metric for the target quarter: midpoint and range, GAAP and non-GAAP, as labelled in the table; (b) the actual metric for that quarter, same basis. Check that the basis (GAAP vs non-GAAP) and unit (% of revenue vs $) match on both sides.
3. Compute actual minus the guidance midpoint (1 percentage point = 100 bps). Use the company-stated rounded actual (e.g. the release's "26.9%") rather than a recomputed ratio. Mention the unrounded recomputation only as a cross-check. If the question says only "beat or miss", use the midpoint, and also state the position against the range ends from the document.
4. Check that the range width and midpoint you quote come from the retrieved text, not memory. Do not carry a ± width from a snippet.
5. Answer with: the sign (beat/miss), the size in the requested unit, both inputs with period and basis, the calculation, and the URLs of both releases.

Task lead (unverified; re-confirm in text): Micron fiscal Q3 2024 (quarter ended May 30, 2024). Actual release: https://www.sec.gov/Archives/edgar/data/723125/000072312524000016/a2024q3ex991-pressrelease.htm. Guidance release (fiscal Q2 2024, issued March 2024): https://www.sec.gov/Archives/edgar/data/723125/000072312524000004/a2024q2ex991-pressrelease.htm. The Q3 10-Q rounds gross margin to a whole percent, so use the release for the actual. In the earlier run, the guided GAAP gross margin was taken from a news-site copy and never confirmed in the SEC release.
