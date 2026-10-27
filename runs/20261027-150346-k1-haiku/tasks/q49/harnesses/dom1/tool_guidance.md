# Tool use

- A search snippet or result title is a lead, not evidence. Open the primary document (8-K EX-99.1 release, 10-Q, 10-K) with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm each figure's period, unit and GAAP/non-GAAP basis in the retrieved text. This applies to guidance, actuals and the current-year outlook alike.
- parse_html_page cannot read PDFs. Use the HTML 8-K exhibit instead. Never send an empty search query; use edgar_search with company and date filters to find a release.
- Cite only documents you opened and retrieved from. Do not list PDFs, articles or releases seen only in search results.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags.
