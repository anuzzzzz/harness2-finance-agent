# Tool guidance

Before searching, decide which documents and periods the question needs: company, form type (10-K, 10-Q, 8-K Exhibit 99.1 press release) and fiscal period. Search with those filters, not with the question's wording.

- `edgar_search`: pass ticker or CIK, date range and form type. If it returns 0 results, change the filters once, then fall back to `web_search`.
- `web_search`: use it to find primary documents. A snippet, an aggregator page or a blog is a lead, not evidence.
- `parse_html_page`: store each primary document under a clear key (for example `amd_q1_24_pr`). Open all the documents you need in parallel in one turn.
- `retrieve_information`: ask one targeted question at a time. On long filings, use `input_character_ranges`. Ask for the exact figure with its period, unit and label, and for the sentence or table row quoted verbatim.

Enough evidence means every figure used in the calculation was read from the text of a primary document actually opened with `parse_html_page` and `retrieve_information`, with period, unit and basis matching the question. A figure seen only in a search result is not verified. If a document cannot be opened, say so and name the secondary source.

Forward-guidance questions (for example the range of a company's revenue outlook for a future quarter):
- The outlook for quarter N is stated in the earnings release for quarter N-1 (the "Current Outlook" or "Business Outlook" section). Open one release per guided quarter, and match each figure to the quarter it guides, not the quarter reported.
- Record the midpoint and the stated band for each quarter ("approximately $X, plus or minus $Y"). Low = midpoint - band, high = midpoint + band. Range % = (high - low) / midpoint, unrounded until the end.
- In this task, the four outlooks are in AMD's 8-K Exhibit 99.1 releases: Q2 2024 outlook in the Q1 2024 release (sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm), Q3 2024 in the Q2 2024 release (.../000000248824000121/q22024991.htm), Q4 2024 in the Q3 2024 release (.../000000248824000161/q32024991.htm), Q1 2025 in the Q4 2024 release (.../000000248825000009/q42024991.htm). The search snippets showed midpoints of $5.7B, $6.7B, $7.5B and $7.1B, each plus or minus $300 million, but these were not read from the opened documents; confirm them by opening the releases.

Output format: when the question prescribes an answer template or a rounding precision (for example "[X.X]%" or "$[X.X] billion"), follow it exactly. It overrides the default two-decimal rule. State the unrounded value in the reasoning above the answer, then give the final line in the requested precision. Put one period per line when asked. Write plain text, with no citation markup or tags, and no commentary about earlier recollections or drafts.

Before `submit_final_result`, re-check each figure against the retrieved text: period, units, rounding as reported, and that the final layout matches the question's template. Say which document each figure came from. Submit while budget remains.
