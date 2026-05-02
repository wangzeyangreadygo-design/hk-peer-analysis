---
name: hk-peer-analysis
description: Generate structured peer analysis reports comparing Hong Kong banks' interim/annual disclosures against CMB Wing Lung ("隆港" = CMB Wing Lung + CMB HK Branch). Use when the user provides one or more HK bank PDFs (HSBC, Standard Chartered HK, BOCHK, Hang Seng, etc.) and asks for a strategic peer analysis in the house style of CMB Wing Lung's strategy team. Output is a Chinese Word document following the fixed four-section structure: Overall Strategy → Retail → Corporate → Treasury/Investment → (optional) Digital/AI.
---

# HK Peer Analysis Skill

## 1. When to trigger this skill

Trigger when the user's request matches any of these patterns:
- Provides one or more HK bank disclosure PDFs (interim report, annual report, results announcement) and asks for "同业分析 / peer analysis / 对标分析 / 业绩简析"
- Mentions CMB Wing Lung (招商永隆) or 隆港 as the comparison baseline
- Asks to compare HK banks (汇丰 / 渣打 / 恒生 / 中银香港 / 东亚 / ZA Bank / etc.) across strategy, retail, corporate, or treasury dimensions
- Asks for a report "in the style of" a sample `.docx` the user provides

Do NOT trigger when the user asks for:
- Pure financial ratio calculation (use a spreadsheet skill)
- Stock price / valuation analysis (this skill focuses on strategic narrative, not quant)
- Banks outside HK jurisdiction

## 2. The house report structure (mandatory)

Every output must follow this structure. Section headers are in Chinese because the deliverable is Chinese.

```
{报告标题}：{期间}业绩报告分析系列之{N}
——{被分析银行列表}整体战略和三大条线业务策略

【导语】 1-2 段，说明本次分析的信源、重点和方法变化

一、整体情况
  （一）战略方向
    - 逐家银行: 战略定位 + 地域重点 + 关键增长引擎（不超过 200 字/家）
    - 与隆港对比的启示
  （二）条线盈利结构
    - 表格: 各行净交易收入/净利息/净手续费/其他占比
    - 文字点评: 结构特征、与隆港差别

二、零售条线
  （一）业绩亮点比较
    - 客户数、AUM、营收同比、非息占比、私行客户数等关键指标
    - 每家一段 150-200 字
    - 隆港对应指标的占位符（敏感数据用 ** 标注）
  （二）可借鉴的业务策略
    1. 与我行相似之处
    2. 与我行不同之处（重点挖掘可学习点）

三、公司条线
  （一）业绩亮点比较
  （二）业务策略对比
    1. 各家主要策略
    2. 细分业务领域对比（IPO 收款行 / 交易银行 / 银团 / 债承）
  （三）我行可借鉴的策略（3 条，每条以"一是...二是...三是..."开头）

四、投金条线
  （一）业绩亮点比较（分金融市场/债券投资/资产托管/资产管理/财资五块）
  （二）我行与其他银行的相似之处
  （三）我行与其他银行的差异 + 可借鉴策略

五、其他 (optional, 数字化/AI 方面)
```

## 3. KPI extraction reference

When parsing PDFs, extract these indicators explicitly. File `references/kpi_glossary.md` contains bilingual terms and each bank's reporting convention.

**Retail (零售条线):**
- 新增客户数 / Net new customers
- 零售 AUM / Retail AUM
- 零售非息收入同比 / Retail non-interest income YoY
- 财富管理收入 / Wealth management income
- 私行客户数 / Private banking clients

**Corporate (公司条线):**
- 工商金融贷款总额 / C&I loans
- 贸易融资贷款 / Trade finance
- 非息收入同比 / Non-interest YoY
- 跨境业务收入占比 / Cross-border revenue share
- 银团排名 / Syndication ranking
- 债承排名 / Bond underwriting ranking

**Treasury/Investment (投金条线):**
- 净交易收益 / Net trading income
- 债券投资占总资产 / Bond investment % of total assets
- 托管资产规模 / AUC (assets under custody)
- 资管 AUM / AUM (asset management)
- 离岸人民币清算额 / Offshore RMB clearing

**Digital/AI (数字化, optional):**
- 移动银行 MAU
- 数码渠道交易量
- AI/模型部署场景
- 开放银行/API 接入方数量

## 4. Execution flow

