# Cursor

Cursor uses `.cursor/rules/*.mdc` files with frontmatter. The HK peer analysis skill is converted into a project-scoped rule.

## Install

Per-project (recommended):

```bash
mkdir -p .cursor/rules
curl -o .cursor/rules/hk-peer-analysis.mdc \
  https://raw.githubusercontent.com/wangzeyangreadygo-design/hk-peer-analysis/main/adapters/cursor/hk-peer-analysis.mdc
```

Global (across all projects):

```bash
mkdir -p ~/.cursor/rules
curl -o ~/.cursor/rules/hk-peer-analysis.mdc \
  https://raw.githubusercontent.com/wangzeyangreadygo-design/hk-peer-analysis/main/adapters/cursor/hk-peer-analysis.mdc
```

## Usage

Open Cursor, create or open a workspace in a folder containing your HK bank PDFs. Reference the rule:

```
@hk-peer-analysis 
分析附件中的中报，对比招商永隆，输出中文 Word 报告
```

Attach PDFs via drag-and-drop. Cursor will load the rule's guidance and apply the mandatory report structure.

## Limitations

- Cursor doesn't execute Python scripts automatically. The `scripts/extract_pdf.py` and `scripts/build_docx.py` must be run manually or via a companion MCP server.
- For full automation, use the Claude Code adapter instead.
