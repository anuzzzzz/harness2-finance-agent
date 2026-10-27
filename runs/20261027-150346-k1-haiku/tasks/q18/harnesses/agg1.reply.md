<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with the company and form filters, not the question's wording. If web_search returns nothing, retry once with a short non-empty query (never an empty or null one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. For a "does the company report X, and how is it defined" question, retrieve the definition verbatim: the section heading, the calculation, what it includes and excludes, the basis (e.g. ARR, currency) and the period it applies to. Do not reconstruct a definition from snippets or general knowledge. Use input_character_ranges on long filings.
- Check the gross and the net variant of a metric separately. Say "not reported" only after searching the opened text with several wordings.
- Respect the as-of date. Filings dated after it (the search index may show them) are not used for the core answer. If mentioned at all, label them as later developments.
- If a metric was dropped or changed, retrieve the filing text or correspondence that says so. SEC comment-letter responses (CORRESP/UPLOAD) often state a commitment. Look for any later letter in the same series that confirms or revises it before saying what the company finally decided. If the filings contradict a stated commitment, say so plainly. Do not infer a change from snippets.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit instead.
- Cite only documents you opened and retrieved from. Do not list a filing, letter, PDF or web page seen only in search results. Do not attribute a statement to a document you did not retrieve it from. Copy source URLs exactly as returned by the tools. If a claim rests only on a snippet, label it as snippet-only or leave it out.
- Before submitting, re-check each quoted figure and definition element against the retrieved text. Then submit with submit_final_result. Write plain text with no citation markup such as <cite> tags.

Leads for this task (Workday retention metrics). They come from search results only, so re-confirm each one in the opened text:
- FY2025 10-K (period ended 2025-01-31, filed 2025-03-11): https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm. The "Gross Revenue Retention Rate" subsection sits in MD&A Results of Operations > Revenues.
- 10-Q for the quarter ended 2024-10-31, filed 2024-12-05: https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm.
- SEC correspondence: Workday's response of 2024-09-04 (https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm). A later letter in the series may exist at https://www.sec.gov/Archives/edgar/data/1327811/000132781124000192/filename1.htm. Open it to see the final position on net retention.
</file>

<notes>
kept -> inv1 tool_guidance (open primary filings, definition verbatim, cite only opened, as-of rule) -> base1 never parsed any document, listed 5 unopened sources including a malformed URL; inv1 and dom1 both parsed the 10-K, 10-Q and CORRESP and cited only those (2/2 candidates fixed it).
revised -> inv1 and dom1 correspondence handling -> both opened only the 9/4/2024 letter, which states a commitment to disclose net retention, contradicting the filings. The base snippet had said net was dropped, probably from the later letter (accession ...24-000192), which neither opened. Added a rule to look for follow-up letters and a lead to that URL, labelled unverified.
kept -> dom1 "check gross and net variants separately, not-reported only after multiple wordings" -> dom1's turn 6 re-query of the 10-Q for net-retention phrasing confirmed absence. Folded into tool_guidance.
dropped -> dom1 skill company_kpi_definition_lookup and its systemprompt trigger -> dom1 took 7 turns against 3 for inv1 with the same factual conclusions. The skill's value was mostly task-specific leads, so always-on guidance covers it at lower cost.
kept -> task-specific leads (shortened) -> both candidates used URLs directly and skipped discovery, saving turns without changing figures. They are labelled as re-confirm-in-text leads.
</notes>