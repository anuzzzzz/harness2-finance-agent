# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K, DEF 14A) and the year the question names. Use edgar_search with company, form_types and date filters. If web_search returns 0 results or errors, retry once with a short non-empty query, then use edgar_search.
- A search snippet, result title or press-release summary is a lead, not evidence. Open the primary document with parse_html_page (clear key per document), then ask retrieve_information one targeted question at a time. Confirm name, date, event and period in the retrieved text.
- Match the document's filing year to the year the question names. A later filing that describes an earlier year does not replace that year's own filing. If the best evidence is from a different year, do not substitute it silently: check the year-X filing first, then say plainly how the other-year item relates.
- parse_html_page cannot read PDFs; use the HTML version from edgar_search.
- Cite only documents you opened and retrieved from. Do not attribute a fact to a filing unless you retrieved it from that filing; say plainly when a fact comes from an unopened lead.
- Write the final answer in plain text with no citation markup, answer first, then supporting facts with dates and sources. Submit with submit_final_result as soon as the facts are verified.
