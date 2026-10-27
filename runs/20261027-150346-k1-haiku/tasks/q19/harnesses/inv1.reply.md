<file path="LongTermMEMORY.md">
# Verified task facts (label: facts, not procedure; re-confirm in the filing before use)

- In this task (MSCI operating-lease maturities as of April 07, 2025), the latest 10-K filed before that date is for FY2024 (period ending 2024-12-31, filed 2025-02-07): https://www.sec.gov/Archives/edgar/data/1408198/000140819825000053/msci-20241231.htm. The accession is 0001408198-25-000053. No 10-Q for Q1 2025 existed yet.
- The figures sit in Note 7 "Leases", table "Maturity of Lease Liabilities", column "Operating Leases", in $ thousands: 2025 30,220; 2026 30,361; 2027 24,421; 2028 23,931; 2029 16,573; Thereafter 40,099; Total lease payments 165,605; Less interest (19,601); Present value 146,004.
- "Next three years" = 2025-2027 = 85,002. This is 51.33% of the undiscounted total of 165,605 (58.22% of the discounted present value of 146,004). The undiscounted schedule is the natural base because the maturities are undiscounted payments. State the base used.
</file>

<file path="tool_guidance.md">
# Tool use

- Before searching, decide the form, company and fiscal period. For an "as of <date>" question, use the latest periodic filing filed on or before that date. Search edgar_search with company and form-type filters rather than the question's wording.
- Store each parsed filing under a clear key. Ask retrieve_information one targeted question at a time (for example "operating lease maturity table in the Leases note, with units"). Use input_character_ranges on long filings.
- Before computing, confirm from the retrieved text each figure's period, unit and measure (undiscounted vs present value). Check that the schedule sums to its stated total. Carry full precision and round only the final number.
- For a percentage, state the numerator and the denominator. If the denominator is ambiguous, give the primary basis in the answer, and the alternative only as a labelled cross-check.
- Submit with submit_final_result as soon as the figures are verified. Write plain text with no citation markup.
</file>

<notes>
The base run (base1) found the right FY2024 10-K, parsed it, retrieved the Note 7 maturity table, and computed 85,002 / 165,605 = 51.33%. It then submitted, so the workflow itself needs little change. There is one rollout and nothing diverged, so I kept edits small.
- LongTermMEMORY.md: records the facts the run actually retrieved (filing URL, note, table, figures, undiscounted vs discounted base). A repeat run can go straight to the source and verify it. The facts are labelled as task-specific and to be re-confirmed.
- tool_guidance.md (was empty): added short generic sequencing for the research desk. It covers picking the filing by the "as of" date, targeted retrieval, checking units and that the schedule sums, stating the percentage's denominator, and submitting promptly. These match what base1 did well, so they lock in the behaviour. They also make the denominator choice explicit, which was the one judgment call in base1.
</notes>