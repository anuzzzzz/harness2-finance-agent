<file path="tool_guidance.md">
# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1, proxy) and fiscal period. Use edgar_search with the company CIK and date filters rather than the question's wording. If web_search returns nothing, retry once with a short non-empty query. Never send an empty or null query. Then use edgar_search or a known primary URL.
- A search snippet, result title or third-party reproduction of a filing (stocklight, statista, stockdividendscreener and similar) is a lead, not evidence, even when it looks like an exact quote. Open the primary filing with parse_html_page (one clear key per document). Then ask retrieve_information one targeted question at a time, using input_character_ranges on long filings. Confirm the figure, period, unit and basis in the retrieved text.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit.
- Before submitting, re-check each figure against the retrieved text (period, unit, rounding). Check that parts sum to the total. Carry full precision and round only the final number. If the filing rounds its figures (for example to the nearest thousand), say the result is approximate.
- Cite only documents you opened and retrieved from. Do not list a filing, spreadsheet, article or PDF seen only in search results. If a figure came only from a snippet, say so plainly.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State each input with its period, unit and source, then the calculation, then the answer in the form the question asks for. Call submit_final_result as soon as the figures are verified.
- Headcount questions: the count is in the 10-K, Item 1 "Human Capital" (employees at fiscal year-end, with a U.S./international split). Match the wording ("full-time") and the date the question names. Say if "internationally" is being treated as outside the U.S. Compute share = part / total from the filing's own components.

Lead for this task (Microsoft, FY ended June 30, 2024; snippet-derived, so re-confirm in the opened text): 10-K at https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm (CIK 0000789019). It was reported to say about 228,000 full-time employees, 126,000 in the U.S. and 102,000 internationally.
</file>

<notes>
kept -> inv1 and dom1 (merged tool_guidance.md) -> base1 answered from a Stocklight/data-site snippet, never opened the 10-K, leaked <cite> markup, sent a null-query search and listed unopened sources. Both candidates parsed the 10-K in turn 1, retrieved the exact sentence (228,000 / 126,000 / 102,000) and submitted in 4 turns, so opening the primary filing worked in 2/2 candidate runs. Both submitted, and neither is unsafe.
revised -> merged the two overlapping rule sets into one short file, adding dom1's "third-party reproductions are not sources" line and inv1's sum-to-total check. This resolves the overlap rather than concatenating.
kept -> dom1 headcount line (Item 1 Human Capital, treat "internationally" as non-U.S. and say so, rounding makes the share approximate) -> dom1's answer shows this wording; it is short and applies to this question type.
kept -> task lead (10-K URL and snippet figures, labelled to re-confirm) -> both candidates went straight to parse_html_page and the retrieved text matched the lead. It saves turns and changed no figure, so it has little transfer value.
dropped -> no skill added in either candidate -> the procedure is short, and both skill-free runs finished in 4 turns.
</notes>