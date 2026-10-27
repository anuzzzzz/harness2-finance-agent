# Tool use

- Decide the documents and periods before searching: company, form (8-K EX-99.1 earnings release), fiscal period. A search snippet or result title is a lead, not evidence. Open each primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text. If web_search returns thin results, retry once with a short non-empty query, then use edgar_search or a known URL. parse_html_page cannot read PDFs or slide decks; use the HTML exhibit.
- Beat/miss versus guidance needs two opened documents per period. The guidance (revenue midpoint and margin) is in the release for the quarter BEFORE the period judged. The actual is in the release for the period itself. Do not take either from a snippet. Every period in the answer needs both figures retrieved from opened text.
- Where guidance is a margin and a revenue midpoint, implied value = midpoint x margin. Take the actual as the reported non-GAAP figure. Use the reconciliation table in the release if the dollar amount is not on the face of the statements. Do not rebuild it as reported margin x revenue unless no dollar figure exists, and say so if you do. Carry full precision and round only the final number. Beat or miss % = (actual - implied) / implied.
- "Last N quarters" is counted back from the as-of date (April 07, 2025). Use only releases dated on or before it. Name the quarters you chose and why.
- Match the answer to the format the question prescribes, including its decimal places and line layout. Give the supporting inputs (guided revenue midpoint, guided margin, implied dollars, actual dollars) per period, then the average the question asks for.
- Re-check each figure against the retrieved text before submitting. A parsed table that looks garbled must be cross-checked against the document's own text. Submit with submit_final_result while budget remains.
- Cite only documents you opened and retrieved from. Do not list a page seen only in search results, and do not attribute a figure to a document you did not retrieve it from. Write the final answer in plain text with no citation markup.

Leads for this task (AMD, FY2024 quarters). These come from search results and an unverified earlier attempt, so re-confirm in the opened text. SEC 8-K earnings releases:
- Q4 2023 release (gives Q1 2024 outlook): https://www.sec.gov/Archives/edgar/data/2488/000000248824000009/q42023991final.htm
- Q1 2024 release (Q1 actual; Q2 outlook): https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm
- Q2 2024 release (Q2 actual; Q3 outlook): https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm
- Q3 2024 release (Q3 actual; Q4 outlook): https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm
- The Q4 2024 actual is in the February 4, 2025 release. Find it with edgar_search (AMD, 8-K, Feb 2025) and open it.
- Earlier unverified readings of the outlook were revenue of about $5.4B, $5.7B, $6.7B and $7.5B (each +/- $300M), with non-GAAP gross margin of about 52%, 53%, 53.5% and 54%. Retrieve the actual outlook text for each quarter.
- Each release prints the non-GAAP gross margin percentage and a GAAP to non-GAAP reconciliation. Retrieve the non-GAAP gross profit dollars from the reconciliation, in $ millions.
