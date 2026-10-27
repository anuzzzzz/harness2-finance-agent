import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from h2fin import harness, llm, tools, experiment  # noqa: E402


def test_base_tree_is_valid_and_has_vals_prompt():
    t = harness.base_tree()
    assert harness.validate(t) == []
    assert "April 07, 2025" in harness.system_blocks(t)[0]["text"]
    assert harness.skills_of(t) == {}


def test_apply_patch_and_skill_trigger_rule():
    base = harness.base_tree()
    reply = ('<file path="skills/foo/SKILL.md">\n---\nname: foo\ndescription: d\n---\nbody\n</file>\n'
             "<notes>\nadded skill\n</notes>")
    tree, notes, keep = harness.apply_patch(base, reply)
    assert not keep and notes == "added skill"
    assert any("trigger" in e for e in harness.validate(tree))   # not named in always-on text
    reply2 = reply + '\n<file path="guardrails.md">\nWhen X, call load_skill with `foo`.\n</file>'
    tree2, _, _ = harness.apply_patch(base, reply2)
    assert harness.validate(tree2) == []
    # untouched files are inherited; KEEP_BASE with no file blocks keeps the base
    assert tree2["systemprompt.md"] == base["systemprompt.md"]
    t3, n3, k3 = harness.apply_patch(base, "<notes>\nKEEP_BASE\n</notes>")
    assert k3 and t3 == base and n3 == "KEEP_BASE"


def test_always_on_cap():
    base = harness.base_tree()
    base["guardrails.md"] = "x" * 20000
    assert any("cap" in e for e in harness.validate(base))


def test_prices_including_haiku_long_context():
    u = {"input_tokens": 1000, "output_tokens": 1000}
    c = llm.price_usage("claude-haiku-5-5", u).cost_usd
    assert abs(c - (1000 * 0.10 + 1000 * 0.50) / 1e6) < 1e-9
    big = {"input_tokens": 150_000, "output_tokens": 100, "server_tool_use": {"web_search_requests": 2}}
    c2 = llm.price_usage("claude-haiku-5-5", big)
    assert c2.web_search_requests == 2
    assert abs(c2.cost_usd - ((150_000 * 0.50 + 100 * 2.50) / 1e6 + 0.02)) < 1e-9


def test_efts_hit_mapping():
    hit = {"_id": "0001065280-25-000044:nflx-20241231.htm",
           "_source": {"ciks": ["0001065280"], "adsh": "0001065280-25-000044", "form": "10-K",
                       "file_date": "2025-01-27", "display_names": ["NETFLIX INC (NFLX)"]}}
    row = tools._hit_to_row(hit)
    assert row["url"] == "https://www.sec.gov/Archives/edgar/data/1065280/000106528025000044/nflx-20241231.htm"
    assert row["form"] == "10-K"


def test_date_clamp():
    s, e = tools._clamp_dates("2024-01-01", "2026-01-01", "2025-04-07")
    assert (s, e) == ("2024-01-01", "2025-04-07")


def test_task_order_is_stratified_and_stable():
    a = experiment.load_tasks(n=10)
    b = experiment.load_tasks(n=10)
    assert [t["task_id"] for t in a] == [t["task_id"] for t in b]
    assert len({t["category"] for t in a}) >= 6


def test_offline_end_to_end(tmp_path):
    rc = experiment.main(["--offline", "--tasks", "2", "--k", "2", "--run-id", "t", "--out", str(tmp_path)])
    assert rc == 0
    s = json.loads((tmp_path / "t" / "summary.json").read_text())
    assert s["n_tasks"] == 2 and s["k"] == 2
    assert s["harness2"]["correct"] >= s["base"]["correct"]
    assert (tmp_path / "t" / "library" / "INDEX.md").is_file()
    assert (tmp_path / "t" / "tasks" / s["tasks"][0]["task_id"] / "rollouts" / "agg1.md").is_file()
    (ROOT / "results" / "t.json").unlink(missing_ok=True)


def test_agent_loop_handles_server_tools_and_pause_turn():
    from h2fin.agent import run_agent
    from h2fin.llm import MockLLM
    from h2fin.mock import FakeHTTP
    seen = {"turns": 0, "roundtrip_ok": False}

    def script(payload):
        seen["turns"] += 1
        msgs = payload["messages"]
        if seen["turns"] == 1:
            return {"content": [{"type": "thinking", "thinking": "hmm", "signature": "sig"},
                                {"type": "server_tool_use", "id": "srv1", "name": "web_search", "input": {"query": "netflix buyback"}},
                                {"type": "web_search_tool_result", "tool_use_id": "srv1",
                                 "content": [{"type": "web_search_result", "url": "https://x", "title": "X", "encrypted_content": "ENC", "page_age": "2025"}]}],
                    "stop_reason": "pause_turn"}
        if seen["turns"] == 2:
            # the paused assistant turn must have been resent verbatim, encrypted content included
            last = msgs[-1]
            seen["roundtrip_ok"] = last["role"] == "assistant" and any(
                b.get("type") == "web_search_tool_result" and b["content"][0]["encrypted_content"] == "ENC" for b in last["content"])
            return {"content": [{"type": "text", "text": "Searching EDGAR."},
                                {"type": "tool_use", "id": "t1", "name": "edgar_search", "input": {"search_query": "buyback", "ciks": ["NFLX"]}}],
                    "stop_reason": "tool_use"}
        if seen["turns"] == 3:
            assert msgs[-1]["role"] == "user" and msgs[-1]["content"][0]["type"] == "tool_result"
            return {"content": [{"type": "text", "text": "done thinking"}], "stop_reason": "end_turn"}
        return {"content": [{"type": "tool_use", "id": "t2", "name": "submit_final_result", "input": {"final_result": "42"}}],
                "stop_reason": "tool_use"}

    llm = MockLLM("haiku", script)
    t = run_agent("q?", harness.base_tree(), llm, task_id="x", label="base1",
                  retriever_factory=lambda: MockLLM("haiku", script), http=FakeHTTP())
    assert seen["roundtrip_ok"]
    assert t.submitted and t.final_answer == "42" and t.stop == "submitted"
    assert t.steps[0].searches[0]["query"] == "netflix buyback" and t.steps[0].searches[0]["results"][0]["url"] == "https://x"
    assert t.steps[1].calls[0]["name"] == "edgar_search" and not t.steps[1].calls[0]["is_error"]
    assert t.turns == 4 and t.steps[2].stop_reason == "end_turn"


def test_web_search_tool_blocks_answer_key_domains():
    from h2fin import config
    ctx = tools.ToolContext(retriever=None)  # type: ignore[arg-type]
    ws = tools.tool_schemas(ctx, web_search=True, max_web_searches=3)[0]
    assert ws["name"] == "web_search" and ws["max_uses"] == 3
    assert "github.com" in ws["blocked_domains"] and "vals.ai" in ws["blocked_domains"]
    assert set(config.WEB_SEARCH_BLOCKED_DOMAINS) <= set(ws["blocked_domains"])


def test_sec_user_agent_always_carries_an_email(monkeypatch=None):
    import os
    os.environ["SEC_USER_AGENT"] = "no email here"
    assert "@" in tools._ua()
    os.environ["SEC_USER_AGENT"] = "Jane Doe jane@example.com"
    assert tools._ua() == "Jane Doe jane@example.com"
    del os.environ["SEC_USER_AGENT"]
