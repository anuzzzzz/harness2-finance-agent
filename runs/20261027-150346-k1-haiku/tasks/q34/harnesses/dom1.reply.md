I'm editing only `tool_guidance.md`: there is one rollout and no divergence, so this is a small change.

<file path="tool_guidance.md">
# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal period. Use edgar_search with company and date filters. If web_search returns 0 results, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information targeted questions. Confirm each figure's period, unit and basis in the retrieved text.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K EX-99.1.
- Share-of-revenue questions (channel partners, a customer type, a segment or region, a product line): the controlling source is the 10-K revenue note ("disaggregation of revenue"), with the MD&A or business section as a cross-check. Retrieve the dollar amount and the total for the same fiscal year, and any percentage the company prints. Compute dollars / total unrounded. Lead with the company-stated percentage if it prints one, and give the computed two-decimal value next to it, labelled as computed. Make sure the total is total revenue and not a subtotal.
- Cite only documents you opened and retrieved from. Do not list a filing, a Financial_Report spreadsheet, an article or a mirror seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text with no citation markup such as <cite> tags. State each figure with its period, unit and source, then the calculation, then the result in the form the question asks for.

Task fact (in this task; re-confirm in the text): Cloudflare FY2024 10-K (period ended 2024-12-31, https://www.sec.gov/Archives/edgar/data/1477333/000147733325000043/cloud-20241231.htm). Channel partner revenue is $337,394K (20% of revenue), against $202,404K (16%) in 2023 and $122,522K (13%) in 2022. Total revenue for 2024 is $1,669,626K, so 337,394 / 1,669,626 = 20.21%. Units are thousands of dollars.
</file>

<notes>
Single base rollout. It reached 20.21% from the 10-K data, but it listed Financial_Report.xlsx and the 10-K as sources, and the trace shows both only in search results. I added a cite-only-opened rule, plain-text output and a no-empty-query rule, copied from the q35 and q45 library entries. I also added a practitioner rule for share-of-revenue questions: use the 10-K revenue note, use the same-year total revenue, and give the company-stated rounded percentage alongside the computed value. The Cloudflare figures are labelled as this task's facts, taken from the base rollout's retrieved text and marked for re-confirmation. No skill was added because this is a single retrieval.
</notes>