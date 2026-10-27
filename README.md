# Harness² × Finance Agent (public set), Anthropic-only

Does **recursive agent harnessing** ([Harness², Google, Oct 2026](https://arxiv.org/abs/2610.14224))
improve a frozen Claude model on **SEC-filing analyst questions**? This repo runs that experiment
end to end on the 50 open questions of the
[Vals AI Finance Agent benchmark](https://www.vals.ai/benchmarks/finance_agent), with nothing
but an `ANTHROPIC_API_KEY`:

* the published Finance Agent harness (system prompt, tools, loop rules) is the **base harness**;
* a port of the Harness² *Propose → Probe → Compose* loop edits that harness per question, with
  no answer key in sight, and keeps a library of adopted harnesses and lessons across questions;
* a separate rubric judge grades the base answer and the Harness² answer afterwards.

Results land in [`results/`](results/README.md) (one row per run) and every trajectory, harness
diff and library entry is kept as a workflow artifact.

## Run it

1. Add the repository secret `ANTHROPIC_API_KEY` (Settings → Secrets and variables → Actions).
   Optionally add a repository *variable* `SEC_USER_AGENT` in the form `Your Name you@example.com`.
   The SEC rejects every request whose User-Agent lacks an e-mail address (HTTP 403, "undeclared
   automated tool"); without the variable the workflow uses your GitHub noreply address.
2. Actions → **experiment** → *Run workflow*. Defaults: 10 questions, k=1, executor Haiku 5.5,
   editor and judge Sonnet 5.5, web search on, stop past $40.
3. When it finishes: the summary is committed to `results/<run_id>.json` and the table in
   `results/README.md`; the full run (`runs/<run_id>/…`) is the workflow artifact.

Locally (same thing):

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-…
python -m h2fin.experiment --tasks 10 --k 1 --executor haiku --editor sonnet --judge sonnet
python -m h2fin.experiment --offline --tasks 2 --k 2      # scripted models, no key, no network
```

A run is resumable: re-running with the same `--run-id` skips finished questions. `--base-reps 0` turns
off the matched-cost control (saves ~3 cheap rollouts per question).

## What one run does

For each question (in a fixed, category-stratified order), with budget `k`:

| stage | what happens | labels |
|---|---|---|
| reference | run the question `k` times under the base harness | `base1..basek` |
| propose | an **INV** editor (how the agent works) and a **DOM** editor (what a practitioner knows), `k` of each, read the task, the base rollouts, the base harness and the library, and return edited harness files | `inv_i`, `dom_i` |
| probe | run each candidate harness once on the same question | |
| compose | `k` composers read everything and emit one final harness each (merge, adopt one, or `KEEP_BASE`) | `agg_i` |
| select | k>1: a blind selector picks one final *answer* (harnesses hidden); k=1: trivial | |
| reflect | an experience record (what each edit did; one transferable lesson, if the evidence supports one) → library | |

`base1` is the **base condition**; the chosen final is the **Harness² condition**. Both are graded
afterwards with the public rubric (`correctness` criteria + one `contradiction` criterion) by a
Claude judge, majority of 3 samples per criterion. *Correct* = every criterion passed (Vals'
accuracy); *pass rate* = share of criteria passed, which has far more resolution on 10–50 questions.

The grader is never visible to the loop: the editors' prompts carry the paper's answer-free
boundary, and the code path that reads answers and rubrics (`judge.py`) runs only after all
questions are done.

## What is faithful, what is changed

| | published | here |
|---|---|---|
| Base harness | Vals `INSTRUCTIONS_PROMPT`, tools, loop rules (text-only turn → "Continue.", only `submit_final_result` ends, 50 turns) | same (prompt copied; question moved to the user turn) |
| `edgar_search` | sec-api.io full-text search (paid) | SEC's own full-text search (`efts.sec.gov`), same parameters, plus ticker→CIK resolution; dates capped at 2025‑04‑07 as in Vals |
| `web_search` | Tavily, results capped at 2025‑04‑07 | Claude's hosted web-search tool (`web_search_20250305`, `max_uses` 8). **No date cap is possible**, so post‑April‑2025 pages can leak; use `--no-web-search` for an EDGAR-only run |
| `parse_html_page`, `retrieve_information` | as published | as published (retriever = executor model; 700k-char cap per inserted document) |
| Judge | GPT‑5.2, mode of 3 | Claude (Sonnet 5.5 by default), majority of 3 per criterion |
| Questions | 337 private test | the 50 public validation questions |
| Harness² surface | 8 components incl. scripts, subagents, plugins; editors edit files in an OpenCode session | 5 components: `systemprompt.md`, `guardrails.md`, `LongTermMEMORY.md`, `tool_guidance.md`, `skills/*/SKILL.md` (on demand via a `load_skill` tool). Editors return `<file>` blocks instead of editing disk. No scripts/subagents/plugins: the executor is an API tool loop |
| Recursion | parallel and sequential modes | parallel mode only |
| Validation | proposal discarded whole on a broken skill trigger, template braces, missing script | same rule for skill triggers/frontmatter/always-on cap (14k chars); a discarded proposal falls back to the base |
| Prompts | `harness2/core/prompts.py` | ported nearly verbatim (`h2fin/prompts.py`), surface and output-format sections rewritten |

So: **scores are not comparable to the Vals leaderboard** (different test set, judge, search
tool), but base vs. Harness² *within a run* is an apples-to-apples comparison, which is the
experiment.

## Cost

Every API response is priced from the table in `h2fin/config.py` (fetched from Anthropic's
pricing page on 2026‑10‑26) and reported per rollout, per task and per run. Rough guide at k=1:

| executor | per question (4 rollouts + 4 editor calls + judging) | 10 questions | 50 questions |
|---|---|---|---|
| Haiku 5.5 | ≈ $1–1.5 | ≈ $10–15 | ≈ $50–75 |
| Sonnet 5.5 | ≈ $2.5–6 | ≈ $25–60 | — |

k=5 multiplies the rollout and editor counts by about 5. `--max-total-cost` stops starting new
questions past a ceiling; `--max-run-cost` caps a single rollout.

## Red-team notes: ways this experiment can mislead, and what guards against each

| threat | status |
|---|---|
| **Cost mismatch.** Harness² spends ~4 rollouts + 4 editor calls per question; a plain base run spends one. Gains could be "more tries", not "better harness". | `--base-reps 3` (default) runs 3 extra base rollouts and picks one with the same blind selector: the *matched-cost control*. Harness² must beat that, not the single base run. The oracle best-of-base is reported as the ceiling of what re-running alone could give. |
| **Noise floor unknown.** Haiku at default temperature varies run to run; a 7-point pass-rate difference on 10 questions may be nothing. | The control rollouts also give the within-question SD of base pass rate; the summary reports a paired sign test and a bootstrap CI. Treat anything inside the CI as nothing. |
| **n is tiny.** 10 questions cannot distinguish a 5-point effect from zero. | Pilot only. The 50-question run is the first one worth quoting, and even that only detects large effects. |
| **k=1 composer prompt said "a defect in 1/1 is noise".** Ported faithfully from the official prompt, where the sentence is written for k>1; at k=1 it tells the composer to ignore the only base failure it has. Run 1 showed the composer rejecting two correct candidates on that reasoning. | Deviation from the official text: at k=1 the sentence is replaced by one that treats the candidates' rollouts as the second and third samples. k≥2 keeps the original wording. |
| **The base run's answer leaks into the Harness² run.** The editors see the base trajectory and may write its findings into the harness ("in this task, …"), as the paper allows. At k=1 that makes `agg1` partly a re-run with the base's answer in the prompt: ties are inflated when the base was right, and a wrong base answer can be entrenched. | Inherent to the method. The library-transfer effect (next question starts from the base harness) and the matched-cost control are the measurements that do not suffer from it. |
| **The gain may be one obvious rule.** Run 2's edits all reduced to "open the primary filing instead of answering from web snippets", which a person would write in five minutes. | `--static-guidance` runs that hand-written rule (`harness.STATIC_TOOL_GUIDANCE`) as a fixed arm. Harness² has to beat it, not just the stock prompt. |
| **A stronger editor can inject knowledge.** With Sonnet editing and Haiku executing, "harness improvement" and "Sonnet knew the answer" are confounded. | Run the ablation `--editor haiku` (same model edits and executes, as in the paper's same-model table). |
| **Web search is a leaky channel.** It is not frozen at April 2025 and can return pages that discuss this benchmark. Run 1's library lessons were mostly "when sec.gov fails, go to web search", i.e. the loop learned to lean on the leaky channel. | Benchmark-discussion domains are blocked at the tool; `h2fin.audit` flags suspect URLs/titles. The clean primary condition is `--no-web-search` (EDGAR is date-capped). |
| **Judge = model, same family as editor.** Style preferences and shared beliefs can move scores. | Per-criterion majority of 3 reduces variance, not bias; the summary reports unanimity, parse failures and mean answer length per condition (a length gap is a judge-gaming tell). Spot-check `graded.json` on any flipped task. |
| **Editors could rewrite the task frame.** Dropping "answer as of April 07, 2025" or the submit instruction would change the task, not the harness. | Validation now rejects a proposal whose `systemprompt.md` lost the as-of date, the submit instruction or the sources format. |
| **Temperature.** Vals ran the executor at temperature 0; this runs the API default. | Not changed (thinking-enabled models do not accept a temperature override); the noise-floor measurement is the mitigation. |
| **Training data.** Claude's training runs past these filings and past the public question file. | Inflates both conditions equally and shrinks the headroom; it cannot be removed, only kept in mind. |

## Caveats, in order of importance

1. **n is small.** 10 questions tell you whether the loop works and roughly where it helps;
   treat differences under ~15 points of pass rate as noise. Run all 50 before concluding anything.
2. **Web search can leak.** The questions are frozen at April 7, 2025; hosted web search is not,
   and the public question set (with expert answers) is on GitHub. The search tool therefore blocks
   `github.com`, `raw.githubusercontent.com`, `gist.github.com`, `vals.ai` and `huggingface.co`;
   every query and result URL is logged, and `python -m h2fin.audit runs/<run_id>` flags any hit
   on those domains and prints answer lengths per stage (a judge-gaming tell). `--no-web-search`
   removes the channel entirely.
3. **The judge is a model.** Per-criterion majority voting reduces variance, not bias; look at
   the per-task `graded.json` before trusting a single flip.
4. **Narrower surface than the paper.** No scripts, subagents or plugins, so some of the paper's
   levers (deterministic helpers, tool-loop hooks) are unavailable here.

## Layout of a run

```
runs/<run_id>/
  manifest.json          models, args, price table, as-of date
  base_harness/          the base tree
  library/               INDEX.md + harnesses/<task>/{harness/, EXPERIENCE.md}
  tasks/<task_id>/
    rollouts/<label>.{json,md}   full trajectories (base1, inv1, dom1, agg1, …)
    harnesses/<label>/           each candidate/final tree, plus <label>.reply.md (editor reply)
    record.json                  the whole task record (selection, experience, costs)
    graded.json                  judge verdicts per rollout (written after the loop)
  summary.{json,md}      the run's numbers
```

## Attribution

* Prompts and method: [google-research/harness2](https://github.com/google-research/harness2),
  Apache‑2.0, © 2026 Google LLC — adapted in `h2fin/prompts.py`.
* Base harness, tool definitions and `data/public.csv`:
  [vals-ai/finance-agent](https://github.com/vals-ai/finance-agent), MIT, © 2025 Vals AI, Inc.
* Harness² paper: *Harness²: Recursive Agent Harnessing for an Open World*, arXiv:2610.14224
  (Google Cloud AI Research / Northwestern University, October 2026).
* Finance Agent Benchmark: Bigeard et al., arXiv:2508.00828.
