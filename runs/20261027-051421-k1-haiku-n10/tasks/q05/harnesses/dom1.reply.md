I'm adding one skill for "who was nominated or appointed to the board in year X" questions, plus a trigger line in `systemprompt.md`. I checked nothing against an answer key, and the base run's answer may be wrong. It submitted Mark S. Finn on the strength of one proxy paragraph, without resolving the year ambiguity.

<file path="skills/board_nominee_lookup/SKILL.md">
---
name: board_nominee_lookup
description: Answer "who was nominated / appointed / elected to the board of company X in year Y" by separating annual-meeting nominees, mid-year appointments and later-seated candidates.
---

# Board nomination / appointment lookup

**Analytic move:** classify and trace. Build the list of every director event in the named calendar year, then say which person the question's wording ("nominated", "appointed", "elected", "to serve") points to.

**Where the facts live**
- Proxy statement (DEF 14A) for that year's annual meeting: "Election of Directors" lists the nominees. Directors who are new that year are usually described by the Nominating Committee paragraph on how they were identified.
- DEFA14A or the voting-results 8-K (Item 5.07) confirm who stood and who was elected.
- 8-K Item 5.02 (and the matching press release) gives mid-year appointments, resignations and the effective date of each.
- The *next* year's proxy narrates a prior-year search. It can name someone who was chosen in year Y but seated in Y+1.

**Procedure**
1. Fix the calendar year Y and list every director event dated in Y: nominees at the Y annual meeting, any Item 5.02 appointment, and any new-director press release. Search for Y-dated press releases and 8-Ks with a query such as "<company> announces nomination board of directors <Y>". Do not rely on the later proxy alone.
2. Separate three categories: (a) a new nominee standing for election at the Y meeting, (b) a director appointed between meetings in Y, and (c) a candidate identified in Y but seated in Y+1. Say which category each person is in, with the dated source.
3. Compare the Y nominee slate against the prior year's slate to find who is new. If nobody is new, say so, then check Item 5.02 filings in Y.
4. If a Y-dated 8-K or press release exists in search results, open it before answering. Do not skip it in favour of a later document.
5. When the wording is ambiguous between a Y nominee and a person seated in Y+1, name the person who matches the question's year, and mention the other with its date.

**Answer contract:** the name(s) with the event type (nominated / appointed / elected), the date, the document and section, the full Y slate when relevant, and any unresolved ambiguity stated plainly. Say whether each fact came from an opened filing or a search excerpt.

**In this task (BBSI, 2024):** the facts below were seen in earlier runs; confirm them before relying on them.
- The April 22, 2024 DEFA14A listed eight nominees: Carley, Clabby, Cusick, Kramer, Meeker, Moradi, Morehouse, Price.
- The 2025 DEF 14A says the Nominating Committee searched in 2024 and the Board selected Mark S. Finn. He was seated effective April 7, 2025.
- A June 5, 2024 8-K from BBSI's IR site was returned by search but was never opened. Check whether it reports a board event before concluding.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks who was nominated, appointed or elected to a company's board of directors in a given year, call load_skill with `board_nominee_lookup`.

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
Motivation (base1): the agent searched with a null query and then ran a single targeted search on Finn. It never opened the June 5, 2024 8-K or any 2024-dated press release, and it never compared the 2024 slate with the prior year. It submitted "Mark S. Finn" after one proxy paragraph and admitted a caveat that the proxy shows no formal 2024 nomination. A person selected in 2024 but seated in April 2025 is a different category from a 2024 nominee. The skill makes the agent enumerate Y-dated director events and classify them, and flags the unopened 8-K as unresolved. The facts about this task are labelled as unverified, and no answer is asserted. The always-on cost is one trigger line. I made no changes to tool guidance, because procedure on tools is owned elsewhere.
</notes>