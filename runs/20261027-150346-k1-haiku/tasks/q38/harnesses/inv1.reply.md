I'm adopting the q47/q48 pattern as always-on `tool_guidance.md` with no skill, because the procedure is short, and adding Lyft facts labelled as such. I have not seen how the base run opened its sources, so the main change is sourcing.

<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (8-K EX-99.1 earnings release, 10-Q, 10-K) and fiscal period. Use edgar_search with company, form and filing-date filters rather than the question's wording. If web_search returns nothing, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Use input_character_ranges on long filings. Confirm figure, period, unit and GAAP/non-GAAP basis in the retrieved text.
- parse_html_page cannot read PDFs (annual-report PDFs, ARS). Use the HTML 8-K exhibit or 10-K/10-Q instead.
- Guidance-versus-actual questions need two opened documents: the release for the quarter BEFORE the period judged (it holds the outlook) and the release or filing that reports the period itself. Read the guided range and the actual from those opened documents, not from snippets or transcripts. Prefer a figure the company states for the quarter. If you must derive a quarter by subtracting nine-month from full-year figures, say so, and cross-check against a stated figure (release, call remarks).
- Compare like with like: same metric definition, same period, same unit. For a ratio guided as a range, take the midpoint of the stated range. Compute the actual ratio from dollar figures at full precision, and also note the company's own rounded stated ratio. If the two bases give different gaps, give the unrounded one as the headline and the other as a labelled alternate. State beat or miss and the difference in the unit the question asks for (bps = percentage-point difference x 100).
- Re-check every figure in the calculation against the retrieved text before submitting. A parsed table that looks garbled must be cross-checked against the document's own text.
- Cite only documents you opened and retrieved from. Do not list a filing, PDF, or transcript seen only in search results, and do not attribute a figure to a document you did not retrieve it from. If a figure came from a snippet only, say so.
- Write the final answer in plain text with no citation markup (no <cite> tags). Give each figure with period, unit and source, then the calculation, then the conclusion. Submit with submit_final_result as soon as the figures are verified.

Leads for this task (Lyft Q4'24 Adjusted EBITDA margin vs Q3'24 guidance; re-confirm in opened text):
- Guidance: Q3'24 earnings release, 8-K EX-99.1, https://www.sec.gov/Archives/edgar/data/1759509/000175950924000121/lyft-20240930xpressrelease.htm. Earlier runs read the Q4'24 outlook there as Gross Bookings $4.28-4.35B, Adjusted EBITDA $100-105M, Adjusted EBITDA margin about 2.3%-2.4% of Gross Bookings (midpoint 2.35%).
- Actual: the Q4'24 earnings release (8-K EX-99.1, filed about Feb 11, 2025) was not found by web_search earlier. Try edgar_search for Lyft 8-K filed 2025-02-01 to 2025-02-28. If it cannot be opened, fall back to the FY2024 10-K (https://www.sec.gov/Archives/edgar/data/1759509/000175950925000025/lyft-20241231.htm) full-year figures minus the Q3'24 10-Q nine-month figures. Earlier runs derived Q4 Adjusted EBITDA $112.8M (FY $382.4M less 9M $269.6M) and Gross Bookings $4,278.9M (FY $16,099.4M less 9M $11,820.5M), margin 2.6361%; management states 2.6%. That gives about +29 bps unrounded, or +25 bps using the rounded 2.6%. Check that the figures are from the same non-GAAP definition.
</file>

<notes>
Motivation: base1 never obtained a Q4 release and listed an annual-report PDF and an unopened transcript as sources. Derived Q4 actual by subtraction without a stated-figure cross-check. Added the following to tool_guidance.md, following the q47/q48 pattern:
- primary-document opening rule;
- the PDF limit;
- two-document guidance-versus-actual procedure;
- cite-only-opened and plain-text rules;
- explicit handling of the rounded versus unrounded ratio, which gives +29 vs +25 bps;
- labelled Lyft task leads: Q3 release URL, guided 2.3-2.4% margin, a search route to the Q4 release, and the derived figures as a fallback.
No skill: the procedure is short, and earlier tasks showed a skill added no effect.
</notes>