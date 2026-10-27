---
name: company_kpi_definition_lookup
description: Answer "does the company report metric X (retention, churn, ARR, backlog, etc.) and how does it define it" from the 10-K/10-Q, including how the disclosure changed over time.
---
ANALYTIC MOVE: classify and trace. Decide whether the company reports the metric, in which documents, with what exact definition and latest value, and whether the disclosure changed.

1. Controlling source: the latest 10-K before the as-of date, in Item 7 MD&A "Key Business Metrics" or a section named for the metric. Check the latest 10-Q too. Earnings releases and prepared remarks only repeat the value. Retrieve the heading, the definition, the value and its as-of date, all from the opened text.
2. Check the gross and the net variant separately. Report each as reported, or state "not reported" only after retrieving from the relevant section of the opened filing. Do not infer absence from one failed retrieval. Re-ask with different wording.
3. Definition contract. Give the company's own wording on: the numerator and denominator (or what is compared); what is included and excluded (expansion, price, churn, contract terms under one year); the measurement basis (ARR, constant currency, annualisation method); and the measurement date. Give the latest value with its date and unit.
4. Disclosure history. Metrics are sometimes changed after SEC staff comment letters. Check the prior-year 10-K and the CORRESP/UPLOAD letters in edgar_search results. Open them before saying a metric was dropped or added, and give the period of the change. Open the letters if you cite them.
5. Answer: yes/no per metric, then the definition, the value with its date, and the history. State plainly anything you did not verify.

Task facts (Workday, WDAY; from search results, re-confirm in the opened text):
- The FY2025 10-K (fiscal year ended Jan 31, 2025, filed 2025-03-11) is https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm. The 10-Q for the quarter ended Oct 31, 2024 is https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm.
- SEC correspondence found in edgar_search: CORRESP filed 2024-09-04 (https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm) and an UPLOAD staff letter dated 2024-08-20. A later 10-K for FY2026 may appear in search results. It postdates the 2025-04-07 as-of date, so do not use it.
- Snippet-level leads, not yet confirmed from opened text: the FY2025 10-K carries a "Gross Revenue Retention Rate" section with a value of about 98%, and Workday told the SEC it would drop net retention disclosure after the quarter ended Oct 31, 2024. Retrieve the definition wording from the 10-K itself.
