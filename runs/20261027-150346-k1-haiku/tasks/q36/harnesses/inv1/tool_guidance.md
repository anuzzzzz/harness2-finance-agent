# Tool use

- Decide the documents before searching: company, form (8-K EX-99.1 press release, 425 filing, S-4/proxy, 10-K or 10-Q) and period or event date. Use edgar_search with company and date filters, not the question's wording. If web_search returns nothing, retry once with a short non-empty query (never null or empty), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm each figure, its unit, and its basis in the retrieved text. Use input_character_ranges on long filings. parse_html_page cannot read PDFs; use the HTML 8-K exhibit or filing instead.
- Deal-price questions ("what price was X acquired at"): open the acquirer's or target's announcement (8-K EX-99.1 or 425) and retrieve (a) per-share consideration and its form (cash, stock with exchange ratio, or mix), (b) equity value, (c) enterprise value and what is included in it (debt, convertibles, net of cash). Say when a stock deal's value is fixed at signing and floats with the acquirer's share price. Say whether the deal has closed as of the as-of date. If two sources give different values for the same measure (for example EV of $2.36B vs $2.4B), retrieve each from its opened document, report both with their sources and say which is precise or rounded. Do not pick one from memory.
- Verify before submitting: re-check every figure against the retrieved text (period, unit, basis). Check implied numbers for consistency, for example equity value divided by price per share, or exchange ratio times acquirer price.
- Respect the as-of date (April 07, 2025). Do not use documents dated after it.
- Cite only documents you opened and retrieved from. Do not list a filing, article, presentation or PDF seen only in search results. If a figure came only from a snippet, say so plainly.
- Write the final answer in plain text with no citation markup (no <cite> tags). State each figure with its unit and source, then any calculation, then the conclusion in the form the question asks for. Submit with submit_final_result as soon as the figures are verified.

Leads for this task (Redfin, RDFN, acquired by Rocket Companies, RKT). These come from search snippets only, so re-confirm each one in the opened text:
- Announced March 10, 2025, all-stock deal. Reported terms: 0.7926 RKT Class A shares per RDFN share, equal to $12.50 per share at signing. Equity value about $1.75B. Enterprise value about $2.36B in Rocket's investor presentation (a PDF, which cannot be parsed). Redfin's Form 425 FAQ reports about $2.4B.
- Rocket press release (8-K EX-99.1): https://www.sec.gov/Archives/edgar/data/1805284/000095014225000696/eh250601250_ex9901.htm
- Redfin Form 425 FAQ: https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm
- Redfin Form 425, March 10, 2025: https://www.sec.gov/Archives/edgar/data/1382821/000162828025011458/form8-kx31025.htm
- Rocket's S-4, filed April 7, 2025, is long and may hold the merger-agreement terms: https://www.sec.gov/Archives/edgar/data/1805284/000110465925032694/tm2511408-1_s4.htm
- The EV figure is the look-alike risk: find where the $2.36B vs $2.4B figures appear in opened text and report both.
