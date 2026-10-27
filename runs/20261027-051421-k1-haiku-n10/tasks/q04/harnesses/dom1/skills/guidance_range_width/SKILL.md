---
name: guidance_range_width
description: Compute how wide a company's guidance range was (low, high, width as % of midpoint) for several quarters, in a prescribed output format.
---

# Guidance range width

**Analytic move:** retrieve and calculate. For each quarter, get the company's own outlook from the earnings release issued BEFORE that quarter (the "Business Outlook" / "Outlook" section of the 8-K Exhibit 99.1 issued with the prior quarter's results). Compute low, high, midpoint and width.

**Where the guidance lives**
- Guidance for quarter Q is in the release for quarter Q-1 (reported about a month after Q-1 ends). For Q2 2024 use the release reporting Q1 2024; for Q1 2025 use the release reporting Q4 2024 (early Feb 2025). Do not use the release for the guided quarter itself, which reports the actual.
- It is usually stated as "revenue of approximately $X billion, plus or minus $Y million". Midpoint = X. Low = X - Y, high = X + Y. Check whether the company states GAAP or non-GAAP; revenue is the same on both.
- In this task (AMD; seen in search excerpts of the 8-Ks, not in opened filings, so re-check): Q2 2024 about $5.7B, Q3 2024 about $6.7B, Q4 2024 about $7.5B and Q1 2025 about $7.1B, each plus or minus $300M. Treat these as hypotheses and confirm the stated midpoint and the plus/minus for each quarter.

**Definitions (state the one you use)**
- "Range as % of midpoint" = (high - low) / midpoint x 100, i.e. the FULL width, not the plus/minus half-width. Example: ±$300M on $5.7B is 0.6 / 5.7 = 10.5263%. Mention the half-width only if useful, in one clause, and never in place of the full-width figure.
- Check that each row foots: midpoint = (low + high) / 2.

**Answer contract**
1. Follow the output format the question prescribes, one line per period, exactly. If it says "[X.X]%", give one decimal (round only at the end: 10.5%, not 10.53%). If it gives "$[X.X] billion", give low and high in billions to one decimal. The question's format overrides the general two-decimal habit.
2. Put the lines in the order the question lists the periods and label them as the question does (Q2 2024, and so on). Do not add extra periods or alternative variants of the figures in the lines themselves.
3. Add after the lines a short working block: the source release and date for each quarter's guidance, midpoint, plus/minus, width in dollars, and the unrounded ratio. Say plainly whether each figure came from an opened filing or a search excerpt.
4. Before submitting, confirm that each guidance figure belongs to the right guided quarter, that the units are billions vs millions, and that the percentage is divided by the midpoint.
