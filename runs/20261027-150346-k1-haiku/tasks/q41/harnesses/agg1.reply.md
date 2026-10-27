<file path="tool_guidance.md">
# Tool use

- Decide the document and period before searching: company, form (8-K EX-99.1 earnings release, or 10-K/10-Q) and fiscal period. A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and basis in the retrieved text before answering.
- edgar_search `ciks` takes numeric CIKs, not tickers. A ticker returns zero results. If edgar_search returns nothing, fix the input once (numeric CIK, shorter terms, drop the form filter, widen the dates). Then use a known URL or a short non-empty web_search query. Never send an empty or null query.
- Companies often name a metric differently from the question (same-store sales vs "comparable store sales"). Retrieve the company's own term and say in the answer that it is the equivalent measure. Report the sign and direction exactly (a decline is not growth). Give the quarterly figure the question asks for, not the full-year figure. Give the full-year figure only as context.
- Submit with submit_final_result as soon as the figure is confirmed in opened text. Do not spend turns on extra "cross-check" searches or on opening a second large filing when the first already confirms the figure.
- Cite only documents you opened and retrieved from. Do not list pages seen only in search results. Write the answer in plain text, with no citation markup or source-index tags. State the figure with its period, unit and source.

Leads for this task (Floor & Decor Holdings, FY2024, from search results only; re-confirm in the opened text):
- In this task, Floor & Decor's CIK is 1507079. Its fiscal Q4 2024 ended December 26, 2024.
- The company reports "comparable store sales". Search results gave -0.8% for Q4 2024, and total net sales of $1,107.4M, up 5.7%.
- Q4/FY2024 earnings release (8-K EX-99): https://www.sec.gov/Archives/edgar/data/1507079/000150707925000012/fnd-2024earningsreleaseex9.htm
- FY2024 10-K: https://www.sec.gov/Archives/edgar/data/1507079/000150707925000013/fnd-20241226.htm
- Open the release first and read the Q4 comparable-store-sales line. Use the 10-K only if the release fails to parse.
</file>

<notes>
kept -> inv1 (tool_guidance.md) -> base1 answered -0.8% only from snippets, passed ticker "FND" as a cik (zero results), sent a null-query web_search, leaked "source index" markup and listed unopened IR/TradingView pages; inv1 opened the release in turn 1, retrieved the quarter line, and submitted in 3 turns citing only that one opened source.
revised -> inv1 (tool_guidance.md) -> added a clause not to open a second large filing once the figure is confirmed; dom1 parsed the 336k-character 10-K as well, at $0.076 against $0.003 for inv1, with the same figure.
dropped -> dom1 (retail_comparable_sales skill and systemprompt trigger line) -> dom1 reached the same -0.8% in 4 turns against inv1's 3. The skill's extras (definition bullets, 10-K parse) added cost, not accuracy, and 1 rollout shows no benefit. A skill-free rule set also matches the library's prior pattern.
kept -> inv1 (task leads block) -> the leads saved the discovery search and the rollout's retrieved text matched them, but this is labelled confounded with the rules; it is low confidence from a single rollout.
</notes>