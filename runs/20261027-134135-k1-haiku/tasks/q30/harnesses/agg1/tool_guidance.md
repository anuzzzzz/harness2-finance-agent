# Tool guidance

Before searching, decide which document and period the question needs: company, form type (10-K, 10-Q, 8-K exhibit), fiscal period and as-of date. Then search with those filters, not the question's wording. Use only documents dated on or before the current date (April 07, 2025). Do not cite later filings.

- `edgar_search`: pass the ticker or CIK, a date range, and the form type. If it returns 0 results, change the filters once. If it still returns nothing, use `web_search` for the primary document. Do not repeat an empty `web_search`.
- `parse_html_page`: store each primary document under a clear key (for example `co_10k_2024`). For full-year or year-end questions, open the 10-K.
- `retrieve_information`: ask one targeted question at a time. On long filings, use `input_character_ranges`. Ask for the exact figure with its period, unit and row label, quoted verbatim. Table extraction can garble rows, so check an unclear row in a second table or note instead of inferring it.

Defined-term questions ("maximum", "if-converted", "dilutive impact", "aggregate"): the question's wording usually matches a phrase or table in the filing. Run one retrieve call that searches the filing for the literal term (for example "maximum number of shares", "if-converted", "potentially dilutive"). Quote the sentence or table row. If the filing states the figure, that figure is the headline answer. Computed variants (other conversion rates, make-whole scenarios) are cross-checks and are labelled as such. Lead with one number and state it plainly. If the filing states no explicit maximum, say so and give the figure it does report.

Convertible-note dilution: take the company's reported if-converted share line (usually in the net loss per share note, check the units) and reconcile it to principal outstanding at the date × conversion rate for each series. Never combine one series at a maximum or make-whole rate with the other series at base rates and present the total as the maximum. A maximum-rate total needs the maximum rate for every series. Capped calls offset economic dilution but do not reduce the gross share count. Mention them separately.

Enough evidence means the figure was read from a period-matching table or note in a primary document that was opened. A calculation built from components is used to check the reported total. A figure seen only in a search result is a lead, not evidence.

Before `submit_final_result`, re-check each figure against the retrieved text for period, units, label and rounding. State which document and table each figure came from. Submit while budget remains.
