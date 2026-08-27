# career-skills

`career-skills` 是面向房地产营销、销售与经营管理场景的能力体系仓库。项目将企业标准、业务方法、数据结构和常用成果沉淀为可组合的 Skill 网络，帮助 AI 在具体任务中形成可追溯、可审核、可执行的专业输出。

本仓库当前优先完善整体体系和公共能力，不以拆分更多独立 Skill 为目标。整体设计见 [NETWORK.md](./NETWORK.md)，节点地图见 [framework/NETWORK-MAP.md](./framework/NETWORK-MAP.md)。

## 体系结构

```text
基础能力层：统一项目、客户、指标、财务、事实、内容和组织标准
      ↓
业务技能层：完成分析、判断、策略、执行和协同工作
      ↓
常用成果层：编排多项能力，形成报告、方案、说辞和管理材料
      ↓
执行结果、复盘数据和新案例回流基础能力层
```

当前网络包含：

- 60 个能力节点，其中包括 6 个已接入体系的原有技能。
- 11 个基础能力模块。
- 23 个业务工作流。
- 20 个常用成果节点，其中 3 个已形成独立成果技能。
- 12 个结构化知识来源、148 条知识原子和 98 项统一指标。
- 15 类公共数据契约、32 项企业输入和 34 条任务路由。
- 自动校验脚本覆盖节点依赖、文件路径、知识与指标引用、YAML 解析及重复映射键等问题。

`draft` 节点表示框架和通用方法已经形成，但仍需继续校准企业口径并完成适用场景验证，不等同于已投入生产。

## 已有技能

| 技能 | 主要用途 |
| --- | --- |
| [content-compliance](./content-compliance) | 房地产营销文案与图片合规审核 |
| [marketing-liaison](./marketing-liaison) | 总部、地区与项目之间的营销判断和协同 |
| [sales-officer](./sales-officer) | 单个客户需求、购买力、意向和跟进策略分析 |
| [sales-talk-coach](./sales-talk-coach) | 项目说辞考核和客户接待实战对练 |
| [saletricks](./saletricks) | 买方异议诊断、销售应答和成交推进 |
| [storyline-creation](./storyline-creation) | 项目故事定位、营造指引和营销工具包 |
| [project-value-strategy](./project-value-strategy) | 项目价值点梳理、落地执行与传播转化策略 |

## 已形成的成果技能

| 技能 | 主要用途 |
| --- | --- |
| [launch-marketing-report](./launch-marketing-report) | 项目首开营销策略报告 |
| [launch-price-report](./launch-price-report) | 首开价格报告和价格会审批材料 |
| [sustained-sales-diagnosis](./sustained-sales-diagnosis) | 持销期专题诊断与改善方案 |

这些成果技能已经通过虚构案例前测。基础信息和企业口径通过业务共创直接确认并持续写回体系，不单独设计通用问卷，也不要求为基础校准准备脱敏材料；执行具体报告任务时，再按成果需要读取现有周月报、台账、会议纪要、专题材料和项目数据。财务口径、审批模板等尚未确认的企业输入继续按实际使用顺序补充。

## 统一项目诊断结构

项目诊断、持销专题及相关经营分析统一采用五部分结构：

1. 管理摘要。
2. 目标与缺口。
3. 项目客观分析。
4. 综合诊断与策略动作。
5. 最后小结。

第三部分根据实际问题综合分析市场、竞争、客户、销售、货量、量价、利润、团队、动作执行和专项任务，数据与对应判断放在一起，不重复设置独立数据章节。利润重点看项目净利润、项目毛利润和项目成本利润率；团队重点看岗位配置与胜任度、销售强度与饱和度、弱项补强，以及佣金、底薪和年度薪酬费用。

第四部分采用总—分结构：先形成项目整体判断、核心矛盾关系和基于项目客观条件的策略倾向，再按主因展开证据、专业判断、影响、策略、关键行动、责任和复盘。主因可以由数据分析得出，也可以由用户、管理者或一线人员补充；二者冲突时并列呈现并说明待验证事项。

第五部分不新增分析，只归纳项目直接执行、地区协调支持和集团决策审批。AI 不根据单项目资料推断公司整体业绩、宏观市场方向或跨项目资源取舍，最终决策由集团和地区结合全局信息作出。

## 目录说明

```text
career-skills/
├── README.md
├── NETWORK.md                    # 总体架构和建设规则
├── framework/
│   ├── skill-network.yaml        # 节点注册表、依赖和状态
│   ├── task-router.yaml          # 用户任务到能力节点的路由
│   ├── enterprise-inputs.yaml    # 待企业确认的制度和数据
│   ├── contracts/                # 公共输入输出契约
│   ├── foundations/              # 基础标准
│   ├── business/                 # 业务工作流规格
│   ├── deliverables/             # 常用成果编排配方
│   ├── knowledge/                # 结构化知识来源
│   ├── examples/                 # 虚构端到端案例
│   └── scripts/                  # 网络校验脚本
└── <skill>/
    ├── SKILL.md                  # 触发条件、工作流和输出纪律
    ├── agents/openai.yaml        # Skill 界面配置（可选）
    ├── references/               # 按需加载的专业资料（可选）
    └── scripts/                  # 确定性计算或处理脚本（可选）
```

## 使用方式

1. 先根据最终成果识别任务，而不是直接拼接多个 Skill。
2. 通过 [framework/task-router.yaml](./framework/task-router.yaml) 定位成果节点或业务节点。
3. 涉及真实项目时，使用 `framework/contracts/` 整理项目、市场、竞争、客户、销售、货量、量价、利润、团队、动作执行和专项任务输入。
4. 对缺失数据明确标注假设和验证动作，不用默认数据代替项目事实。
5. 最终输出应保留“经营意图 → 事实 → 核心矛盾 → 策略 → 动作 → 目标与预算 → 复盘”的推导链。

单个已有 Skill 也可以独立调用。例如：

```text
使用 $sales-talk-coach，做一轮中级复访谈价对练。
使用 $saletricks，分析客户说“价格太高”的真实顾虑并给出下一步话术。
使用 $launch-price-report，根据项目、客储和房源资料编制首开价格报告。
```

## 校验

运行网络校验，检查节点、依赖、路径、知识原子、指标、企业输入、任务路由、YAML 解析和重复映射键：

```bash
python3 framework/scripts/validate_network.py
```

运行三个端到端虚构案例校验：

```bash
python3 framework/examples/launch-marketing-synthetic/validate_case.py
python3 framework/examples/launch-price-synthetic/validate_case.py
python3 framework/examples/sustained-sales-diagnosis-synthetic/validate_case.py
```

## 建设状态

当前建设重点是校准企业输入并走通完整纵向链路；具体成果在实际使用或前测时，再按需引用项目资料和案例。节点状态、实施顺序和激活标准见 [framework/BUILD-ROADMAP.md](./framework/BUILD-ROADMAP.md)。
