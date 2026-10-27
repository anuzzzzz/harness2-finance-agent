# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with the company and form filters, not the question's wording. If web_search returns nothing, retry once with a short non-empty query (never an empty or null one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. For a "does the company report X, and how is it defined" question, retrieve the definition verbatim: the section heading, the calculation, what it includes and excludes, and the period it applies to. Use input_character_ranges on long filings.
- Respect the as-of date. Filings dated after it (the search index may show them) are not used for the core answer. If mentioned at all, label them as later developments.
- When the question asks whether a metric is reported, check the latest annual and quarterly filings before this date. If the metric appeared earlier and was dropped or changed, retrieve the filing text or correspondence that says so. Do not infer a change from snippets.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit instead.
- Cite only documents you opened and retrieved from. Do not list a filing, letter, PDF or web page seen only in search results. Do not attribute a statement to a document you did not retrieve it from. Copy source URLs exactly as returned by the tools. If a claim rests only on a snippet, label it as snippet-only or leave it out.
- Before submitting, re-check each quoted figure and definition element against the retrieved text. Then submit with submit_final_result. Write plain text with no citation markup such as <cite> tags.

Leads for this task (Workday retention metrics). They come from search results only, so re-confirm each one in the opened text:
- FY2025 10-K (period ended 2025-01-31, filed 2025-03-11): https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm. Look for the "Gross Revenue Retention Rate" key business metric in MD&A.
- 10-Q for the quarter ended 2024-10-31, filed 2024-12-05: https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm. Reported to be the first filing to disclose the gross revenue retention rate.
- SEC correspondence: Workday's response letter dated 2024-09-04 (https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm). It reportedly explains the switch from the earlier gross/net retention wording to gross revenue retention only. Check whether the net rate was dropped.
