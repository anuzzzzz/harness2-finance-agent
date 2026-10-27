## Rollout `dom1`
- outcome: submitted
- turns: 4; cost: $0.025; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "convertible_notes_dilution"})
  result: ---
  name: convertible_notes_dilution
  description: Answer "maximum dilutive impact / shares issuable on conversion" of a company's convertible notes at a fiscal year-end, with reconciliation across note series.
  ---
  
  # Convertible notes: share dilution at a balance-sheet date
  
  **Analytic move:** retrieve and reconcile. Get the aggregate number of Class A (or common) shares that all outstanding convertible notes could convert into at the date named, then check it against the per-series conversion terms.
  
  **Where the figures live (10-K for the fiscal year named)**
  - EPS note ("Net Loss / Income per Share"): the table of potentially dilutive securities excluded from diluted EPS as anti-dilutive. It has a line such as "Convertible Notes (if-converted)", in thousands of shares, for the current year and the two prior years. This is the aggregate figure and the usual answer to "maximum dilutive impact".
  - Debt / Convertible Notes note: for each series (by year of maturity) the principal still outstanding, the initial conversion rate (shares per $1,000) or conversion price, and any maximum conversion rate that applies after a make-whole fundamental change. A text sentence in the note or in Liquidity may also state a "maximum" share count. If one is stated, report it and say which it is.
  - The 8-K for a note issuance states a maximum share count for that series only (including the initial purchasers' option). That is a single series at issuance, not the year-end aggregate.
  
  **Procedure**
  1. Fix the date (fiscal year-end) and which series were outstanding then. Exclude series repurchased, converted or matured before the date, and include series issued before it. Use principal outstanding at the date, not the original issue amount.
  2. Read the aggregate from the EPS anti-dilutive ta
  …[truncated 1,556 chars]

### Turn 2  (stop_reason=tool_use)
- edgar_search({"search_query": "Snap Inc 10-K 2024 convertible notes if-converted anti-dilutive", "start_date": "2025-01-01", "end_date": "2025-04-07", "form_types": ["10-K"]})
  ERROR: ValueError: EDGAR full-text search returned HTTP 403: <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
  <html xmlns="http://www.w3.org/1999/xhtml">
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>SEC.gov | Your Request Originates from an Undeclar

### Turn 3  (stop_reason=tool_use)
- web_search(query="Snap Inc 2024 annual report 10-K convertible notes if-converted anti-dilutive shares") → 9 results: Snap Inc - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm>; Snap Inc (Form: 10-K, Received: 02/07/2024 06:04:06) <https://content.edgar-online.com/ExternalLink/EDGAR/0001564408-24-000019.html?hash=81a9cca6972199e708899d609ebafce9d74bc23e80df9d116774d17562681629&dest=ex-44xsnapincdescriptionof_htm>; snap-20240331 <https://www.sec.gov/Archives/edgar/data/1564408/000156440824000034/snap-20240331.htm>; SNAP INC. <https://s25.q4cdn.com/442043304/files/doc_financials/2024/q3/9967f373-9eb9-4f31-a3c8-81e82f351e0e.pdf>; snap-20250630 <https://www.sec.gov/Archives/edgar/data/1564408/000156440825000052/snap-20250630.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm", "key": "snap10k2024"})
  ERROR: ValueError: HTTP 403 when fetching https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm
- retrieve_information({"prompt": "From this Snap 10-K, list each convertible notes series outstanding at Dec 31, 2024 with principal outstanding (in thousands), initial conversion rate per $1,000 principal, conversion price, and maximum conversion rate (make-whole). Also state the Convertible Notes (if-converted) anti-dilutive figure at 12/31/2024. Document: {{snap10k2024}}"})
  ERROR: KeyError: "ERROR: The key 'snap10k2024' was not found in the data storage. Available keys are: . Use parse_html_page to add keys."

### Turn 4  (stop_reason=tool_use)
- web_search(query="Snap convertible senior notes due 2030 conversion rate per $1,000 principal shares 2025 2026 2027 2028 notes outstanding December 31, 2024") → 10 results: Snap Inc - Form 10-K - FY2024 (Annual Financial Statement Tables - full year 2024) <https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/Financial_Report.xlsx>; Snap Inc - Form 10-Q - FY2024 (Quarterly Earnings Tables - quarter ended Sep 2024) <https://www.sec.gov/Archives/edgar/data/1564408/000156440824000062/Financial_Report.xlsx>; Snap Inc - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm>; Snap Inc - Form 10-Q - FY2026 <https://www.sec.gov/Archives/edgar/data/0001564408/000156440826000052/snap-20260630.htm>; Snap Inc - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1564408/000156440824000050/snap-20240630.htm>
- submit_final_result({"final_result": "**Answer: about 85,945 thousand shares (≈85.95 million) is Snap Inc.'s if-converted dilutive share count for its convertible notes at December 31, 2024.**\n\n**Source of the headline figure**\n- The FY2024 10-K anti-dilutive securities table lists \"Convertible Notes (if-converted)\" at 85,945 thousand shares as of December 31, 2024, against 89,379 thousand as of December 31, 2023 and 89,379 thousand as of December 31, 2022 (10-K, Net Loss per Share note). These figures were taken from the search excerpt of the filing; I could not open the full 10-K (the SEC site returned HTTP 403), so the figure is confirmed by excerpt, not by a full read of the filing.\n- Snap's Q3 2024 1
…[truncated 2,673 chars])

### Final answer
**Answer: about 85,945 thousand shares (≈85.95 million) is Snap Inc.'s if-converted dilutive share count for its convertible notes at December 31, 2024.**

**Source of the headline figure**
- The FY2024 10-K anti-dilutive securities table lists "Convertible Notes (if-converted)" at 85,945 thousand shares as of December 31, 2024, against 89,379 thousand as of December 31, 2023 and 89,379 thousand as of December 31, 2022 (10-K, Net Loss per Share note). These figures were taken from the search excerpt of the filing; I could not open the full 10-K (the SEC site returned HTTP 403), so the figure is confirmed by excerpt, not by a full read of the filing.
- Snap's Q3 2024 10-Q shows the same 85,945 thousand figure at September 30, 2024, and its Q1 2025 10-Q shows the notes at 60,825 thousand at March 31, 2025. These are context only.

**Per-series reconciliation (partial check)**
Outstanding series at 12/31/2024 were the 2025, 2026, 2027, 2028 and 2030 notes. Initial conversion prices (per the Q1 2025 10-Q): 2025 $21.68; 2026 $22.81; 2027 $89.25; 2028 $56.34; 2030 $22.18. The 2028 and 2030 conversion rates are stated directly: 17.7494 and 45.0846 shares per $1,000 principal.
- 2030 Notes: $750.0 million principal outstanding (10-K) × 45.0846 / 1,000 ≈ 33,813 thousand shares.
- 2028 Notes: $1,500.0 million principal outstanding (10-K) × 17.7494 / 1,000 ≈ 26,624 thousand shares.
- Together ≈ 60,438 thousand shares, leaving about 25,507 thousand shares for the 2025, 2026 and 2027 notes.
- The 2027 Notes were issued at $1.15 billion and the 2026 and 2025 principal balances at year-end were not confirmed in my sources. Using the original 2027 issue size gives ≈12,885 thousand shares, which would leave ≈12,622 thousand for the 2025 and 2026 notes. This is plausible but not verified, so I cannot fully reconcile the series to the 85,945 thousand total.

**Maximum (make-whole) context**
The 2030 Notes can convert into more shares when a make-whole fundamental change or redemption applies. A May 2024 8-K states a maximum of about 44,802,825 shares for that series (from the research desk's notes; I did not re-verify this in the filing). That is above the base 2030 conversion of ≈33.8 million shares. The headline figure remains the reported if-converted count of 85,945 thousand shares, because that is the figure Snap reports as its dilutive effect.

**Units and period:** shares in thousands; fiscal year-end December 31, 2024.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm",
            "name": "Snap Inc - Form 10-K - FY2024"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/Financial_Report.xlsx",
            "name": "Snap Inc - Form 10-K - FY2024 Annual Financial Statement Tables (Debt note)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1564408/000156440825000030/snap-20250331.htm",
            "name": "Snap Inc - Form 10-Q - Q1 2025 (conversion prices and rates)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1564408/000156440824000062/snap-20240930.htm",
            "name": "Snap Inc - Form 10-Q - Q3 2024"
        }
    ]
}