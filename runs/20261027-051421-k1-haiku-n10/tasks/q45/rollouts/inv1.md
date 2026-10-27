## Rollout `inv1`
- outcome: submitted
- turns: 2; cost: $0.024; submitted: True

### Turn 1  (stop_reason=end_turn)
In fiscal 2024, Airbnb's adjustment for stock-based compensation expense in its Adjusted EBITDA reconciliation was **$1,407 million**.

This figure comes from a search excerpt of the FY2024 Form 10-K, not from an opened copy of the filing. The reconciliation table is in millions and shows 2023 and 2024 side by side. 
Net income | $4,792 | $2,648
 and the table lists 
Stock-based compensation expense | 1,120 | 1,407
, so the 2024 column is $1,407 million.

The 2023 figure of $1,120 million matches the prior-year 10-K. That filing's table shows 
1,120.
 for stock-based compensation expense.

As a consistency check, the 10-Q for the nine months ended September 30, 2024 shows 
Stock-based compensation expense(1) | 286 | 362 | 830 | 1,039
. That implies roughly $368 million in Q4 2024 (1,407 − 1,039), which is plausible.

Note that this adjustment is the add-back line in the Adjusted EBITDA reconciliation. It is the same expense recognized in the income statement, and the 10-K's stock-based compensation expense note reports the same total.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. - Form 10-K - FY2024"
        },
        {
            "url": "https://content.edgar-online.com/ExternalLink/EDGAR/0001559720-24-000006.html?hash=8fb59a79794331d61fbddd144f54c3e63f372875378160b08c84a6274e949294&dest=exh1011sfo_888brannanxgrou_htm",
            "name": "Airbnb, 
…[truncated 287 chars]
- web_search(query="Airbnb 2024 10-K adjusted EBITDA reconciliation stock-based compensation expense") → 9 results: Airbnb, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm>; Airbnb, Inc. (Form: 10-K, Received: 02/16/2024 16:03:41) <https://content.edgar-online.com/ExternalLink/EDGAR/0001559720-24-000006.html?hash=8fb59a79794331d61fbddd144f54c3e63f372875378160b08c84a6274e949294&dest=exh1011sfo_888brannanxgrou_htm>; Airbnb, Inc. (Form: 10-Q, Received: 11/07/2024 16:11:19) <https://content.edgar-online.com/ExternalLink/EDGAR/0001559720-24-000032.html?hash=a643e8dabffb3836e06f49b2a4a9b345a8db1f7d9ac322bececde9bc6fbf2818&dest=exh101eleventhamendment-ex_htm>; Airbnb, Inc. (Form: 10-Q, Received: 08/06/2024 16:11:04) <https://content.edgar-online.com/ExternalLink/EDGAR/0001559720-24-000024.html?hash=54847390365eef7f589b106218c8b09ff9bf5be46e968ce19f94e5ad9747f4ef&dest=exh101airbnb-elinormertzpr_htm>; Q3 2024 Shareholder Letter <https://s26.q4cdn.com/656283129/files/doc_financials/2024/q3/Airbnb_Q3-2024-Shareholder-Letter_Final.pdf>
- web_search(query="Airbnb fourth quarter full year 2024 results adjusted EBITDA reconciliation table stock-based compensation") → 10 results: Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/abnb-20240930.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000024/abnb-20240630.htm>

### Turn 2  (stop_reason=tool_use)
- submit_final_result({"final_result": "Airbnb's adjustment for stock-based compensation expense in fiscal 2024 was $1,407 million.\n\nSource and basis: This figure comes from a search excerpt of the FY2024 Form 10-K, not from an opened copy of the filing. The Adjusted EBITDA reconciliation table is presented in millions, with 2023 and 2024 columns. Net income was $4,792 million (2023) and $2,648 million (2024). The stock-based compensation expense line reads 1,120 (2023) and 1,407 (2024). The 2024 figure is therefore $1,407 million.\n\nCross-checks:\n- The prior-year 10-K (FY2023) shows stock-based compensation expense of 1,120 for 2023, matching the 2023 column above.\n- The Q3 2024 Form 10-Q shows stock-based 
…[truncated 1,172 chars])

### Final answer
Airbnb's adjustment for stock-based compensation expense in fiscal 2024 was $1,407 million.

Source and basis: This figure comes from a search excerpt of the FY2024 Form 10-K, not from an opened copy of the filing. The Adjusted EBITDA reconciliation table is presented in millions, with 2023 and 2024 columns. Net income was $4,792 million (2023) and $2,648 million (2024). The stock-based compensation expense line reads 1,120 (2023) and 1,407 (2024). The 2024 figure is therefore $1,407 million.

Cross-checks:
- The prior-year 10-K (FY2023) shows stock-based compensation expense of 1,120 for 2023, matching the 2023 column above.
- The Q3 2024 Form 10-Q shows stock-based compensation expense of 1,039 for the nine months ended September 30, 2024. The implied Q4 2024 amount is about 368 (1,407 minus 1,039), which is plausible.

Note: This is the add-back line in the non-GAAP Adjusted EBITDA reconciliation. It is not separately verified against the stock-based compensation note in the FY2024 10-K, since I did not open that section of the filing.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. - Form 10-K - FY2024"
        },
        {
            "url": "https://content.edgar-online.com/ExternalLink/EDGAR/0001559720-24-000006.html?hash=8fb59a79794331d61fbddd144f54c3e63f372875378160b08c84a6274e949294&dest=exh1011sfo_888brannanxgrou_htm",
            "name": "Airbnb, Inc. (Form: 10-K, Received: 02/16/2024) - FY2023 Adjusted EBITDA reconciliation"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/abnb-20240930.htm",
            "name": "Airbnb, Inc. - Form 10-Q - FY2024 (Q3)"
        }
    ]
}