# 项目分类与阶段模型

状态：`draft`

## 目的

用相互独立的分类轴描述项目，不把物业、销售阶段、管理关注度、利润约束和专项任务混成一个项目类型。所有业务技能和成果技能先读取项目分类，再选择适用的分析方法和动作模块。

## 分类轴

### 1. 物业类型 `property_type`

| 值 | 定义 |
| --- | --- |
| `residential` | 住宅产品 |
| `parking` | 车位产品 |
| `commercial` | 商铺或其他商业产品 |
| `mixed` | 同一任务同时涉及多种物业，输出时仍需分别核算 |

库存不是物业类型，应通过库存结构和销售阶段表达。

### 2. 销售阶段 `sales_stage`

销售阶段只保留首开、持销和尾盘三类：

| 值 | 定义 | 主要管理内容 |
| --- | --- | --- |
| `launch` | 围绕项目首次开盘组织经营准备，并延续至首开日后第二个自然日（`D0-D+2`）结束 | 首开货量、价格、客户、推广、展示、销售组织、关键节点和首开业绩 |
| `sustained` | `D+2`结束后进入持续销售和滚动加推，直至满足尾盘条件 | 流速、客户转化、货量结构、价格、渠道、费用和滚动策略 |
| `tail` | 全盘剩余住宅套数严格少于50套后的专项收尾销售阶段 | 尾货结构、难售原因、清栋清盘、团队调整、组织投入和退出安排 |

蓄客、认筹、加推、选房等属于销售技术动作或关键事件，不作为长期销售阶段。售楼处开放、样板房开放、认筹等首开储客节点发生在首开阶段，总部关注其计划时间、实际完成、效果和关键数据。首开日及之后两个自然日形成的有效认购均计入首开销售业绩。

`D+2`结束后转入持销阶段。持销期仍会进行储客和加推，具体节奏和组织原则上由地区公司自行把控；涉及重大价格、资源或权限事项时再按治理规则升级。全盘剩余住宅套数严格少于50套时转入尾盘阶段，开始重点管理尾货清理和团队调整。

项目定位、启动会等属于前置决策工作，不作为销售阶段枚举。首开筹备的正式起点仍需继续共创确认。

### 3. 交付维度 `delivery_context`

交付是与销售阶段并行的独立维度，不替代首开、持销或尾盘。项目可以在持销或尾盘的同时进入交付，也可以在交付期间继续销售剩余货量。

交付维度至少记录：

```yaml
delivery_context:
  active: false
  phase: null
  milestones: []
  risks: []
  cross_function_tasks: []
```

交付阶段的细分状态、进入退出节点和跨专业责任后续在交付管理专题中确认。

### 4. 管理关注度 `management_attention`

管理关注度描述总部在所有项目常规管理基础上的关注聚焦程度。所有项目都会投入管理精力，正常项目也不能脱离跟踪；分类差异在于是否需要总部增加关注、提高复盘频次或组织专项支持。关注度不是经营健康度评分，也不由单一指标自动计算。

| 值 | 定义 | 管理方式 |
| --- | --- | --- |
| `normal` | 项目各方面没有明显问题，按既定计划执行即可 | 保持常规跟踪、经营复盘和必要支持，异常时再升级关注 |
| `key` | 项目具有重大经营、战略或组织意义，需要总部持续聚焦 | 明确关注原因、关键节点、责任人和需要支持的事项；重点项目不等于问题项目 |
| `difficult` | 项目已经遇到较难解决的问题，需要总部高度关注 | 聚焦关键难题、保护边界和可行解法；按客观条件调整销售与价格预期，不套用正常项目要求 |

管理关注度与销售阶段相互独立：首开、持销、尾盘项目均可被列为正常、重点或难点。亏损是财务事实或约束，不单独作为关注度枚举；亏损项目通常需要较高关注，但仍应说明具体关注原因。

关注度主要由总部结合销售业绩完成情况作出综合判断，并应记录判断原因和复核节点。年度合约额目标完成与全年预计实现反映长期结果，月度任务完成与全月预计反映短期执行，两者同时管理、相互校验，不相互替代。后续完成压力、低流速、销售质量、市场变化、项目重大意义和专项任务用于补充解释，但不能按单一阈值自动生成关注度。难点项目的问题通常已经不容易解决，应设置符合现实的销售、价格和利润预期，而不是机械沿用正常项目基准。

### 5. 经营目标与专项任务 `management_objectives`

大多数项目以销售业绩为主要目标，同时兼顾利润。不要把现金流、库存、品牌等常规经营结果随意设成与销售并列的项目主目标。

项目目标按以下结构记录：

```yaml
management_objectives:
  sales_objective: primary
  profit_requirement: balanced
  sales_expectation: null
  price_expectation: null
  special_tasks:
    - task_id: null
      task_type: government-coordination | supporting-facility | land-exchange | fit-out | other
      task_goal: null
      formal_management_source: null
      owner: null
      collaborators: []
      success_criteria: null
      status: not-started | in-progress | blocked | completed | unknown
      current_progress: null
      milestones:
        - milestone: null
          target_date: null
          actual_date: null
          status: not-started | in-progress | delayed | completed | unknown
          evidence_ids: []
      blockers: []
      next_action: null
      regional_support_needed: []
      group_decisions_needed: []
      review_date: null
```

