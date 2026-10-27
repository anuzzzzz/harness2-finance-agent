<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (8-K EX-99.1 earnings release, 10-Q, 10-K) and fiscal period. Use edgar_search with company and date filters rather than the question's wording. If web_search returns nothing, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP or constant-currency basis in the retrieved text. Use input_character_ranges on long documents. parse_html_page cannot read PDFs; use the HTML 8-K exhibit.
- Respect the as-of date (April 07, 2025). Search results can include filings dated after it (for example results releases from mid-2025). Do not use them. Say plainly that guidance later than the as-of date is excluded.
- Multi-year "did the company beat guidance" questions: for each fiscal year, the guidance is the outlook in each earlier release (the prior-year Q4 release gives the initial outlook; Q1, Q2 and Q3 releases give revisions), and the actual is in that year's Q4 or full-year release. Open the Q4 release of each year (it holds the actual and the next year's initial outlook) and the Q3 release (the last guidance before the result). Retrieve the low and high ends and the basis (constant currency vs reported, percent vs dollars). Judge each year against both the initial and the final guidance, and state the count under each reading so the answer does not depend on a hidden choice. Say which reading the headline uses. "At the top end" is not "above". If the question could mean quarterly beats against consensus, say that is a different measure and do not invent a quarterly count unless each quarter was retrieved from opened text.
- When guidance is given as a percent change, convert to dollars using the prior-year base from the filing, label the result as derived, and carry full precision. Constant-currency percent and reported dollars can differ.
- For current-year guidance as of the as-of date, use the latest release dated on or before it, and state what it replaced and the original range.
- Before submitting, re-check each figure against the retrieved text (period, unit, basis). A parsed table that looks garbled must be cross-checked against the document's own text.
- Cite only documents you opened and retrieved from. Do not list a filing, article or PDF seen only in search results. If a figure came only from a snippet, say so.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags or loose quote fragments. State each figure with its period, unit and source, then the comparison, then the conclusion in the form the question asks for.

Leads for this task (General Mills, from search results only; re-confirm in the opened text). SEC 8-K EX-99.1 releases:
- Q4 FY2022 (June 2022; FY2023 initial outlook): https://www.sec.gov/Archives/edgar/data/40704/000119312522184385/d370020dex99.htm
- Q3 FY2023 (March 2023): https://www.sec.gov/Archives/edgar/data/40704/000119312523077267/d816383dex99.htm
- Q4 FY2023 (June 2023; FY2023 actual, FY2024 initial outlook): https://www.sec.gov/Archives/edgar/data/40704/000119312523176744/d41355dex99.htm
- Q3 FY2024 (March 2024): https://www.sec.gov/Archives/edgar/data/40704/000119312524072050/d798673dex99.htm
- Q4 FY2024 (June 2024; FY2024 actual, FY2025 initial outlook): https://www.sec.gov/Archives/edgar/data/40704/000119312524168511/d786387dex99.htm
- Q3 FY2025 (Mar 19, 2025; FY2025 outlook as of the as-of date): https://www.sec.gov/Archives/edgar/data/40704/000119312525057150/d902176dex99.htm
- General Mills states adjusted diluted EPS guidance as a percent change in constant currency from the prior-year base, not as a dollar range.
</file>

<notes>
kept -> inv1 tool_guidance (open-primary-document, cite-only-opened, plain-text, as-of exclusion, initial-vs-final reading) -> base1 made only web_search calls, listed unopened PDFs/articles and leaked citation markup; inv1 (6 turns) and dom1 (9 turns) both parsed the releases, retrieved the same figures, and gave identical 2-of-2 final / 1-of-2 initial counts.
revised -> inv1 leads block -> added the Q4 FY2022 release URL that both candidates found via edgar_search, so the FY2023 initial outlook needs no discovery step; dropped the "not found" line.
kept -> dom1 "at the top end is not above" and "label derived dollar ranges" wording -> dom1's final answer applied them correctly; folded into the tool_guidance multi-year bullet.
dropped -> dom1 skill guidance_beat_count_multi_year and its systemprompt trigger line -> dom1's skill run took 9 turns against inv1's 6 with the same figures, and earlier library entries (q47, q48) showed no extra effect from a skill; the procedure is short enough for always-on text.
dropped -> any quarterly-consensus beat count -> neither candidate retrieved quarterly actuals or consensus; the guidance says to flag it as a different measure and not to invent a count.
</notes>