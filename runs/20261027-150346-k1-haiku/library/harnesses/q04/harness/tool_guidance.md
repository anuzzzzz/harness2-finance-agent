# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1 earnings release), fiscal period. Prefer edgar_search with company and date filters over question-worded web_search. If web_search returns 0 results, retry once with a shorter query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open each primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question per document. Confirm the figure, period, unit and wording in the retrieved text before it enters a calculation. If a document cannot be fetched, say so and name where the figure came from.
- parse_html_page cannot read PDFs. Use the HTML 8-K EX-99.1 or the 10-K/10-Q.
- Use input_character_ranges on long filings rather than re-reading everything.
- Cite only documents you opened and retrieved from. Do not list a press-release page you only saw in search results.
- Write the final answer in plain text with no citation markup such as <cite> tags. When the question gives an output format, follow it exactly, one line per period; put working after the formatted lines.
- Once every input is verified in primary text, submit with submit_final_result immediately.
