---
name: concentration_risk_disclosure
description: Answer "what is company X's vendor / supplier / customer / bank concentration risk as of FY Y" from a 10-K, with quotes, the scope of each dependency, and no imported or inferred names.
---

# Concentration-risk questions (vendor, supplier, customer, sponsor bank, geography)

ANALYTIC MOVE: classify and trace. Find every place the filing discloses a dependency, then say what is concentrated, on how many counterparties, and with what quantification.

Where it lives in a 10-K (check each one, in this order):
1. Financial-statement notes. Note 1 "Summary of Significant Accounting Policies" often has a "Concentration Risk" or "Concentration of Credit Risk" paragraph. A separate "Significant customers" or "Major suppliers" note may also exist. The note is the controlling source for the as-of year.
2. Item 1A Risk Factors. Search for "single third-party", "sole source", "depend on", "sponsor bank", "limited number of vendors". These state the scope of the dependency, such as which services and which regions, and often go beyond the note.
3. Item 1 Business (sponsorship, processing, supply relationships) and MD&A (percentage-of-revenue or volume statements, such as "no single customer exceeded X%").

Answer contract, with each part labelled:
- The dependency, quoted verbatim from the filing and tied to a section and page: who or what is concentrated, how many counterparties ("one vendor"), which regions and services.
- Whether the counterparty is named. If the filing does not name it, say "not named in the filing". Never supply a name from memory, from inference, or from a different filing or year. If a name is unconfirmed, leave it out.
- Quantification as of the as-of date, with units and period: % of revenue or volume, or balances. If none is disclosed, say so. Give the prior-year comparison only if the filing gives it.
- Contractual exit terms and mitigants, such as the termination notice period and backup-systems language. Quote them. Do not reword them into a stronger or weaker claim.
- Offsetting concentrations (customer, reseller or merchant percentage limits) kept separate from the vendor dependency. Report them only if retrieved from the opened text.
- A one-line conclusion that assesses the risk (for example, single-point dependency, no quantified share) using only disclosed facts.

Checks before submitting:
- Use the filing for the as-of fiscal year. An older prospectus or earlier 10-K (for example, one that listed two vendors) is not the as-of position. Open and cite it only if you use it, and label it historical.
- Every figure or name in the answer must come from text you retrieved. Tool-output truncation means a claim is unverified until you re-retrieve it with a narrower question.
- Cite only documents you actually opened. End with the sources dictionary in the format the system prompt prescribes.

In this task (Shift4 Payments, FY2024 10-K, accession 0001794669-25-000011, four-20241231.htm), verified in the retrieved text:
- Note 1, "Concentration Risk": "The Company's merchant processing activity in North America is facilitated by one vendor." The note adds that the company believes the vendor maintains appropriate backup systems and alternative arrangements. The vendor is not named, and no percentage or 2023 comparison is given.
- The same note, on the sponsor bank: Shift4 is not a "member bank" in North America and relies on a sponsorship agreement with a member bank. If the agreement is breached, the bank may terminate it, and the company would have 180 days to find an alternative sponsor. The bank is not named in the note.
- Item 1A: in the U.S., EU and Canada the company depends on a single third-party processor for services such as merchant authorization and settlement. Re-retrieve the full sentence and cite it, because the earlier retrieval was truncated.
- A sponsor-bank name (for example, "Citizens") was not confirmed in the retrieved text. Do not assert one.
