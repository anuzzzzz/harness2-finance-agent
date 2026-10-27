# Tool guidance

Before searching, decide which documents and periods the question needs: company, form type (10-K, 10-Q, 8-K Exhibit 99.1 press release) and fiscal period. Search with those filters, not with the question's wording.

- `edgar_search`: pass ticker or CIK, date range and form type. If it returns 0 results, change the filters once, then fall back to `web_search`.
- `web_search`: use it to find primary documents. A snippet, an aggregator page or a blog is a lead, not evidence.
- `parse_html_page`: store each primary document under a clear key (for example `co_q1_24_pr`). Open all the documents you need in parallel in one turn.
- `retrieve_information`: ask one targeted question at a time. On long filings, use `input_character_ranges`. Ask for the exact figure with its period, unit and label, and for the sentence or table row quoted verbatim.

Enough evidence means every figure used in the calculation was read from the text of a primary document that was actually opened with `parse_html_page` and `retrieve_information`, with period, unit and basis matching the question. A figure seen only in a search result is not verified. Do not write that a figure was "checked against" or "read from" a filing unless a retrieve call on that filing returned it. If a document cannot be opened, say so and name the secondary source.

Forward-guidance questions (for example the range of a company's revenue outlook for a future quarter):
- The outlook for quarter N is stated in the earnings release for quarter N-1 (the "Current Outlook" or "Business Outlook" section). Open one release per guided quarter, and match each figure to the quarter it guides, not the quarter reported.
- Record the midpoint and the stated band for each quarter ("approximately $X, plus or minus $Y"). Low = midpoint - band, high = midpoint + band. Range % of midpoint = (high - low) / midpoint, unrounded until the end.

Output format: when the question prescribes an answer template or a rounding precision (for example "[X.X]%" or "$[X.X] billion"), follow it exactly, including line breaks and labels. It overrides the default two-decimal rule. State the unrounded value in the reasoning above the answer, then give the formatted lines, one per requested period, in the order asked. Write plain text with no citation markup or tags, and no commentary about earlier recollections or drafts.

Before `submit_final_result`, re-check each figure against the retrieved text: period, units, rounding as reported, and that the final layout matches the question's template. Say which document each figure came from. Submit while budget remains.
