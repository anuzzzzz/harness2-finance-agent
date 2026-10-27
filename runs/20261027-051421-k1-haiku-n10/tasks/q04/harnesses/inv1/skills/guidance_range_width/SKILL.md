---
name: guidance_range_width
description: Compute how wide a company's guidance range was (low to high, as % of midpoint) for several consecutive quarters.
---

# Guidance range width across quarters

**Analytic move:** retrieve, then calculate. Each quarter's guidance sits in the PRIOR quarter's earnings release; the width is (high - low) / midpoint.

**Procedure**
1. Map each target quarter to the release that issued its guidance: guidance for quarter Q comes from the release reporting quarter Q-1 (its "Business Outlook" / "Outlook" section). Write the mapping out before searching (e.g. Q2 2024 guidance = release for Q1 2024, issued about April 30, 2024). Use the company's fiscal quarters.
2. For each quarter, get the outlook sentence from the release text (8-K Exhibit 99.1 or the IR press release): midpoint and the plus/minus amount. Record whether it is stated as "approximately $X, plus or minus $Y" or as an explicit low-high range. Do not take one quarter's figure from another quarter's release, and do not use actuals.
3. Low = midpoint - Y, high = midpoint + Y (or the stated endpoints). Check units (billions vs millions) and basis (revenue vs margin, GAAP vs non-GAAP).
4. Width % = (high - low) / midpoint x 100, computed from unrounded dollars. Note once that half-width (plus/minus %) is half of this only if the question's wording is ambiguous; otherwise follow the question's wording ("range ... of midpoint" means full width).
5. Final formatting: use exactly the line template the question gives, one line per period, with the decimals it prescribes (e.g. one decimal for dollars and percent). Put unrounded calculations beneath, not in the formatted lines. Do not add extra comparisons the question did not ask for.
6. Before submitting: confirm every quarter has a figure seen in tool output, recompute each percentage once, and that the lines are in the order the question lists.
