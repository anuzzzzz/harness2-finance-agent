<file path="tool_guidance.md">
# Tool use

- Before searching, decide the form, company and fiscal period the question needs (10-Q, 10-K or 8-K EX-99.1). Use edgar_search with company and date filters, not the question's wording. If web_search returns nothing, retry once with a short non-empty query. Never send an empty or null query. After that, use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page under a clear key. Then ask retrieve_information one targeted question at a time. Use input_character_ranges on long filings. Confirm each figure's period, unit and basis in the retrieved text, and quote the table row.
- For a "last N months as of date X" question, the period is the fiscal year-to-date covered by the latest periodic filing filed on or before X. Say which period you used. If the filing gives both three-month and year-to-date columns, use the year-to-date column and report the three-month one only as labelled context.
- Compute any shares or mix percentages from the retrieved dollar figures at full precision. Check that the components sum to the reported total. Round only the final number.
- Cite only documents you opened and retrieved from. Do not list a press release, transcript or article seen only in search results, and do not quote a sentence from one. If a figure came only from a snippet, say so or leave it out.
- Write the final answer in plain text with no citation markup. Give the headline figures first. Then give each figure with its period and unit, the calculation, and the sources. Submit with submit_final_result as soon as the figures are verified. Do not add a caveat that the figures were unchecked; verify them instead.
</file>

<notes>
kept -> inv1 tool_guidance.md (generic rules) -> base1 listed the unopened Q3 press release as a source and quoted its "66%" line from a snippet, and issued a null-query search; inv1 and dom1 (both carrying a cite-only-opened rule) listed only the opened 10-Q and made no null searches. The edit is carried in 2/2 candidate runs and 0/1 base run; the numbers were identical in all runs, so the effect is on sourcing hygiene.
kept -> inv1 period-selection and sum-check lines -> base1 never stated how "last 9 months as of 11/12/2024" was resolved, while inv1 and dom1 both stated the 10-Q YTD period and checked components sum to total; short and generic, so kept always-on.
revised -> inv1 task-fact block (10-Q URL and figures) -> dropped. Task-specific leads showed no transfer value in the q45-q48 library entries, and base1 found the 10-Q in two turns anyway.
dropped -> dom1 skill period_mix_from_filing and its systemprompt trigger -> dom1 took 4 turns against 3 for inv1 (no skill), with the same figures and sourcing, so no visible benefit. The procedure is short enough for always-on guidance, and the skill carried task facts. Both candidates ran once each and neither failed to submit.
dropped -> base1's closing caveat that figures were unchecked against raw text -> replaced by inv1's instruction to verify instead of caveating. dom1's run did the same through its retrieval of the exact table headers.
</notes>