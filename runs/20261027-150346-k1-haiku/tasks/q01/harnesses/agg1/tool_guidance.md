# Tool use

- Decide the documents and the as-of date before searching: company, form (10-K, 10-Q, 8-K and its EX-99 exhibits, DEFA14A, CORRESP), and period. Use edgar_search with the company CIK and date filters, not the question's wording. If web_search returns 0 results, retry once with a short non-empty query (never an empty or null query), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Use input_character_ranges on long filings. Confirm the fact, date and wording in the retrieved text.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit.
- Respect the as-of date (April 07, 2025). Do not use, cite or list a document filed or dated after it, even if search returns it. A snippet that mentions a later event is not usable.
- Cite only documents you opened and retrieved from. Do not list a filing as a source, or attribute a statement to it, unless you retrieved that statement from it. If a fact came from a snippet only, say so or leave it out.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. Give each fact with its date and source. Submit with submit_final_result as soon as the facts are verified.
