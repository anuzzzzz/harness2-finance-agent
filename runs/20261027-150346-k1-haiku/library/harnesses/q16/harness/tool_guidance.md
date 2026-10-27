# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K and exhibits, 424B5 prospectus supplement, FWP, EX-99.1) and date window. Use edgar_search with company and date filters. If web_search returns 0 results, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. For long filings, ask about one topic per call. Confirm each figure's period, unit and share count in the retrieved text.
- If a snippet suggests a material fact the filings do not show (for example an upsized deal or an exercised over-allotment option), open that page (company press release first) with parse_html_page and confirm it. Do not drop the fact and do not assert it unopened. If it cannot be opened, say it is unconfirmed.
- parse_html_page cannot read PDFs. Use the HTML filing.
- Cite only documents you opened and retrieved from. Do not list a press release, article or mirror seen only in search results.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State each term with its figure, unit and source document. Submit with submit_final_result once the terms are verified.
