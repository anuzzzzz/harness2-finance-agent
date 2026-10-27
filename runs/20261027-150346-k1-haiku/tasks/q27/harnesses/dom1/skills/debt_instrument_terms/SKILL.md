---
name: debt_instrument_terms
description: Report the terms of a named debt or hybrid security (junior subordinated debentures, subordinated notes, preferred) from a company's 10-K debt note, with each term tied to opened text.
---
ANALYTIC MOVE: trace and classify. The input is a named instrument and a fiscal year. The result is a term sheet for that instrument only, read from the filing's own words.

1. Where the terms live. In a 10-K, the governing text is the debt note in the financial statements (often titled "Capital Structure" or "Debt"). It has a table of principal, rate and maturity by instrument, followed by narrative on call, interest deferral and covenants. MD&A "Capital Resources" and Item 5 or the exhibit index give corroboration. Open the filing itself. A snippet or a prior-year filing is not enough. Terms can change between years, for example a LIBOR replacement.
2. Keep look-alike instruments apart. "Junior subordinated debentures" are different from "subordinated debentures", "senior notes" and preferred stock. Each has its own principal, rate and maturity. Name the instrument exactly as the table does. If the filing has several lines, report only the one asked about, and note the others in one line.
3. Term checklist, each tied to the opened text and flagged "not stated" if absent:
   - issuer, series name and the principal outstanding at fiscal year-end, with the prior year for comparison, in the filing's units;
   - coupon, fixed or floating, any switch date, and the floating benchmark plus spread. Check for a LIBOR-to-SOFR fallback and the spread adjustment;
   - scheduled maturity versus final maturity;
   - optional redemption: dates, price and any make-whole;
   - interest deferral: maximum length, compounding, any obligation to issue stock, and the dividend or repurchase restrictions that apply during deferral;
   - ranking and any replacement-capital covenant, only if the filing says so. Do not infer them.
4. Answer contract: a short lead sentence giving the instrument, principal and coupon. Then the term list with periods and units. Then the document and section for each term. Include only what the question asks. Leave out ratings and commentary unless asked. Quote dates exactly (day, month, year).
5. Before submitting, confirm that every term comes from text you retrieved in this session, that the fiscal year is the one asked, and that the sources list only opened documents.

Task facts (Allstate FY2024; they came from search snippets of the 10-K, so re-confirm them in the opened text). The FY2024 10-K is at https://www.sec.gov/Archives/edgar/data/899051/000089905125000015/all-20241231.htm (CIK 899051). Snippets showed $500 million of Series A 6.500% Fixed-to-Floating Rate Junior Subordinated Debentures due 2067. The scheduled maturity is May 15, 2057 and the final maturity is May 15, 2067. They are redeemable at par on or after May 15, 2037, or earlier at a make-whole price in certain circumstances. After May 15, 2037 they pay quarterly at three-month CME Term SOFR plus a spread adjustment of 0.26161% plus 2.120%, replacing LIBOR. Interest may be deferred for up to 10 years and compounds during deferral. The floating rate subordinated debentures due 2053 are a separate instrument.
