## Rollout `dom1`
- outcome: submitted
- turns: 4; cost: $0.131; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "convertible_dilution_lookup"})
  result: ---
  name: convertible_dilution_lookup
  description: Find the maximum share dilution from a company's outstanding convertible notes at a balance-sheet date, and reconcile it to principal x conversion rate by series.
  ---
  ANALYTIC MOVE: look up, then reconcile. Report the number of shares issuable on conversion of all outstanding convertible notes at the date asked, and check it against the debt footnote.
  
  1. Controlling sources in the 10-K:
     - The net income (loss) per share note has a table of potentially dilutive securities excluded from diluted EPS. It usually has a line such as "Convertible Notes (if-converted)", in thousands of shares. This is the headline figure.
     - The debt note gives, for each series, the principal outstanding, the conversion rate per $1,000 of principal and the conversion price.
  2. Reconcile. For each series, shares = principal / 1,000 x conversion rate. Sum the series and compare with the EPS-table line. Carry full precision and round only at the end. If the two differ, say why (for example a series repaid or converted during the year, or make-whole shares) and name which figure you use.
  3. Keep these distinct and label them: shares on an if-converted basis, shares actually included in diluted EPS (zero when there is a net loss, because they are anti-dilutive), and any offset from capped calls or hedges. State whether the capped calls are netted into the figure. Do not net them unless the filing does.
  4. Check the units (thousands of shares vs millions), the date (the period-end the question names, not the filing date), and that every series outstanding at that date is included. Take principal amounts from the debt note at that date, not from the original issue size.
  5. Answer contract: the total shares with unit and date, the per-series tabl
  …[truncated 917 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm", "key": "snap10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: snap10k. (614,017 characters)
  The data_storage currently contains the following keys:
  snap10k
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Snap Inc. 10-K text: {{snap10k}}. (1) Find the net income (loss) per share note table of potentially dilutive securities excluded from diluted EPS as of December 31, 2024, and quote the Convertible Notes (if-converted) line and units. (2) Find the convertible senior notes table in the debt note: for each series (2025, 2026, 2027, 2028, 2030 notes), give principal outstanding at 12/31/2024, conversion rate per $1,000 principal, and conversion price. (3) State whether capped calls are netted in the figures and whether any notes were repaid/converted during 2024. Give exact figures."})
  result: ## 1. Net loss per share: potentially dilutive securities
  
  The table of potentially dilutive shares excluded from diluted net loss per share (as of December 31, 2024) shows:
  
  - **Convertible Notes (if-converted): 85,945 (in thousands), i.e., about 85.9 million shares of Class A common stock.**
  
  The table is stated in thousands of shares.
  
  ## 2. Convertible senior notes (Note 7 and related disclosures)
  
  | Series | Principal at 12/31/2024 | Conversion rate (shares per $1,000) | Conversion price (approx.) |
  |---|---|---|---|
  | 2025 Notes | $36,240 thousand ($36.2M) | 46.1233 | $21.68 |
  | 2026 Notes | $249,754 thousand ($249.8M) | 43.8481 | $22.81 |
  | 2027 Notes | $1,150,000 thousand ($1.15B) | 11.2042 | $89.25 |
  | 2028 Notes | $1,500,000 thousand ($1.50B) | 17.7494 | $56.34 |
  | 2030 Notes | $750,000 thousand ($750.0M) | 45.0846 | $22.18 |
  
  Total principal outstanding is $3,685,994 thousand. The 2030 conversion rate is 45.0846 per $1,000, and the 2030 Notes were issued in May 2024.
  
  ## 3. Capped calls, repayments, and conversions
  
  **Capped calls:** They are not netted against the notes. The notes are carried at face value less unamortized debt issuance costs. The capped call cost was recorded as a reduction of additional paid-in capital, and the capped calls are not remeasured while they remain equity-classified. The 2030 net proceeds of $671.5M were net of issuance costs and the cash used for the 2030 capped calls, but that is a cash-proceeds figure, not a balance-sheet netting. The remaining capped calls were out-of-the-money at year-end. The 2025 capped calls were terminated in May 2024 for $62.7M of proceeds, recorded in APIC.
  
  **Repayments during 2024:** Yes, through privately negotiated repurchases (the "Note Repurchases"):
  - **February 2024:** $100.0M of 2025 Notes a
  …[truncated 574 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: about 85,945 thousand shares (≈85.9 million Class A shares) as of December 31, 2024.**\n\nThis is the maximum potential (if-converted) dilution from Snap Inc.'s convertible senior notes. It is not the number of shares included in diluted EPS. Because Snap reported a net loss, those notes were anti-dilutive and excluded from diluted net loss per share.\n\n**Step 1: Headline figure.** The net loss per share note's table of potentially dilutive securities excluded from diluted EPS shows \"Convertible Notes (if-converted)\" of 85,945 (in thousands) as of December 31, 2024.\n\n**Step 2: Per-series reconciliation (shares = principal / 1,000 × conversion rate).** Princip
…[truncated 1,665 chars])

### Final answer
**Answer: about 85,945 thousand shares (≈85.9 million Class A shares) as of December 31, 2024.**

This is the maximum potential (if-converted) dilution from Snap Inc.'s convertible senior notes. It is not the number of shares included in diluted EPS. Because Snap reported a net loss, those notes were anti-dilutive and excluded from diluted net loss per share.

**Step 1: Headline figure.** The net loss per share note's table of potentially dilutive securities excluded from diluted EPS shows "Convertible Notes (if-converted)" of 85,945 (in thousands) as of December 31, 2024.

**Step 2: Per-series reconciliation (shares = principal / 1,000 × conversion rate).** Principal and conversion rates are from the debt note at 12/31/2024:

| Series | Principal ($ thousands) | Conversion rate (per $1,000) | Shares (thousands) |
|---|---|---|---|
| 2025 Notes | 36,240 | 46.1233 | 1,671.51 |
| 2026 Notes | 249,754 | 43.8481 | 10,951.24 |
| 2027 Notes | 1,150,000 | 11.2042 | 12,884.83 |
| 2028 Notes | 1,500,000 | 17.7494 | 26,624.10 |
| 2030 Notes | 750,000 | 45.0846 | 33,813.45 |
| **Total** | **3,685,994** | | **85,945.13** |

The sum of 85,945.13 thousand shares matches the disclosed 85,945 thousand figure. The 2026 principal (249,754) was taken from the tool's reading of the debt note; the reconciliation to the disclosed total supports it.

**Step 3: Other considerations.**
- Capped calls are not netted. The filing states that the notes are carried at face value less unamortized issuance costs, and the capped calls are recorded in equity. The figure above is therefore gross of any capped call offset.
- Repurchases in 2024 reduced the 2025 and 2026 series. In February 2024 Snap repurchased $100.0M of 2025 Notes and $351.2M of 2026 Notes. In May 2024 it repurchased about $147.9M of 2025 Notes and about $237.5M of 2026 Notes. The figure reflects principal remaining after these repurchases.
- No notes were converted during 2024. The 2030 Notes were issued in May 2024.
- Units are thousands of shares, and the date is the period end (12/31/2024).

**Sources:**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm",
            "name": "Snap Inc. FY2024 Form 10-K (snap-20241231.htm)"
        }
    ]
}