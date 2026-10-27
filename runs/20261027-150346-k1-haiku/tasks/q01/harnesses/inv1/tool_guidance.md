# Tool use

- Decide the documents and the as-of date before searching: company, form (10-K, 10-Q, 8-K and its EX-99 exhibits, DEFA14A, CORRESP), and period. Use edgar_search with the company CIK and date filters, not the question's wording. If web_search returns 0 results, retry once with a short non-empty query (never an empty or null query), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Use input_character_ranges on long filings. Confirm the fact, date and wording in the retrieved text.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit.
- Respect the as-of date (April 07, 2025). Do not use, cite or list a document filed or dated after it, even if search returns it. Check the filing date of each source before relying on it. A snippet that mentions a later event is not usable.
- Questions about how a company "has addressed" an event call for the company's own statements. Read at least one company-authored document on the event (8-K exhibit, press release, proxy-soliciting letter or Q&A) in addition to the annual-report risk factors. Report what the company did (legal action, regulatory engagement, operating restrictions, investment continuity, communications) separately from risks it warns about.
- Cite only documents you opened and retrieved from. Do not list a filing as a source, or attribute a statement to it, unless you retrieved that statement from it. If a fact came from a search snippet only, say so or leave it out.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. Give each fact with its date and source. Submit with submit_final_result as soon as the facts are verified; do not spend turns past that point.

In this task (verified in the FY2024 10-K, filed 2025-01-31, https://www.sec.gov/Archives/edgar/data/1163302/000116330225000018/x-20241231.htm):
- The merger-pending discussion is in Item 1 (Agreement and Plan of Merger; Business Strategy; Capital Structure), Item 1A (the "business uncertainties and contractual restrictions while the Merger is pending" risk factor), Item 3 and Item 7 (Business Update).
- The facts are:
  - On January 3, 2025 the President issued an order prohibiting the merger.
  - CFIUS extended the abandonment deadline to June 18, 2025.
  - A Petition for Review was filed in the D.C. Circuit.
  - The merger agreement restricts debt, buybacks and M&A without Nippon's consent.
- Company-authored documents to read for the "how addressed" part (filed before the as-of date) are in edgar_search for CIK 1163302: the January 3 and January 6, 2025 8-K exhibits and the DEFA14A filings of January 27 and March 25-26, 2025.
- The Q1 2025 10-Q and the June 2025 articles post-date April 07, 2025. Do not use them.
