The base run answered 3.3 from search snippets and never opened the primary document, so I added short always-on guidance on verifying figures and on how to cite them.

<file path="tool_guidance.md">
# Tool use

- Decide the document and period before searching: company, form (10-K, 8-K EX-99.1 shareholder letter, 10-Q), fiscal period. Prefer edgar_search with the company and date filters. If web_search returns 0 results, retry once with a shorter query, then move to edgar_search or a known primary URL.
- A search snippet is a lead, not evidence. Before submitting, open the primary document with parse_html_page (store it under a clear key), then ask retrieve_information one targeted question (e.g. "average nights per booking by region, FY2024"). Confirm the figure, period, unit and region/segment in that text. Only if the primary document cannot be fetched or parsed, say so in the answer and rely on the snippet, naming it as the source.
- Use input_character_ranges on long filings rather than re-reading everything.
- Look-alike figures: check whether the question wants the company-reported (rounded) figure or a derived or third-party unrounded one. Report the company-stated figure as the answer, and mention the other only as supporting context with its source.
- Write the final answer in plain text. Do not include citation markup such as <cite index=...> tags. State the figure, period and unit, the calculation if any, and the source of each figure.
- Submit with submit_final_result as soon as the figure is verified in the primary text.

# Facts verified or suggested in this task (labelled; re-check)
- Airbnb's regional "average nights per booking" is not an obvious 10-K line item. A search snippet from the Q4 2024 shareholder letter (https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf, also the 8-K EX-99.1 filed 2025-02-13, accession 0001193125-25-026054) reported 2024 values: North America 4.1, EMEA 3.8, Latin America 3.7, Asia Pacific 3.3. The base run did NOT confirm this in the document text, so open the letter or EX-99.1 and confirm it. The 10-K is https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm.
</file>

<notes>
In base1, the agent submitted from search snippets after one empty web_search and one edgar_search. It never ran parse_html_page or retrieve_information on the shareholder letter or the 10-K, so 3.3 was never verified against primary text. The final answer also leaked raw <cite index> markup. The agent mixed 3.3 (company-reported) with 3.33 (third-party unrounded) without saying which one the answer is. I did not add a skill, since the fix is short sequencing guidance. The task fact is labelled as unverified because the run did not confirm it. The URLs come from the trajectory.
</notes>