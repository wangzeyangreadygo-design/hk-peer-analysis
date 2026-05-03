# Claude Code / Claude Desktop

## Install

```bash
mkdir -p ~/.claude/skills
cd ~/.claude/skills
git clone https://github.com/wangzeyangreadygo-design/hk-peer-analysis.git hk-peer-analysis
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
- **Real 永隆 figures not appearing in output**: The skill uses whatever real data you provide (inline, attached files, or prior-turn context). If a number appears as `{{待填}}` when you expected a real figure, check whether you actually supplied it. The skill will never invent a number.
