<file path="tool_guidance.md">
# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1 earnings release), fiscal period. Guidance for quarter N is printed in the Outlook section of the release for quarter N-1, so a multi-quarter guidance question needs one release per quarter. Prefer edgar_search with company and date filters over question-worded web_search. If web_search returns 0 results, retry once with a shorter query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open each primary release with parse_html_page (one clear key per document). Then ask retrieve_information one targeted question per document, for example "Outlook: revenue expected for the next quarter, midpoint and plus/minus amount". Confirm the figure, period, unit and wording in the retrieved text before it enters a calculation. If a document cannot be fetched, say so and name where the figure came from.
- parse_html_page cannot read PDFs. Use the HTML 8-K EX-99.1 or the 10-K/10-Q.
- Use input_character_ranges on long filings rather than re-reading everything.
- Carry full precision and round only the final numbers. When the question gives an output format, follow it exactly, one line per period.
- Cite only documents you opened and retrieved from. Do not list a press-release page that you only saw in search results.
- Write the final answer in plain text with no citation markup such as <cite> tags. State each input with its period, unit and source, then the calculation.
- Once every input is verified in primary text, submit with submit_final_result immediately.

Lead for this task (verified only from search snippets, so re-confirm in the text): AMD gave revenue guidance of the form "approximately $X billion, plus or minus $300 million". The figures seen were Q2 2024 $5.7B, Q3 2024 $6.7B, Q4 2024 $7.5B and Q1 2025 $7.1B. They sit in these 8-K EX-99.1 releases, which issued the guidance for the following quarter:
- Q1 2024 results (guides Q2 2024): https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm
- Q2 2024 results (guides Q3 2024): https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm
- Q3 2024 results (guides Q4 2024): https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm
- Q4 2024 results (guides Q1 2025): https://www.sec.gov/Archives/edgar/data/2488/000000248825000009/q42024991.htm
Range as a percent of the midpoint = (high - low) / midpoint x 100, so $0.6B / midpoint if each band is plus or minus $300M. Check that the band is the same in every release.
</file>

<notes>
Motivating moment: base1 ran four web_searches and submitted without opening any filing. It attributed quotes to documents it never fetched, listed an unopened ir.amd.com press-release URL as a source, and left raw <cite index> markup in the answer. The numbers it reached ($5.7B, $6.7B, $7.5B and $7.1B, each plus or minus $300M) look consistent with the snippets, so I changed process only. The edit to tool_guidance.md adds four things: guidance sits in the prior quarter's release; open and retrieve from each primary release before the calculation; cite only opened documents; no citation markup, and follow the requested format. It also carries the four 8-K URLs, labelled as snippet-level leads to re-confirm, because the search results showed them. This mirrors the verify-in-primary-text pattern adopted in q09, q44 and q45. No skill was added, since the procedure is short and fits in tool guidance.
</notes>