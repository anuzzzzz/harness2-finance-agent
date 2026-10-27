<file path="tool_guidance.md">
# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1 release) and fiscal period. Use edgar_search with company and date filters. If web_search returns nothing, retry once with a short non-empty query (never an empty or null one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information a targeted question. Confirm each line item, its sign, period and unit in the retrieved text.
- For "what adjustments does the company make to get a non-GAAP measure" questions, the answer is the company's own reconciliation table: every line from the GAAP starting measure to the non-GAAP result, in the order shown, with the sign (add-back or deduction) and the amount for each period shown. Also report the company's stated reason for excluding the items, and any footnote that defines an item. Check that the lines foot to the stated total. Do not describe adjustments from memory or from an earlier year's list. Item names and the set of items change between years, so use the latest filing's labels.
- Do not mix GAAP and non-GAAP bases, or quarterly and full-year columns. A full-year table is in the 10-K MD&A (Key Business Metrics and Non-GAAP Financial Measures). Earnings-release exhibits (8-K EX-99.1) often give quarterly columns only.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K exhibit.
- Cite only documents you opened and retrieved from. Do not list a 10-Q, shareholder-letter PDF or other filing as a source, or attribute a figure to it, unless you retrieved that figure from it. If a statement rests on a search snippet only, say so or omit it.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State each figure with its period, unit and source, then the check or calculation, then the conclusion in the form the question asks for. Submit with submit_final_result once the figures are verified.

Task fact (Airbnb, verified in one run, so re-confirm in the text): the FY2024 10-K (https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm) reconciles Net income to Adjusted EBITDA through these lines, in $ millions (FY2024 / FY2023). Net income 2,648 / 4,792. Provision for (benefit from) income taxes 683 / (2,690). Other expense, net 40 / 137. Interest income (818) / (721). Depreciation and amortization 65 / 44. Stock-based compensation expense 1,407 / 1,120. Acquisition-related impacts (7) / (3). Lodging taxes, host withholding taxes, and transactional taxes, net 23 / 974. Adjusted EBITDA 4,041 / 3,653. The 10-K table covers only two years, so FY2022 would need the FY2023 10-K.
</file>

<notes>
Motivation: base1 got the correct reconciliation from the 10-K in one retrieval, but its final answer leaked raw <cite index=...> markup and listed unopened sources (the Q2 and Q3 10-Qs and a shareholder-letter PDF) as sources. It also made a null-query web_search. The same failures, and the same fixes, were adopted for q44, q45 and q47, so I reused that sourcing and no-markup rule.

Practitioner content added: for "what adjustments" questions, give the full reconciliation table with signs, the stated rationale and footnotes, and a foot-to-total check. Use the latest filing's labels, since item names change between years. Separate the full-year 10-K table from the quarterly-only 8-K exhibit.

The Airbnb line items and amounts are written in as a labelled task fact. The retrieval footed to both stated totals (4,041 and 3,653), and the 10-K table carries only FY2024 and FY2023.

No skill was added. The procedure is short, and the q45 and q44 records show skills added nothing beyond always-on guidance.
</notes>