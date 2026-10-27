# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal period. Use edgar_search with company and date filters.
- A search snippet is a lead, not evidence. Open the primary filing with parse_html_page (one clear key per filing) and confirm each figure, period, unit and basis with retrieve_information.
- A 10-K shows three years of cash-flow and income-statement data, but later filings may recast earlier years. Take each year from the filing you opened for it, or state which filing's (possibly recast) figure you used.
- Cite only documents you opened and retrieved from. Do not list a filing as a source unless a figure came from it.
- Write the final answer in plain text with no citation markup. Submit as soon as figures are verified.
