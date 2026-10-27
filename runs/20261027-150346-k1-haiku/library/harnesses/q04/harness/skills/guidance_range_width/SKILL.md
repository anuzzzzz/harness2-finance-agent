---
name: guidance_range_width
description: Compute how wide a company's quarterly revenue (or other) guidance range was, as a % of its midpoint, for several consecutive quarters, with each quarter's guide taken from the prior quarter's earnings release.
---
ANALYTIC MOVE: for each target quarter, find the guidance issued in the PRIOR quarter's earnings release (8-K EX-99.1, "Outlook" section). Then compute width = (high - low) / midpoint x 100.

1. Mapping. Guidance for quarter N sits in the release reporting quarter N-1. Quarter N's own release holds the actual and the guide for N+1, which is the wrong period. Four target quarters need four releases, one per preceding quarter.
2. Read the exact wording. AMD-style guidance reads "revenue to be approximately $X billion, plus or minus $Y million": midpoint X, low X-Y, high X+Y, width 2Y / X. If a company gives an explicit low-high range, use those figures and take the midpoint as their average. State which form was used.
3. Units. Convert millions to billions before building low and high (e.g. $300 million = $0.3 billion). Compute the percentage from the unrounded midpoint.
4. Format. The question's format string controls. If it says "[X.X]%", give one decimal, rounding only at the end; show the unrounded value in the working. One line per period, in the order listed, then the short working.
5. Verify. Take each midpoint and band from the retrieved text of that quarter's release, not from a snippet or news summary (secondary sites sometimes misquote the midpoint). Check that the period named in the sentence matches the target quarter and that the band is the same in every release. List as sources only releases you opened.

Task lead (AMD; re-confirm each in the filing text). Prior runs read "approximately $X billion, plus or minus $300 million" in these 8-K EX-99.1 releases:
- Q2 2024 guide $5.7B, in the Q1 2024 release: https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm
- Q3 2024 guide $6.7B, in the Q2 2024 release: https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm
- Q4 2024 guide $7.5B, in the Q3 2024 release: https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm
- Q1 2025 guide $7.1B, in the Q4 2024 release: https://www.sec.gov/Archives/edgar/data/2488/000000248825000009/q42024991.htm
