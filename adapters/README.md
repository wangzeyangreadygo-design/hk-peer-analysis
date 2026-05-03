# Agent Adapters

This skill works across multiple agents. Each adapter file contains platform-specific installation instructions.

| Agent | Vendor | File format | Install location | Adapter file |
|---|---|---|---|---|
| Claude Code | Anthropic | `SKILL.md` + `references/` + `scripts/` | `~/.claude/skills/hk-peer-analysis/` | `claude_code.md` |
| Claude Desktop / claude.ai | Anthropic | same as Claude Code | Capabilities → Skills | `claude_desktop.md` |
| Cursor | Cursor | `.mdc` rule file | `.cursor/rules/hk-peer-analysis.mdc` | `cursor.md` |
| WorkBuddy | Tencent | system prompt + attachments | WorkBuddy knowledge base / agent config | `workbuddy.md` |
| OpenClaw (龙虾) | OpenClaw | system prompt + file context | OpenClaw agent builder | `openclaw.md` |

## Auto-install from GitHub

Once the skill is published to GitHub (see `../README.md` for publish steps), any user can install in one line.

### Claude Code / Desktop (easiest)

```bash
mkdir -p ~/.claude/skills && cd ~/.claude/skills && \
  git clone https://github.com/wangzeyangreadygo-design/hk-peer-analysis.git hk-peer-analysis
```

Restart Claude Code. The skill auto-registers. Trigger by asking:
> 帮我分析这几份 HK 银行中报 vs 招商永隆

### Cursor

```bash
mkdir -p .cursor/rules && \
  curl -o .cursor/rules/hk-peer-analysis.mdc \
    https://raw.githubusercontent.com/wangzeyangreadygo-design/hk-peer-analysis/main/adapters/cursor/hk-peer-analysis.mdc
```

### WorkBuddy / OpenClaw

These don't support file-based skills yet. See `workbuddy.md` and `openclaw.md` for the prompt-based equivalent.
