# 调用流程

## 目录

- 默认前置总纲
- 任务类型判断
- 项目文档按需读取
- 客户盘点优先级
- 原话归一
- 真伪判断
- 深因判断
- 技法链选择
- 小结判断
- 收口动作
- 何时停止硬推
- 合规复核

## 默认前置总纲

每次使用本 skill，先按 [03-sales-response-principles.md](./03-sales-response-principles.md) 建立底层判断：

- 通用销售判断先按全局规则；
- 涉及具体项目事实时，再按 [project-documents/README.md](../project-documents/README.md) 使用该项目自己的文档；
- 信息不足先追问，不为了完成格式硬总结；
- 合规优先于成交，尤其是学校、政策、价格、优惠、市场走势；
- 输出必须服务下一步动作，不停在泛泛建议；
- 用户要求盘点、总结或制定跟进策略时，优先走客户盘点和阶段性客户小结流程。

## 任务类型判断

先判断本轮属于哪类任务，再决定读取哪些模块：

| 任务类型 | 判断信号 | 默认动作 |
|---|---|---|
| 客户盘点 | 盘点客户、分析需求、怎么跟、下一步怎么聊 | 补齐客户信息，判断意向等级，必要时生成阶段性客户小结 |
| 项目事实检索 | 项目怎么样、价格、户型、学校、竞品、按项目口径回答 | 先读该项目自己的知识地图和对应项目文档，再生成销售表达 |
| 单点异议 | 房子大/小、楼层、价格、区位、家人、资金等 | 走标签 -> 深因 -> 技法 -> 推进 |
| 学区合规 | 能不能读、对口、划片、规划学校、未来会不会变 | 只讲证据链和概率，不做保证 |
| 竞品对比 | 某盘也在看、哪个好、为什么贵/便宜 | 先承认事实，再按客户需求排序 |
| 价格谈判 | 多少钱、最低价、优惠、折扣、赠品 | 先探支付力，再阶梯释放，不一次亮底 |
| 市场下行 | 买了会不会跌、等市场稳、二手房卖不掉 | 转回自住价值和等待成本，不预测行情 |

## 项目文档按需读取

当用户给出项目名、项目资料、项目文档内容，或要求“按项目口径回答”时：

1. 先读 [project-documents/README.md](../project-documents/README.md)，确认项目文档结构和读取原则；
2. 再读该项目自己的入口文档 `00-project-knowledge-map`，确认文档路由；
3. 按问题类型读取该项目自己的主题文档：
   - 产品、面积、价格、付款、优惠：`02-product-and-pricing`
   - 区位、交通、学校、配套：`03-location-school-faq`
   - 竞品、板块、二手房、新房对比：`04-competitor-summary`
   - 项目专属客户异议：`05-objection-handling`
   - 加推、调价、活动、去化、窗口期：`06-project-dynamics`
   - 项目总览和适配客群：`01-project-core-card`
4. 如果项目文档有自定义路由，例如 `sales-opening-script` 或 `competitor-summary`，按入口文档推荐优先读取；
5. 从项目文档抽取事实，再用本 skill 的通用模块生成话术；
6. 项目文档不存在、为空、过期或标注“待补充 / 待确认”时，不得自行补全事实。

## 客户盘点优先级

当用户给的是一段客户情况，而不是单句异议时，不要急着生成话术。先判断信息是否足够：

- 缺预算、首付、月供、目标总价时，优先问支付力；
- 缺决策人、出资人、使用人时，优先问购买逻辑；
- 缺首访时间、复访、竞品、房源匹配时，优先问成交阶段；
- 缺核心顾虑时，优先问客户最满意点和最大抗性。

只有客户身份、核心诉求、预算或购房阶段形成稳定判断，或用户明确要求小结时，才生成阶段性客户小结。

## 原话归一

先把客户口语化原话归一成标准标签，不要按客户字面意思逐句回。

- 一次只定 `1 个主标签`
- 可补 `0 到 2 个副标签`
- 如果客户抛出很多理由，先抓最像挡箭牌或最影响成交的那一个

例子：

- “楼层太高了，而且价格也不便宜，我老公还觉得等等政策。”
- 主标签可定为 `price-total-high` 或 `product-floor-high`
- 副标签可定为 `family-spouse` `delay-policy`

