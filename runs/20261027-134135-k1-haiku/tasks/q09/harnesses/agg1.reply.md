<file path="tool_guidance.md">
# Tool guidance

Before searching, decide which documents and periods the question needs: company, form type (10-K, 10-Q, 8-K Exhibit 99.1 press release) and fiscal period. Search with those filters, not with the question's wording.

- `edgar_search`: pass ticker or CIK, date range and form type. If it returns 0 results, change the filters once, then fall back to `web_search`.
- `web_search`: use it to find primary documents. A snippet, an aggregator page or a blog is a lead, not evidence.
- `parse_html_page`: store each primary document under a clear key (for example `co_q2_pr`, `co_q3_pr`). Open the documents you need in parallel in one turn.
- `retrieve_information`: ask one targeted question at a time. On long filings, use `input_character_ranges`. Ask for the exact figure with its period, unit and GAAP/non-GAAP label, and for the sentence or table row quoted verbatim.

Enough evidence means every figure that enters the calculation was read from the text of a primary document that was actually opened with `parse_html_page` and `retrieve_information`. Its period, unit and basis (GAAP vs non-GAAP) must match the question. A figure seen only in a search result is not verified, so open its source before using it. If a document cannot be opened, say so in the answer and name the secondary source.

Guidance-versus-actual questions (beat or miss, by how much) need two documents:
- The guidance comes from the Business Outlook table in the earnings release for the PRIOR quarter, which is the release that guides the quarter in question.
- The actual comes from the earnings release for the quarter itself. Confirm that the fiscal period end matches the quarter the guidance covers.
- Use the same basis for both (GAAP with GAAP, non-GAAP with non-GAAP). Releases give both bases side by side and they differ. Headline "above the high end" language usually refers to non-GAAP.
- Guidance is usually a midpoint plus or minus a band. Benchmark against the midpoint and say so. Also state where the actual fell relative to the range (above, inside or below) and the distance to the nearest bound.
- Convert percentage-point differences to basis points (1 pt = 100 bps) at full precision. Where the release reports a rounded percentage, show both: the difference using the unrounded actual from the dollar figures (margin $ / revenue $), and the difference using the reported rounded percentage. Label which is which and round only the final number.

Before `submit_final_result`, re-check each figure against the retrieved text: period, segment, units, GAAP vs non-GAAP, and rounding as reported. In the answer, say which document each figure came from. Submit while budget remains.
</file>

<notes>
kept -> inv1 (generic parts of tool_guidance.md) -> base1 submitted in 1 turn from search snippets with no parse/retrieve call (1/1 base); inv1 opened both releases in parallel at turn 1 and quoted the guidance and actual rows in 3 turns, so "opened primary document" plus parallel opening is retained.
dropped -> inv1 task-specific fact block (Micron URLs and the 25.5% guidance) -> task-specific leads would pollute a reusable library harness. They are also unverified against document text, and the agent finds them in one search anyway.
dropped -> dom1 skill `guidance_vs_actual` and its systemprompt trigger line -> dom1 spent turn 1 loading the skill and reached the same answer as inv1, which used tool guidance only. The skill's task-specific leads are not reusable, and always-on prompt text was added for no observed gain. The generic content is folded into one short tool_guidance paragraph instead.
kept -> dom1 content (midpoint benchmark, GAAP/GAAP matching, range-position reporting, showing both unrounded and reported-percentage bps) -> dom1's final answer showed 139.77 bps and 140 bps with range position. inv1 gave only 140 from the rounded 26.9%, so this fills a precision gap. Both rollouts submitted and none produced nothing, so the merge carries no unsubmitted-run risk.
</notes>