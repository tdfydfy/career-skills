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
