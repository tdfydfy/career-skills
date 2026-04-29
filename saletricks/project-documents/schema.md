# 项目文档本地结构

项目文档是项目专属事实资料，不是全局话术。每个项目应维护自己的一套 Markdown 文件。

## 推荐目录

```text
<project-name>/
  00-project-knowledge-map.md
  01-project-core-card.md
  02-product-and-pricing.md
  03-location-school-faq.md
  04-competitor-summary.md
  05-objection-handling.md
  06-project-dynamics.md
  <custom-doc>.md
```

## 文件规则

| 文件 | 用途 |
|---|---|
| `00-project-knowledge-map.md` | 项目入口和文档路由 |
| `01-project-core-card.md` | 项目总览、客群、卖点、风险 |
| `02-product-and-pricing.md` | 户型、面积、总价、付款、优惠 |
| `03-location-school-faq.md` | 区位、交通、学校、配套 FAQ |
| `04-competitor-summary.md` | 竞品、板块、新房/二手房对比 |
| `05-objection-handling.md` | 项目专属客户异议与应对 |
| `06-project-dynamics.md` | 加推、调价、活动、去化、销售节奏 |
| `<custom-doc>.md` | 项目自定义资料，由知识地图说明何时读取 |

## 使用约束

- 没有状态字段；文件存在就可读取，文件不存在就说明缺失。
- 文件内容是事实来源，不是自动对客承诺。标注“待补充 / 待确认 / 过期”的内容不能对客承诺。
- 项目事实优先于通用话术；全局合规边界优先于项目事实。
- 学校、学区、招生、价格折扣、优惠、交付和政策等高风险信息，必须同时遵守 `references/99-red-lines.md`。
