# 标签体系

## 主标签

主标签用于描述客户当前挂在嘴边的表面异议。

### 产品类

- `product-large`
- `product-small`
- `product-floor-high`
- `product-floor-low`
- `product-orientation-weak`
- `product-daylight-weak`
- `product-crowded`
- `product-quiet`

### 价格类

- `price-total-high`
- `price-unit-high`
- `price-value-doubt`
- `price-too-low`

### 区位类

- `location-bad`
- `location-school-weak`
- `location-commute`
- `location-immature`

### 家庭类

- `family-spouse`
- `family-mother`
- `family-child`
- `family-decision-maker-absent`

### 拖延类

- `delay-not-urgent`
- `delay-policy`
- `delay-price-cut`
- `delay-new-project`
- `delay-old-project`
- `delay-see-more`

### 资金类

- `funds-no-money`
- `funds-down-payment`
- `funds-monthly-pressure`
- `funds-cashflow-unclear`

### 信任与竞品类

- `trust-developer`
- `trust-delivery`
- `trust-market-downturn`
- `competition-compare`

### 销售应答总纲类

这些标签不是普通异议标签，而是切换工作模式的标签。出现后优先读 [03-sales-response-principles.md](./03-sales-response-principles.md)。

- `sales-customer-review`：客户盘点、需求分析、跟进策略、怎么聊
- `sales-customer-summary`：阶段性客户小结、客户盘点结果、跟进策略总结
- `sales-school-compliance`：学校、学区、划片、对口、规划学校、政策变化
- `sales-price-negotiation`：报价、优惠、折扣、最低价、赠品、车位、物业费
- `sales-competitor-advisory`：竞品对比、二选一、多个项目取舍
- `sales-market-downturn`：怕跌、等市场、二手房卖不掉、贵了不如将就
- `sales-project-docs`：项目文档、项目主卡、项目知识地图、按项目口径回答

## 深因标签

深因标签不是客户嘴上说的，而是更像真的卡点。

- `cause-budget`：预算、首付、月供压力
- `cause-risk`：怕买错、怕兑现不了、怕后悔
- `cause-family`：家人意见不统一
- `cause-compare`：项目之间还没比明白
- `cause-delay`：想继续拖，暂不愿定
- `cause-information`：信息不够，无法判断
- `cause-no-urgency`：需求不紧，时点不强
- `cause-face-saving`：不想直接说真实原因
- `cause-decision-absence`：真正拍板的人不在场
- `cause-unfit`：这套真的不适合
- `cause-customer-summary-needed`：用户要形成阶段性客户小结或跟进策略总结
- `cause-school-compliance-risk`：客户关注学校确定性，存在合规承诺风险
- `cause-price-negotiation`：客户不是单纯嫌贵，而是在试探支付边界、优惠权限或成交诚意
- `cause-market-downturn`：客户用投资涨跌逻辑替代自住价值判断
- `cause-project-fact-needed`：需要先确认项目事实，不能直接套通用话术

## 技法标签

- `tactic-empathy`
- `tactic-diagnose`
- `tactic-tradeoff`
- `tactic-scene`
- `tactic-family-translation`
- `tactic-cost-of-wait`
- `tactic-contrast`
- `tactic-reverse`
- `tactic-threshold`
- `tactic-loss-aversion`
- `tactic-future-self`
- `tactic-third-party`
- `tactic-switch`
- `tactic-micro-close`
- `tactic-customer-inventory`
- `tactic-payment-probe`
- `tactic-staged-concession`
- `tactic-evidence-chain`
- `tactic-compliance-reframe`
- `tactic-objective-compare`
- `tactic-need-ranking`

## 使用规则

- 主标签只定一个，除非客户明确从一个点切到另一个点
- 副标签最多两个，否则对话会被拆得过散
- 深因优先选一到两个，不要把所有可能性都报出来
- 同一句话里，标签顺序按 “表面异议 -> 深因 -> 技法 -> 收口” 组织

例子：

- “价格太高了，我老公也不同意，再等等政策。”
- 可标为：`price-total-high + family-spouse + delay-policy`
- 深因可判：`cause-family + cause-delay`
- 技法可选：`tactic-family-translation + tactic-cost-of-wait`

- “帮我盘点一下这个客户，下一步怎么跟？”
- 可标为：`sales-customer-review`
- 深因可判：`cause-information` 或 `cause-customer-summary-needed`
- 技法可选：`tactic-customer-inventory + tactic-diagnose`

- “这个项目到底能不能读那个学校？客户一直问。”
- 可标为：`sales-school-compliance + location-school-weak`
- 深因可判：`cause-school-compliance-risk + cause-risk`
- 技法可选：`tactic-evidence-chain + tactic-compliance-reframe`

- “按这个项目口径，帮我回客户问总价和学校的问题。”
- 可标为：`sales-project-docs + sales-price-negotiation + sales-school-compliance`
- 深因可判：`cause-project-fact-needed + cause-price-negotiation + cause-school-compliance-risk`
- 先读：`project-documents/README.md`，再读该项目自己的价格文档和学校 FAQ，最后套用对应技法
