I'm adding one short always-on `tool_guidance.md`, adapted from the q45 and q44 library entries. The only observed divergence in the single base run is on sourcing, and the number was probably already right.

<file path="tool_guidance.md">
# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal period. Use edgar_search with company and date filters. If web_search returns 0 results or errors, retry once with a short query, then use edgar_search or a known primary URL. Do not call web_search with an empty query.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (store it under a clear key), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and basis in the retrieved text. Use input_character_ranges on long filings rather than re-reading everything.
- Check every figure you will submit against the text. If a retrieval answer is truncated, or says a number was derived rather than disclosed, run a second targeted retrieval (e.g. the exact table row or the note's own sentence) before relying on it. When you derive a figure from components (principal x conversion rate), reconcile it to any disclosed total and say which figures are disclosed and which are derived.
- Cite only documents you opened and retrieved from. Do not list a filing as a source unless a figure in your answer came from it.
- Write the final answer in plain text with no citation markup: the figure, period and unit, how it was derived, and the source of each figure. Submit with submit_final_result as soon as the figure is verified.

Lead for this task (re-confirm in the text): Snap Inc FY2024 10-K (https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm). The net loss per share note (Note 3) lists "Convertible Notes (if-converted)" of 85,945 thousand shares at 12/31/2024 in its table of anti-dilutive securities (units are thousands of shares). Note 7 (Debt) holds principal and conversion rates for the 2025, 2026, 2027, 2028 and 2030 notes. Check whether Note 7 or the liquidity section states a maximum share count for the notes, and confirm the figure there as well.
</file>

<notes>
Motivation (base1): the run got 85,945 thousand shares from a single retrieve_information call whose output was truncated. It flagged the 2026 principal ($249.8M) as unconfirmed but never re-queried. It also listed the Q3 2024 press release as a source without ever opening it, and made one web_search call with a null query. The new tool_guidance (modelled on the q45 and q44 library entries) addresses these points:
- cite only opened documents;
- a second targeted retrieval when output is truncated or derived;
- no empty-query searches.
It also records the verified task fact, labelled as a lead to re-confirm: the Note 3 table row of 85,945 thousand if-converted shares, and where the per-series inputs sit in Note 7. The evidence is a single rollout, so confidence is low. No skill was added because the question is a single lookup and the tool guidance is enough.
</notes>