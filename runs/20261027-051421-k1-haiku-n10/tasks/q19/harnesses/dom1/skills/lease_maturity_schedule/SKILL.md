---
name: lease_maturity_schedule
description: Answer questions on operating/finance lease (or debt, purchase-obligation) maturities "in the next N years", with the share of the total.
---

# Lease / obligation maturity questions

**Analytic move:** calculate. Sum the first N annual rows of the maturity table, then divide by the table's total. Inputs are the undiscounted annual payments and the undiscounted total.

**Where the figures live:** in the latest 10-K filed on or before the question date, in the Leases note, in the table "maturities of lease liabilities". It sits next to the lines "Less: interest" and "Present value of lease liabilities". The figures may be in thousands, so check the table header.

**Procedure**
1. Pick the latest annual filing as of the question date. For an April 2025 question this is the FY2024 10-K (period ended Dec 31, 2024), not an older 10-K and not an unfiled later 10-Q. Retrieve the table from the filing text (parse_html_page, then retrieve_information), not from a search snippet or memory. Confirm every year row and the total against the page.
2. Use the right lease type. Operating and finance leases usually have separate tables or columns, so use the one the question names. Do not mix in sublease income or the lease liabilities on the balance sheet.
3. "Next three years" means the first three fiscal-year rows after the balance-sheet date (for FY2024, 2025, 2026 and 2027). Exclude "Thereafter" and the later years.
4. Percentage: the default denominator is **total undiscounted lease payments**, because the numerator is undiscounted. Show the PV-based share (against the liability net of imputed interest) only as a labelled secondary figure. Never mix an undiscounted numerator with a PV denominator without saying so.
5. Check that the table foots: the rows must sum to the total, and total minus interest must equal the PV. If they do not, you have misread a row or the units.

**Answer contract:** each annual figure with its year and unit (state $ thousands as given), the unrounded sum, the percentage to two decimals, the denominator used, the filing and period, and the URL. Write plain text and do not leave raw citation tags in the answer.

**Task fact (MSCI, FY2024 10-K, accession 0001408198-25-000053):** the base run took these from a search snippet and did not open the filing, so re-verify them against the filing before use. Operating lease payments in $ thousands: 2025 30,220; 2026 30,361; 2027 24,421; 2028 23,931; 2029 16,573; thereafter 40,099; total 165,605; interest (19,601); PV 146,004. If they hold, the 3-year sum is 85,002 and the share is 85,002/165,605 = 51.33%.
