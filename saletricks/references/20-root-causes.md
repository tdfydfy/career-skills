# 深因库

## 目录

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
- `cause-project-fact-needed`

## `cause-budget`

- 信号：总价、首付、月供会反复出现；客户问法偏数字和承受力
- 不要直接说：咬咬牙就行
- 优先问：是首付卡住，还是月供卡住？
- 适合技法：`tactic-diagnose` `tactic-tradeoff` `tactic-switch`

## `cause-risk`

- 信号：反复追问开发商、交付、学区、区位、市场
- 不要直接说：您想太多了
- 优先问：您最怕买错的是哪一件事？
- 适合技法：`tactic-diagnose` `tactic-contrast` `tactic-reverse`

## `cause-family`

- 信号：客户本人态度不差，但频繁提家人意见
- 不要直接说：您自己定就行
- 优先问：家里谁最关键，他最在意什么？
- 适合技法：`tactic-family-translation` `tactic-diagnose`

## `cause-compare`

- 信号：总说再看看、还没比完、竞品名字很多
- 不要直接说：别看了就买这个
- 优先问：还差哪一项没比明白？
- 适合技法：`tactic-contrast` `tactic-micro-close`

## `cause-delay`

- 信号：等政策、等价格、等新盘、等以后再说
- 不要直接说：错过就没了
- 优先问：您在等哪个具体条件？
- 适合技法：`tactic-cost-of-wait` `tactic-diagnose`

## `cause-information`

- 信号：问题很多但不成体系，像还没形成判断框架
- 不要直接说：这些都不重要
- 优先问：您现在最想先搞清哪一项？
- 适合技法：`tactic-diagnose` `tactic-scene` `tactic-contrast`

## `cause-no-urgency`

- 信号：需求存在，但时间线宽松；不急入住、不急结婚、不急换房
- 不要直接说：买房都要趁早
- 优先问：您不急的是入住时间，还是决定时间？
- 适合技法：`tactic-cost-of-wait` `tactic-tradeoff`

## `cause-face-saving`

- 信号：理由轻飘、反复变、像在给退出找台阶
- 不要直接拆穿：您其实就是不想买
- 优先问：如果只留一个最真实的原因，会是哪一个？
- 适合技法：`tactic-empathy` `tactic-diagnose` `tactic-reverse`

## `cause-decision-absence`

- 信号：真正拍板的人没到场；客户自己不敢给明确结论
- 不要直接逼定：现在就拍板
- 优先问：最后拍板的人最看重什么？
- 适合技法：`tactic-family-translation` `tactic-micro-close`

## `cause-unfit`

- 信号：客户能清楚指出不可接受项，且该问题客观存在
- 不要强行重构：把硬伤说成亮点
- 优先问：如果只改一个条件，您最希望改哪一个？
- 适合技法：`tactic-switch`

## `cause-customer-summary-needed`

- 信号：用户要求盘点客户、生成小结、做阶段性总结、制定跟进策略
- 不要直接说：这个客户很有意向 / 继续跟进即可
- 优先问：缺不缺预算、决策人、购房时机、竞品比较、核心顾虑这些关键信息？
- 适合技法：`tactic-customer-inventory` `tactic-diagnose`
- 关键规则：信息不足时先追问；信息充分或用户明确要求小结时，按阶段性客户小结模板输出；默认不输出保存状态或持久化字段

## `cause-school-compliance-risk`

- 信号：客户问能不能读、是否对口、会不会划出去、规划学校能否入学
- 不要直接说：保证能读、肯定对口、绝对不变
- 优先问：孩子入学时间、目标学校、当前官方划片或规划依据、项目到学校距离
- 适合技法：`tactic-evidence-chain` `tactic-compliance-reframe` `tactic-micro-close`
- 关键规则：用历史惯性、地理距离、容量逻辑建立概率判断，最终以教育局公布为准

## `cause-price-negotiation`

- 信号：客户问最低价、优惠、折扣、能不能便宜、送什么，或反复磨具体房号价格
- 不要直接说：这是底价、领导特批、明天涨价
- 优先问：首付能到多少、月供上限、付款方式、今天是否能定、谁最终拍板
- 适合技法：`tactic-payment-probe` `tactic-staged-concession` `tactic-micro-close`
- 关键规则：先判断支付力和成交诚意，再阶梯释放，不一次亮底牌

## `cause-market-downturn`

- 信号：客户怕买了会跌、等市场稳、二手房卖不掉、觉得贵不如将就
- 不要直接说：以后肯定涨、现在就是底、再不买就亏
- 优先问：客户买房是自住、改善、学区、养老，还是短期投资？
- 适合技法：`tactic-compliance-reframe` `tactic-cost-of-wait` `tactic-tradeoff`
- 关键规则：不预测涨跌，把问题从投资判断拉回居住价值和等待成本

## `cause-project-fact-needed`

- 信号：用户要求按某项目口径回答，或问题涉及项目具体户型、价格、学校、优惠、交付、竞品、动态
- 不要直接说：根据通用经验，这个项目应该是……
- 优先问：有没有项目文档、项目名、项目主卡、价格文档、学校 FAQ 或最新动态？
- 适合技法：`tactic-evidence-chain` `tactic-diagnose` `tactic-micro-close`
- 关键规则：先按 [project-documents/README.md](../project-documents/README.md) 和该项目自己的文档找项目事实，再用通用销售应答框架组织表达；没有事实时明确提示需确认

## 判断原则

- 深因优先选最能解释客户行为的，不选最“好听”的
- 一次通常只抓一到两个深因，多了会分散动作
- 真不匹配时，最强的话术不是反驳，而是换房源
