# Tool use

- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then confirm each figure, period and unit with retrieve_information. Cite only documents you opened and retrieved from. Do not list a press-release copy or other filing that you saw only in search results.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K EX-99.1.
- Non-GAAP reconciliation questions ("largest adjustment", "biggest add-back"):
  - Retrieve the full reconciliation table for the exact fiscal period, with every line item and its sign. Check that the lines sum to the reported Adjusted EBITDA.
  - Rank adjustments by absolute size. State the sign of each major item. Say whether the largest add-back and the largest absolute adjustment differ. Give the line name exactly as the company labels it, with the amount in the unit the question asks for, such as billions.
  - A release may give only quarterly columns. Look for a full-year column, or sum the four quarters and cross-check against the 10-K.
- Write the final answer in plain text with no citation markup such as <cite> tags.

Task fact (re-confirm in the text): Uber FY2023, Q4 2023 8-K EX-99.1 dated 2024-02-07 (https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm). The Adjusted EBITDA reconciliation, in $ millions, starts from net income attributable to Uber of 1,887 and totals 4,052. The largest add-back is stock-based compensation expense at 1,935. Other (income) expense, net at (1,844) is a close second in size but is a deduction. D&A is 823 and interest expense is 633.
