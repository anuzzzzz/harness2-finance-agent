<file path="tool_guidance.md">
# Tool use

- Before searching, fix the company, form type (10-K / 10-Q / 8-K Exhibit 99.1), and fiscal period. Use the latest filing already published as of the question date. Search with those terms plus the exact line item, not with the question's wording. Always pass a non-empty `query`; a null query returned unrelated results.
- `edgar_search` and `parse_html_page` on sec.gov often return HTTP 403 here. `edgar_search` failed twice in the one Airbnb run. Do not retry a 403 and do not call `edgar_search` again after one failure. Make one or two targeted `web_search` calls (company, form, year, table name). The results often give the sec.gov URL and the table text. You may try `parse_html_page` once on a non-sec.gov copy of the filing, such as the company's IR or q4cdn PDF. If it succeeds, ask `retrieve_information` one targeted question at a time.
- Check the line item before using it. "Adjustment" in a non-GAAP reconciliation (Adjusted EBITDA, adjusted net income, free cash flow) means the add-back line in that reconciliation table. It can differ from the cash-flow-statement line of the same name, so name the table the figure came from.
- Enough evidence is the figure, with its period, units (thousands vs millions) and table, read from filing text or a search excerpt that quotes the table. Do not give a figure you have not seen in some tool output, and do not cite a document you did not see.
- Say in the answer whether the figure came from an opened filing or from a search excerpt. Do not write "verified" for a figure seen only in an excerpt. Cite only URLs that appeared in tool results.
- Do the arithmetic on unrounded numbers, re-check it once, and round only the final result.
- Write the answer as plain text with no raw citation tags. Once the figure is in hand, call `submit_final_result` right away.
</file>

<notes>
Motivation (base1): the run hit edgar_search 403 twice (turns 1-2) and issued a null-query web_search. Its final answer gave detailed figures (net income, Adjusted EBITDA, 1,120 prior year) with no opened-filing evidence in the trace. It also cited a Q3 10-Q URL that never appeared in a tool result. The edits add one bounded 403 fallback with a stop condition, a ban on null queries, a definition of "enough evidence", a rule to cite only seen URLs and to disclose the excerpt basis, and a note that "adjustment" means the add-back line in the non-GAAP reconciliation. The last is a procedure point, not a matter fact. The library's q19 and q09 show the same fallback pattern; I copied its core idea. I did not encode Airbnb figures or a memory entry: the 1,407 figure was never confirmed from filing text in the trace, so it is not established fact.
</notes>