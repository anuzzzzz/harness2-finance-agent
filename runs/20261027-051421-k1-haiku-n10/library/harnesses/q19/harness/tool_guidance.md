# Tool use

- Decide the company, form type (10-K / 10-Q) and fiscal period first. As of the question date, use the latest filing already published.
- SEC endpoints often return HTTP 403 here. `edgar_search` failed in every run that tried it, and `parse_html_page` on sec.gov URLs also returned 403. Do not retry a 403 and do not loop on index pages. Go straight to `web_search` (company, form, fiscal year, and the specific table or line item). Results often include the filing text and give the sec.gov URL.
- You may try `parse_html_page` once on the filing URL, then `retrieve_information` for targeted questions. If the parse fails, work from the search excerpt.
- A figure seen only in a search excerpt must be described as such in the answer. Never call it "verified against the filing" unless you opened the filing. Still check period, units (thousands vs millions) and whether the figure is discounted or undiscounted, and check that the table foots.
- Do the arithmetic on unrounded numbers, re-add the components once, and round only the final result.
- Write the answer as plain text, with no raw citation tags. Submit with `submit_final_result` as soon as the figures are in hand. Do not spend the remaining budget on extra searching.
