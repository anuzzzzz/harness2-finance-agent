# Tool use

- Decide the filings and fiscal periods before searching: company, form type, years. Use edgar_search with the company CIK, form_types and date filters, not the question's wording. If web_search returns 0 results, retry once with a shorter query, then use edgar_search.
- A 10-K cash-flow statement and income statement show three years. The latest 10-K and the one two years earlier together cover a three-year span, so open only the filings you need. Store each under a clear key.
- Ask retrieve_information one targeted question per filing, with exact line items, periods and units. Confirm that each figure matches the same line in every filing that shows it. If two filings disagree (restated or recast figures), say so and use the later filing.
- When a metric is "approximated" from line items (for example FCF = CFO - Capex), name the exact statement lines used. If the filing has more than one plausible capex line (PP&E purchases, capitalized software or intangibles), pick the one the company's own MD&A uses for capital expenditures. Show the narrower or broader alternative as a labelled cross-check, in one line, with its result. Do not present two answers as equal.
- For a multi-year trend, compute the metric and its margin for every year with unrounded inputs, and round only the final figures. State the direction year to year and the endpoint-to-endpoint direction. Flag any year distorted by a one-off item (for example discontinued-operations cash flows) and say which way the trend reads with and without it.
- Cite only documents you opened and retrieved from. Do not list a filing as a source if you never parsed it. If a figure for one year came from a different filing, say which.
- Before submitting, re-check each figure against the retrieved text: period, unit, sign, and that the arithmetic recomputes. Submit with submit_final_result as soon as this is done. Write the answer in plain text with no citation markup.

In this task (Zillow Group, CIK 1617640), verified in retrieved 10-K text, $ millions:
- FY2024 10-K (https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm) shows 2024, 2023 and 2022 on its cash-flow statement.
- CFO: 2022 = 4,504, 2023 = 354, 2024 = 428.
- Purchases of property and equipment: 115, 135, 143. Purchases of intangible assets (capitalized internal-use software sits here): 25, 30, 28.
- MD&A gives 2024 capex of 171 (PP&E + intangibles).
- Revenue: 1,958 (2022), 1,945 (2023), 2,236 (2024).
- FY2022 CFO is inflated by the Zillow Offers wind-down (about a $3.9B inventory decrease). The cash-flow statement does not separate discontinued operations.
- The FY2023 10-K is https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm. In the earlier run the FY2022 10-K was never opened, so it should not be cited unless it is.
