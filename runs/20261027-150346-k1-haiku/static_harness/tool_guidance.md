# Tool guidance

- Answer from primary documents. Find the relevant SEC filing with edgar_search (company, form type, date range), open it with parse_html_page, and read the figures with retrieve_information. Web search results and third-party sites are leads, not evidence.
- Before using a figure, check that its period, units and basis match the question. Show the calculation.
- Call submit_final_result with the answer and its sources before running out of turns.
