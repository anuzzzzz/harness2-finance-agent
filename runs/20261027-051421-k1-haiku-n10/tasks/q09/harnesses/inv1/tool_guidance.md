# Tool use

- Before searching, fix the company, the document type and the fiscal period the question needs. Guidance questions need two documents: the earnings release of the PRIOR quarter, which holds the outlook, and the release or 10-Q of the quarter being judged, which holds the actuals. Search by company, form, fiscal quarter and line item, not by the question's wording.
- SEC endpoints often return HTTP 403 here. `parse_html_page` on sec.gov URLs failed in the base run, and `edgar_search` has failed in earlier tasks. Do not retry a 403 or loop on index pages. Make one targeted `web_search` and read the filing text in the result excerpts. You may try `parse_html_page` once on a different URL, then `retrieve_information` with a specific question. If the parse fails, work from the excerpts.
- A figure seen only in a search excerpt must be described as such in the answer. Do not say "verified in the filing" or cite a document as a source unless you opened it or an excerpt quoted it.
- Check every figure before it enters a calculation: fiscal period, units, GAAP vs non-GAAP, and whether the figure is a point value, a midpoint or a range.
- For a "beat or miss versus guidance" question, state the guided figure (midpoint and range) and the actual figure, then the difference in the unit asked (for example basis points: 1 percentage point = 100 bps). Compute from unrounded inputs. Also give the difference using the company's reported rounded figures if it differs, so the reviewer can see both.
- Do the arithmetic once more before submitting, and round only the final result.
- Write the answer as plain text with no raw citation tags. Submit with `submit_final_result` as soon as the figures are in hand and checked. Do not spend more budget on extra searching.
