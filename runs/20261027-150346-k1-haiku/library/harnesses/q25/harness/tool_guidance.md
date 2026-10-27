# Tool use

- Decide the document and period before searching: company, form (10-K), fiscal year. Use edgar_search with company, form type and date filters. A fiscal year may not match the calendar year, so check the period-ending date in the result.
- A search snippet is a lead, not evidence. Open the primary filing with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. parse_html_page cannot read PDFs.
- retrieve_information output can be truncated on broad prompts. Ask for one or two headings or groups per call rather than relying on a cut-off answer.
- Absence claims: say a filing "does not mention X" only if a targeted retrieval for that exact term came back empty, and even then phrase it as "not found in the retrieved text". A negative from one broad summary retrieval is not established fact; leave it out if unverified.
- Before submitting, check the draft against retrieved text. Every item must trace to a retrieved passage.
- Cite only documents you opened and retrieved from. Write plain text with no citation markup. Submit with submit_final_result as soon as the answer is verified.
