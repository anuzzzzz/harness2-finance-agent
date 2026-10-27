## Rollout `ctl2`
- outcome: submitted
- turns: 1; cost: $0.070; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Coca-Cola dividend payout ratio 2024") → 10 results: COCA COLA CO - Form ARS - FY2024 <https://www.sec.gov/Archives/edgar/data/21344/000110465925024268/tm257314d2_ars.pdf>; COCA-COLA EUROPACIFIC PARTNERS plc - Form 6-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1650107/000165010725000015/ccep2024fyreport2nd6k.htm>; COCA COLA CO - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/21344/000002134424000060/ko-20240927.htm>; COCA COLA CO - Form DEF 14A - FY2024 <https://www.sec.gov/Archives/edgar/data/21344/000155837024003468/ko-20240501xdef14a.pdf>; Coca-Cola Co Share Dividends <https://www.fidelity.co.uk/factsheet-data/factsheet/US1912161007USD-coca-cola-co/dividends>
- web_search(query="PepsiCo dividend payout ratio 2024") → 10 results: PEPSICO INC - Form ARS - FY2024 <https://www.sec.gov/Archives/edgar/data/77476/000130817925000292/pep4354281-ars.pdf>; PEPSICO INC - Form DEF 14A - FY2024 <https://www.sec.gov/Archives/edgar/data/77476/000130817924000258/pep_courtesy-pdf.pdf>; PEPSICO INC - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/77476/000007747624000052/pep-20240907.htm>; PEPSICO INC - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/77476/000007747624000042/pep-20240615.htm>; PEPSICO INC - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/77476/000007747624000017/pep-20240323.htm>
- web_search(query="Keurig Dr Pepper dividend payout ratio 2024") → 9 results: Keurig Dr Pepper Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1418135/000141813524000090/kdp-20240930.htm>; Keurig Dr Pepper Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1418135/000141813524000076/exhibit991keurigdrpepperde.htm>; Keurig Dr Pepper Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1418135/000141813524000097/exhibit991keurigdrpepperde.htm>; Keurig Dr Pepper Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1418135/000141813524000060/exhibit991keurigdrpepperde.htm>; KEURIG DR PEPPER Dividend Payout Ratio: 2.34 — 311% Above <https://www.gurufocus.com/term/payout/KDP>
- web_search(query="Keurig Dr Pepper full year 2024 results diluted EPS net income") → 10 results: Keurig Dr Pepper Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1418135/000141813524000006/ex991-keurigdrpepperreport.htm>; Keurig Dr Pepper Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1418135/000141813524000073/kdp-20240630.htm>; Keurig Dr Pepper Inc. - Form ARS - FY2024 <https://www.sec.gov/Archives/edgar/data/1418135/000119312525096897/d893272dars.pdf>; Keurig Dr Pepper Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1418135/000141813524000090/kdp-20240930.htm>; Keurig Dr Pepper Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1418135/000141813525000013/kdp-20241231.htm>
- web_search(query="PepsiCo full year 2024 results reported EPS net income attributable") → 9 results: PEPSICO INC - Form 10-K - FY2024 (Annual Financial Statement Tables - full year 2024) <https://www.sec.gov/Archives/edgar/data/77476/000007747625000007/Financial_Report.xlsx>; PEPSICO INC - Form DEF 14A - FY2024 <https://www.sec.gov/Archives/edgar/data/77476/000130817924000258/pep_courtesy-pdf.pdf>; PEPSICO INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/77476/000007747624000010/q420238-kxexhibit991.htm>; PEPSICO INC - Form 10-Q - FY2024 (Quarterly Earnings Tables - quarter ended Sep 2024) <https://www.sec.gov/Archives/edgar/data/77476/000007747624000052/Financial_Report.xlsx>; PEPSICO INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/77476/000007747624000019/q120248-kxexhibit991.htm>
- web_search(query="Coca-Cola Europacific Partners 2024 dividend payout ratio comparable profit") → 10 results: COCA-COLA EUROPACIFIC PARTNERS plc - Form 6-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1650107/000165010725000011/ccep2024fyreport1st6k.htm>; COCA-COLA EUROPACIFIC PARTNERS plc - Form 6-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1650107/000165010724000064/cce-20240628.htm>; COCA-COLA EUROPACIFIC PARTNERS plc - Form 6-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1650107/000165010724000035/ccepq12024tradingupdate-1s.htm>; COCA-COLA EUROPACIFIC PARTNERS plc - Form 6-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1650107/000165010725000015/ccep2024fyreport2nd6k.htm>; COCA-COLA EUROPACIFIC PARTNERS plc - Form 20-F - FY2024 <https://www.sec.gov/Archives/edgar/data/1650107/000165010725000039/cce-20241231.htm>
- submit_final_result({"final_result": "**Answer: FY24 dividend payout ratio ranking (highest to lowest)**\n\n1. **Keurig Dr Pepper (KDP): about 84.76%**\n2. **Coca-Cola (KO): about 78.86%**\n3. **PepsiCo (PEP): about 76.69%**\n4. **Coca-Cola Europacific Partners (CCEP): about 49.87%**\n\n**Method.** I used one consistent formula for everyone: FY24 dividends per share declared divided by FY24 diluted EPS. For CCEP, which reports under IFRS, I used comparable diluted EPS, because that is the basis its own payout policy uses.\n\n**Inputs and calculations**\n\n- **Coca-Cola (KO).** Annualized 2024 dividend of $1.94 per share, per <cite index=\"1-7\">Our annualized common stock dividend was $1.94 per share and $1.84 
…[truncated 5,808 chars])

### Final answer
**Answer: FY24 dividend payout ratio ranking (highest to lowest)**

1. **Keurig Dr Pepper (KDP): about 84.76%**
2. **Coca-Cola (KO): about 78.86%**
3. **PepsiCo (PEP): about 76.69%**
4. **Coca-Cola Europacific Partners (CCEP): about 49.87%**

**Method.** I used one consistent formula for everyone: FY24 dividends per share declared divided by FY24 diluted EPS. For CCEP, which reports under IFRS, I used comparable diluted EPS, because that is the basis its own payout policy uses.

**Inputs and calculations**

- **Coca-Cola (KO).** Annualized 2024 dividend of $1.94 per share, per <cite index="1-7">Our annualized common stock dividend was $1.94 per share and $1.84 per share in 2024 and 2023</cite>. The 2024 diluted EPS of $2.46 comes from a third-party data page that shows <cite index="9-3">Earnings Per Share: 2.46 USD</cite>. I could not confirm that EPS figure against KO's 10-K. Ratio: 1.94 / 2.46 = 78.86%.
- **PepsiCo (PEP).** Declared 2024 dividends were $3.975 for the first 36 weeks, per the Q3 10-Q, which reports that <cite index="13-1">Cash dividends declared per common share were $ 1.355and $ 1.265for the 12 weeks ended September 7, 2024</cite>. Adding the Q4 2024 dividend of $1.355 gives $5.33. Full-year diluted EPS was <cite index="47-3">$1.11 $6.95</cite> (Q4 and full year 2024). Ratio: 5.33 / 6.95 = 76.69%.
- **Keurig Dr Pepper (KDP).** Declared 2024 dividends were $0.66 for the first nine months, per the Q3 10-Q (<cite index="21-3">We have declared total dividends of $0.66 per share and $0.615 per share for the first nine months of 2024 and 2023</cite>). The Q4 2024 dividend was <cite index="23-1">$0.23 per share</cite>, giving $0.89. Full-year GAAP diluted EPS was <cite index="34-9,34-10">Diluted EPS decreased 32.3% to $1.05 per diluted share as compared to $1.55 in the prior year.</cite> Ratio: 0.89 / 1.05 = 84.76%.
- **Coca-Cola Europacific Partners (CCEP).** FY24 dividend per share was <cite index="54-2">FY dividend per share €1.97 +7.1%, maintains annualised payout ratio of ~50%</cite>. The 20-F states the company's payout policy: <cite index="53-10">maintaining a payout ratio of approximately 50% in line with our dividend policy</cite>. The comparable diluted EPS of €3.95 is read from a table in the FY24 6-K, where the comparable column shows 3.95, so this is an inference from the table layout. Ratio: 1.97 / 3.95 = 49.87%.

**Cross-check against third-party data.** Third-party sites use different methods and give different numbers. Fidelity lists KO at 79.46% and PEP at 77.29% for 2024. Digrin lists KO at 77.91% on a trailing basis. The ordering of KO above PEP holds on these sources too. KDP's cash-based ratio is also high: one source reports <cite index="27-6">For 2024, KDP paid $1.19 billion in dividends against $1.66 billion in free cash flow, producing a payout ratio of 72.1%.</cite> That measure is not comparable to the earnings-based ratios above.

**Caveats**

- The ranking of KO, PEP, and KDP is close. A difference of about 2 percentage points between KO and PEP could change if a different EPS basis (adjusted vs. GAAP) is used.
- Adjusted (non-GAAP) EPS would lower KDP's ratio sharply, because KDP's GAAP EPS was depressed by impairments. KDP reported <cite index="38-7">Adjusted diluted EPS increased 7.8% to $1.92.</cite> On that basis, its ratio would be about 46%.
- Monster Beverage and other beverage peers were not included because they do not pay a regular dividend.

**Sources:** KO 2024 ARS (sec.gov), PepsiCo Q3 2024 10-Q and Q4 2024 earnings release, KDP Q3 2024 10-Q and FY2024 10-K/earnings release, CCEP FY2024 6-K and 20-F, Fidelity and Digrin dividend data pages.

{
    "sources": [
        {"url": "https://www.sec.gov/Archives/edgar/data/21344/000110465925024268/tm257314d2_ars.pdf", "name": "Coca-Cola FY2024 Annual Report (ARS)"},
        {"url": "https://www.fidelity.co.uk/factsheet-data/factsheet/US1912161007USD-coca-cola-co/dividends", "name": "Fidelity - Coca-Cola Co Share Dividends"},
        {"url": "https://www.digrin.com/stocks/detail/KO/payout_ratio", "name": "Digrin - Coca-Cola Payout Ratio"},
        {"url": "https://www.sec.gov/Archives/edgar/data/77476/000007747624000052/pep-20240907.htm", "name": "PepsiCo Q3 2024 Form 10-Q"},
        {"url": "https://www.sec.gov/Archives/edgar/data/77476/000007747625000007/Financial_Report.xlsx", "name": "PepsiCo FY2024 10-K Financial Report"},
        {"url": "https://investors.pepsico.com/docs/pepsico-5v9wci20/media/Files/investors/q4-2024-earnings-release.pdf", "name": "PepsiCo Q4 and Full-Year 2024 Earnings Release"},
        {"url": "https://www.fidelity.co.uk/factsheet-data/factsheet/US7134481081-pepsico-inc/dividends", "name": "Fidelity - PepsiCo Inc Share Dividends"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1418135/000141813524000090/kdp-20240930.htm", "name": "Keurig Dr Pepper Q3 2024 Form 10-Q"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1418135/000141813524000076/exhibit991keurigdrpepperde.htm", "name": "Keurig Dr Pepper Dividend Increase Release (Sept 2024)"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1418135/000141813524000097/exhibit991keurigdrpepperde.htm", "name": "Keurig Dr Pepper Q4 2024 Dividend Declaration"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1418135/000141813525000013/kdp-20241231.htm", "name": "Keurig Dr Pepper FY2024 Form 10-K"},
        {"url": "https://www.keurigdrpepper.com/keurig-dr-pepper-reports-q4-and-full-year-2024-results-and-provides-2025-outlook-26/", "name": "Keurig Dr Pepper Q4 and FY2024 Results"},
        {"url": "https://finance.yahoo.com/news/keurig-dr-pepper-dividend-streak-171528496.html", "name": "Yahoo Finance - Keurig Dr Pepper Dividend Streak Analysis"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1650107/000165010725000015/ccep2024fyreport2nd6k.htm", "name": "Coca-Cola Europacific Partners FY2024 6-K"},
        {"url": "https://ir.cocacolaep.com/news-releases/news-release-details/coca-cola-ep-plc-preliminary-unaudited-results-q4-fy-2024", "name": "Coca-Cola EP PLC Preliminary Results Q4 & FY 2024"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1650107/000165010725000039/cce-20241231.htm", "name": "Coca-Cola Europacific Partners FY2024 Form 20-F"}
    ]
}