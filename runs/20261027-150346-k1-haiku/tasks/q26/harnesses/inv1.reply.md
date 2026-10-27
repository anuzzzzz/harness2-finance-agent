<file path="tool_guidance.md">
# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with the company CIK and a date window rather than the question's wording. If web_search returns nothing, retry once with a short non-empty query. Never send a null or empty query. Then use edgar_search or a known primary URL.
- A search snippet, result title or third-party reproduction of a filing is a lead, not evidence. Open the primary filing with parse_html_page (one clear key per document). Then ask retrieve_information one targeted question at a time, using input_character_ranges on long filings. Confirm the figure, period, unit and basis in the retrieved text. A count a filing gives in one sentence still has to be read from the opened filing.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit.
- Before submitting, re-check each figure in the calculation against the retrieved text (period, unit, rounding). State if the filing rounds its figures. Carry full precision and round only the final number. Check that the parts sum to the total and that the percentage complements add to 100.
- Cite only documents you opened and retrieved from. Do not list a filing, spreadsheet, article or PDF seen only in search results. If a figure came only from a snippet, say so plainly.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State each figure with its period, unit and source, then the calculation, then the answer in the form the question asks for. Call submit_final_result as soon as the figures are verified.

Lead for this task (Microsoft headcount at June 30, 2024). The FY2024 10-K is at https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm (CIK 0000789019, filed 2024-07-30). The employee count is in Item 1, in the "Human Capital" section. A search snippet of a reproduction of the filing gave "approximately 228,000 people on a full-time basis, 126,000 in the U.S. and 102,000 internationally". The 10-K says "internationally" for the non-U.S. group. Re-confirm these three numbers in the opened 10-K text before using them. The outside-U.S. share is the international count divided by the total.
</file>

<notes>
Motivation: base1 never opened the 10-K. It answered from a search snippet of a third-party reproduction (Stocklight) and a data-site snippet, and it issued a null-query web_search. It listed the unopened 10-K and two other pages as sources and leaked raw <cite index> markup into the final answer. The figures (228,000 / 126,000 / 102,000, giving 44.74%) were plausible but were never confirmed in the primary filing.
Edit: adapted the library's open-primary / cite-only-opened / plain-text / no-empty-query rules in a short tool_guidance.md. Added the verified 10-K URL (from edgar_search results) and the Human Capital location. The headcount numbers are labelled as snippet-derived and to be re-confirmed. Added a sum/complement re-check and a rounding note. No skill added, since the procedure is short and applies to every run.
</notes>