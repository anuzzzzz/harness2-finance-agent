---
name: retail_comparable_sales
description: Look up a retailer's same-store / comparable-store sales growth for a fiscal quarter or year from its earnings release or 10-K, with the correct period, sign and definition.
---

# Retail same-store / comparable sales lookup

ANALYTIC MOVE: lookup plus classification. Map the question's wording ("same-store sales", "SSS", "comps", "comparable store sales") to the company's own reported metric, then read its value for the exact fiscal period.

WHERE IT LIVES
- Quarterly: the 8-K EX-99.1 earnings release for that quarter. The headline bullets and the "Fourth Quarter / Fiscal Year Results" paragraph state the comp %.
- Full year: the same Q4 release, or the 10-K MD&A (key performance measures and the "Comparable store sales" discussion). The 10-K usually breaks the full-year comp into transactions and average ticket.
- Fiscal quarters are not calendar quarters. Name the quarter by its end date (for example "13 weeks ended Dec 26, 2024") and make sure the figure is for that quarter, not the full year or a neighbouring quarter. The Q4 release prints the Q4 comp and the full-year comp side by side, so check which one you picked.

ANSWER CONTRACT
1. The comp % with its sign. Say plainly "growth of -0.8%" or "a decline of 0.8%" as the case may be. Do not report a negative comp as growth without saying so.
2. The period (fiscal quarter, with the end date) and the company's name for the metric.
3. The company's definition, retrieved from the filing (for example, how long a store must be open to enter the comp base, and how e-commerce or relocated stores are treated). Do not state a definition from memory.
4. Total net sales growth for the same period, if the release gives it, so the reader sees that comp and total growth differ (new stores drive total growth). Do not substitute one for the other.
5. The full-year comp as context only if it is retrieved. Keep it clearly separate from the quarter figure.
6. Sources: only documents you opened. Plain text, no citation markup.

CHECKS BEFORE SUBMITTING
- The percentage is the period named in the question (quarter versus year).
- The figure is the company's reported comp. Do not rebuild it from dollar sales.
- If the release has several comp measures (total, store-only, ticket, transactions), report the headline comp and name any others separately.

TASK FACTS (Floor & Decor Holdings, FND; verified as sources, to be re-confirmed in the opened text)
- FND's term is "comparable store sales". The SEC CIK is 1507079; use the CIK, not the ticker, in edgar_search.
- Fiscal 2024 Q4 was the quarter ended December 26, 2024. The release is the 8-K EX-99.1 at https://www.sec.gov/Archives/edgar/data/1507079/000150707925000012/fnd-2024earningsreleaseex9.htm, and the 10-K is https://www.sec.gov/Archives/edgar/data/1507079/000150707925000013/fnd-20241226.htm.
- The earlier run's search snippets gave Q4 2024 comparable store sales of -0.8%, net sales of $1,107.4M (+5.7%), and a full-year comp of -7.1%. Confirm these in the opened release.
