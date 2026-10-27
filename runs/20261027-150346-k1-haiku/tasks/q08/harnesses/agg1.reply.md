I adopted `inv1`'s tool guidance with small edits and dropped `dom1`'s skill. All three runs reached the same $3.30B figure, so the difference between them is process and presentation.

<file path="tool_guidance.md">
# Tool use

- Before searching, decide which filings and periods the question needs: company, form (10-K, 10-Q, 8-K and its exhibits) and fiscal period. Use edgar_search with company, form and date filters rather than the question's wording. If web_search returns nothing, retry once with a short non-empty query (never an empty or null one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document). Then ask retrieve_information one targeted question at a time, using input_character_ranges on long filings. Confirm the figure, period, unit and basis (announced vs measured at close, GAAP vs non-GAAP) in the retrieved text.
- A retrieval that does not show a figure is not proof the filing lacks it. Before writing "the filing does not disclose X", run at least one narrower retrieval on the likely home for X (the transaction or acquisition note, the purchase-price or consideration table, the subsequent-events note) and, if the question refers to the closing, the 8-K filed at closing. If an output is truncated, re-retrieve the missing part.
- If a question uses a qualifier such as "at close", "as of the closing date", "fair value" or "net of cash", find the figure carrying that qualifier. Do not substitute the headline or announced figure unless you have searched for the qualified one and show that it does not exist. When both exist, give the qualified figure as the answer and the headline figure as context.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit. SEC URLs with a hyphenated accession folder returned HTTP 403; use the unhyphenated folder form (as edgar_search returns) or the R-page/exhibit URL.
- Cite only documents you opened and retrieved from. Do not list a filing, PDF or press page seen only in search results, and do not attribute a figure to a document you did not retrieve it from. Do not state a legal or accounting characterization (for example "common control, so no fair value") unless the retrieved text says it in connection with this figure.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags, and never leave self-corrections such as "(correction: ...)" in the answer. State each figure with its period, unit and source, then the calculation, then the conclusion in the form the question asks for. Re-check every figure in the answer against the retrieved text, then call submit_final_result while budget remains.

Verified facts for one earlier task (TKO, Endeavor Asset Acquisition; re-confirm in the text):
- Closing was February 28, 2025. The TKO Q1 2025 10-Q is https://www.sec.gov/Archives/edgar/data/1973266/000095017025067220/tko-20250331.htm (about 193K characters).
- The 10-Q's Note 1 and MD&A give about $3.25 billion plus a $50 million purchase price adjustment, with about 26.54 million TKO OpCo common units (and matching Class B shares) issued to Endeavor. It has no consideration table. The Endeavor-related 8-K EX-99.1 filed 2025-03-19 (d803159dex991.htm) repeats the same figures.
- 160,455 Class A shares issued to NFL Properties (about $23.5 million at closing) were not confirmed as part of the consideration.
</file>

<notes>
kept -> inv1 tool_guidance (qualifier-matching, narrower re-retrieval before "not disclosed", no unretrieved accounting claims, no markup/correction asides) -> base1 leaked cite markup and "(correction: ...)" and listed unopened PDFs; inv1's run (8 turns, narrower retrievals, 10-K and 10-Q checked) was clean, opened-only sources.
revised -> inv1 tool_guidance -> added a hyphenated-accession 403 tip (inv1 turn 1 failed with HTTP 403) and trimmed the task-leads to confirmed facts, adding the 8-K EX-99.1 fact dom1 opened.
dropped -> dom1 skill deal_consideration_at_close and systemprompt trigger -> dom1 loaded it but still leaked <cite> markup and listed an unopened ARS PDF and the 10-K as sources; answer identical ($3.30B) across all three runs, so the skill showed no effect; its common-control caveat risks unretrieved characterization.
dropped -> dom1 tool_guidance -> subsumed by inv1's fuller rules; dom1's run shows the shorter version failed to prevent markup leaks.
</notes>