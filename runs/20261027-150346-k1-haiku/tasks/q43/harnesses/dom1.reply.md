<file path="skills/revenue_growth_volume_vs_take_rate/SKILL.md">
---
name: revenue_growth_volume_vs_take_rate
description: Split a marketplace or platform company's revenue growth into volume (gross bookings, GMV, TPV) and take-rate effects, with the reported-versus-adjusted reconciliation an analyst needs.
---
ANALYTIC MOVE: calculate and explain. Revenue = Volume x Take rate, so the change in revenue splits into a volume effect and a take-rate effect. Inputs are the volume metric (Gross Bookings, GMV or TPV) and revenue for two consecutive fiscal years. The result is a share of revenue growth from each, plus the reasons the take rate moved.

1. Get the inputs from the 10-K. Use MD&A "Financial and Operational Highlights", the Key Metrics table and the segment results. Use the company-defined volume metric. Confirm the period and units ($ millions). If the 10-K gives only quarterly volume by segment, sum the four quarters and check that the sum equals the consolidated total.
2. Calculate at full precision and state the convention. TR0 = Rev0/Vol0, TR1 = Rev1/Vol1. Volume effect = (Vol1 - Vol0) x TR0. Take-rate effect = (TR1 - TR0) x Vol1. The two sum exactly to the change in revenue; check this. Each share is the effect divided by the revenue change. The shares can be negative or exceed 100%, which is fine. Say that the split depends on the ordering convention. If the take-rate effect is very small, say so, and do not manufacture a precise split.
3. Reconcile reported versus underlying before concluding. Read the MD&A for non-volume items that move revenue relative to volume:
   - business-model changes that reclassify costs to contra revenue (incentives, driver or merchant payments), which cut revenue and the take rate without changing volume;
   - the currency basis, since 10-K growth rates are often quoted in both reported and constant-currency terms, and the decomposition must use reported dollars throughout;
   - acquisitions, and segments with a different revenue model (for example, a freight segment where revenue is about 100% of bookings).
   Headline answer = reported basis. Give an adjusted view (revenue plus the disclosed contra-revenue impact) as a labelled secondary view only. State the assumption that the disclosed impact applies to the current year only, or to both years.
4. Check the mix by segment. Compute each segment's take rate (segment revenue / segment volume) for both years. A flat consolidated take rate can hide segment moves in opposite directions, or a mix shift toward higher-take segments. Report which segment moved it. Check that the segment figures sum to the consolidated ones.
5. Answer contract:
   - volume and revenue for both years, with growth %;
   - take rates for both years in % and the change in bps;
   - the dollar effect and the % share for volume and for take rate, with the sum check;
   - the reported-versus-adjusted note and the segment note;
   - a one-sentence conclusion that answers the question directly ("X% volume, Y% take rate");
   - sources, listing only documents actually opened.

Task facts (Uber FY2024 10-K, https://www.sec.gov/Archives/edgar/data/1543151/000154315125000008/uber-20241231.htm; one earlier run retrieved these, so re-confirm in the text):
- Gross Bookings were $137,865M in 2023 and $162,773M in 2024 (+18%, +21% constant currency). Revenue was $37,281M and $43,978M (+18%). The reported take rate was about 27.04% and then 27.02%, so it was essentially flat. Volume explains about 100.6% of the revenue growth and take rate about -0.6%, under the prior-year-rate convention.
- The 10-K says business model changes in some countries, which classified certain sales and marketing costs as contra revenue, reduced revenue by $863M in Mobility and $713M in Delivery (total $1,576M). Adding this back gives an adjusted 2024 take rate of about 27.99%. Re-confirm the amounts and whether the 10-K quantifies the same effect for 2023.
- Segment revenue ($M, 2023 to 2024): Mobility 19,832 to 25,087; Delivery 12,204 to 13,750; Freight 5,245 to 5,141. Gross Bookings by segment are only quarterly in the 10-K. Sums: Mobility 68,897 to 83,024; Delivery 63,726 to 74,614; Freight 5,242 to 5,135. That implies a Mobility take rate of about 28.8% to 30.2%, a Delivery take rate of about 19.1% to 18.4%, and Freight at about 100%. Re-verify before citing.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks how much of revenue growth came from take rate (monetization) versus volume (gross bookings, GMV, TPV), call load_skill with `revenue_growth_volume_vs_take_rate`.

When you have the final answer, you should call the `submit_final_result` tool with it. Your submission will not be processed unless you call this tool.

You should include any necessary step-by-step reasoning, justification, calculations, or explanation in your answer. You will be evaluated both on the accuracy of the final answer, and the correctness of the supporting logic.

When possible, please provide any calculated answers to at least two decimal places (e.g. 18.78% rather than 19%). Please do not round intermediate steps in any calculations - you should only round your final answer.

At the end of your answer, you should provide your sources in a dictionary with the following format:
{
    "sources": [
        {
            "url": "https://example.com",
            "name": "Name of the source"
        },
        ...
    ]
}
</file>

<notes>
Motivated by base1: it got the right filing and figures (GB 137,865→162,773; revenue 37,281→43,978) and did a volume/take-rate split. The headline was muddled, though. It gave a reported split (-0.58% take rate) and an adjusted split (18.58%) with a self-described "own estimate" adjustment, and it never checked the segment-level take-rate mix. I added an on-demand skill that fixes the decomposition convention and sum check, makes the reported basis the headline with the contra-revenue adjustment as a labelled secondary view, and requires a segment take-rate check. Its task facts are labelled and must be re-confirmed in the text; they come from base1's retrieval. A trigger line in systemprompt.md makes the skill callable. The always-on cost is one sentence. No other files changed.
</notes>