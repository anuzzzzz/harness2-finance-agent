## Rollout `ctl3`
- outcome: submitted
- turns: 3; cost: $0.093; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Airbnb shares of Class A common stock outstanding", "ciks": ["ABNB"], "start_date": "2025-01-01", "top_n_results": 5})
  result: {"total_matching_documents": 10, "page": 1, "results": [{"form": "S-8", "file_date": "2025-02-13", "period_ending": null, "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-25-026162", "document": "d869144dexfilingfees.htm", "description": "EX-FILING FEES", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026162/d869144dexfilingfees.htm"}, {"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}, {"form": "8-K", "file_date": "2025-02-13", "period_ending": "2025-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-25-026054", "document": "d915198dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm"}, {"form": "SCHEDULE 13G/A", "file_date": "2025-02-13", "period_ending": null, "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720", "0001834147"], "accession": "0000950170-25-020202", "document": "primary_doc.xml", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1559720/000095017025020202/primary_doc.xml"}, {"form": "SCHEDULE 13G/A", "file_date": "2025-02-13", "period_ending": null, "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720", "0001834152"], "accession": "0000950170-25-020207", "document": "primary_doc.xml", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1559720/000095017025020207/primary_doc.xml"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb10k. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb10k
  
- retrieve_information({"prompt": "From this 10-K document, what are the number of shares of Class A, Class B, and any other class of common stock outstanding as stated on the cover page (as of the latest date given)? Quote the exact sentence. {{abnb10k}}"})
  result: The cover page states:
  
  "As of January 31, 2025, 432,876,657 shares of the registrant's Class A common stock were outstanding, 188,462,942 shares of the registrant's Class B common stock were outstanding, no shares of the registrant's Class C common stock were outstanding, and 9,200,000 shares of the registrant's Class H common stock were outstanding."
  
  So, as of January 31, 2025:
  - **Class A:** 432,876,657 shares
  - **Class B:** 188,462,942 shares
  - **Class C:** 0 shares
  - **Class H:** 9,200,000 shares

### Turn 3  (stop_reason=tool_use)
Airbnb's most recent share count available as of April 7, 2025 is on the cover page of its 10-K for fiscal 2024, filed February 13, 2025. The cover page gives counts as of January 31, 2025.

Class A: 432,876,657 shares
Class B: 188,462,942 shares
Class H: 9,200,000 shares

The cover page also reports no Class C shares outstanding. The figures come from an automated extraction of the filing, which I did not re-check line by line against the original page.
- submit_final_result({"final_result": "Class A: 432,876,657 shares\nClass B: 188,462,942 shares\nClass H: 9,200,000 shares\n\n(As of January 31, 2025, per the cover page of Airbnb's 10-K for fiscal year 2024, filed February 13, 2025. The cover page also states that no Class C common stock shares were outstanding. Figures come from an automated extraction of the filing and were not manually re-verified.)\n\n{\n    \"sources\": [\n        {\n            \"url\": \"https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm\",\n            \"name\": \"Airbnb, Inc. Form 10-K for fiscal year ended December 31, 2024\"\n        }\n    ]\n}"})

### Final answer
Class A: 432,876,657 shares
Class B: 188,462,942 shares
Class H: 9,200,000 shares

(As of January 31, 2025, per the cover page of Airbnb's 10-K for fiscal year 2024, filed February 13, 2025. The cover page also states that no Class C common stock shares were outstanding. Figures come from an automated extraction of the filing and were not manually re-verified.)

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year ended December 31, 2024"
        }
    ]
}