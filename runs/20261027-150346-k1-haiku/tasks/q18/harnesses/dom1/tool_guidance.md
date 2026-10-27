# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with company and date filters. If web_search returns nothing, retry once with a short non-empty query (never an empty or null one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Use input_character_ranges on long filings. Confirm each figure's period, unit and basis in the retrieved text.
- When the question asks for a definition, retrieve the company's own wording from the opened filing and quote or closely paraphrase it. Do not reconstruct a definition from snippets or from general knowledge of the metric.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit.
- Respect the as-of date. Filings dated after it may be mentioned only as labelled later developments, never as the basis of the answer.
- Cite only documents you opened and retrieved from. Do not list a filing, PDF or letter seen only in search results, and do not attribute a claim to a document you did not retrieve it from. Copy URLs exactly as returned.
- Write the final answer in plain text. Never paste citation markup such as <cite> tags. Submit with submit_final_result once the claims are verified in primary text.
