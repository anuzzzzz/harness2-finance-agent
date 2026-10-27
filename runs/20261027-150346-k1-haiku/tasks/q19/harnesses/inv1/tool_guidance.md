# Tool use

- Before searching, decide the form, company and fiscal period. For an "as of <date>" question, use the latest periodic filing filed on or before that date. Search edgar_search with company and form-type filters rather than the question's wording.
- Store each parsed filing under a clear key. Ask retrieve_information one targeted question at a time (for example "operating lease maturity table in the Leases note, with units"). Use input_character_ranges on long filings.
- Before computing, confirm from the retrieved text each figure's period, unit and measure (undiscounted vs present value). Check that the schedule sums to its stated total. Carry full precision and round only the final number.
- For a percentage, state the numerator and the denominator. If the denominator is ambiguous, give the primary basis in the answer, and the alternative only as a labelled cross-check.
- Submit with submit_final_result as soon as the figures are verified. Write plain text with no citation markup.
