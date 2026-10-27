I'm adding one always-on tool-guidance file. The base run answered from search snippets without opening any document, so the file makes it open the primary filings and re-check each figure before submitting.

<file path="tool_guidance.md">
# Tool guidance

Before searching, decide which documents and periods the question needs: company, form type (10-K, 10-Q, 8-K Exhibit 99.1 press release) and fiscal period. Search with those filters, not with the question's wording.

- `edgar_search`: pass ticker or CIK, date range and form type. If it returns 0 results, change the filters once, then fall back to `web_search`.
- `web_search`: use it to find primary documents. A snippet, an aggregator page or a blog is a lead, not evidence.
- `parse_html_page`: store each primary document under a clear key (for example `mu_q2fy24_pr`, `mu_q3fy24_pr`).
- `retrieve_information`: ask one targeted question at a time. On long filings, use `input_character_ranges`. Ask for the exact figure with its period, unit and GAAP/non-GAAP label, and for the sentence or table row quoted verbatim.

Enough evidence means every figure that enters the calculation was read from the text of a primary document that was actually opened with `parse_html_page` and `retrieve_information`. Its period, unit and basis (GAAP vs non-GAAP) must match the question. A figure seen only in a search result is not verified. Open its source in the same turn as the search, and open the documents you need in parallel rather than one per turn. If a document cannot be opened, say so in the answer and name the secondary source.

Guidance-versus-actual questions need two documents:
- The guidance comes from the Business Outlook table in the earnings release for the PRIOR quarter (the release that guides the quarter in question).
- The actual comes from the earnings release for the quarter itself. Prefer the figure the company itself reports, to the precision it reports.
- Use the same basis for both (GAAP with GAAP). The guidance usually gives a midpoint plus or minus a range. Compute the difference against the midpoint, and also say where the actual fell relative to the range. Convert percentage-point differences to basis points (1 pt = 100 bps) at full precision, and round only the final number.
- Task fact (from search results in this task, not yet read from the documents): Micron's fiscal Q3 2024 ended May 30, 2024. The guidance sits in the fiscal Q2 2024 release (`.../000072312524000004/a2024q2ex991-pressrelease.htm`). The actuals sit in the fiscal Q3 2024 release (`.../000072312524000016/a2024q3ex991-pressrelease.htm`) and the 10-Q (`.../000072312524000019/mu-20240530.htm`). Confirm the GAAP gross margin guidance and the reported GAAP gross margin from those texts.

Before `submit_final_result`, re-check each figure against the retrieved text: period, segment, units, GAAP vs non-GAAP, and rounding as reported. In the answer, say which document each figure came from. If the sources report a rounded figure and you computed a more precise one, show both and label them. Submit while budget remains.
</file>

<notes>
Motivating moment: in base1 the agent ran two web searches and then submitted in the same turn, never calling parse_html_page or retrieve_information. The guidance (25.5% ± 1.5%) and the actual (gross margin 1,832 on revenue 6,811, from the 10-Q) came from search snippets. The run also computed 26.8977% from rounded-table dollars rather than the company's reported percentage. The edit does four things:
- It defines "enough evidence" as an opened primary document.
- It gives a generic procedure for guidance-versus-actual questions: guidance from the prior-quarter release, actuals from the current release, same GAAP/non-GAAP basis, difference against the midpoint plus position in the range.
- It adds a labelled task fact with the document URLs seen in the search results, flagged as unverified against document text.
- It adds a pre-submit re-check.
The evidence does not establish the company-reported GAAP margin figure, so I did not state it.
</notes>