<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (8-K EX-99.1 earnings release), fiscal period. A search snippet or result title is a lead, not evidence. Open each primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text. If web_search returns thin results, retry once with a short non-empty query (never an empty one), then use edgar_search or a known URL. parse_html_page cannot read PDFs or slide decks; use the HTML exhibit.
- Beat/miss versus guidance needs two opened documents per period. The guidance (revenue midpoint and margin) is in the release for the quarter BEFORE the period judged. The actual is in the release for the period itself. Do not take either from a snippet or from the neighbouring quarter's guide. Quote the guided margin exactly as printed (it may be a half-point, such as 53.5%).
- Where guidance is a margin plus a revenue midpoint, implied value = midpoint x margin. Take the actual as the reported non-GAAP dollar figure from the current-quarter column of the release's reconciliation table. Do not rebuild it as rounded margin x revenue unless no dollar figure exists, and say so if you do. Carry full precision and round only the final number. Beat or miss % = (actual - implied) / implied. The average of percentages is the simple mean of the per-quarter percentages.
- "Last N quarters" is counted back from the as-of date (April 07, 2025). Use only releases dated on or before it. Name the quarters you chose.
- Follow the answer format the question prescribes (line layout, labels, units, and the number of decimals it shows, e.g. "X.X %"). Show the unrounded working beneath it: guided revenue midpoint, guided margin, implied dollars, actual dollars, per period, then the average.
- Re-check each figure against the retrieved text before submitting. A garbled parsed table must be cross-checked against the document's own text. Submit with submit_final_result while budget remains.
- Cite only documents you opened and retrieved from. Do not list pages seen only in search results. Write the answer in plain text with no citation markup.

Leads for this task (AMD, FY2024 quarters; re-confirm in the opened text). SEC 8-K EX-99.1 releases:
- Q4 2023 release (Q1 2024 outlook): https://www.sec.gov/Archives/edgar/data/2488/000000248824000009/q42023991final.htm
- Q1 2024 release (Q1 actual; Q2 outlook): https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm
- Q2 2024 release (Q2 actual; Q3 outlook): https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm
- Q3 2024 release (Q3 actual; Q4 outlook): https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm
- Q4 2024 release (Feb 4, 2025; Q4 actual): https://www.sec.gov/Archives/edgar/data/2488/000000248825000009/q42024991.htm
</file>

<notes>
kept -> inv1 tool_guidance (open both guidance and actual releases, as-of window, sources only if opened) -> base1 used only 4 web_searches and opened no release, listed unopened sources; inv1 opened all five releases in 4 turns and submitted; dom1 did the same in 7 turns, so the rule works in 2/2 edited runs.
revised -> inv1 format rule -> inv1 printed two-decimal percentages though the question prescribes "X.X %"; dom1 followed one decimal. I merged dom1's follow-the-prescribed-decimals rule into the always-on text.
dropped -> dom1 skill guidance_implied_gross_profit and its systemprompt trigger line -> dom1 took 7 turns with the skill versus 4 for inv1 without it, and the figures were identical. The procedure is short, and library entries q47 and q48 kept it in tool_guidance. This saves always-on and trigger cost.
kept -> release URLs as leads (including the Q4 2024 HTML exhibit URL found by both runs via edgar_search) -> both candidates reached the same figures from these releases (guides 52/53/53.5/54%, actuals 2,861/3,101/3,657/4,140), so the leads were correct and saved discovery turns.
kept -> dom1's "quote guided margin exactly, never reuse neighbouring quarter's margin" -> base1 assumed 53.5%/54% unverified from snippets; both candidates confirmed them in opened text.
Neither candidate run failed to submit; no unsafe edit.
</notes>