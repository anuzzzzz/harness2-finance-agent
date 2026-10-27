# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with company and date filters (form type, file-date window) rather than the question's wording. If web_search returns nothing, retry once with a short non-empty query. Never send an empty or null query.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question per figure. Confirm period, unit and basis in the retrieved text. Use input_character_ranges on long filings.
- parse_html_page cannot read PDFs (annual-report ARS PDFs, for example). Use the HTML 10-K or 8-K exhibit.
- Enough evidence means every figure in the answer was retrieved from an opened document. Submit as soon as that holds. Re-do each calculation once and check that wording ("sharp", "plateau") matches the computed numbers.
- Cite only documents you opened and retrieved from. Do not list a filing seen only in search results, and do not attribute a figure to a document you did not retrieve it from. If a figure came from a snippet only, say so plainly.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags.
