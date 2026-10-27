<file path="tool_guidance.md">
# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal period. Use edgar_search with company and date filters, not the question's wording. If web_search returns 0 results, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm each figure's period, unit and basis in the retrieved text. On a long 10-K use input_character_ranges rather than re-reading everything.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K EX-99.1. An XBRL Financial_Report.xlsx seen in search results is not a parsed source.
- Share-of-revenue or mix questions (channel partners, customer type, segment, region, product line): the controlling source is the 10-K revenue note ("disaggregation of revenue"). Retrieve the dollar amount, the same-year total revenue (not a subtotal), and any percentage the company prints. Give the company-stated percentage as the headline answer, then the unrounded recomputation (amount / total, two decimals) as a labelled cross-check, so a reviewer sees both.
- Cite only documents you actually parsed and retrieved from. Do not list a filing, spreadsheet, article or mirror seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text with no citation markup (no <cite> tags). State each figure with period, unit and source, then the calculation. Submit with submit_final_result as soon as the figures are verified in the opened text.
</file>

<notes>
kept -> inv1 (tool_guidance: snippet-is-lead, open primary doc, cite-only-opened, no empty query, plain text) -> base1 never called parse_html_page/retrieve_information yet listed the 10-K and Financial_Report.xlsx as sources; inv1 and dom1 both parsed the 10-K, retrieved the Note 3 table and cited only it (2/2 vs base 0/1).
kept -> inv1 (stated percentage as headline, recomputation as cross-check) -> the 10-K prints 20% while the dollar recompute is 20.21%; inv1 led with the stated 20% and showed 20.21% as a check, while base1 and dom1 headlined 20.21%. The stated figure is the safer primary since both are shown.
merged -> dom1 (revenue-note as controlling source, same-year total not subtotal) -> folded into the single share-of-revenue bullet; dom1's headline-computed-first ordering dropped in favour of inv1's stated-first ordering.
dropped -> inv1 and dom1 task-fact blocks (Cloudflare URL and figures) -> task-specific leads have no transfer value in the library, and both runs retrieved the figures from the opened text anyway.
dropped -> any skill -> single retrieval from one document; all runs completed in 3-4 turns without one. All rollouts submitted, so there is no unsafe edit.
</notes>