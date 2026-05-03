# HK Peer Analysis Skill

Automates a four-section peer-analysis report for Hong Kong locally incorporated licensed banks.

Feed in one or more HK bank interim/annual PDFs; out comes a Chinese Word document in the standard house style:

> 整体情况 → 零售 → 公司 → 投金 → 数字化/AI

Covers **30 business-comparable banks** (22 traditional + 8 digital), derived from the HKMA list of 32 locally incorporated licensed banks.

## Install

### Claude Code

```bash
mkdir -p ~/.claude/skills && cd ~/.claude/skills
git clone https://github.com/wangzeyangreadygo-design/hk-peer-analysis.git
# restart Claude Code
```

### Other agents

See [`adapters/`](./adapters/) for Cursor, WorkBuddy, and OpenClaw setups.

## Dependencies

```bash
pip install pypdf python-docx
```

## Repo structure

```
SKILL.md                           main skill definition
references/
  ├── hk_banks.json                30 banks + IR URLs
  ├── kpi_glossary.md              bilingual KPI definitions
  ├── report_template.md           report scaffold
  └── sample_output_structure.md   house-style reference
scripts/
  ├── extract_pdf.py               PDF → structured JSON
  └── build_docx.py                JSON → .docx
adapters/                          per-agent setup guides
```

## Update

```bash
cd ~/.claude/skills/hk-peer-analysis && git pull
```

## The one hard rule: don't fabricate

Every number, ratio, ranking, or qualitative claim in the output must be traceable to a source:

- **Peer banks** — cite their published disclosures (PDFs).
- **招商永隆** — use real figures when the user provides them; otherwise leave `{{待填}}` placeholders for the strategy team to fill downstream.

Never invent a number.
