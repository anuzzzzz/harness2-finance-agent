## Rollout `static1`
- outcome: submitted
- turns: 4; cost: $0.084; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "3D Systems director compensation 2023 table", "ciks": ["DDD"], "start_date": "2024-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 8, "page": 1, "results": [{"form": "10-K", "file_date": "2024-08-13", "period_ending": "2023-12-31", "company": "3D SYSTEMS CORP  (DDD)  (CIK 0000910638)", "ciks": ["0000910638"], "accession": "0000910638-24-000030", "document": "ddd-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/910638/000091063824000030/ddd-20231231.htm"}, {"form": "DEF 14A", "file_date": "2025-04-04", "period_ending": "2025-05-16", "company": "3D SYSTEMS CORP  (DDD)  (CIK 0000910638)", "ciks": ["0000910638"], "accession": "0001193125-25-073438", "document": "d867556ddef14a.htm", "description": "DEF 14A", "url": "https://www.sec.gov/Archives/edgar/data/910638/000119312525073438/d867556ddef14a.htm"}, {"form": "ARS", "file_date": "2025-04-04", "period_ending": "2024-12-31", "company": "3D SYSTEMS CORP  (DDD)  (CIK 0000910638)", "ciks": ["0000910638"], "accession": "0001193125-25-073455", "document": "d873024dars.pdf", "description": "ARS", "url": "https://www.sec.gov/Archives/edgar/data/910638/000119312525073455/d873024dars.pdf"}, {"form": "10-K", "file_date": "2025-03-27", "period_ending": "2024-12-31", "company": "3D SYSTEMS CORP  (DDD)  (CIK 0000910638)", "ciks": ["0000910638"], "accession": "0000910638-25-000005", "document": "ddd-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/910638/000091063825000005/ddd-20241231.htm"}, {"form": "10-Q", "file_date": "2024-08-20", "period_ending": "2024-03-31", "company": "3D SYSTEMS CORP  (DDD)  (CIK 0000910638)", "ciks": ["0000910638"], "accession": "0000910638-24-000035", "document": "ddd-20240331.htm", "description": "10-Q", "url": "https://www.sec.gov/Archives/edgar/data/910638/000091063824000035/ddd-20240331.htm"}, {"form": "DEF 14A", "file_date": "2024-
  …[truncated 991 chars]
