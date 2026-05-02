# KPI Glossary — HK Bank Peer Analysis

Bilingual KPI definitions and per-bank reporting conventions. Use this as the canonical mapping when extracting data from PDFs.

## Retail Banking / 零售条线

| English | 中文 | Notes |
|---|---|---|
| Net new retail customers | 新增零售客户数 | HSBC reports in 万名; SCB reports globally not HK-specific; Hang Seng reports growth % |
| Retail AUM | 零售 AUM | HSBC in USD; others in HKD. Hang Seng discloses wealth AUM separately |
| Retail non-interest income YoY | 零售非息收入同比 | Key driver — wealth, insurance, investment fees |
| Wealth management income | 财富管理收入 | HSBC breaks into "wealth fees + insurance"; SCB calls it "Wealth Solutions" |
| Private banking clients | 私行客户数 | HSBC: "Global Private Banking"; SCB: "Affluent + Priority Private"; BOCHK: "私人财富" |
| Mortgage new bookings | 新造按揭贷款 | 关注环比 (vs prior half-year), market share rank |

## Corporate Banking / 公司条线

| English | 中文 | Notes |
|---|---|---|
| C&I loans (HK-booked) | 工商金融贷款 (香港使用) | HSBC/SCB report full HK book; BOCHK discloses "在香港使用" explicitly |
| Trade finance loans | 贸易融资贷款 | Watch YoY — bellwether for cross-border activity |
| Cross-border revenue share | 跨境业务收入占比 | SCB discloses >40%; HSBC doesn't break out |
| GPS / Transaction banking fee income | 环球支付与现金管理手续费 | HSBC: "GPS", SCB: "Transaction Banking", BOCHK: "环球交易银行/iGTB" |
| Syndication league table | 银团排名 (HK/Macau) | Bookrunner by deal count (中资preference) vs by volume (外资preference) |
| Bond underwriting league table | 债承排名 | Dealogic / Bloomberg league tables |
| IPO receiving bank | IPO 收款行 | Small number of banks participate; share matters more than revenue |

## Treasury & Markets / 投金条线

| English | 中文 | Notes |
|---|---|---|
| Net trading income | 净交易收益 | 受 swap income + FX + rates trading 驱动 |
| Bond investment / total assets | 债券投资占总资产 | 各行口径不一 (FVTPL vs FVOCI vs amortized cost合并) |
| Loan / total assets | 客户贷款占总资产 | 与债券投资此消彼长 |
| Assets under custody (AUC) | 托管资产规模 | BOCHK 领跑中资; HSBC/SCB 披露有限 |
| Asset management AUM | 资管 AUM | Hang Seng Investment ETFs; BOCHK asset mgmt |
| Offshore RMB clearing | 离岸人民币清算额 | BOCHK 占全球 >70% |
| RMB bond underwriting | 离岸人民币债承 | BOCHK 第一 |

## Digital / AI / 数字化

| English | 中文 | Notes |
|---|---|---|
| Mobile banking MAU | 移动银行月活 | 各行披露不规范 |
| Digital channel transaction volume | 数码渠道交易量 | |
| AI / model deployments | AI 模型部署场景 | HSBC 的 Zing、Hang Seng 的 H+、BOCHK 的数码营销 AI 模型 |
| GenAI sandbox participation | GenAI 沙盒参与 | HKMA GenA.I. Sandbox (2025+) |
| Open banking / API partners | 开放银行/API 接入方 | IADS 参与行有 28 家, BOCHK/Hang Seng/HSBC/SCB 都是 |
| Virtual currency / tokenization | 数字货币/代币化 | 数码港元先导计划、e-HKD、Project Ensemble |

## Sensitive terms — always mask with `**`

Any number, rank, or qualitative claim about the following entities that the user has not explicitly provided must be masked as `**`:
- 招商永隆 / 永隆 / CMB Wing Lung
- 港分 / 招行香港分行 / CMB HK Branch
- 隆港 (= 永隆 + 港分 combined)
- 我行 / 本行

Example:
> 恒生零售非息同比增长 37%，隆港零售非息同比增长 **（永隆**，港分**）

## Regulatory authorities and programs (do not translate)

- HKMA (Hong Kong Monetary Authority / 金管局)
- HKEX (Hong Kong Exchanges / 港交所)
- IADS (Interbank Account Data Sharing / 户口互联计划)
- GenA.I. Sandbox (HKMA/Cyberport joint, 2025+)
- e-HKD / 数码港元
- Project Ensemble (HKMA tokenization project)
- Cross-boundary Wealth Management Connect / 跨境理财通
- Stock Connect / 互联互通
- Bond Connect / 债券通