## 真伪判断

先判断是真异议还是挡箭牌。

- 真异议：说法具体、愿意继续聊、能说出阈值
- 挡箭牌：说法模糊、理由会替换、说完就想结束

可用的试探句：

- “您更介意的是总价压力，还是觉得这套本身不值？”
- “如果这个点解决了，您会继续往下看，还是还有别的关键卡点？”
- “这句话是您自己的顾虑，还是家里那位最在意的点？”

## 深因判断

把表面异议映射到深因，而不是直接上话术。

最常见深因：

- `cause-budget`
- `cause-risk`
- `cause-family`
- `cause-compare`
- `cause-delay`
- `cause-information`
- `cause-no-urgency`
- `cause-face-saving`
- `cause-decision-absence`
- `cause-unfit`
- `cause-customer-summary-needed`
- `cause-school-compliance-risk`
- `cause-price-negotiation`
- `cause-market-downturn`

对应说明见 [20-root-causes.md](./20-root-causes.md)。

## 技法链选择

默认用短链，不要堆技巧。

- 稳妥链：`tactic-empathy -> tactic-diagnose -> tactic-tradeoff -> tactic-micro-close`
- 巧劲链：`tactic-empathy -> tactic-reverse -> tactic-tradeoff -> tactic-micro-close`
- 家庭链：`tactic-empathy -> tactic-family-translation -> tactic-contrast -> tactic-micro-close`
- 观望链：`tactic-empathy -> tactic-cost-of-wait -> tactic-contrast -> tactic-micro-close`
- 价格谈判链：`tactic-payment-probe -> tactic-staged-concession -> tactic-micro-close`
- 学区合规链：`tactic-evidence-chain -> tactic-compliance-reframe -> tactic-micro-close`
- 竞品链：`tactic-objective-compare -> tactic-need-ranking -> tactic-micro-close`
- 盘点链：`tactic-customer-inventory -> tactic-diagnose -> tactic-micro-close`
- 不匹配链：`tactic-empathy -> tactic-switch`

具体母招见 [21-tactics.md](./21-tactics.md)。

## 小结判断

需要生成阶段性客户小结时，按 [03-sales-response-principles.md](./03-sales-response-principles.md) 的客户小结模板输出。

可以生成阶段性小结的条件：

- 客户基础身份、核心诉求、预算或购房阶段已形成稳定判断；
- 用户明确要求盘点客户、生成小结、分析客户或制定跟进策略；
- 相比上一轮，客户状态出现明确新增或变化。

不要生成小结的情况：

- 信息仍过少，无法稳定判断；
- 只是寒暄、重复确认或没有新增事实；
- 同一阶段没有实质变化。

默认不输出 JSON，不写保存状态。只有用户明确要求结构化 JSON 时，才输出非持久化 `customer-summary` JSON；跟进建议留在正文，不写入 JSON。

## 收口动作

回应完一定推进，不要停在“您再考虑”。

优先级通常是：

1. 锁唯一卡点
2. 锁二访或复看
3. 锁关键决策人到场
4. 锁预算线
5. 锁两套对比
6. 锁一个竞品比较
7. 锁替代房号

收口模板见 [22-closing-moves.md](./22-closing-moves.md)。

## 何时停止硬推

以下情况不要强行“克服异议”：

- 客户已经明确指出当前房源的硬伤，而且硬伤客观存在
- 首付或月供缺口明显超出承受能力
- 学区、通勤、照护老人等边界是刚需硬约束
- 真正决策人不在场，现有对话只能做信息铺垫

此时优先做两件事：

- 换房源或换户型
- 约下一次把关键人带上

## 合规复核

最终输出前检查：

- 学区：不得说保证能读、绝对对口、肯定不变，只能讲历史、距离、容量和以官方公布为准；
- 价格：不得虚构底价、领导特批、明天涨价、房源紧张；
- 市场：不得预测涨跌，不把自住客户引向短线投资判断；
- 竞品：不得编造竞品缺陷，只比较可验证维度；
- 客户小结：未知字段写 `null`，意向等级只写 `A/B/C/D/null`。
