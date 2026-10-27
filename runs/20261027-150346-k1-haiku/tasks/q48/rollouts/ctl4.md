## Rollout `ctl4`
- outcome: submitted
- turns: 2; cost: $0.048; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Lemonade fourth quarter 2024 results full year guidance") → 10 results: Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000019/lmndq42023shlfinal.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000054/shareholderletterq12024f.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000100/lmndshlq22024final.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm>; Lemonade reports first full year of positive free cash flow in 2024 <https://www.insurancebusinessmag.com/us/news/breaking-news/lemonade-reports-first-full-year-of-positive-free-cash-flow-in-2024-526549.aspx>
- web_search(query="Lemonade third quarter 2024 results full year 2024 guidance raised") → 10 results: Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000100/lmndshlq22024final.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000019/lmndq42023shlfinal.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000054/shareholderletterq12024f.htm>; Shareholder Letter Q3 2024 <https://www.lemonade.com/investor-relations-bo/wp-content/uploads/2025/04/LMND-Q3-2024-SHL-Final-10-30-24.pdf>
- web_search(query="Lemonade full year 2024 revenue gross earned premium results February 2025") → 0 results: 
- parse_html_page({"url": "https://www.lemonade.com/investor-relations-bo/wp-content/uploads/2025/04/LMND-Shareholder-Letter-Q4-2024.pdf", "key": "lmnd_q4"})
  ERROR: ValueError: The URL points to a PDF, which this tool cannot parse. Find an HTML version.

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Lemonade, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1691421/000169142125000146/lmndshareholderletterq32.htm>; Lemonade, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1691421/000169142125000062/lmndshareholderletterq12.htm>; Lemonade, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1691421/000169142125000120/lmndshareholderletterq22.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000019/lmndq42023shlfinal.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm>
- web_search(query="Lemonade second quarter 2024 revenue gross earned premium results") → 9 results: Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000100/lmndshlq22024final.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000019/lmndq42023shlfinal.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000054/shareholderletterq12024f.htm>; Shareholder Letter Q2 2024 <https://www.lemonade.com/investor-relations-bo/wp-content/uploads/2025/04/Shareholder-Letter-Q2-2024-FINAL-7-30-24-3-30PM.pdf>
- submit_final_result({"final_result": "**Short answer:** Lemonade's FY2024 results met or beat the full-year guidance it set in its Q3 2024 shareholder letter (October 30, 2024). In-force premium landed at the top of the range, gross earned premium and revenue came in slightly above the top of their ranges, and the Adjusted EBITDA loss was slightly smaller than the best case in the range.\n\n**Prior guidance (Q3 2024 letter, Oct 2024)**\nLemonade said it was <cite index=\"32-6\">increasing full year guidance for gross earned premium and revenue, and reaffirming guidance for FY 2024 for all other metrics.</cite> The full-year ranges were: in-force premium (IFP) $940–$944M, gross earned premium (GEP) $823–$826M, r
…[truncated 4,178 chars])

### Final answer
**Short answer:** Lemonade's FY2024 results met or beat the full-year guidance it set in its Q3 2024 shareholder letter (October 30, 2024). In-force premium landed at the top of the range, gross earned premium and revenue came in slightly above the top of their ranges, and the Adjusted EBITDA loss was slightly smaller than the best case in the range.

**Prior guidance (Q3 2024 letter, Oct 2024)**
Lemonade said it was <cite index="32-6">increasing full year guidance for gross earned premium and revenue, and reaffirming guidance for FY 2024 for all other metrics.</cite> The full-year ranges were: in-force premium (IFP) $940–$944M, gross earned premium (GEP) $823–$826M, revenue $522–$524M, and Adjusted EBITDA loss of ($155)–($151)M (<cite index="32-7">Q4 2024 Full Year 2024 Low - High ... In Force Premium (IFP) $940 $944 $940 $944 Gross Earned Premium (GEP) $222 $225 $823 $826 Revenue $144 $146 $522 $524 Adjusted EBITDA Loss ($29) ($25) ($155) ($151)</cite>).

**Actual FY2024 results**
- **IFP:** <cite index="9-19,9-20">Lemonade ended 2024 with IFP of $944 million, representing 26% year on year growth, and an Adj. EBITDA loss of ($150) million, 13% year on year improvement.</cite> This is at the top of the $940–$944M range.
- **Gross earned premium:** Summing the four 2024 quarters (Q1 $187.9M per the <cite index="28-6">Q1 2024 key metrics table</cite>; Q2 $199.9M per <cite index="31-5">the second quarter gross earned premium of $199.9 million</cite>; Q3 $213.1M per <cite index="32-1">Third quarter gross earned premium of $213.1 million</cite>; Q4 $226.4M per <cite index="27-3">Fourth quarter gross earned premium of $226.4 million</cite>) gives $827.3M. That is $1.3M (0.16%) above the $826M top of the range, and $2.8M (0.34%) above the $824.5M midpoint.
- **Revenue:** Summing the quarters (Q1 $119.1M per <cite index="28-1">First quarter revenue of $119.1 million</cite>; Q2 $122.0M per <cite index="31-6">Second quarter revenue of $122.0 million</cite>; Q3 $136.6M per <cite index="32-2">Third quarter revenue of $136.6 million</cite>; Q4 $148.8M per <cite index="27-4">Fourth quarter revenue of $148.8 million</cite>) gives $526.5M. The proxy statement independently reports <cite index="38-1">total revenue increased $96.7 million, or 22% to $526.5 million</cite>. This is $2.5M (0.48%) above the $524M top of the range, and $3.5M (0.67%) above the $523M midpoint.
- **Adjusted EBITDA:** The reported loss of ($150)M is $1M smaller than the ($151)M best case in the guidance range, a 0.66% improvement on the top end.

**Context**
Lemonade had originally guided in February 2024 to <cite index="13-1">Revenue of $505 - $510 million</cite> for FY2024, so the October raise was followed by a further beat. Its own commentary said it had <cite index="9-19">delivered on that guidance with notable precision</cite>.

**Caveat:** The GEP and revenue totals are my sums of the reported quarterly figures. They match the $526.5M revenue total in the proxy statement. The $827.3M GEP total matches the quarterly sum but I did not find a separate full-year source for it in the pre-April 2025 materials.

**Sources:**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm",
            "name": "Lemonade Q3 2024 Shareholder Letter (8-K, Oct 30, 2024)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142125000021/lmndshareholderletterq42.htm",
            "name": "Lemonade Q4 2024 Shareholder Letter (8-K, Feb 2025)"
        },
        {
            "url": "https://www.marketscreener.com/quote/stock/LEMONADE-INC-109161819/news/Lemonade-Q4-2024-Earnings-Conference-Call-Letter-to-Shareholders-49159411/",
            "name": "Lemonade Q4 2024 Earnings Conference Call Letter to Shareholders (MarketScreener)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142125000057/lmnd-20250423.htm",
            "name": "Lemonade DEF 14A proxy statement (FY2024 revenue)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142124000054/shareholderletterq12024f.htm",
            "name": "Lemonade Q1 2024 Shareholder Letter (8-K)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142124000100/lmndshlq22024final.htm",
            "name": "Lemonade Q2 2024 Shareholder Letter (8-K)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142124000019/lmndq42023shlfinal.htm",
            "name": "Lemonade Q4 2023 Shareholder Letter with initial FY2024 guidance (8-K, Feb 2024)"
        }
    ]
}