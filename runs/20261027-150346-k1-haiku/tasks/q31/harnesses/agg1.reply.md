<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1 earnings release) and fiscal period. Use edgar_search with company and date filters, not the question's wording. If web_search returns nothing, retry once with a short non-empty query. Never send an empty or null query. Then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document). Then ask retrieve_information one targeted question at a time. Confirm each figure's period, unit and GAAP/non-GAAP basis in the retrieved text. Use input_character_ranges on long filings.
- parse_html_page cannot read PDFs, and some commercial sites return HTTP 403. On a failed fetch, do not retry the same URL. Switch once to the SEC HTML filing or exhibit for the same document.
- When a metric the question names (for example gross profit or gross margin) is not a reported line, derive it from reported lines (for example revenue minus cost of sales). Say it is derived and give the formula. Check whether the company reports a similarly named segment measure (for example a shop-level margin on a different basis). Say which one you used and why, and label the other as an alternate.
- For what-if or projection questions, retrieve the base-year inputs from source text. Apply the stated growth and margin change exactly as worded: 500 bps is 5.00 percentage points, and 2024 to 2026 is two compounding periods. Carry full precision and round only the final number to the unit the question asks. Cross-check by a second route (for example base profit grown at the old margin, less the margin change times projected revenue).
- Cite only documents you opened and retrieved from. A URL that failed to load, or that you saw only in search results, is not a source. Write the final answer in plain text with no citation markup. State each figure with its period, unit and source, then the calculation, then the conclusion. Submit with submit_final_result as soon as the figures are verified.
</file>

<notes>
kept -> inv1 tool_guidance (general rules) -> base1 listed a Business Wire URL as a source after it returned HTTP 403 and was never opened, and issued a null-query search (1/1 base rollouts); inv1 opened only the SEC exhibit, listed only that, and submitted in 2 turns
revised -> inv1 task-fact lead block (Dutch Bros URL and figures) -> dropped; library entries show task-specific leads save turns without transfer value, and the rules already cover the derived-gross-profit and alternate-margin handling
dropped -> dom1 skill scenario_projection_margin and the systemprompt trigger line -> dom1 loaded it and used 5 turns versus inv1's 2 with the same $467M answer; its procedure is already in the tool_guidance projection and derived-metric bullets, so the extra on-demand file and always-on trigger buy nothing
kept -> dom1 cite-only-opened and no-markup rules -> already merged into the tool_guidance above; dom1's sources list was clean, matching inv1
kept -> basis labelling (consolidated 26.55% vs shop 22.3%) -> folded into the derived-metric bullet as a general rule; all three runs reached $466.57M, rounded to $467M, so no accuracy difference. Both candidate rollouts submitted; none produced nothing.
</notes>