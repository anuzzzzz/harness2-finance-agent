# Tool use

- A search snippet is a lead, not evidence. Every figure in a calculation (guidance range, exchange-rate assumption, monthly revenue) must be read from a document opened with parse_html_page and confirmed with retrieve_information. Do not call a figure "guidance" or "assumed" if you only inferred it from a different document.
- Respect the question's as-of date: do not use documents published after it, even if search returns them.
- Cite only documents you opened and retrieved from. Write the final answer in plain text with no citation markup such as <cite> tags.