- edgar_search({"search_query": "3D Systems proxy statement director compensation fiscal 2023", "form_types": ["DEF 14A"], "start_date": "2024-01-01"})
  result: {"total_matching_documents": 208, "page": 1, "results": [{"form": "DEF 14A", "file_date": "2025-04-04", "period_ending": "2025-05-16", "company": "3D SYSTEMS CORP  (DDD)  (CIK 0000910638)", "ciks": ["0000910638"], "accession": "0001193125-25-073438", "document": "d867556ddef14a.htm", "description": "DEF 14A", "url": "https://www.sec.gov/Archives/edgar/data/910638/000119312525073438/d867556ddef14a.htm"}, {"form": "DEF 14A", "file_date": "2024-08-13", "period_ending": "2024-08-30", "company": "3D SYSTEMS CORP  (DDD)  (CIK 0000910638)", "ciks": ["0000910638"], "accession": "0001193125-24-199863", "document": "d914592ddef14a.htm", "description": "DEF 14A", "url": "https://www.sec.gov/Archives/edgar/data/910638/000119312524199863/d914592ddef14a.htm"}, {"form": "DEF 14A", "file_date": "2025-04-02", "period_ending": "2025-05-16", "company": "FLOWSERVE CORP  (FLS)  (CIK 0000030625)", "ciks": ["0000030625"], "accession": "0001308179-25-000353", "document": "fls013554-def14a.htm", "description": "DEFINITIVE PROXY STATEMENT", "url": "https://www.sec.gov/Archives/edgar/data/30625/000130817925000353/fls013554-def14a.htm"}, {"form": "DEF 14A", "file_date": "2025-04-02", "period_ending": "2025-05-16", "company": "FLOWSERVE CORP  (FLS)  (CIK 0000030625)", "ciks": ["0000030625"], "accession": "0001308179-25-000353", "document": "fls_courtesy-pdf.pdf", "description": "DEFINITIVE PROXY STATEMENT", "url": "https://www.sec.gov/Archives/edgar/data/30625/000130817925000353/fls_courtesy-pdf.pdf"}, {"form": "DEF 14A", "file_date": "2024-04-02", "period_ending": "2024-05-16", "company": "FLOWSERVE CORP  (FLS)  (CIK 0000030625)", "ciks": ["0000030625"], "accession": "0001308179-24-000421", "document": "fls4266791-def14a.htm", "description": "FLOWSERVE CORP - DEF 14A", "url": "https://www.sec.gov/
  …[truncated 5,452 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/910638/000119312524199863/d914592ddef14a.htm", "key": "proxy2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: proxy2024. (355,532 characters)
  The data_storage currently contains the following keys:
  proxy2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this proxy statement, find the Director Compensation table for fiscal year 2023 (Name, Fees Earned or Paid in Cash, Stock Awards, Option Awards, All Other Compensation, Total for each director), and the total of all directors' 2023 compensation. Also state any footnotes on the basis. Document: {{proxy2024}}"})
  result: ## Director Compensation for 2023
  
  | Name | Fees Earned or Paid in Cash ($) | Stock Awards ($)⁽¹⁾ | Option Awards ($) | All Other Compensation ($) | Total ($) |
  |---|---|---|---|---|---|
  | Malissia R. Clinton | 90,000 | 150,000 | — | — | 240,000 |
  | William E. Curran | 105,000 | 150,000 | — | — | 255,000 |
  | Claudia N. Drayton | 68,113 | 150,000 | — | — | 218,113 |
  | Thomas W. Erickson | 78,764 | 150,000 | — | — | 228,764 |
  | Jim D. Kever | 70,000 | 150,000 | — | — | 220,000 |
  | Charles G. McClure, Jr. | 250,000 | 150,000 | — | — | 400,000 |
  | Kevin S. Moore | 95,000 | 150,000 | — | — | 245,000 |
  | Vasant Padmanabhan | 66,236 | 150,000 | — | — | 216,236 |
  | John J. Tracy | 90,000 | 150,000 | — | — | 240,000 |
  | **Total** | **913,113** | **1,350,000** | **—** | **—** | **2,263,113** |
  
  The proxy statement's table does not include an Option Awards column. No director received option awards in 2023, so the column is shown as "—" here.
  
  ## Total Director Compensation for 2023
  
  The total of all non-employee directors' 2023 compensation is **$2,263,113**.
  
  ## Footnotes and Basis
  
  - **Stock Awards (footnote 1):** Amounts represent the aggregate grant date fair value of stock awards computed under FASB ASC Topic 718. Each director in office received 18,094 shares of Common Stock on May 16, 2023, as an annual equity award under the 2015 Incentive Plan. Shares were valued at the closing price on the grant date of $8.29 per share, giving $150,000 per director. Under the Non-Employee Director Compensation Policy, these shares are fully vested when issued.
  - **Dr. Graves:** As an employee, Dr. Graves received no additional compensation for his service as a director in 2023, so he is excluded from the table.
  - **Board Chair fee:** Mr. McClure's $250,000 fee reflects the Board Chair r
  …[truncated 631 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: $2,263,113 total director compensation paid to 3D Systems' non-employee directors for fiscal 2023.**\n\n**Source and basis**\n- The 2023 figures appear in 3D Systems' proxy statement (DEF 14A) filed August 13, 2024, which reports the \"Director Compensation for 2023\" table. The filing was late because of the company's delayed 2023 10-K (filed the same day, August 13, 2024).\n- Dr. Graves (an employee) received no additional compensation for board service, so he is excluded from the table.\n- Stock awards: each director in office received 18,094 shares on May 16, 2023, valued at $8.29 per share, or $150,000 per director (grant-date fair value under ASC 718). These
…[truncated 1,866 chars])

### Final answer
**Answer: $2,263,113 total director compensation paid to 3D Systems' non-employee directors for fiscal 2023.**

**Source and basis**
- The 2023 figures appear in 3D Systems' proxy statement (DEF 14A) filed August 13, 2024, which reports the "Director Compensation for 2023" table. The filing was late because of the company's delayed 2023 10-K (filed the same day, August 13, 2024).
- Dr. Graves (an employee) received no additional compensation for board service, so he is excluded from the table.
- Stock awards: each director in office received 18,094 shares on May 16, 2023, valued at $8.29 per share, or $150,000 per director (grant-date fair value under ASC 718). These shares are fully vested when issued.
- Cash fees reflect the Non-Employee Director Compensation Policy retainers. Mr. McClure's $250,000 reflects the Board Chair retainer.
- No director received option awards or all-other compensation in 2023.

**Director-by-director (USD)**

| Director | Cash fees | Stock awards | Total |
|---|---|---|---|
| Malissia R. Clinton | 90,000 | 150,000 | 240,000 |
| William E. Curran | 105,000 | 150,000 | 255,000 |
| Claudia N. Drayton | 68,113 | 150,000 | 218,113 |
| Thomas W. Erickson | 78,764 | 150,000 | 228,764 |
| Jim D. Kever | 70,000 | 150,000 | 220,000 |
| Charles G. McClure, Jr. | 250,000 | 150,000 | 400,000 |
| Kevin S. Moore | 95,000 | 150,000 | 245,000 |
| Vasant Padmanabhan | 66,236 | 150,000 | 216,236 |
| John J. Tracy | 90,000 | 150,000 | 240,000 |

**Calculation check**
- Cash fees: 90,000 + 105,000 + 68,113 + 78,764 + 70,000 + 250,000 + 95,000 + 66,236 + 90,000 = 913,113
- Stock awards: 9 × 150,000 = 1,350,000
- Total: 913,113 + 1,350,000 = 2,263,113

**Caveat:** I read the table through an automated extraction of the proxy text, not by visually checking the original page. The row totals and the column sums reconcile, so I am confident in the figure. The 2023 total is also the figure for the fiscal year asked about; the later 2025 proxy covers 2024 compensation and should not be used here.

**Sources**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/910638/000119312524199863/d914592ddef14a.htm",
            "name": "3D Systems DEF 14A proxy statement (filed 2024-08-13)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/910638/000091063824000030/ddd-20231231.htm",
            "name": "3D Systems Form 10-K for fiscal year 2023 (filed 2024-08-13)"
        }
    ]
}