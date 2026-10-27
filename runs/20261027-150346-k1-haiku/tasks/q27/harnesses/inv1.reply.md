I've added a `tool_guidance.md` for this task and left the other files alone. The evidence is a single rollout (base1), so the confidence is low.

<file path="tool_guidance.md">
# Tool use

- Decide the document and period before searching: company, form (10-K), fiscal year, and the section that governs the question (for debt terms, the debt / capital structure note and the MD&A capital-resources discussion). Use edgar_search with the company CIK and date filters, not the question's wording. Never issue a web_search with an empty or null query. If web_search returns nothing, retry once with a short non-empty query, then use edgar_search or a known URL.
- A search snippet or result title is a lead, not evidence. Open the primary filing with parse_html_page (one clear key), then ask retrieve_information one targeted question at a time. Use input_character_ranges on long filings. Confirm each term (amount, rate, maturity, call/redemption, deferral, ranking, covenants), its period, and its units in the retrieved text. parse_html_page cannot read PDFs. Use the HTML filing.
- "Terms of" questions: retrieve every term the filing states for the instrument, and keep it separate from similarly named instruments (here, the Subordinated Debentures are different from the Junior Subordinated Debentures). If the filing is silent on a term, say so rather than inferring it.
- Re-check each figure against the retrieved text before submitting. Submit with submit_final_result while budget remains.
- Cite only documents you opened and retrieved from. Do not list pages seen only in search results (press releases, annual-report PDFs, rating-agency notes), and do not attribute a statement to a filing you did not retrieve it from. Write the answer in plain text with no citation markup such as <cite> tags.

Leads for this task (Allstate, FY2024; taken from search snippets only, so re-confirm in the opened text):
- FY2024 10-K (filed 2025-02-24), CIK 899051: https://www.sec.gov/Archives/edgar/data/899051/000089905125000015/all-20241231.htm
- Snippets reported: $500 million Series A 6.500% Fixed-to-Floating Rate Junior Subordinated Debentures due 2067. Scheduled maturity May 15, 2057 and final maturity May 15, 2067. Redeemable at par on or after May 15, 2037, or earlier at the greater of par and a make-whole price in certain circumstances. 6.500% fixed to May 15, 2037, then a floating rate (3-month LIBOR + 2.120%, replaced by CME Term SOFR + 0.26161% spread adjustment). Interest deferral of up to 10 years, with compounding. Common-stock issuance obligations (alternative payment mechanism). Dividend restrictions during deferral. Verify these in the opened 10-K debt note, including the seniority wording and any replacement-capital or ranking language.
</file>

<notes>
Motivation: in base1 the agent never called parse_html_page or retrieve_information. It found the 10-K URL via edgar_search, then submitted from search snippets. It attributed the terms to the "FY2024 Form 10-K" without opening it, and listed the unopened Financial_Report.xlsx, the ARS PDF and an A.M. Best press release as sources. It leaked raw cite markup, issued a null-query web_search, and admitted it never found the seniority clause. The new guidance requires opening the 10-K, retrieving each term, citing only opened documents, writing plain text, and never searching with an empty query. The task leads (URL and snippet-derived terms) are labelled as unverified. No skill is added, because the procedure is short and matches earlier library entries that used always-on tool guidance.
</notes>