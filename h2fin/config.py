"""Models, prices and fixed constants for the Finance Agent × Harness² experiment.

Prices are USD per million tokens, from https://platform.claude.com/docs/en/about-claude/pricing
(fetched 2026-10-26). Update here if Anthropic changes them; every cost figure in a run is
computed from this table, so the run manifest records a copy of it.
"""

from __future__ import annotations

# Short aliases accepted on the command line → Claude API model ids.
MODEL_ALIASES = {
    "haiku": "claude-haiku-5-5",
    "sonnet": "claude-sonnet-5-5",
    "opus": "claude-opus-5-5",
    "fable": "claude-fable-5-1",
}

# input, output, cache_write (5m), cache_read — plus optional long-context tier.
PRICES: dict[str, dict] = {
    "claude-haiku-5-5": {
        "input": 0.10, "output": 0.50, "cache_write": 0.125, "cache_read": 0.01,
        "long_threshold": 100_000,
        "long": {"input": 0.50, "output": 2.50, "cache_write": 0.625, "cache_read": 0.05},
    },
    "claude-sonnet-5-5": {"input": 2.0, "output": 10.0, "cache_write": 2.5, "cache_read": 0.10},
    "claude-opus-5-5": {"input": 4.0, "output": 20.0, "cache_write": 5.0, "cache_read": 0.20},
    "claude-fable-5-1": {"input": 10.0, "output": 50.0, "cache_write": 12.5, "cache_read": 0.25},
    # Older ids, in case someone points the runner at them.
    "claude-sonnet-5": {"input": 2.0, "output": 10.0, "cache_write": 2.5, "cache_read": 0.20},
    "claude-opus-5": {"input": 5.0, "output": 25.0, "cache_write": 6.25, "cache_read": 0.50},
    "claude-haiku-4-5": {"input": 1.0, "output": 5.0, "cache_write": 1.25, "cache_read": 0.10},
    "claude-sonnet-4-6": {"input": 3.0, "output": 15.0, "cache_write": 3.75, "cache_read": 0.30},
}

WEB_SEARCH_USD_PER_CALL = 10.0 / 1000.0  # $10 per 1,000 searches

# The Vals harness freezes the world at this date; EDGAR searches are capped at it.
AS_OF_DATE = "2025-04-07"
AS_OF_DATE_HUMAN = "April 07, 2025"

API_URL = "https://api.anthropic.com/v1/messages"
API_VERSION = "2023-06-01"

# Which web-search tool version to attach to the executor. `web_search_20250305` is the basic
# tool; newer versions default to dynamic filtering through code execution, which we do not
# want inside a tool loop we are trying to keep identical across runs.
WEB_SEARCH_TOOL_TYPE = "web_search_20250305"

# Domains the hosted web search must never return: the public question set with its expert
# answers lives on GitHub (vals-ai/finance-agent and this repo), the leaderboard site has worked
# examples, and dataset mirrors exist on Hugging Face.
WEB_SEARCH_BLOCKED_DOMAINS = ["github.com", "raw.githubusercontent.com", "gist.github.com",
                              "vals.ai", "huggingface.co"]

# Always-on harness text is capped so proposals cannot bloat the executor's context.
ALWAYS_ON_CHAR_CAP = 14_000


def resolve_model(name: str) -> str:
    return MODEL_ALIASES.get(name, name)
