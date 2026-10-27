# Tool use

- Decide the document and period before searching: company, form (10-K, 8-K EX-99.1 earnings release or shareholder letter, 10-Q), fiscal period. Prefer edgar_search with company and date filters. If web_search returns 0 results, retry once with a shorter query, then move to edgar_search or a known primary URL.
- parse_html_page cannot read PDFs (it errors). For a PDF shareholder letter, use the HTML 10-K or the 8-K EX-99.1 from edgar_search instead.
- A search snippet is a lead, not evidence. Before submitting, open the primary document with parse_html_page (store it under a clear key), then ask retrieve_information one targeted question (e.g. "average nights per booking by region, FY2024"). Confirm the figure, period, unit and region or segment in that text. Do not say a filing "reports" a figure unless you actually retrieved it from that filing. If the primary document cannot be fetched, say so and name the snippet source.
- Use input_character_ranges on long filings rather than re-reading everything.
- Look-alike figures: report the company-stated (rounded) figure as the answer. Mention third-party or unrounded variants only as labelled cross-checks.
- Write the final answer in plain text. Do not include citation markup such as <cite index=...> tags. State the figure, period and unit, the calculation if any, and the source of each figure.
- Submit with submit_final_result as soon as the figure is verified in the primary text.
