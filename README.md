# HK Peer Analysis Skill

Automates the 招商永隆银行战略团队 workflow for generating Hong Kong bank peer-analysis reports.

Feed in one or more HK bank interim/annual PDFs; out comes a Chinese Word document in the standard four-section house style (整体情况 → 零售 → 公司 → 投金 → 数字化/AI).

## What's in this repo

```
skill/
├── SKILL.md                      # main skill definition (Claude Code format)
├── references/
│   ├── hk_banks.json             # 28 canonical HK locally-incorporated licensed banks + IR URLs
│   ├── kpi_glossary.md           # bilingual KPI definitions
│   ├── report_template.md        # mandatory report scaffold
│   └── sample_output_structure.md
├── scripts/
│   ├── extract_pdf.py            # PDF → structured JSON
│   └── build_docx.py             # JSON → .docx in house style
├── adapters/
│   ├── README.md
│   ├── claude_code.md            # Anthropic Claude Code / Desktop
│   ├── cursor.md                 # Cursor IDE
│   ├── cursor/hk-peer-analysis.mdc
│   ├── workbuddy.md              # Tencent WorkBuddy
│   └── openclaw.md               # 龙虾 / OpenClaw
└── README.md                     # you are here
```

## Install

### Claude Code (one-liner)

```bash
mkdir -p ~/.claude/skills && cd ~/.claude/skills && \
  git clone https://github.com/{YOUR_ORG}/hk-peer-analysis-skill.git hk-peer-analysis
```

### Other agents

See `adapters/README.md`.

## Dependencies

```bash
pip install pypdf python-docx
```

## Publishing to GitHub (for skill authors)

The strategy team can publish this skill to an internal or public GitHub repo in ~5 minutes:

### Step 1: Create the repo

1. Go to https://github.com/new (or your internal GitHub Enterprise)
2. Name: `hk-peer-analysis-skill`
3. Visibility: **Private** (recommended — contains internal workflows) or Public
4. Initialize: **don't** — we'll push existing files
5. Click Create

### Step 2: Push this folder

```bash
cd /path/to/skill
git init
git add .
git commit -m "Initial HK peer analysis skill"
git branch -M main
git remote add origin https://github.com/{YOUR_ORG}/hk-peer-analysis-skill.git
git push -u origin main
```

### Step 3: Share the install URL

Once pushed, share with teammates:

```
Install:
git clone https://github.com/{YOUR_ORG}/hk-peer-analysis-skill.git ~/.claude/skills/hk-peer-analysis
```

For a one-click install experience, add a release with a tarball:

```bash
git tag v1.0.0
git push origin v1.0.0
```

GitHub auto-generates a release tarball at `https://github.com/{YOUR_ORG}/hk-peer-analysis-skill/archive/refs/tags/v1.0.0.tar.gz`.

### Step 4: Version updates

Each time you change `SKILL.md` or references:

```bash
git add -u && git commit -m "Update KPI glossary for 2025H2 conventions"
git push
git tag v1.1.0 && git push origin v1.1.0
```

Users run `git pull` in their `~/.claude/skills/hk-peer-analysis/` folder to update.

## Test it

```bash
cd ~/.claude/skills/hk-peer-analysis
python scripts/extract_pdf.py hsbc_hk /path/to/HSBC-interim-2025.pdf --out /tmp/hsbc.json
cat /tmp/hsbc.json | jq .kpis_best_effort
```

## The sacred rule

**Never fabricate CMB Wing Lung / 隆港 data.** Every claim about the house must be either (a) explicitly provided by the user or (b) masked with `**`. This is non-negotiable.

## Credits

Structure reverse-engineered from CMB Wing Lung strategy team's sample output (2025 interim analyses). Bank list verified against HKMA Register of Authorized Institutions as of April 2026.

## License

Internal use. Do not distribute outside CMB group without authorization.
