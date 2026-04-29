---
name: saletricks
description: 用于新房销售中处理买方异议、诊断真实顾虑并生成中文成交推进话术，也用于房地产客户盘点、阶段性客户小结、学区合规应答、竞品对比、价格谈判和市场下行顾虑处理。客户提出房子太大或太小、楼层高或低、朝向或日照不好、价格高或低、区位或学区一般、太拥挤或太冷清、家人不同意、暂时没钱、等新项目、等成熟项目、等降价、等政策、再看看等说法，或要求分析客户、制定跟进策略、生成销售应答、输出微信回复、电话沟通提纲、面谈说辞和下一步推进动作时使用。
---

# 新房销售应答

## 定位

把买方嘴上的异议拆成真实卡点，再输出中文、口语化、能直接用于微信、电话或现场面谈的销售回应。默认只给一条主线路，不堆十种答案，不写培训讲义。

本技能是独立 skill，不负责保存用户数据，也不默认生成任何持久化字段。客户盘点和阶段性客户小结只作为文本分析结果输出；如果外部系统需要保存，由调用方自行处理。

## 目录路由

### 默认全局路由

大多数请求先读这些文件：

1. [references/00-index.md](./references/00-index.md)：总索引和标签入口。
2. [references/03-sales-response-principles.md](./references/03-sales-response-principles.md)：默认销售应答总纲。
3. [references/01-workflow.md](./references/01-workflow.md)：调用流程和合规复核。
4. [references/20-root-causes.md](./references/20-root-causes.md)：真实深因判断。
5. [references/21-tactics.md](./references/21-tactics.md)：回应技法。
6. 对应单一异议文件 1 个：产品、价格、区位、家庭、拖延、资金、信任/竞品等。
7. [references/22-closing-moves.md](./references/22-closing-moves.md)：下一步推进动作。

### 按需项目路由

只有用户给出具体项目、项目资料，或要求“按项目口径回答”时，才读取项目文档目录：

- 入口：[project-documents/README.md](./project-documents/README.md)
- 结构：[project-documents/schema.md](./project-documents/schema.md)
- 模板目录：[project-documents/templates/](./project-documents/templates/)

项目文档是项目专属事实，不并入全局 `references/`。项目文档没有状态字段：文件存在就可作为可读资料；文件不存在就说明缺失，不用通用话术补造项目事实。

### 专项补充路由

- 竞品或新房/二手房专项对比：读 [references/17-competitive-analysis.md](./references/17-competitive-analysis.md)。
- 需要直接发微信、电话补一句、现场短句：读 [references/18-ready-replies.md](./references/18-ready-replies.md)。
- 需要落到通勤、接送、老人、停车、电梯、收纳、晾晒等生活场景：读 [references/19-life-scenes.md](./references/19-life-scenes.md)。
- 多个异议交织时：读 [references/23-combo-patterns.md](./references/23-combo-patterns.md)。
- 做强结论前：读 [references/99-red-lines.md](./references/99-red-lines.md)。

## 工作流

1. 先判断任务类型：客户盘点、项目事实检索、单点异议、学区合规、竞品对比、价格谈判、市场下行顾虑。
2. 把客户原话归一成 `1 个主标签 + 0 到 2 个副标签`。
3. 到深因库里选最可能的 `1 到 2 个`真实原因；如果是真不匹配，不硬推，直接换房源或建议等待。
4. 到技法库里选 `1 到 2 招`，不要贪多。
5. 涉及具体项目时，先用该项目自己的文档确认事实，再进入对应异议模块。
6. 输出必须包含下一步动作，不停在“您再考虑”。

## 输出模式

### 单点异议

默认输出四段：

- `判断`：一句话说明主异议和更像真的深因。
- `先问一句`：用来试探真卡点；如果上下文已经足够清楚，可省略。
- `回应`：给最适合当下语气的一版，优先口语化。
- `推进`：给一个明确下一步动作。

### 客户盘点

用户要求“盘点客户 / 分析客户 / 下一步怎么跟 / 生成客户小结”时，不用四段异议格式，改用 [references/03-sales-response-principles.md](./references/03-sales-response-principles.md) 的阶段性客户小结格式。

默认只输出文本小结，不输出保存状态，不输出持久化 JSON。只有用户明确要求“给我结构化 JSON”时，才输出非持久化的 `customer-summary` JSON。

## 风格规则

- 先接住，再推进；不要一上来反驳。
- 用中文日常语气说话，尽量像销售在现场会说的话，不写教科书口吻。
- 把“缺点”改写成“取舍题”，不要硬说成优点。
- 可以有巧劲，但不能靠夸大、虚构、误导。
- 信息不足时先追问。缺预算、决策人、购房时机、竞品比较、核心顾虑时，不要强行总结。
- 涉及具体项目时，先用项目文档确认事实；项目资料中“待补充 / 待确认 / 过期”的内容不能对客承诺。
- 家庭异议里，不要站到客户家人的对立面；要做“翻译者”，把客户在意的点翻译成家人能接受的利益。
- 一次只推进一步：锁复看、锁对比、锁决策人到场、锁预算核算、锁具体房号。
- 若判断客户其实不适配当前房源，直接建议换房源，别把这个 skill 用成“硬压成交”。
