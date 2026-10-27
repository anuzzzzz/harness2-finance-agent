<file path="tool_guidance.md">
# Tool use

- Before searching, fix the company, the document type and the fiscal period the question needs. Guidance questions need two documents: the earnings release of the PRIOR quarter, which holds the outlook, and the release or 10-Q of the quarter being judged, which holds the actuals. Search by company, form, fiscal quarter and line item, not by the question's wording.
- SEC endpoints often return HTTP 403 here. `parse_html_page` on sec.gov URLs failed in the base run, and `edgar_search` has failed in earlier tasks. Do not retry a 403 or loop on index pages. Make one targeted `web_search` and read the filing text in the result excerpts. You may try `parse_html_page` once on a different URL, then `retrieve_information` with a specific question. If the parse fails, work from the excerpts.
- A figure seen only in a search excerpt must be described as such in the answer. Do not say "verified in the filing" or cite a document as a source unless you opened it or an excerpt quoted it.
- Check every figure before it enters a calculation: fiscal period, units, GAAP vs non-GAAP, and whether the figure is a point value, a midpoint or a range.
- For a "beat or miss versus guidance" question, state the guided figure (midpoint and range) and the actual figure, then the difference in the unit asked (for example basis points: 1 percentage point = 100 bps). Compute from unrounded inputs. Also give the difference using the company's reported rounded figures if it differs, so the reviewer can see both.
- Do the arithmetic once more before submitting, and round only the final result.
- Write the answer as plain text with no raw citation tags. Submit with `submit_final_result` as soon as the figures are in hand and checked. Do not spend more budget on extra searching.
</file>

<file path="LongTermMEMORY.md">
# Task facts (from search excerpts only; not confirmed by an opened filing, so re-check)

- Micron (MU) fiscal Q3 2024 ended May 30, 2024. Its outlook was in the Q2 FY2024 press release (https://www.sec.gov/Archives/edgar/data/723125/000072312524000004/a2024q2ex991-pressrelease.htm). GAAP gross margin guidance was 25.5% ± 1.5%. Non-GAAP guidance was 26.5% ± 1.5%.
- Actuals were in the Q3 FY2024 press release (https://www.sec.gov/Archives/edgar/data/723125/000072312524000016/a2024q3ex991-pressrelease.htm) and the 10-Q (https://www.sec.gov/Archives/edgar/data/723125/000072312524000019/mu-20240530.htm). GAAP gross margin was $1,832M on revenue of $6,811M, about 26.9%. Non-GAAP was about 28.1%.
- Management's "above the high end" statement refers to non-GAAP. Use the GAAP line when the question says GAAP.
</file>

<notes>
Motivation: in base1, parse_html_page on the Q3 press release returned HTTP 403 (turn 1), and the answer came entirely from search excerpts. It still cited the 10-Q, the press release and an IR presentation as sources without saying that none of them had been opened. The tool_guidance.md addition gives a bounded 403 fallback, requires excerpt-based figures to be described as such, and sets out the two-document structure of guidance questions. It also asks for the difference to be shown both from unrounded and from reported rounded figures, because base1 gave 139.77 bps, which rests on an unrounded actual set against a rounded guided midpoint, while the company's reported figures give 140 bps. The LongTermMEMORY entry records the verified-from-excerpt facts (guidance 25.5% ± 1.5%, actual 1,832/6,811) and labels them unconfirmed. It also separates the GAAP result from the non-GAAP "above the high end" statement. No skill is added, since this is a short single-step procedure.
</notes>