# saletricks

`saletricks` 是面向新房销售场景的销售应答 skill，用于把客户原话拆成真实卡点，并输出可直接用于微信、电话、现场面谈和客户跟进的中文话术。

它不只是话术库。当前版本已把客户盘点、阶段性客户小结、学区合规、竞品对比、价格谈判和市场下行抗性处理整合为默认总纲。调用时应先读取 `references/03-sales-response-principles.md`，最后进入具体异议模块。项目文档不属于全局总纲，只在涉及具体项目或“按项目口径回答”时，按 `project-documents/` 的结构读取该项目自己的资料。

这是独立 skill，不负责保存用户数据。客户小结默认只作为文本分析输出，不输出保存状态；只有用户明确要求结构化结果时，才输出非持久化 JSON。

## 适用场景

- 客户说房子太大、太小、楼层高低、朝向或日照不好、社区太拥挤或太冷清。
- 客户说价格高、单价贵、总价压力大、优惠不够、想磨价或要赠品。
- 客户担心区位、通勤、学区、板块成熟度、开发商、交付或市场下行。
- 客户拿竞品、新房、二手房、成熟盘做比较。
- 客户说家人不同意、决策人不在场、暂时没钱、再看看、等政策、等降价。
- 销售需要盘点客户、判断意向等级、制定下一步跟进策略。
- 需要生成阶段性客户小结或结构化客户分析结果。
- 需要按项目自己的项目文档、项目主卡、价格文档、学校 FAQ 或项目动态生成项目专属话术。

## 使用方式

在支持 Codex/OpenAI skills 的环境中，把整个 `saletricks/` 目录安装到 skills 目录后调用：

```text
用 $saletricks 分析这个客户，给我一版微信回复和下一步推进动作。
```

也可以直接描述任务：

```text
客户觉得总价高，还说要回去问老婆，你帮我判断真实卡点并给话术。
```

```text
盘点一下这个客户，信息不足就先问关键问题，信息够的话输出阶段性客户小结。
```

## 默认流程

1. 先读 `references/03-sales-response-principles.md`，确定本轮是客户盘点、项目事实检索、异议处理、阶段性客户小结、学区合规、竞品对比、价格谈判还是市场下行抗性。
2. 如果涉及具体项目，读 `project-documents/README.md`，再按项目自己的知识地图、项目主卡、产品价格、学校 FAQ、竞品、异议和动态文档提取事实。
3. 读 `references/00-index.md` 和 `references/02-tags.md`，把客户原话归一成 `1 个主标签 + 0 到 2 个副标签`。
4. 读 `references/20-root-causes.md`，判断最可能的 `1 到 2 个`深因。
5. 读 `references/21-tactics.md`，选择 `1 到 2 个`回应技法。
6. 进入对应模块文件，例如价格看 `11-price.md`，学区看 `12-location.md`，竞品看 `16-trust-and-competition.md` 或 `17-competitive-analysis.md`。
7. 输出判断、试探问题、回应话术和明确推进动作；如果用户要求客户盘点或小结，则按阶段性客户小结模板输出。

## 目录结构

```text
saletricks/
  SKILL.md
  agents/
    openai.yaml
  references/
    00-index.md
    01-workflow.md
    02-tags.md
    03-sales-response-principles.md
    10-product.md
    11-price.md
    12-location.md
    13-family.md
    14-delay.md
    15-funds.md
    16-trust-and-competition.md
    17-competitive-analysis.md
    18-ready-replies.md
    19-life-scenes.md
    20-root-causes.md
    21-tactics.md
    22-closing-moves.md
    23-combo-patterns.md
    99-red-lines.md
  project-documents/
    README.md
    schema.md
    templates/
      00-project-knowledge-map.md
      01-project-core-card.md
      02-product-and-pricing.md
      03-location-school-faq.md
      04-competitor-summary.md
      05-objection-handling.md
      06-project-dynamics.md
```

## 关键文件

- `SKILL.md`：skill 入口，定义触发场景、默认流程和最小加载路径。
- `references/03-sales-response-principles.md`：默认总纲，包含客户盘点、阶段性客户小结、学区合规、竞品、价格和市场下行规则。
- `references/01-workflow.md`：调用流程，包含任务类型判断、小结判断和合规复核。
- `references/02-tags.md`：标签体系，包含表面异议、深因、技法和销售应答总纲类标签。
- `references/20-root-causes.md`：深因库，帮助判断客户真实卡点。
- `references/21-tactics.md`：技法库，提供回应策略。
- `references/99-red-lines.md`：红线，约束学区、价格、政策、市场和客户小结输出。
- `project-documents/README.md`：项目文档资料包入口，只存放项目文档结构、读取规则和模板；真实项目内容应放在各项目自己的知识库中。
- `project-documents/schema.md`：本地项目文档目录结构，说明文件存在即读取、文件缺失即提示缺失。

## 输出要求

默认输出四段：

- `判断`：一句话说明主异议和真实深因。
- `先问一句`：试探真实卡点；上下文足够清楚时可省略。
- `回应`：给一版口语化、可直接使用的话术。
- `推进`：给一个明确下一步动作。

如果用户明确要求“盘点客户 / 生成小结 / 分析客户 / 制定跟进策略”，不要使用四段异议格式，应按 `03-sales-response-principles.md` 的阶段性客户小结模板输出。默认不输出保存状态，不输出持久化 JSON；只有用户明确要求结构化 JSON 时，才输出 `customer-summary`。

## 合规边界

- 不虚构学区、入学资格、政策方向、利率变化、优惠、涨价、降价、房源紧张程度。
- 不说“保证能读”“绝对对口”“肯定不变”“内部关系”。
- 不预测市场涨跌，不把自住客户引导成短线投资判断。
- 不把配偶、父母、孩子描述成阻碍成交的人。
- 客户小结未知字段写 `null`，意向等级只写 `A/B/C/D/null`。

## 维护说明

- 增加新异议时，先在 `02-tags.md` 补标签，再在对应模块文件补场景。
- 增加新深因时，更新 `20-root-causes.md`。
- 增加新技法时，更新 `21-tactics.md`，并在 `01-workflow.md` 的技法链里挂接。
- 涉及合规、客户小结或默认流程的变化，必须同步更新 `03-sales-response-principles.md` 和 `99-red-lines.md`。
- 调整项目文档结构或模板时，更新 `project-documents/`；不要把某个项目的专属内容写入全局 `references/`。
