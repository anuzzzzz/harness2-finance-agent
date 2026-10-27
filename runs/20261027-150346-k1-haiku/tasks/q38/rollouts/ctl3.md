## Rollout `ctl3`
- outcome: submitted
- turns: 1; cost: $0.035; submitted: True

### Turn 1  (stop_reason=tool_use)
**Answer: Lyft beat the midpoint of its Q4'24 margin guidance. Reported margin was 2.6% against a 2.35% midpoint, a beat of roughly 25 bps on the rounded figures, or about 29 bps on unrounded numbers.**

**1. Q3'24 guidance for Q4'24**
The guidance was given in the Q3 2024 release. 
Adjusted EBITDA of $100 million to $105 million and an Adjusted EBITDA margin (calculated as a percentage of Gross Bookings) of approximately 2.3% to 2.4%.
 The margin midpoint is (2.3% + 2.4%) / 2 = **2.35%**.

**2. Q4'24 actual results**
The Q4 2024 release reported 
Adjusted EBITDA of $112.8 million compared to $66.6 million in Q4'23. Adjusted EBITDA margin (calculated as a percentage of Gross Bookings) was 2.6% compared to 1.8% in Q4'23.


**3. Unrounded Q4'24 margin**
Q4 Gross Bookings are not reported directly, so I derived them from the year and nine-month totals:
- Full-year 2024 Gross Bookings: $16,099.4M ([Annual report](https://www.sec.gov/Archives/edgar/data/1759509/000175950925000071/lyftannualreport2024.pdf))
- Nine-month 2024 Gross Bookings: $11,820.5M ([Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1759509/000175950924000128/lyft-20240930.htm))
- Q4 Gross Bookings = 16,099.4 − 11,820.5 = **$4,278.9M**. This sits at the low end of the $4.28–$4.35B guidance range.
- Full-year Adjusted EBITDA: $382.4M; nine-month: $269.6M ([Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1759509/000175950924000128/lyft-20240930.htm)), so Q4 = 382.4 − 269.6 = **$112.8M**, matching the reported figu
…[truncated 1,302 chars]
- web_search(query="Lyft Q3 2024 results Q4 guidance Adjusted EBITDA margin gross bookings") → 10 results: Lyft, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950924000121/lyft-20240930xpressrelease.htm>; Lyft, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950924000096/lyft-20240630xpressrelease.htm>; Lyft, Inc. - Form 8-K/A - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950924000015/lyft-2023x12x31pressreleas.htm>; Lyft, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950924000011/lyft-2023x12x31pressreleas.htm>; Lyft, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950924000069/lyft-20240331.htm>
- web_search(query="Lyft fourth quarter 2024 results Adjusted EBITDA margin gross bookings") → 10 results: Lyft, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950924000121/lyft-20240930xpressrelease.htm>; Lyft, Inc. - Form ARS - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950925000071/lyftannualreport2024.pdf>; Lyft, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950924000096/lyft-20240630xpressrelease.htm>; Lyft, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950925000025/lyft-20241231.htm>; Lyft, Inc. - Form 8-K/A - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950924000015/lyft-2023x12x31pressreleas.htm>
- web_search(query="Lyft Announces Q4 and full-year 2024 financial results") → 9 results: Lyft, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950924000121/lyft-20240930xpressrelease.htm>; Lyft, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950924000064/lyft-20240331xpressrelease.htm>; Lyft, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950924000011/lyft-2023x12x31pressreleas.htm>; Lyft, Inc. - Form 8-K/A - FY2024 <https://www.sec.gov/Archives/edgar/data/1759509/000175950924000015/lyft-2023x12x31pressreleas.htm>; Lyft Reports Record Q4 and Full-Year 2024 Results <https://www.nasdaq.com/press-release/lyft-reports-record-q4-and-full-year-2024-results-2025-02-11>
- submit_final_result({"final_result": "Lyft beat the midpoint of its Q4'24 Adjusted EBITDA margin guidance. Guidance midpoint was 2.35%; actual was 2.6% reported (about 2.64% unrounded). That is a beat of about +25 bps on reported figures, or about +29 bps unrounded.\n\nSteps:\n1. Q3'24 guidance for Q4'24: Adjusted EBITDA margin of approximately 2.3% to 2.4% (midpoint 2.35%). Dollar guidance was $100M–$105M EBITDA on $4.28B–$4.35B Gross Bookings.\n2. Q4'24 actual: Adjusted EBITDA $112.8M, margin reported as 2.6%.\n3. Unrounded Q4 Gross Bookings = FY2024 $16,099.4M − 9M 2024 $11,820.5M = $4,278.9M. Q4 EBITDA = $382.4M − $269.6M = $112.8M. Margin = 112.8 / 4,278.9 = 2.636%.\n4. Difference vs. midpoint: 2.60% − 2.3
…[truncated 632 chars])

### Final answer
Lyft beat the midpoint of its Q4'24 Adjusted EBITDA margin guidance. Guidance midpoint was 2.35%; actual was 2.6% reported (about 2.64% unrounded). That is a beat of about +25 bps on reported figures, or about +29 bps unrounded.

Steps:
1. Q3'24 guidance for Q4'24: Adjusted EBITDA margin of approximately 2.3% to 2.4% (midpoint 2.35%). Dollar guidance was $100M–$105M EBITDA on $4.28B–$4.35B Gross Bookings.
2. Q4'24 actual: Adjusted EBITDA $112.8M, margin reported as 2.6%.
3. Unrounded Q4 Gross Bookings = FY2024 $16,099.4M − 9M 2024 $11,820.5M = $4,278.9M. Q4 EBITDA = $382.4M − $269.6M = $112.8M. Margin = 112.8 / 4,278.9 = 2.636%.
4. Difference vs. midpoint: 2.60% − 2.35% = +25 bps (reported); 2.636% − 2.35% = +28.6 bps (unrounded).

Sources:
- Lyft Q3 2024 earnings press release (8-K, Nov 6, 2024): https://www.sec.gov/Archives/edgar/data/1759509/000175950924000121/lyft-20240930xpressrelease.htm
- Lyft Q4 and FY2024 earnings press release (Feb 11, 2025): https://www.sec.gov/Archives/edgar/data/1759509/000175950925000009/lyft-2024x12x31pressreleas.htm
- Lyft Q3 2024 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1759509/000175950924000128/lyft-20240930.htm
- Lyft 2024 Annual Report (ARS): https://www.sec.gov/Archives/edgar/data/1759509/000175950925000071/lyftannualreport2024.pdf