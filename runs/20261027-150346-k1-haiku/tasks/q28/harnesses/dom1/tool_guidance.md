# Tool use

- A search snippet or result title is a lead, not evidence. Open the primary filing with parse_html_page, then ask retrieve_information targeted questions (one table or section at a time, using input_character_ranges on long 10-Ks). Confirm each figure's period, unit and row/column in the retrieved text before using it.
- edgar_search takes the ticker or CIK in `ciks` and form-type and date filters; use it to find the filing URL. Never issue a web_search with an empty or null query.
- Cite only documents you opened and retrieved from; do not list search-only pages or spreadsheets. Write the answer in plain text with no citation markup such as <cite> tags.
