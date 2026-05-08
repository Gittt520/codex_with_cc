#!/usr/bin/env python3
from pathlib import Path
import re

repo = Path(__file__).resolve().parents[1]
skill = repo / "skills" / "codex-with-cc"
skill_md = skill / "SKILL.md"
openai_yaml = skill / "agents" / "openai.yaml"

assert (skill / "CODEX_WITH_CC.md").exists()
assert (skill / "scripts" / "runtime.py").exists()
assert (skill / "scripts" / "delegate_to_claude.py").exists()
assert (skill / "scripts" / "install_codex_with_cc.py").exists()
assert (skill / "windows_scripts" / "delegate_to_claude.ps1").exists()
assert (skill / "macos_scripts" / "delegate_to_claude.sh").exists()
assert "docs/codex_with_cc" not in (skill / "CODEX_WITH_CC.md").read_text(encoding="utf-8")

text = skill_md.read_text(encoding="utf-8")
frontmatter = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
assert frontmatter, "SKILL.md must start with YAML frontmatter"
frontmatter_text = frontmatter.group(1)

assert "name: codex-with-cc" in frontmatter_text
description_match = re.search(r"^description:\s*(.+)$", frontmatter_text, re.MULTILINE)
assert description_match, "description is required"
description = description_match.group(1)
assert len(description) <= 1024
for trigger in (
    "child-agent",
    "subagent",
    "sub-agent",
    "child-thread",
    "subthread",
    "delegation",
    "worker-execution",
    "子代理",
    "子线程",
    "多代理",
    "委派",
    "派工",
    "执行层",
):
    assert trigger in description

for required in (
    "spawn_agent",
    "CODEX_CLAUDE_CHILD_THREAD=1",
    "delegate_to_claude",
    "current working directory",
    "gpt-5.3-codex",
    "fork_context: false",
    "Process Log",
    "Summary",
    "Changed Files",
    "Verification",
    "Final Result",
    "Risks Or Follow-ups",
):
    assert required in text

metadata = openai_yaml.read_text(encoding="utf-8")
assert 'display_name: "Codex With CC"' in metadata
assert 'default_prompt: "Use $codex-with-cc' in metadata
assert "allow_implicit_invocation: true" in metadata

print("codex_with_cc skill tests passed")
