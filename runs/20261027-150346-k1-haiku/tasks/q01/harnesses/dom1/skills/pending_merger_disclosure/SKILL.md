---
name: pending_merger_disclosure
description: Explain how a company has addressed a pending merger or acquisition and what it does to its operations, using the company's own filings (10-K risk factors, business update, legal proceedings, 8-Ks, proxy material) as of the question date.
---
ANALYTIC MOVE: explain/trace. Inputs are the company's own disclosures about the deal. Result: a dated account of (a) deal status and legal or regulatory path, (b) operating restrictions, (c) effects on employees, customers and suppliers, (d) how the business is being run meanwhile.

1. Cutoff. Use only documents dated on or before the question date. A later 10-Q, press article or merger-agreement summary may appear in search. Do not use it or list it as a source, because it describes events after the cutoff.
2. Controlling sources, in order:
   - The latest 10-K before the date. Item 1 (Agreement and Plan of Merger, Business Strategy, Capital Allocation), Item 1A (merger-related risk factors), Item 3 (Legal Proceedings), Item 7 (Business Update, Capital Requirements) and Note 1.
   - 8-Ks (Item 8.01 or 7.01, EX-99) for status events. Find them with edgar_search by CIK and date range.
   - DEFA14A and proxy filings for management's own messaging. Note that a filing the agent has not opened can't be cited.
3. Required parts of the answer:
   - Status timeline with exact dates: signing, shareholder vote, regulatory or government action, extension or outside dates, litigation filed.
   - Interim operating covenants: ordinary-course requirement, consent rights (M&A, debt, buybacks), non-solicit, and what the company says it can't do because of them.
   - Stated effects on employees, retention, labor relations, customers and suppliers. Label each as a company-stated risk or an actual event.
   - Continuing operations and capital plans: capex guidance, major projects, and the benefits the company says it would lose if the deal fails (investment commitments, termination fees). Give figures with period and unit.
   - A plain statement of what the filings do not say, for example "no retention program disclosed".
4. Checks: every date and dollar figure was retrieved from an opened document, and each is attributed to the document it came from. Don't state a termination fee, outside date or per-share price unless retrieved. Write plain text with no citation markup.

Task facts (in this task: United States Steel, CIK 1163302, Nippon Steel merger; re-confirm in the text). The FY2024 10-K (filed Jan 31, 2025) is https://www.sec.gov/Archives/edgar/data/1163302/000116330225000018/x-20241231.htm. One run retrieved the following from it. On Jan 3, 2025 the President issued an order prohibiting the merger and requiring abandonment within 30 days. On Jan 10, 2025 CFIUS extended that deadline to June 18, 2025. A Petition for Review was filed in the D.C. Circuit alleging the order was issued for purely political reasons. The risk factor is titled "We are subject to business uncertainties and contractual restrictions while the Merger is pending". The 10-K also covers limits on debt and buybacks, BR2 construction in Arkansas, and Wheeling-Nippon sales. Do not cite the Q1 2025 10-Q: it postdates April 7, 2025.
