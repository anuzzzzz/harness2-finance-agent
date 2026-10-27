<file path="tool_guidance.md">
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
</file>

<notes>
kept -> inv1 -> inv1 opened all four releases in parallel at turn 1 and quoted each outlook sentence at turn 2, versus base1 and dom1, which submitted from snippets with no filing opened (2/2 non-inv1 runs); inv1 cost $0.009 and took 3 turns, so the opened-document rule costs little.
revised -> inv1 -> removed the AMD-specific URLs and snippet-derived midpoints. The library lessons (q44, q45, q30) say task facts in the harness are confounded and not reusable, and the generic guidance-quarter-N-1 recipe already finds the right releases.
kept -> inv1/dom1 output-format rule -> base1 gave 10.53% and similar two-decimal values and left raw cite tags and a "recollection" note, although the question's template is [X.X]%. Both candidates' final answers used one decimal in the template layout; I merged the rule and added "including line breaks and labels".
revised -> dom1 -> dropped its allowance for snippet-quoted evidence. dom1 ran with that allowance, never opened a filing, and its answer claims "checked against the 8-K outlook text", which overstates its verification (the same pattern as agg1 in q44). I added a rule not to claim a read-through unless a retrieve call returned the figure.
kept -> dom1 -> its no-process-chatter rule is merged into the output-format line.
dropped -> skills -> no skill; the guidance fits in a few always-on lines and the library shows skills added a load turn with no gain.
</notes>