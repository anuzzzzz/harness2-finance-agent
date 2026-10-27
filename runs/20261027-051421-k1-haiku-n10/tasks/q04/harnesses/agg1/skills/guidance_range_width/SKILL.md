---
name: guidance_range_width
description: Compute how wide a company's guidance range was (low, high, width as % of midpoint) for several consecutive quarters, in the question's prescribed format.
---

# Guidance range width across quarters

**Analytic move:** retrieve, then calculate. Each quarter's guidance sits in the PRIOR quarter's earnings release; the width is (high - low) / midpoint.

**Procedure**
1. Map each target quarter to the release that issued its guidance: guidance for quarter Q comes from the release reporting quarter Q-1 (its "Business Outlook" / "Outlook" section, 8-K Exhibit 99.1 or the IR press release). Write the mapping out before searching (e.g. Q2 2024 guidance = release for Q1 2024, issued about April 30, 2024). Use the company's fiscal quarters. Never use the release for the guided quarter itself (that reports the actual).
2. For each quarter, get the outlook sentence from release text: midpoint and the plus/minus amount, or explicit low-high endpoints. Do not take one quarter's figure from another quarter's release.
3. Low = midpoint - Y, high = midpoint + Y (or the stated endpoints). Check units (billions vs millions) and basis (revenue vs margin, GAAP vs non-GAAP). Confirm midpoint = (low + high) / 2.
4. "Range as % of midpoint" = (high - low) / midpoint x 100, the FULL width, not the plus/minus half-width. Compute from unrounded dollars. Mention the half-width only in one clause, if at all, never in place of the full width.
5. Final formatting: use exactly the line template the question gives, one line per period, in the order listed, with the decimals it prescribes (e.g. "[X.X]%" means one decimal; round only at the end). The question's format overrides the general two-decimal habit. Put the working beneath the lines: source release and date, midpoint, plus/minus, width in dollars, unrounded ratio, and whether each figure came from an opened document or a search excerpt. Do not add extra comparisons the question did not ask for.
6. Before submitting: confirm every quarter has a figure seen in tool output, and recompute each percentage once.
