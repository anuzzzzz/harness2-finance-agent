## Rollout `ctl3`
- outcome: submitted
- turns: 2; cost: $0.036; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Lemonade fourth quarter 2024 results full year guidance") → 10 results: Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000019/lmndq42023shlfinal.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000054/shareholderletterq12024f.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000100/lmndshlq22024final.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm>; Lemonade reports first full year of positive free cash flow in 2024 <https://www.insurancebusinessmag.com/us/news/breaking-news/lemonade-reports-first-full-year-of-positive-free-cash-flow-in-2024-526549.aspx>
- web_search(query="Lemonade third quarter 2024 results raises full year 2024 guidance") → 9 results: Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000100/lmndshlq22024final.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000019/lmndq42023shlfinal.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000054/shareholderletterq12024f.htm>; Shareholder Letter Q3 2024 <https://www.lemonade.com/investor-relations-bo/wp-content/uploads/2025/04/LMND-Q3-2024-SHL-Final-10-30-24.pdf>
- parse_html_page({"url": "https://www.lemonade.com/investor-relations-bo/wp-content/uploads/2025/04/LMND-Shareholder-Letter-Q4-2024.pdf", "key": "q4letter"})
  ERROR: ValueError: The URL points to a PDF, which this tool cannot parse. Find an HTML version.

### Turn 2  (stop_reason=tool_use)
**Short answer:** Lemonade's FY2024 results landed at or slightly above the top of the full-year ranges it set in its Q3 2024 report (October 30, 2024). It met or beat every metric I could verify.

**The prior guidance (Q3 2024 letter)**
In that letter, 
the company increased full year guidance for gross earned premium and revenue, and reaffirmed guidance for FY 2024 for all other metrics.
 The updated FY2024 ranges were:
- In force premium (IFP): $940–$944M (
$940 $944
)
- Gross earned premium (GEP): $823–$826M
- Revenue: $522–$524M (
raised its annual revenue forecast to $522-524 million, compared to the previous estimate of $511-515 million
)
- Adjusted EBITDA loss: ($155)–($151)M

**Actual FY2024 results vs. that guidance**

| Metric | Q3 2024 FY guidance | FY2024 actual | Versus guidance |
|---|---|---|---|
| IFP (year-end) | $940–$944M | $944M | At the top of the range |
| GEP | $823–$826M | $827.3M | Above the top of the range by $1.3M |
| Revenue | $522–$524M | $526.5M | Above the top of the range by $2.5M |
| Adj. EBITDA loss | ($155)–($151)M | ($150)M | Better than the top of the range by $1M |

Sources for actuals: the Q4 2024 shareholder letter says that 
the company delivered on that guidance with notable precision, ending 2024 with IFP of $944 million, representing 26% year on year growth, and an Adj. EBITDA loss of ($150) million
. The proxy statement reports that 
total revenue increased $96.7 million, or 22% to $526.5 million
. The FY2025 Form 10-K comparativ
…[truncated 1,954 chars]
- web_search(query="Lemonade full year 2024 revenue gross earned premium results million February 2025") → 10 results: Lemonade, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1691421/000169142125000062/lmndshareholderletterq12.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000019/lmndq42023shlfinal.htm>; Lemonade, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1691421/000169142125000120/lmndshareholderletterq22.htm>; Lemonade, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1691421/000169142125000146/lmndshareholderletterq32.htm>; Lemonade, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm>
- submit_final_result({"final_result": "Lemonade's FY2024 results landed at or slightly above the top of the full-year ranges it set in its Q3 2024 report (Oct 30, 2024), and beat the guidance midpoint on every metric I could verify.\n\nPrior guidance (Q3 2024 letter, FY2024): IFP $940–$944M; GEP $823–$826M; Revenue $522–$524M; Adjusted EBITDA loss ($155)–($151)M.\n\nActuals: IFP $944M (top of range); GEP $827.3M (above top by $1.3M); Revenue $526.5M (above top by $2.5M); Adjusted EBITDA loss ($150)M (better than top by $1M).\n\nMidpoint comparison (calculated): IFP +$2M (+0.21%); GEP +$2.8M (+0.34%); Revenue +$3.5M (+0.67%); Adj. EBITDA loss $3M smaller than the ($153)M midpoint (about 1.96% better).\n\nCaveats:
…[truncated 1,182 chars])

### Final answer
Lemonade's FY2024 results landed at or slightly above the top of the full-year ranges it set in its Q3 2024 report (Oct 30, 2024), and beat the guidance midpoint on every metric I could verify.

Prior guidance (Q3 2024 letter, FY2024): IFP $940–$944M; GEP $823–$826M; Revenue $522–$524M; Adjusted EBITDA loss ($155)–($151)M.

Actuals: IFP $944M (top of range); GEP $827.3M (above top by $1.3M); Revenue $526.5M (above top by $2.5M); Adjusted EBITDA loss ($150)M (better than top by $1M).

Midpoint comparison (calculated): IFP +$2M (+0.21%); GEP +$2.8M (+0.34%); Revenue +$3.5M (+0.67%); Adj. EBITDA loss $3M smaller than the ($153)M midpoint (about 1.96% better).

Caveats: SBC (~$64M guided) and capex (~$10M guided) were not verified. 2024 comparatives in later filings may be presented on a slightly different basis.

Sources:
{"sources": [
{"url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm", "name": "Lemonade Q3 2024 Shareholder Letter (Form 8-K)"},
{"url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142125000021/lmndshareholderletterq42.htm", "name": "Lemonade Q4 2024 Shareholder Letter (Form 8-K)"},
{"url": "https://www.lemonade.com/investor-relations-bo/wp-content/uploads/2025/04/LMND-Shareholder-Letter-Q4-2024.pdf", "name": "Lemonade Shareholder Letter Q4 2024 (PDF)"},
{"url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142125000057/lmnd-20250423.htm", "name": "Lemonade DEF 14A proxy statement"},
{"url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142126000016/lmnd-20251231.htm", "name": "Lemonade FY2025 Form 10-K (2024 comparatives)"},
{"url": "https://www.calcalistech.com/ctechnews/article/byzoy4b11jx", "name": "Calcalist Tech: Lemonade shares soar after promising Q3 results"}
]}