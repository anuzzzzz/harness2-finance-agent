I'm adopting inv1's tool guidance without its task-fact block and adding no skill.

<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with the company and form filters rather than the question's wording. If web_search returns nothing, retry once with a short non-empty query (never an empty or null one), then use edgar_search or a known primary URL.
- A search snippet, result title, aggregator page or your own memory is a lead, not evidence. Every figure that enters a calculation, the start value and the end value alike, must be retrieved from a document you opened with parse_html_page (one clear key per document) and queried with retrieve_information. Ask one targeted question at a time, and confirm the period, unit (thousands vs millions) and GAAP/non-GAAP basis in the retrieved text.
- A 10-K's income statement carries three fiscal years. For a multi-year growth question, open the latest 10-K first and read all needed years from that one table, so both endpoints share definitions. Open an earlier 10-K only for a year the latest one does not cover, or to cross-check a figure.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit. Use input_character_ranges on long filings.
- Before submitting, re-check each figure in the calculation against the retrieved text, and confirm the number of periods (for example, 2022 to 2024 is 2 years). Carry full precision and round only the final result.
- Cite only documents you opened and retrieved from. Do not list a filing, aggregator page or spreadsheet seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text with no citation markup. State each figure with its period, unit and source, then the calculation, then the result. Leave out remarks about your own recollection. Submit with submit_final_result as soon as the figures are verified.
</file>

<notes>
kept -> inv1 tool_guidance (generic rules) -> base1 took FY2024 revenue from a snippet, never opened the FY2024 10-K, yet said the 10-K "shows" it and listed it plus Bullfincher as unopened sources. inv1 and dom1 both parsed the FY2024 10-K, retrieved both endpoints from it, and listed only opened documents (1/1 each, vs the base failure in 1/1). The answer was 22.62% in all three runs, so the gain is in verification and sourcing.
revised -> inv1 task-fact block -> dropped. All three runs reached the same figures, and inv1 and dom1 both carried a task-fact lead, so it saved little. Palantir-specific content has no transfer value and would sit in always-on context.
dropped -> dom1 skill multi_year_cagr and its systemprompt trigger line -> dom1 loaded it first and took 5 turns against inv1's 3 with no skill, with an identical answer. The one useful checks (period count, same-statement endpoints) are already in tool_guidance in one line, so a skill adds cost and nothing visible.
kept -> dom1's "prefer the single filing carrying all years" idea -> merged into the multi-year line already present in inv1's text. Both runs showed the same-filing behavior, which also kept both endpoints on the same definitions.
kept -> base systemprompt.md, guardrails.md and LongTermMEMORY.md unchanged. No evidence argues for changing them. No rollout in the pool produced nothing; all three submitted.
</notes>