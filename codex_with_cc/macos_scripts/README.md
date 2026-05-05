# macOS Scripts

macOS support is not implemented yet.

When installing this workflow on macOS, the installing AI should use the behavior in the source repository's `codex_with_cc/windows_scripts` directory as the reference and implement equivalent native macOS scripts in this directory. A macOS target install may not include `windows_scripts`, so use the upstream/source checkout rather than assuming a sibling directory exists after installation.

Do not copy Windows PowerShell commands directly into macOS instructions. Preserve the same workflow boundaries: the Codex main thread plans and reviews, a Codex child thread invokes the delegate entrypoint, and the delegate entrypoint calls Claude Code CLI.
