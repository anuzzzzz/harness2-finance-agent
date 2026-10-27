# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K or 6-K), and fiscal period or month. Search with those filters, not the question's wording. If web_search returns 0 results, retry once with a short non-empty query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open each primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm each figure's period, unit and basis in the retrieved text before it enters a calculation. A figure that appears only in a snippet must be labelled as such, and an assumption that is inferred (for example an FX rate) must be confirmed in an opened document or called an inference.
- parse_html_page cannot read PDFs. Use the HTML 6-K, 8-K EX-99.1, 10-Q or 10-K.
- If the question states an "as of" date earlier than the system date, use only information published by the question's date. Search results dated later (for example the actual quarter-end results) are not inputs. Do not cite them.
- Cite only documents you opened and retrieved from. Do not list a filing seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. Carry full precision and round only the final numbers. Submit with submit_final_result once the figures are verified.
