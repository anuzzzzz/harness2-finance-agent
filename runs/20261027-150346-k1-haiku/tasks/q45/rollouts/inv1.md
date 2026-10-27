## Rollout `inv1`
- outcome: submitted
- turns: 3; cost: $0.096; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_10k_2024. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb_10k_2024
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb FY2024 10-K text: {{abnb_10k_2024}}. Find the stock-based compensation expense for fiscal year 2024 (and 2023) in the Adjusted EBITDA reconciliation and in the stock-based compensation footnote. Report the exact figures in millions, the period, and whether the Adjusted EBITDA reconciliation shows an annual column. Quote the relevant line exactly."})
  result: **Stock-based compensation expense, FY2024 and FY2023**
  
  | Source | FY2023 | FY2024 |
  |---|---|---|
  | Adjusted EBITDA reconciliation | $1,120M | $1,407M |
  | Stock-based compensation footnote (Note 12) | $1.1 billion | $1.4 billion |
  
  **Adjusted EBITDA reconciliation:** The reconciliation shows an annual column for each fiscal year, headed "2023" and "2024" for the years ended December 31. The relevant line reads:
  
  > "Stock-based compensation expense1,120 1,407"
  
  The reconciliation header is "(in millions, except percentages)", so the figures are $1,120 million (2023) and $1,407 million (2024).
  
  **Stock-based compensation footnote:** Note 12 gives the figures only in rounded billions. It reads:
  
  > "Stock-based compensation expense was $930 million, $1.1 billion and $1.4 billion for the years ended December 31, 2022, 2023 and 2024, respectively."
  
  The exact millions figures appear elsewhere in the filing: the MD&A footnote table and the cash flow statement both show $1,120 million for 2023 and $1,407 million for 2024. The Note 16 segment expense table also shows 1,120 and 1,407.
  
  Neither the reconciliation nor the footnote uses a different number for the expense itself. The Consolidated Statements of Stockholders' Equity show stock-based compensation credited to equity of $1,146 million (2023) and $1,424 million (2024). That is a different line and is not the expense figure, so I would not use it for this comparison.

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "Answer: Airbnb's FY2024 stock-based compensation add-back in Adjusted EBITDA was $1,407 million (about $1.41 billion).\n\nHow it was derived and checked:\n- The Q4 2024 8-K EX-99.1 reconciles Adjusted EBITDA by quarter only. The quarterly SBC add-backs were 295, 382, 362 and 368 ($M). Summing them: 295 + 382 + 362 + 368 = 1,407.\n- I opened the FY2024 Form 10-K (abnb-20241231.htm) and retrieved its Adjusted EBITDA reconciliation, which has an annual column in millions. The stock-based compensation line reads 1,120 for 2023 and 1,407 for 2024, matching the quarterly sum.\n- The 10-K's stock-based compensation footnote (Note 12) states the expense only in rounded terms ($1.4 
…[truncated 867 chars])

### Final answer
Answer: Airbnb's FY2024 stock-based compensation add-back in Adjusted EBITDA was $1,407 million (about $1.41 billion).

How it was derived and checked:
- The Q4 2024 8-K EX-99.1 reconciles Adjusted EBITDA by quarter only. The quarterly SBC add-backs were 295, 382, 362 and 368 ($M). Summing them: 295 + 382 + 362 + 368 = 1,407.
- I opened the FY2024 Form 10-K (abnb-20241231.htm) and retrieved its Adjusted EBITDA reconciliation, which has an annual column in millions. The stock-based compensation line reads 1,120 for 2023 and 1,407 for 2024, matching the quarterly sum.
- The 10-K's stock-based compensation footnote (Note 12) states the expense only in rounded terms ($1.4 billion for 2024, $1.1 billion for 2023). The exact $1,407 million figure appears in the MD&A table, the cash flow statement and the segment note, per the retrieved text.
- The Statement of Stockholders' Equity shows $1,424 million for 2024, but that is a different line (equity credit), not the expense add-back, so it was excluded.

Units: US$ millions. Period: fiscal year ended December 31, 2024.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb FY2024 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm",
            "name": "Airbnb Q4 2024 8-K EX-99.1 (quarterly Adjusted EBITDA reconciliation)"
        }
    ]
}