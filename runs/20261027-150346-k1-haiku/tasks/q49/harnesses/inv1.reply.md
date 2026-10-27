I made one change: a new `tool_guidance.md`. It follows the q47/q48 pattern but is scoped to company-guidance questions that span several fiscal years. I did not add a skill, because the procedure is short and earlier tasks showed a skill adding nothing here.

<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (8-K EX-99.1 earnings release, 10-Q, 10-K) and fiscal period. Use edgar_search with company and date filters rather than the question's wording. If web_search returns nothing, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP or constant-currency basis in the retrieved text. Use input_character_ranges on long documents. parse_html_page cannot read PDFs; use the HTML 8-K exhibit.
- Respect the as-of date (April 07, 2025). Search results can include filings dated after it (for example results releases from mid-2025). Do not use them. Say plainly that guidance later than the as-of date is excluded.
- Multi-year "did the company beat guidance" questions: for each fiscal year, the guidance is the outlook table or text in each earlier release (the prior-year Q4 release gives the initial outlook; Q1, Q2 and Q3 releases give revisions), and the actual is in that year's Q4 or full-year release. Open the Q4 release of each year (it holds the actual and the next year's initial outlook) and the Q3 release (the last guidance before the result). Retrieve the low and high ends and the basis (constant currency vs reported, percent vs dollars). Judge each year against both the initial and the final guidance, and state the count under each reading so the answer does not depend on a hidden choice. If the ambiguity matters (annual vs quarterly beats), say which reading the headline uses and give the other briefly.
- When guidance is given as a percent change, convert to dollars using the prior-year base from the filing and carry full precision. Note that constant-currency percent and reported dollars can differ.
- For the current-year guidance as of the as-of date, use the latest release dated on or before it, and state what changed from the earlier range.
- Re-check each figure you are about to submit against the retrieved text (period, unit, basis) before calling submit_final_result. A parsed table that looks garbled must be cross-checked against the document's own text.
- Cite only documents you opened and retrieved from. Do not list a filing, article or PDF seen only in search results. If a figure came only from a snippet, say so.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags or loose quote fragments. State each figure with its period, unit and source, then the comparison, then the conclusion in the form the question asks for.

Leads for this task (General Mills, from search results only; re-confirm in the opened text). SEC 8-K EX-99.1 releases:
- Q4 FY2023 release (June 2023; FY2023 actual, FY2024 initial outlook): https://www.sec.gov/Archives/edgar/data/40704/000119312523176744/d41355dex99.htm
- Q3 FY2023 release (March 2023): https://www.sec.gov/Archives/edgar/data/40704/000119312523077267/d816383dex99.htm
- Q2 FY2024 release (Dec 2023): https://www.sec.gov/Archives/edgar/data/40704/000119312523299294/d660865dex99.htm
- Q3 FY2024 release (Mar 2024): https://www.sec.gov/Archives/edgar/data/40704/000119312524072050/d798673dex99.htm
- Q4 FY2024 release (June 2024; FY2024 actual, FY2025 initial outlook): https://www.sec.gov/Archives/edgar/data/40704/000119312524168511/d786387dex99.htm
- Q3 FY2025 release (Mar 19, 2025; FY2025 outlook as of the as-of date): https://www.sec.gov/Archives/edgar/data/40704/000119312525057150/d902176dex99.htm
- The FY2022 Q4 release (June 2022, FY2023 initial outlook) was not found in the searches; find it with edgar_search if the initial FY2023 guidance is needed.
- General Mills states adjusted diluted EPS guidance as a percent change in constant currency from the prior-year base (FY2023 $4.30; FY2024 $4.52 per the earlier run, so verify), not as a dollar range.
</file>

<notes>
Motivation: the base run answered from search snippets without any parse_html_page or retrieve_information call. It left loose quote fragments in the answer. It listed many unopened releases as sources. It compared only the last (Q3) guidance, and the FY2023 initial guidance was never retrieved. It never stated how the count changes under an initial-guidance reading. It also saw mid-2025 filings in search results with no rule on the as-of date. The new tool_guidance applies the same open-the-primary-document, cite-only-opened and plain-text rules adopted for q47/q48, and adds the as-of exclusion and the initial-versus-final guidance reading for multi-year guidance questions. It labels the General Mills release URLs from the base searches as unverified leads. I did not add a skill, since the procedure is short and earlier tasks showed no extra effect from one.
</notes>