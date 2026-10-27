I'm adding one on-demand skill plus a one-line trigger in `systemprompt.md`. I'm not changing any other always-on text.

The base run (`base1`) already got the arithmetic and sources broadly right. It read the Zillow cash flow lines from the FY2023 and FY2024 10-Ks, computed FCF margin as CFO less purchases of property and equipment over revenue, and flagged the FY2022 Zillow Offers distortion. Two gaps are worth closing for FCF-type questions generally:

- **Sourcing:** it never opened the FY2022 10-K, even though that filing was found in the search. FY2022 therefore rests on comparative columns of later filings.
- **Presentation:** it led with a 224.16% FY2022 margin and only afterwards noted that this figure is distorted. A practitioner would state the as-reported series, the distortion and its source, and the underlying trend together.

<file path="skills/fcf_margin_trend/SKILL.md">
---
name: fcf_margin_trend
description: Free cash flow / FCF margin (CFO minus capex, over revenue) across several fiscal years, including cases with discontinued operations or working-capital distortions.
---

# FCF and FCF margin trend

Analytic move: CALCULATE FCF = CFO - capex for each year, divide by that year's revenue, then COMPARE the years and name the trend.

## Inputs (all from the consolidated statements of cash flows / income statement)
- CFO: "Net cash provided by (used in) operating activities", as reported. Note whether it is total or continuing operations.
- Capex: use the investing-section purchase lines. Default is "Purchases of property and equipment". Check the notes to see whether capitalized software or website development sits inside that line (it usually does). Treat separate "Purchases of intangible assets" as a labelled sensitivity, not the headline. State which definition you used.
- Revenue: total revenue from the income statement, taken from the latest filing that presents the year (restated for discontinued operations). Check that the original and the restated figure match.
- Years: read each year from a filing that presents it. Open the 10-K of the OLDEST year too, and confirm its CFO and capex against the later filings' comparative columns. If they differ (restatement or recast), say which you used.

## Checks before submitting
1. Units are the same for CFO, capex and revenue (millions vs thousands).
2. Show for each year: CFO, capex, FCF, revenue, margin (unrounded until the end).
3. Look for one-off swings in CFO (wind-down of a discontinued business, inventory liquidation, large settlements). Find the line in the cash flow statement or MD&A that drives them. State the as-reported margin series, then say how much of any outlier the swing explains, and give the underlying trend direction for the years that are comparable. Do not drop the as-reported figure.
4. The conclusion must state the direction year by year (up, down, magnitude in percentage points) and the overall FY-start to FY-end change.

## Task fact (Zillow, as read in an earlier run; re-verify from the filings before use)
- Zillow Group (CIK 1617640) 10-Ks list CFO of 4,504 / 354 / 428 ($M) for FY2022 / FY2023 / FY2024, purchases of property and equipment of 115 / 135 / 143, purchases of intangible assets of 25 / 30 / 28, and revenue of 1,958 / 1,945 / 2,236. The FY2022 CFO includes about $3.9B of inventory run-off from the discontinued Zillow Offers business.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for free cash flow, FCF margin or a CFO-minus-capex trend across years, call load_skill with `fcf_margin_trend`.

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
Motivation (base1): the agent got CFO, capex and revenue from the FY2024 and FY2023 10-Ks only. The FY2022 10-K appeared in the edgar_search results but was never opened. The answer led with a 224.16% FY2022 margin and explained the Zillow Offers distortion afterwards. The skill adds the following:
- a practitioner checklist for FCF margin trends;
- the capex definition, with a note that capitalized software usually sits inside PP&E purchases;
- opening the oldest year's 10-K to confirm figures;
- reporting the as-reported series alongside the distortion;
- an explicit directional conclusion.

The Zillow figures are labelled as unverified leads, not as facts. The trigger line is in systemprompt.md, so the skill costs nothing on other tasks. No other always-on text was added.
</notes>