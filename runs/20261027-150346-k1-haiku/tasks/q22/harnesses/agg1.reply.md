<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form type, fiscal period. Search with those filters, e.g. edgar_search with the CIK and form_types. Do not search with the question's wording. Never send an empty or null web_search query. If web_search returns nothing, go straight to edgar_search or a known URL.
- A snippet or result title is a lead, not evidence. Open each primary document with parse_html_page under a clear key. Then ask retrieve_information one targeted question at a time, quoting the table row and column headers. Use input_character_ranges on long filings.
- Multi-year questions: each 10-K's comparative table covers only two or three years. Plan the fewest filings that cover every requested year. Do not open a filing whose years another opened filing already covers.
- Ratio questions: take the numerator and denominator from the same table in the same filing, with the same period and units. Check units (millions versus billions) before dividing. Carry full precision and round only the final number.
- Where a filing prints a metric rounded in a table and with more precision in narrative text, make the headline answer from the table figures as printed. Show the more precise narrative-based result beneath it, labelled as an alternate. Never build a figure by adding a reported change to another year's figure, because that is a derived input. If you must, label it as derived.
- Re-check every figure against the retrieved text (period, unit, basis) before computing. A successful tool call does not establish that a figure is correct.
- Submit with submit_final_result as soon as the figures are verified. Put the lines in exactly the format the question prescribes, with the working underneath.
- Cite only documents you opened and retrieved from. Write plain text with no citation markup.

Task facts (Airbnb, CIK 1559720; verified in the opened 10-Ks):
- "Key Business Metrics" table in Item 7 MD&A, in millions: Nights and Experiences Booked and Gross Booking Value (GBV).
- The FY2024 10-K (https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm) covers 2023 and 2024.
  - Nights and Experiences Booked: 448 (2023), 492 (2024).
  - GBV: $73,252 (2023), $81,784 (2024).
- The FY2023 10-K (https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm) covers 2022 and 2023.
  - Nights and Experiences Booked: 394 (2022), 448 (2023).
  - GBV: $63,212 (2022), $73,252 (2023).
  - Its MD&A narrative gives 393.7M (2022) and 448.2M (2023).
- The FY2022 10-K shows 2021 and 2022 only, so it is not needed for FY2022-2024.
- The FY2024 10-K narrative says only that nights rose 43.3M year over year. It does not state a precise 2024 total.
- Printed-table ratios: 63,212/394 = $160.44, 73,252/448 = $163.51, 81,784/492 = $166.23. The narrative-precision alternates are about $160.56 and $163.44. Both bases differ by cents, so state which basis the headline uses.
</file>

<notes>
kept -> inv1 tool_guidance.md (table-as-printed headline basis, no derived inputs, fewest filings, no null queries) -> base1 opened all 3 10-Ks, headlined 160.56/163.44/166.40 using an unprinted derived 2024 input (448.2+43.3), and issued a null-query search; inv1 finished in 3 turns with printed-table figures 160.44/163.51/166.23 and the precise-nights version as a labelled alternate.
dropped -> dom1 skill kpi_ratio_from_reported_metrics plus its systemprompt trigger line -> dom1 reached the identical numbers as inv1 but took 5 turns (load_skill and an extra edgar_search) with no extra benefit; the procedure is short and fits always-on tool guidance, matching earlier library lessons that skills add no observed effect for short procedures.
kept -> task-fact block (Airbnb 10-K URLs and table values) inside inv1 tool_guidance -> both candidates retrieved identical table values from the opened filings, so the leads are verified and saved discovery turns; the generic rules above them carry the transferable part.
</notes>