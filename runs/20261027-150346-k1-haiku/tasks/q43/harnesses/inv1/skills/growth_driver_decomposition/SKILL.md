---
name: growth_driver_decomposition
description: Split a revenue (or similar) change into a volume effect and a rate effect, such as take rate times gross bookings, price times units, or yield times balances, and report each driver's share of the growth.
---
ANALYTIC MOVE: decompose. Result = Rate x Volume, so the change in the result is the sum of a volume effect and a rate effect.

1. Define the terms from the company's own filing. Volume is the company's volume metric (e.g. Gross Bookings, units, volume). Rate = result / volume (e.g. take rate = revenue / gross bookings). Retrieve both years of the volume and the result from the same document, with units, and note any constant-currency vs reported difference. Use reported figures in the calculation.
2. State the formula before computing, and use one formula that sums exactly:
   - Volume effect = (Volume1 - Volume0) x Rate0
   - Rate effect = (Rate1 - Rate0) x Volume1
   - Check that the two effects sum to the total change.
   - Share of growth = effect / total change. Shares can exceed 100% or be negative when the rate fell.
3. Compute at full precision and round only the final percentages and amounts. Show the rates to at least two decimals in percent, and the rate change in bps.
4. Adjustments. If the filing says a reclassification, business-model change, acquisition or one-off distorted the rate, retrieve its disclosed amount and its wording. Compute the headline on reported figures, then add a second view labelled as adjusted, stating what was added back and to which year. Do not blend the two views, and say plainly that the adjustment is your estimate. If the filing's own narrative attributes the growth to a driver (e.g. "primarily attributable to an increase in Gross Bookings"), quote it as corroboration.
5. Answer contract: first sentence gives the direct answer (the share from rate vs volume, and which view it is); then inputs with period, unit and source; the formula and arithmetic; the labelled alternate; sources limited to documents opened.
