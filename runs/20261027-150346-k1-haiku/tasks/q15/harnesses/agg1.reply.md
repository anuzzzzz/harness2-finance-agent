<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. If edgar_search returns other companies (name matching is loose), retry once with the ticker or full legal name and the filing-year date window. Then try web_search with a short non-empty query (never empty or null) and look for an sec.gov URL, then use a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary filing with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm each figure's period, unit and line-item definition in the retrieved text. Use input_character_ranges on long filings. A figure seen only in a snippet may not enter the final calculation until it is confirmed in an opened document.
- Prefer the 10-K (face financial statements) over a press release. One 10-K carries both year-end balance-sheet columns and three years of income-statement lines, so open the latest 10-K before any older filing.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit.
- For a ratio, retrieve numerator and denominator inputs separately, each with period and unit. If the question does not fix the convention (for example, average versus ending balance), compute the standard one as the headline and show the alternate on one labelled line. Carry full precision and round only the final number. Re-check each input against the retrieved text just before submitting.
- If a cost line excludes items shown on a separate line (for example depreciation and amortization), use the reported line as-is and say so in one sentence.
- Cite only documents you opened and retrieved from. Do not list a press release, article or PDF seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State each figure with its period, unit and source, then the calculation, then the conclusion. Submit with submit_final_result as soon as the figures are verified.

Lead for this task (United States Steel Corp., FY2024; from search snippets only, so re-confirm in the opened text): the FY2024 10-K appeared at https://www.sec.gov/Archives/edgar/data/1163302/000116330225000018/x-20241231.htm (CIK 1163302, ticker X). Retrieve the consolidated statements of operations and the balance sheet from it.
</file>

<notes>
kept -> inv1 tool_guidance.md -> base1 submitted from snippets, opened no document, listed two unopened release pages and leaked cite markup; inv1 opened the 10-K in turn 1, retrieved cost of sales 14,060 and inventories 2,168/2,128, cited only the 10-K, no markup, and submitted in 3 turns (0 of 1 candidate runs unsubmitted).
revised -> inv1 task lead -> trimmed to the 10-K URL only; the snippet figures were dropped so the agent must retrieve them from the filing, and the lead carries no transfer value.
revised -> inv1 ratio bullet -> added a one-line rule on cost lines that exclude separate D&A, taken from dom1's skill, since both runs correctly noted the exclusion.
dropped -> dom1 skill ratio_from_10k_statements and its systemprompt trigger line -> dom1 loaded the skill and then needed 5 turns for the same 6.55x/6.49x answer that inv1 reached in 3 turns without a skill; no visible gain, and it adds context cost.
kept -> dom1 sourcing and markup rules -> merged into the same guidance as inv1, which already covers them; overlapping content was not duplicated.
kept -> base systemprompt.md, guardrails.md, LongTermMEMORY.md -> unchanged; no evidence argued for edits. All runs submitted, so no edit is flagged as unsafe.
</notes>