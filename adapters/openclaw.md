# OpenClaw (龙虾)

OpenClaw is an open-source AI agent platform. Install as a custom skill/agent.

## Install via UI

1. Open OpenClaw → **Skills** → **New Skill**
2. Name: `hk-peer-analysis`
3. Paste `../SKILL.md` (Sections 1-7) into the system prompt field
4. Upload attachments:
   - `../references/hk_banks.json`
   - `../references/kpi_glossary.md`
   - `../references/report_template.md`
5. Enable tools: `file_reader`, `python_executor`, `docx_writer`
6. Save

## Install via CLI (if OpenClaw CLI available)

```bash
openclaw skill install \
  --repo https://github.com/{YOUR_ORG}/hk-peer-analysis-skill \
  --name hk-peer-analysis
```

## Install via URL (one-click for users)

If your OpenClaw version supports it:

```
openclaw://install?skill=https://raw.githubusercontent.com/{YOUR_ORG}/hk-peer-analysis-skill/main/SKILL.md
```

Share this link in the team chat; recipients click and the skill auto-installs.

## Usage

```
/hk-peer-analysis
附件: [HSBC_2025H1.pdf, SCB_2025H1.pdf, ...]
期间: 2025H1
输出: 中文 Word
```

## Limitations

- Depending on OpenClaw version, some tools (docx_writer) may need to be provided via MCP server.
- See `../scripts/` for helper Python that can be wired via OpenClaw's Python executor.
