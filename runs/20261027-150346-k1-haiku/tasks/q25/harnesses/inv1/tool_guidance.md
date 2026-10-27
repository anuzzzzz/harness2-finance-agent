# Tool use

- Decide the document and period before searching: company, form (10-K), fiscal year. Use edgar_search with company, form type and date filters. Note that a fiscal year may not match the calendar year, so check the period-ending date in the result.
- A search snippet is a lead, not evidence. Open the primary filing with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. parse_html_page cannot read PDFs.
- Summarizing a section of a filing (for example Item 1A risk factors):
  - First retrieve the exact list of risk-factor headings and the section subheadings, in order. Treat that list as the map of what the filing says.
  - Then retrieve the substance of each heading that bears on the question, one or two headings per call. Use input_character_ranges on a long filing. Retrieve outputs can be truncated, so re-ask in smaller pieces rather than relying on a cut-off answer.
  - Cover regulatory points that sit under non-regulatory headings (cybersecurity, financial matters, operations, general risks), but label them as such and separate them from the filing's own regulatory subheading.
  - State "the filing does not mention X" only if a targeted retrieval over the risk-factor text came back empty. Otherwise say the point was not found in the retrieved passages. Never present a negative from a single summary retrieval as established fact.
- Before submitting, reread the draft against the retrieved text. Every item must trace to a retrieved passage. Cut anything that does not.
- Cite only documents you opened and retrieved from. Write plain text with no citation markup. Submit with submit_final_result as soon as the summary is verified.

Task fact (in this task, from one earlier run; re-confirm in the text): Paylocity's FY2024 10-K covers the fiscal year ended June 30, 2024 and was filed 2024-08-02: https://www.sec.gov/Archives/edgar/data/1591698/000159169824000151/pcty-20240630.htm. Its Item 1A has a "Legal and Regulatory Matters" group with three headings:
  1. changes in regulatory laws or requirements applicable to its software and services (this includes money transmitter and AI sub-risks);
  2. failure to comply with data privacy laws and regulations (HIPAA, GDPR, CCPA);
  3. adverse tax laws or regulations.
Further regulatory-flavored points sit elsewhere, in the cybersecurity, financial matters, operations and general risk groups.
