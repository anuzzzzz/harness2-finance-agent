---
name: guidance_range_width
description: Compute how wide a company's quarterly revenue (or other) guidance range was, as a % of its midpoint, for several consecutive quarters, with each quarter's guide taken from the prior quarter's earnings release.
---
ANALYTIC MOVE: for each target quarter, find the guidance issued in the PRIOR quarter's earnings release (8-K EX-99.1, "Outlook" or "Business Outlook" section). Then compute width = (high - low) / midpoint x 100.

1. Mapping. Guidance for quarter N sits in the release reporting quarter N-1. Quarter N's own release holds the actual and the guide for N+1, which is the wrong period for N. For four consecutive target quarters you need four releases, one per quarter before each target, and each guide must come from its own release.
2. Read the exact wording. AMD-style guidance reads "revenue to be approximately $X billion, plus or minus $Y million". That gives midpoint X, low X-Y and high X+Y, and the width is 2Y / X. If a company gives an explicit low-high range, use those figures and take the midpoint as their average. State which form was used.
3. Units. Convert millions to billions before building the low and high ends (e.g. $300 million = $0.3 billion). Compute the percentage from the unrounded midpoint.
4. Format. The question's format string controls. If it says "[X.X]%", give one decimal, and round only at the end. You may show the unrounded value in the working. Make one line per period, in the order the question lists them. Keep the dollar figures to one decimal if the format says so. If a guided figure has more precision, say so in the working.
5. Verify. Take each midpoint and band from the retrieved text of that quarter's release, not from a search snippet or a news summary. Secondary sites sometimes misquote the midpoint. Check that the period named in the sentence ("for the second quarter of 2024") matches the target quarter. List as sources only the releases you opened and retrieved from.
6. Answer contract: one line per quarter in the requested format, then the short working (midpoint, band, width formula) and the source release for each quarter.

Task lead (AMD; re-confirm each in the filing text). Earlier runs read the following wording in AMD's releases:
- Q2 2024 guide, in the Q1 2024 release (https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm): $5.7B +/- $300M.
- Q3 2024 guide, in the Q2 2024 release (https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm): $6.7B +/- $300M.
- Q4 2024 guide, in the Q3 2024 release (https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm): $7.5B +/- $300M.
- Q1 2025 guide, in the Q4 2024 release (https://www.sec.gov/Archives/edgar/data/2488/000000248825000009/q42024991.htm): $7.1B +/- $300M.
If all four hold, each range is $0.6B wide. The widths are 0.6/5.7 = 10.526%, 0.6/6.7 = 8.955%, 0.6/7.5 = 8.000% and 0.6/7.1 = 8.451%. Rounded to one decimal these are 10.5%, 9.0%, 8.0% and 8.5%.
