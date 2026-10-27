## Rollout `ctl2`
- outcome: submitted
- turns: 3; cost: $0.025; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Airbnb reconciliation net income to adjusted EBITDA shareholder letter") → 0 results: 
- edgar_search({"search_query": "Airbnb Adjusted EBITDA reconciliation net income", "ciks": ["ABNB"], "top_n_results": 5})
  result: {"total_matching_documents": 45, "page": 1, "results": [{"form": "8-K", "file_date": "2022-02-15", "period_ending": "2022-02-15", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-22-043371", "document": "d251410dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312522043371/d251410dex991.htm"}, {"form": "8-K", "file_date": "2022-11-01", "period_ending": "2022-11-01", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-22-274904", "document": "d408297dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312522274904/d408297dex991.htm"}, {"form": "8-K", "file_date": "2023-05-09", "period_ending": "2023-05-09", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-23-139392", "document": "d453262dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312523139392/d453262dex991.htm"}, {"form": "8-K", "file_date": "2024-08-06", "period_ending": "2024-08-06", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-194849", "document": "d831385dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm"}, {"form": "8-K", "file_date": "2022-05-03", "period_ending": "2022-05-03", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-22-138654", "document": "d711122dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312522138654/d711122dex991.htm"}]}

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 9 results: Airbnb Q2 2026 Shareholder Letter <https://s26.q4cdn.com/656283129/files/doc_financials/2026/q2/v2/Airbnb-Q2-2026-Shareholder-Letter.pdf>; Airbnb Q1 2026 Shareholder Letter <https://s26.q4cdn.com/656283129/files/doc_financials/2026/q1/Airbnb_Q1-2026-Shareholder-Letter.pdf>; Q2 2024 Shareholder Letter <https://s26.q4cdn.com/656283129/files/doc_financials/2024/q2/Airbnb_Q2-2024-Shareholder-Letter_Final.pdf>; Q3 2024 Shareholder Letter <https://s26.q4cdn.com/656283129/files/doc_financials/2024/q3/Airbnb_Q3-2024-Shareholder-Letter_Final.pdf>; Q1 2023 Shareholder Letter <https://s26.q4cdn.com/656283129/files/doc_financials/2023/q1/Airbnb_Q1-2023-Shareholder-Letter_Final.pdf>
- parse_html_page({"url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/Airbnb_Q4-2024-Shareholder-Letter_Final.pdf", "key": "abnb_q4_2024"})
  ERROR: ValueError: The URL points to a PDF, which this tool cannot parse. Find an HTML version.

### Turn 3  (stop_reason=tool_use)
- web_search(query="Airbnb Adjusted EBITDA is defined as net income adjusted for provision for income taxes, other income, depreciation, amortization, stock-based compensation") → 10 results: Airbnb files to go public <https://techcrunch.com/2020/11/16/airbnb-files-to-go-public/>; Airbnb, Inc. - Form DRS - FY2020 <https://www.sec.gov/Archives/edgar/data/1559720/000095012320009252/filename1.htm>; Airbnb, Inc. - Form DRS/A - FY2020 <https://www.sec.gov/Archives/edgar/data/1559720/000095012320010021/filename1.htm>; Airbnb 8K Results of Operations and Financial Condition <https://capedge.com/filing/1559720/0001193125-24-033706/8-K/file/2>; Airbnb, Inc. - Form S-1 - FY2020 <https://www.sec.gov/Archives/edgar/data/1559720/000119312520294801/d81668ds1.htm>
- submit_final_result({"final_result": "Airbnb starts its Adjusted EBITDA reconciliation from GAAP net income (loss) and adds back or removes a set of items. As of April 7, 2025, the most recent definition I could confirm is the one in its Q3 2024 shareholder letter, which I cross-checked against earlier SEC filings.\n\n**Adjustments (from the most recent definition I could confirm, Q3 2024 letter, with the list in earlier filings):**\n\n1. **Income taxes:** Airbnb removes the provision for (benefit from) income taxes. The Q3 2024 letter's definition starts with <cite index=\"18-4\">provision for (benefit from) income taxes</cite>.\n2. **Other income/expense and interest income:** Airbnb removes <cite index=\"18-
…[truncated 3,966 chars])

### Final answer
Airbnb starts its Adjusted EBITDA reconciliation from GAAP net income (loss) and adds back or removes a set of items. As of April 7, 2025, the most recent definition I could confirm is the one in its Q3 2024 shareholder letter, which I cross-checked against earlier SEC filings.

**Adjustments (from the most recent definition I could confirm, Q3 2024 letter, with the list in earlier filings):**

1. **Income taxes:** Airbnb removes the provision for (benefit from) income taxes. The Q3 2024 letter's definition starts with <cite index="18-4">provision for (benefit from) income taxes</cite>.
2. **Other income/expense and interest income:** Airbnb removes <cite index="18-4">other income (expense), net, and interest income</cite>. The company explains that <cite index="18-4">Adjusted EBITDA does not reflect interest income and other income (expense), net, which include unrealized and realized gains and losses on foreign currency exchange, investments, and financial instruments</cite>. Its 2022 filings also listed interest expense as a separate item in this group (<cite index="16-5">interest income, interest expense, and other income (expense), net</cite>).
3. **Depreciation and amortization:** Airbnb removes <cite index="16-5">depreciation and amortization</cite>.
4. **Stock-based compensation:** Airbnb removes <cite index="18-4">stock-based compensation expense</cite>. It notes that this is <cite index="18-4">a significant recurring expense in our business</cite>, which is why it is a material exclusion.
5. **Acquisition-related impacts:** Airbnb removes <cite index="16-5">acquisition-related impacts consisting of gains (losses) recognized on changes in the fair value of contingent consideration arrangements</cite>.
6. **Lodging tax reserve changes:** Airbnb removes <cite index="16-5">net changes to the reserves for lodging taxes for which management believes it is probable that we may be held jointly liable with Hosts for collecting and remitting such taxes</cite>.
7. **Restructuring charges:** Airbnb removes restructuring charges, as listed in its 2022 definition (<cite index="16-5">and (vii) restructuring charges</cite>). The Q3 2024 excerpt I could access cut off before items (vi) and (vii), so I could not confirm this item in the latest letter itself.

**Earlier items:** Filings from 2021 and 2022 also excluded <cite index="15-2">stock-settlement obligations related to the IPO</cite>, meaning employer taxes tied to the IPO. This item does not appear in the Q3 2024 excerpt, so it may have been dropped.

**Rationale:** Airbnb says the excluded items are <cite index="16-6">non-cash in nature, or because the amount and timing of these items is unpredictable, not driven by core results of operations</cite>.

**Caveats:** Search results also included shareholder letters dated after April 7, 2025. I disregarded those because they postdate the question's date. The Q4 2024 letter (published around February 2025) is the most recent full reconciliation I could not parse, since the PDF could not be read by the tool. Its definition may differ slightly from the Q3 2024 wording above.

**Sources:**
- Q3 2024 Shareholder Letter (Airbnb): https://s26.q4cdn.com/656283129/files/doc_financials/2024/q3/Airbnb_Q3-2024-Shareholder-Letter_Final.pdf
- Airbnb 8-K (2022 results, FY2022 definition): https://www.sec.gov/Archives/edgar/data/1559720/000119312522210001/d353427dex991.htm
- Airbnb 8-K (FY2021 definition): https://www.sec.gov/Archives/edgar/data/1559720/000119312521160458/d476842dex991.htm
- Q4 2024 Shareholder Letter (Airbnb, referenced but not parsed): https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/Airbnb_Q4-2024-Shareholder-Letter_Final.pdf

{
    "sources": [
        {
            "url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q3/Airbnb_Q3-2024-Shareholder-Letter_Final.pdf",
            "name": "Airbnb Q3 2024 Shareholder Letter"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312522210001/d353427dex991.htm",
            "name": "Airbnb Form 8-K FY2022 (Adjusted EBITDA definition)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312521160458/d476842dex991.htm",
            "name": "Airbnb Form 8-K FY2021 (Adjusted EBITDA definition)"
        },
        {
            "url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/Airbnb_Q4-2024-Shareholder-Letter_Final.pdf",
            "name": "Airbnb Q4 2024 Shareholder Letter"
        }
    ]
}