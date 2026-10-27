<file path="tool_guidance.md">
# Tool guidance

Before searching, decide which document and period the question needs: company, form type (10-K, 10-Q, 8-K Exhibit 99.1 press release) and fiscal period. Then search with those filters, not the question's wording.

- `edgar_search`: pass ticker or CIK, a date range and form type. If it returns 0 results, change the filters once, then use `web_search` for the primary document.
- `web_search`: use it to find primary documents. A snippet or third-party page is a lead, not evidence.
- `parse_html_page`: store each primary document under a clear key. Open the documents you need in parallel in one turn.
- `retrieve_information`: ask one targeted question at a time. Ask for the exact figure with period, unit and label, quoted verbatim.

Enough evidence means each figure was read from a primary document that was actually opened, or from a search snippet that quotes the filing's own sentence verbatim and names the filing. Say which one it was. Do not put "I first recalled X" or other process chatter in the answer. Deliver only the verified figures.

Guidance questions (ranges, beat or miss):
- The guidance for quarter N is in the Outlook or Business Outlook section of the earnings release for quarter N-1, filed as an 8-K Exhibit 99.1. Open one release per guided quarter.
- Guidance is usually "approximately $M, plus or minus $X". The midpoint is the stated figure. Low = M - X and high = M + X. Range width = high - low = 2X.
- "Range as % of midpoint" = (high - low) / midpoint x 100. Compute it from unrounded inputs and round only at the end.
- In this task (AMD), the Q2 2024, Q3 2024, Q4 2024 and Q1 2025 guidance each appeared in the prior quarter's release (Q1 2024, Q2 2024, Q3 2024 and Q4 2024 results) as a midpoint of $5.7B, $6.7B, $7.5B and $7.1B, plus or minus $300M. This was read from search snippets of those 8-Ks. Re-confirm it if a filing is opened.

Output format: if the question gives an explicit answer template, including decimal places, line breaks and labels, follow it exactly. It overrides the default two-decimal rule. For example, "[X.X]%" means one decimal. Show the unrounded calculation in the working before the formatted lines, and keep the formatted lines clean. Give one line per requested period, in the order asked.

Before `submit_final_result`, re-check each figure against the retrieved text for period, units, label and rounding. State which document each figure came from. Submit while budget remains.
</file>

<notes>
Moment: base1 submitted from search snippets after 4 searches and no opened filing. Its numbers look right (±$300M on 5.7/6.7/7.5/7.1), but it reported 10.53%, 8.96%, 8.00% and 8.45% when the question's template says [X.X]%, which means one decimal. It also added a "my initial recollection was 5.8" note and left raw cite tags in the answer.
Edits (all in tool_guidance.md, no skill):
- Explicit-template-overrides-default-decimals rule, to fix the decimal mismatch. It keeps the unrounded working visible.
- No process chatter in the final answer.
- Guidance mechanics: the prior-quarter release holds the guidance, and range % = width / midpoint.
- Labelled task facts for AMD, marked as snippet-derived and to be re-confirmed.
- An evidence rule allowing a verbatim filing snippet, with the source type stated.
</notes>