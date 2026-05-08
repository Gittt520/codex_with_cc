#!/usr/bin/env python3
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
text = (repo / "AI_INSTALL.md").read_text(encoding="utf-8")

assert ".codex/skills/codex-with-cc" in text
assert "$CODEX_HOME/skills/codex-with-cc" in text
assert "$codex-with-cc" in text
assert "Any user mention of child-agent, subagent, sub-agent, child-thread, subthread, delegation, worker-execution, or Chinese equivalents such as 子代理、子线程、多代理、委派、派工、执行层 is a workflow trigger." in text
assert "codex_with_cc/scripts/delegate_to_claude.py" not in text
assert "skills/codex-with-cc/scripts/delegate_to_claude.py" in text
assert "skills/codex-with-cc/windows_scripts/delegate_to_claude.ps1" in text
assert "skills/codex-with-cc/macos_scripts/delegate_to_claude.sh" in text
assert "$env:CODEX_HOME\\skills\\codex-with-cc\\windows_scripts\\test_delegate_runtime.ps1" in text
assert "${CODEX_HOME:-$HOME/.codex}/skills/codex-with-cc/macos_scripts/test_delegate_runtime.sh" in text
assert "Windows 全局 skill 不要安装 `macos_scripts`；macOS 全局 skill 不要安装 `windows_scripts`。两个平台都必须安装共享的 `scripts/*.py`。" in text
assert "安装或更新 skill 时必须清理旧安装产物：`docs/codex_with_cc`、`doc/codex_with_cc` 和 `AGENTS.md` 中的托管块。" in text
assert "全局 skill 运行时以当前工作目录作为目标项目根目录" in text
assert "macOS 支持尚未实现" not in text

print("ai install doc tests passed")
