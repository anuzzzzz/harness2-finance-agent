<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with company and date filters. If web_search returns nothing, retry once with a short non-empty query (never an empty or null one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Use input_character_ranges on long filings. Confirm each figure's period, unit and basis in the retrieved text.
- When the question asks for a definition, retrieve the company's own wording from the opened filing and quote or closely paraphrase it. Do not reconstruct a definition from snippets or from general knowledge of the metric.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit.
- Respect the as-of date. Filings dated after it may be mentioned only as labelled later developments, never as the basis of the answer.
- Cite only documents you opened and retrieved from. Do not list a filing, PDF or letter seen only in search results, and do not attribute a claim to a document you did not retrieve it from. Copy URLs exactly as returned.
- Write the final answer in plain text. Never paste citation markup such as <cite> tags. Submit with submit_final_result once the claims are verified in primary text.
</file>

<file path="skills/company_kpi_definition_lookup/SKILL.md">
---
name: company_kpi_definition_lookup
description: Answer "does the company report metric X (retention, churn, ARR, backlog, etc.) and how does it define it" from the 10-K/10-Q, including how the disclosure changed over time.
---
ANALYTIC MOVE: classify and trace. Decide whether the company reports the metric, in which documents, with what exact definition and latest value, and whether the disclosure changed.

1. Controlling source: the latest 10-K before the as-of date, in Item 7 MD&A "Key Business Metrics" or a section named for the metric. Check the latest 10-Q too. Earnings releases and prepared remarks only repeat the value. Retrieve the heading, the definition, the value and its as-of date, all from the opened text.
2. Check the gross and the net variant separately. Report each as reported, or state "not reported" only after retrieving from the relevant section of the opened filing. Do not infer absence from one failed retrieval. Re-ask with different wording.
3. Definition contract. Give the company's own wording on: the numerator and denominator (or what is compared); what is included and excluded (expansion, price, churn, contract terms under one year); the measurement basis (ARR, constant currency, annualisation method); and the measurement date. Give the latest value with its date and unit.
4. Disclosure history. Metrics are sometimes changed after SEC staff comment letters. Check the prior-year 10-K and the CORRESP/UPLOAD letters in edgar_search results. Open them before saying a metric was dropped or added, and give the period of the change. Open the letters if you cite them.
5. Answer: yes/no per metric, then the definition, the value with its date, and the history. State plainly anything you did not verify.

Task facts (Workday, WDAY; from search results, re-confirm in the opened text):
- The FY2025 10-K (fiscal year ended Jan 31, 2025, filed 2025-03-11) is https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm. The 10-Q for the quarter ended Oct 31, 2024 is https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm.
- SEC correspondence found in edgar_search: CORRESP filed 2024-09-04 (https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm) and an UPLOAD staff letter dated 2024-08-20. A later 10-K for FY2026 may appear in search results. It postdates the 2025-04-07 as-of date, so do not use it.
- Snippet-level leads, not yet confirmed from opened text: the FY2025 10-K carries a "Gross Revenue Retention Rate" section with a value of about 98%, and Workday told the SEC it would drop net retention disclosure after the quarter ended Oct 31, 2024. Retrieve the definition wording from the 10-K itself.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks whether a company reports a business metric (retention, churn, ARR, backlog and the like) and how it defines it, call load_skill with `company_kpi_definition_lookup`.

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
Motivating moment: base1 did one edgar_search and one null-query web_search, then submitted. It never parsed the FY2025 10-K. The definition (ARR basis, exclusions, constant currency) and the history of net-retention disclosure came from snippets. The sources list included a URL it had not seen in full (a malformed ".../000010149/filename1.pdf" link) and a prepared-remarks PDF it never opened. It also made an empty-query search.
- tool_guidance.md: short always-on rules. A definition must be retrieved from opened text. Cite only opened documents. Respect the as-of date. Never send an empty query.
- New skill company_kpi_definition_lookup, with a trigger line in systemprompt.md. It sets out what a KPI-definition answer must contain: the gross and net variants, the numerator/denominator, inclusions and exclusions, the measurement basis and date, and the disclosure history via the SEC correspondence. It carries verified-from-search task leads (the 10-K and 10-Q URLs and the CORRESP/UPLOAD letters), labelled to be re-confirmed. The snippet-level claims (98%, net retention dropped) are marked as unconfirmed leads, not facts.
</notes>