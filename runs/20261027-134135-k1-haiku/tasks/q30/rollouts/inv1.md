## Rollout `inv1`
- outcome: submitted
- turns: 3; cost: $0.135; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm", "key": "snap_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: snap_10k_2024. (614,017 characters)
  The data_storage currently contains the following keys:
  snap_10k_2024
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this 10-K document, find the convertible notes note (Note 7 or similar). Quote verbatim any sentence containing \"maximum number of shares\" or \"maximum\" related to shares issuable upon conversion of the convertible notes, and the potentially dilutive / if-converted share amounts as of December 31, 2024. Also quote the EPS note table row \"Convertible Notes (if-converted)\" with values for 2024 and 2023, and the conversion rates per $1,000 principal and principal amounts for each series (2025, 2026, 2027, 2028, 2030 notes). Units and period must be stated.\n\nDocument: {{snap_10k_2024}}"})
  result: ## Result: No maximum share cap for conversion is disclosed
  
  I found no sentence in the document that states a maximum number of shares issuable upon conversion of the Convertible Notes. The only "maximum" sentences relate to the 2017 Equity Incentive Plan, not the notes. For example, Item 11 states: "The maximum number of shares of our Class A common stock available for future issuance under our 2017 Plan as of December 31, 2024 is 152,488,503." The Note 7 capped call disclosures use per-share cap prices, not a share cap. The conversion amounts below are therefore the stated initial conversion rates applied to principal.
  
  ## 1. Potentially dilutive (if-converted) shares, as of December 31, 2024
  
  Note 3 (Net Loss per Share) states:
  
  > "The following potentially dilutive shares were excluded from the calculation of diluted net loss per share because their effect would have been anti-dilutive:As of December 31,202420232022(in thousands)…Convertible Notes (if-converted)85,94589,37989,379"
  
  Units: thousands of shares. Period: as of December 31 for each year.
  
  Note 3 also states:
  
  > "For the periods presented, our potentially dilutive shares relating to stock options, RSUs, RSAs, and Convertible Notes were not included in the computation of diluted net loss per share as the effect of including these shares in the calculation would have been anti-dilutive."
  
  Note 7 states:
  
  > "As of December 31, 2024, the if-converted value of the Convertible Notes did not exceed the principal amount."
  
  ## 2. Conversion rates and principal by series
  
  Units: conversion rates are Class A shares per $1,000 principal. Conversion prices are $ per share. Principal is in thousands of dollars as of December 31, 2024, from the Note 7 table.
  
  **2030 Notes (Note 7):**
  > "The 2030 Notes are convertible i
  …[truncated 2,783 chars]

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: about 85,945 thousand shares (≈85.95 million Class A shares) as of 12/31/2024.**\n\nThis is the figure the filing reports for the potentially dilutive shares from the convertible notes. The filing does not give a separate \"maximum\" share number for the notes.\n\n**Step 1 – EPS note (Note 3, Net Loss per Share, FY2024 10-K).** The table of potentially dilutive shares excluded from diluted EPS as anti-dilutive shows \"Convertible Notes (if-converted)\" at 85,945 thousand shares as of 12/31/2024, versus 89,379 thousand as of 12/31/2023 and 89,379 thousand as of 12/31/2022. Units are thousands of shares.\n\n**Step 2 – Convertible notes note (Note 7).** The initial c
…[truncated 1,827 chars])

### Final answer
**Answer: about 85,945 thousand shares (≈85.95 million Class A shares) as of 12/31/2024.**

This is the figure the filing reports for the potentially dilutive shares from the convertible notes. The filing does not give a separate "maximum" share number for the notes.

**Step 1 – EPS note (Note 3, Net Loss per Share, FY2024 10-K).** The table of potentially dilutive shares excluded from diluted EPS as anti-dilutive shows "Convertible Notes (if-converted)" at 85,945 thousand shares as of 12/31/2024, versus 89,379 thousand as of 12/31/2023 and 89,379 thousand as of 12/31/2022. Units are thousands of shares.

**Step 2 – Convertible notes note (Note 7).** The initial conversion rates (Class A shares per $1,000 principal) and principal outstanding at 12/31/2024 (in thousands of dollars) are:
- 2025 Notes: 46.1233 shares per $1,000; principal $36,240
- 2026 Notes: 43.8481 shares per $1,000; principal $249,754
- 2027 Notes: 11.2042 shares per $1,000; principal $1,150,000
- 2028 Notes: 17.7494 shares per $1,000; principal $1,500,000
- 2030 Notes: 45.0846 shares per $1,000; principal $750,000

**Step 3 – Reconciliation (my calculation, principal × conversion rate ÷ 1,000, in thousands of shares):**
- 2025: 36,240 × 46.1233 / 1,000 = 1,671.7
- 2026: 249,754 × 43.8481 / 1,000 = 10,950.3
- 2027: 1,150,000 × 11.2042 / 1,000 = 12,884.8
- 2028: 1,500,000 × 17.7494 / 1,000 = 26,624.1
- 2030: 750,000 × 45.0846 / 1,000 = 33,813.5
- Total ≈ 85,944.4 thousand, which agrees with the 85,945 thousand in Note 3 after rounding.

**Check for a "maximum" figure.** I searched the 10-K for "maximum" language tied to the notes. The only "maximum" share figure found relates to the 2017 Equity Incentive Plan (152,488,503 shares available for future issuance), not the convertible notes. Note 7 states that the if-converted value did not exceed the principal amount at 12/31/2024, so the notes were not in a position where conversion value exceeded principal.

**Caveat.** The 85,945 thousand figure is the if-converted share count from the notes at their initial conversion rates. It is the maximum dilutive effect the filing quantifies for the notes. The filing does not present it as a cap.

**Sources:**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm",
            "name": "Snap Inc. FY2024 Form 10-K (accession 0001564408-25-000019), Notes 3 and 7"
        }
    ]
}