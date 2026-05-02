# Claude Code / Claude Desktop

## Install

```bash
mkdir -p ~/.claude/skills
cd ~/.claude/skills
git clone https://github.com/{YOUR_ORG}/hk-peer-analysis-skill.git hk-peer-analysis
```

Restart Claude Code. Verify registration:

```bash
ls ~/.claude/skills/hk-peer-analysis/SKILL.md
```

## Update later

```bash
cd ~/.claude/skills/hk-peer-analysis && git pull
```

## Usage

Drop the HK bank PDFs into your current working directory, then ask:

```
请使用 hk-peer-analysis skill 分析这几份中报，对比招商永隆，
期间 = 2025H1，输出 Word。
```

Or let it auto-trigger by mentioning HK bank names:

```
帮我做汇丰渣打恒生和中银香港 2025 中报的同业分析
```

## Dependencies

```bash
pip install pypdf python-docx
```

## Troubleshooting

- **Skill not triggering**: Check `~/.claude/settings.json` — skill auto-discovery requires `enableSkillsDiscovery: true` (default).
- **Chinese characters render as boxes in output .docx**: Install SimSun/SimHei fonts on your system, or set alternate CJK fonts in `scripts/build_docx.py`.
- **`**` placeholders missing**: The skill enforces masking of CMB Wing Lung data. If the user explicitly provides internal figures in the prompt, those can be used — but never invented.
