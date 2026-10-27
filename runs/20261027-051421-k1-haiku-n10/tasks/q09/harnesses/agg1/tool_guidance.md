# Tool use

- Before searching, fix the company, document type and fiscal period. Guidance questions need two documents: the prior quarter's earnings release (the outlook) and the release or 10-Q of the quarter being judged (the actuals). Search by company, form, fiscal quarter and line item.
- SEC endpoints often return HTTP 403 here (`parse_html_page` on sec.gov failed in 2/2 base-style runs that tried it). Do not retry a 403 or loop on index pages. Make a targeted `web_search` and read the filing text in the excerpts. You may try `parse_html_page` once on a different URL, then `retrieve_information` with a specific question.
- A figure seen only in a search excerpt must be described as such. Do not say "verified in the filing", and do not cite a document as opened, unless you opened it or an excerpt quoted it.
- Check each figure before use: fiscal period, units, GAAP vs non-GAAP, and point value vs midpoint vs range.
- Do the arithmetic from unrounded inputs, re-check it once, and round only the final result.
- Write the answer as plain text with no raw citation tags. Submit with `submit_final_result` as soon as the figures are in hand.
