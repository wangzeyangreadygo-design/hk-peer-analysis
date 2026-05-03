# Sample Output Structure (annotated)

Skeleton of the CMB Wing Lung strategy team's output style. Use as a stylistic reference when drafting new reports. Where the user supplies real 永隆 figures, use them. Where no figure is supplied, leave `{{待填}}`.

## Example opening

> 2025中期业绩报告分析系列之二
> ——汇丰渣打恒生整体战略和三大条线业务策略
>
> 9月1日中银香港发布了2025中期业绩报告（累计已有7家同业发布了中期业绩报告），目前我行相关部门对同业数据的整理和分析多集中在财务指标方面，本次主要从整体战略和三大条线业务策略角度...

Key patterns:
- Title line: `{期间}业绩报告分析系列之{汉字序号}`
- Subtitle: 副标题以破折号 "——" 开头，说明分析维度
- 导语 (lead paragraph) 1-2 段，放在一级标题前
- 导语讲明: 信源 + 方法变化 + 本次关注点

## Example per-bank strategic summary (Section 一.（一）)

> 汇丰控股：全球财富管理与机构业务协同的巨头，以区域分散化和业务多元化为特点，经营覆盖全球、商业银行、交易银行、财富管理等。汇丰正通过简化组织架构来聚焦核心战略...

~200 字, 包含: 定位 + 地域策略 + 条线重心 + 增长点。

## Example revenue structure table (Section 一.（二）)

| | 汇丰银行 | 渣打银行 | 中银香港 | 永隆银行 |
|---|---|---|---|---|
| 净交易收入 | 35% | 53% | 31% | {{待填}} |
| 净利息收入 | 47% | 31% | 63% | {{待填}} |
| 净服务费及佣金收入 | 19% | 15% | 16% | {{待填}} |
| 其他 | -1% | 1% | -10% | {{待填}} |

永隆列用用户提供的真实数据填入；未提供则留 `{{待填}}`。

## Example retail highlights paragraph (Section 二.（一）)

> 汇丰香港上半年零售客户新增60万名，较年初增长16.7%；零售AUM1.1万亿美元，较年初增长8.3%；零售非息收入13.6亿美元，同比增幅45%。渣打集团（未单独区分香港）上半年有13.5万名全新客户开户...

Pattern:
- 每家一段, 连续 3-4 个指标
- 具体数字带单位 (万名/美元/%)
- 同比/环比对比 (较年初 + 同比增幅)

Then 永隆段:
> 永隆零售条线上半年新增客户 {{待填}}，较年初增长 {{待填}}。零售 AUM 较年初增长 {{待填}}，其中财富管理 AUM 较年初增长 {{待填}}。

## Example action paragraph (Section 二.（三）)

> 一是加大数字化获客投入，提升线上理财 AUM 转化率。我行可借鉴恒生 Mobile Banking 端财富产品组合推荐算法，结合招行集团 App 能力，在三个月内完成首轮灰度测试。
> 二是发挥我行跨境代发优势，将重点放在大湾区新移民与跨境就业人群。相对于香港四大行庞大的零售网点覆盖，我行差异化聚焦中小型高净值与新移民客群，更具投入产出比。
> 三是在零售和公司业务联动方面，可以考虑参考恒生"薪转代发 + 子女教育金 + 企业主私行"的协同策略，实现从 C&I 客户到其高管、员工的纵向穿透。

Three-point structure with 一是/二是/三是 prefixes. Each point states a concrete action, its rationale, and the reference peer (if any).

## Bond investment table example (Section 四.（一）.2)

| | 汇丰银行 | 渣打银行 | 恒生 | 中银香港 | 永隆 |
|---|---|---|---|---|---|
| 客户贷款占比 2024 | 32% | 37% | 46% | 40% | {{待填}} |
| 客户贷款占比 2025H1 | 31% | 35% | 44% | 39% | {{待填}} |
| 债券投资占比 2024 | 41% | 28% | 38% | 34% | {{待填}} |
| 债券投资占比 2025H1 | 42% | 30% | 37% | 39% | {{待填}} |

Must include footnote on 口径说明 (methodology): "各行财报披露口径不一，本表格取数为..."

## DO NOT

- Do not use emoji
- Do not add "本报告由 AI 生成" disclaimers
- Do not fabricate CMB Wing Lung numbers
- Do not use future-tense speculation (e.g. "预计将...") for peer banks without source citation
- Do not praise peers ("卓越的", "世界级的"). Describe neutrally.

## DO

- Cite PDF page numbers when quoting specific figures
- Preserve the four-section structure even when one section is thin
- Use the real 招商永隆 numbers the user provides; fall back to `{{待填}}` when no number is supplied
- Use 一是/二是/三是 for recommendation lists
- End each 二级 section with a 永隆对比 paragraph