- 常规项目采用“销售业绩主导、兼顾利润”的目标关系。
- 个别重点、难点或亏损项目存在较强利润压力时，可将 `profit_requirement` 调整为 `priority`，明确流速让位于利润，并相应调整销售和价格预期。
- 项目层面的策略分析综合市场、客户、销售、货量、价格、利润和专项目标等客观数据，形成维持现状、加快销售、保护价格或等待窗口等项目情景，说明各情景的适用条件、量价结果、库存周期和风险。
- 项目分析可以说明“从项目客观条件看哪个情景更有支撑”，但不自行判断公司整体业绩缺口、宏观市场方向或跨项目资源取舍，也不代替最终经营决策。集团和地区结合整体经营情况作最终选择；其正式下达的目标、利润边界和策略要求作为项目输入读取，不由成果技能推断。
- 公司整体缺数或管理层判断后续市场下行时，集团、地区可决定降价抢跑；公司业绩充足且管理层判断市场将好转时，也可决定提价或保留货量等待。此类公司级理由应标记为管理输入和决策依据，与项目客观分析分开呈现。
- 政府沟通、配套落地、换地、精装等个性化要求作为 `special_tasks` 单独记录，不挤占销售目标字段，也不被通用枚举限制。每项任务至少保留正式来源、任务目标、成功标准、责任人、节点、当前进展、阻碍、下一动作和所需支持；未取得进展信息时标记未知，不以销售结果反推任务已经完成。
- 专项任务与销售阶段、交付维度并行。它可以影响销售、利润或交付，但不得据此改写项目的首开、持销、尾盘阶段；同一事项同时属于交付管理时，通过任务标识关联，不重复形成相互冲突的状态。
- 利润优先和专项任务必须由有权管理主体确认，成果技能不得根据单一指标自行推断。

### 6. 市场环境 `market_condition`

- `hot`：需求和流速较强，可评估集中释放和价格优化。
- `stable`：供需相对稳定，以结构和转化效率为主。
- `weak`：需求不足或竞争加剧，需要控制预期和资源效率。
- `structural-opportunity`：整体市场一般，但特定板块、时点、面积段或业态存在供需错配。

市场环境必须注明统计范围、统计周期和证据，不可只用主观感受判断。

### 7. 推售模式 `sales_mode`

- `concentrated-launch`：以明确节点集中蓄客、认筹、选房和成交。
- `continuous-sale`：持续释放、持续沟通、来客即转化。
- `batch-release`：按楼栋、产品或客户成熟度分批释放。
- `special-clearance`：针对顶底、特殊位置或尾货进行专项去化。

## 首开关键决策节点

### 启动会

在拿地后召开，确定项目整体策略、整盘及分业态价格、货值、利润和其他核心经营指标，是后续经营比较的重要基准。

### 首开价格评审会

在首次开盘前召开，通常距启动会三至六个月，决策首开范围、首开整体及分业态价格、首开销售套数、合约额和去化目标。期间经济技术指标和市场行情允许发生变化，但报告必须与启动会基准逐项对比，原则上尽量保持或超越启动会指标；未达到时说明原因、影响和补救方案。

## 推售单元

每个重点推售单元至少记录：

```yaml
unit_scope: null
location_and_product: null
available_units: null
target_price: null
strategic_role: null
target_sales: null
target_customer: null
supporting_actions: []
constraints: []
```

这里的 `strategic_role` 只描述该批房源在推售组合中的作用，例如引流、走量、标杆、利润贡献或难售处理，不代表项目整体经营目标。

## 标准分类输出

```yaml
project_classification:
  property_type: null
  sales_stage: launch | sustained | tail
  delivery_context:
    active: false
    phase: null
    milestones: []
    risks: []
  management_attention: normal | key | difficult
  attention_reasons: []
  attention_assessed_by: null
  attention_review_date: null
  management_objectives:
    sales_objective: primary
    profit_requirement: balanced | priority
    sales_expectation: null
    price_expectation: null
    special_tasks: []
  market_condition: null
  sales_mode: null
  evidence_ids: []
  assumptions: []
  unresolved_items: []
```

## 已确认与待共创

已确认：

- 销售阶段仅包括首开、持销、尾盘。
- 蓄客、认筹、加推等是技术动作或事件，不是销售阶段。
- 首开日及之后两个自然日（`D0-D+2`）属于首开业绩窗口，窗口内有效认购计入首开销售业绩，之后进入持销。
- 持销期储客和加推原则上由地区公司自行把控。
- 全盘剩余住宅套数严格少于50套时进入尾盘，重点转向尾货清理和团队调整。
- 交付是与销售阶段并行的独立维度。
- 管理关注度分为正常、重点、难点，不是经营健康度评分。
- 关注度主要由总部以销售业绩完成情况为首要依据综合判断；年度目标管理长期结果，月度任务管理短期执行，二者不冲突；所有项目均保持管理投入，正常不等于不管。
- 项目通常以销售业绩为主并兼顾利润；个别项目可利润优先，并可设置个性化专项任务。项目层面提供客观分析和情景测算，集团、地区结合整体经营作最终量价决策。

待继续共创：

- 首开筹备的正式起点。
- 重点、难点项目的复核频次、升级、降级和退出机制。
- 交付维度的细分状态及跨专业责任。
- 利润优先模式的确认权限和最低经营边界。
- 不同物业类型是否使用相同阶段规则。

## 来源原子

主要引用 `PROJ-001` 至 `PROJ-004`、`STRAT-002` 至 `STRAT-007`、`GOV-009`、`LPR-001` 至 `LPR-003`、`OPM-032` 至 `OPM-036`。
