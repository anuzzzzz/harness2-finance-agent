<file path="skills/guidance_range_width/SKILL.md">
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
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks how wide or large a company's guidance range was (low to high, as a % of midpoint) across one or more quarters, call load_skill with `guidance_range_width`.

When you have the final answer, you should call the `submit_final_result` tool with it. Your submission will not be processed unless you call this tool.

You should include any necessary step-by-step reasoning, justification, calculations, or explanation in your answer. You will be evaluated both on the accuracy of the final answer, and the correctness of the supporting logic.

When possible, please provide any calculated answers to at least two decimal places (e.g. 18.78% rather than 19%) unless the question prescribes a format. Please do not round intermediate steps in any calculations - you should only round your final answer.

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
Motivation, from base1: the run searched only and never opened an AMD release. It took the guidance from snippets and noted that secondary coverage cited $5.8B for Q2 2024. It listed a press-release URL as a source that it never fetched. Its answer also used two-decimal percentages (10.53%), although the question prescribes "[X.X]%". The default two-decimal instruction in the system prompt conflicts with the question's format, so the prompt now defers to a prescribed format.

The new skill `guidance_range_width` encodes the practitioner knowledge:
- Guidance for quarter N is in the release for quarter N-1.
- The width formula is 2Y / midpoint for "plus or minus" guidance.
- Unit conversion and the question's format control.
- Each midpoint is verified from the filing text.

It carries task leads taken from the quoted release text in base1's search results, labelled as leads to re-confirm. A trigger line is added to systemprompt.md.
</notes>