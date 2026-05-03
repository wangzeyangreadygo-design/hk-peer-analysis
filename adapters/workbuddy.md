# WorkBuddy (Tencent)

WorkBuddy is Tencent's internal AI assistant. Install as a custom agent.

## Install

1. Open WorkBuddy → **智能体中心 / Agent Center** → **创建智能体 / Create Agent**
2. Name: `HK 同业分析助手`
3. Description: `基于香港本地银行披露，生成对标招商永隆的战略分析报告`
4. System prompt: paste the entire contents of `../SKILL.md` (Sections 1-7)
5. Knowledge base: upload
   - `../references/hk_banks.json`
   - `../references/kpi_glossary.md`
   - `../references/report_template.md`
   - The two sample output Word docs (as style references)
6. Tools: enable **文件解析** (file parsing) and **代码执行** (code execution) if available
7. Save & test

## Usage

In WorkBuddy chat, select the `HK 同业分析助手` agent, then:

```
@HK同业分析助手
附件：[drag in HSBC/SCB/Hang Seng/BOCHK 中报 PDFs]
期间：2025H1
请输出标准 4 章节 Word 报告，永隆相关数据如未提供请留 {{待填}}
```

## Sharing with team

- Publish the agent to your team space (企业空间) for reuse.
- Recipients invoke by @mentioning the agent.
- Knowledge-base updates propagate automatically.

## Limitations

- WorkBuddy doesn't execute arbitrary Python → the `scripts/build_docx.py` rendering must be done by the user copying the markdown output and converting locally.
- File size limits apply. Large annual reports (>50MB) may need to be split.
