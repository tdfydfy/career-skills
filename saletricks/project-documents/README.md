# 项目文档资料包

这个目录用于存放“项目专属文档”的结构说明和默认模板。项目文档不是全局销售话术的一部分，不应该和 `references/03-sales-response-principles.md` 混在一起。

使用原则：

- 全局文档是通用规则，适用于所有项目，放在 `references/`。
- 项目文档是项目事实，每个项目都需要独立维护，放在项目自己的知识库中。
- 本目录只存放项目文档的结构、模板和读取规则，不放某个真实项目的长期内容。
- 当用户要求“按某项目口径回答”时，先读取该项目自己的项目文档，再用 `saletricks` 的全局规则生成话术。
- 项目文档没有状态字段；文件存在就可读取，文件不存在就说明缺失。

## 读取顺序

1. 先读项目的 `00-project-knowledge-map`，确认该项目有哪些文档、哪些是入口文档、是否存在自定义文档。
2. 根据问题读取对应项目文档：
   - 项目总览、客群、卖点、风险：`01-project-core-card`
   - 户型、面积、价格、付款、优惠：`02-product-and-pricing`
   - 区位、交通、学校、配套：`03-location-school-faq`
   - 竞品、板块、新房/二手房对比：`04-competitor-summary`
   - 项目专属客户异议：`05-objection-handling`
   - 加推、调价、活动、去化、销售节奏：`06-project-dynamics`
3. 从项目文档提取事实，再用 `references/03-sales-response-principles.md` 和对应异议模块生成销售表达。
4. 项目文档缺少事实、文件不存在、内容过期，或标注“待补充 / 待确认”时，不得自行补全。

## 文件说明

- [schema.md](./schema.md)：本地项目文档目录结构、文件用途和使用约束。
- [templates/00-project-knowledge-map.md](./templates/00-project-knowledge-map.md)：项目知识地图。
- [templates/01-project-core-card.md](./templates/01-project-core-card.md)：项目主卡。
- [templates/02-product-and-pricing.md](./templates/02-product-and-pricing.md)：产品与价格。
- [templates/03-location-school-faq.md](./templates/03-location-school-faq.md)：区位配套与学校 FAQ。
- [templates/04-competitor-summary.md](./templates/04-competitor-summary.md)：竞品对比。
- [templates/05-objection-handling.md](./templates/05-objection-handling.md)：客户异议与应对。
- [templates/06-project-dynamics.md](./templates/06-project-dynamics.md)：项目动态与销售节奏。

## 自定义项目文档

项目可以有默认模板之外的自定义文档，例如：

- `sales-opening-script`：项目介绍、学校答疑、价格口径。
- `competitor-summary`：竞品资料和对比逻辑。

自定义文档的读取优先级由该项目的 `00-project-knowledge-map` 决定。只要文件存在，并且被入口文档推荐，就可以优先于默认模板使用。

## 维护建议

- 项目创建后先补齐 7 篇默认模板。
- 每次加推、调价、优惠变化后，优先更新 `02-product-and-pricing` 和 `06-project-dynamics`。
- 每次竞品有新动作后，优先更新 `04-competitor-summary`。
- 每次一线反馈新异议后，优先更新 `05-objection-handling`。
- 每次学校、政策、周边配套有新信息后，优先更新 `03-location-school-faq`。