Follow these steps in order. Do NOT skip Step 2.

### Step 1: Identify inputs
- Confirm which banks' PDFs you have. Match against `references/hk_banks.json` (28 canonical banks).
- Confirm the reporting period (interim 6M vs annual 12M). Mixing periods is a red flag — warn the user.

### Step 2: Extract per-bank structured data
For each PDF, extract and store in memory as JSON:
```json
{
  "bank": "HSBC (HK)",
  "period": "2025H1",
  "strategic_direction": "...",
  "retail": {"new_customers": "...", "aum": "...", "nii_yoy": "...", "highlights": [...]},
  "corporate": {"loans": "...", "trade_finance": "...", "strategies": [...]},
  "treasury": {"net_trading": "...", "bond_pct": "...", "custody": "...", "am_aum": "..."},
  "digital": {"initiatives": [...]}
}
```

Use `scripts/extract_pdf.py` as a utility. It uses pypdf and outputs structured JSON.

### Step 3: Build comparison matrix
Create a wide table: rows = banks, columns = KPI. Include CMB Wing Lung column with `**` placeholders (sensitive data must be masked — this is a hard rule).

### Step 4: Draft narrative sections
Use `references/report_template.md` as the scaffold. For each section:
1. Open with 1-2 sentences framing the comparison
2. Describe each bank's position in ~150-200 字
3. Close with "与隆港对比" paragraph containing `**` placeholders

### Step 5: Extract learnable strategies
For each business line, group strategies into:
- **与我行相似的** (validate-and-continue signal)
- **与我行不同且值得借鉴的** (action signal — this is the most valuable section for management)
- **与我行不同但不适合照搬的** (explicitly note why — size, license, customer base)

### Step 6: Output as Word document
Generate a `.docx` matching the sample style. Use `scripts/build_docx.py`. Key formatting rules:
- 标题宋体 / 正文宋体 12pt
- 表格居中、表头加粗
- 敏感数据一律用 `**` 占位符（不许猜测隆港真实数据）
- 文末不要加 "本报告由 AI 生成" 字样（战略团队会署名）

## 5. The sacred `**` rule

**Any number, growth rate, ranking, or qualitative claim about 招商永隆 / 隆港 / 港分 / 永隆 / 我行 that was not explicitly provided in the user's message MUST be replaced with `**`.**

This is non-negotiable. The downstream consumer is a strategy team that fills in real numbers from internal systems. Fabricating CMB Wing Lung data — even as a plausible estimate — causes downstream trust failure.

Correct:
> 永隆零售条线上半年营收同比增长**（永隆**，港分**），其中非息同比增长**

Incorrect:
> 永隆零售条线上半年营收同比增长 8.5%（估算）

## 6. Tone guidelines

- Analytical but not advisory. Describe, don't prescribe.
- Use 同业/对标 terminology (中银香港, 发钞行, 大行, 四大行, 第一梯队).
- Avoid marketing language (creative/revolutionary/world-class). The audience is skeptical bankers.
- When a peer action can't be replicated (e.g. HSBC's global network), say so explicitly.
- Quantitative comparisons should cite source: "恒生 2025 中报 P.42"

## 7. Files in this skill

- `SKILL.md` — you are here
- `references/hk_banks.json` — 28 canonical HK locally-incorporated licensed banks with IR URLs
- `references/kpi_glossary.md` — bilingual KPI definitions and per-bank reporting conventions
- `references/report_template.md` — the report scaffold
- `references/sample_output_structure.md` — annotated example from CMB Wing Lung strategy team
- `scripts/extract_pdf.py` — PDF → structured JSON extractor
- `scripts/build_docx.py` — JSON → formatted .docx builder
- `adapters/` — setup instructions for Cursor, WorkBuddy (Tencent), OpenClaw (龙虾), Claude Code
- `README.md` — installation and GitHub publishing guide

## 8. Quick usage

Once installed, invoke with:

```
Please analyze these HK bank reports against CMB Wing Lung:
[attach HSBC_interim_2025.pdf, SCB_HK_interim_2025.pdf, HangSeng_interim_2025.pdf]

Output: Chinese Word document, following the standard 4-section structure.
Period: 2025 H1.
```

The skill will auto-detect banks, extract data, build the comparison, and produce a `.docx` at `~/Desktop/HK_Peer_Analysis_{date}.docx`.
