# 独立技能实施清单

用于把注册表中的 `draft` 节点转成可发现的独立 Skill。

## 初始化前

- 确认节点职责、触发场景和不负责事项。
- 完成P0企业输入校准。
- 确认依赖节点和公共契约。
- 准备一个正常场景和一个异常场景样本。

## 初始化

使用 `skill-creator` 提供的 `init_skill.py` 创建根目录技能，名称与节点ID保持一致或在注册表中记录映射。

每个技能只保留：

```text
skill-name/
├── SKILL.md
├── agents/openai.yaml
├── references/
├── scripts/
└── assets/
```

仅创建实际需要的资源目录。

## SKILL.md

- YAML frontmatter只包含 `name` 和 `description`。
- `description` 同时写清能力和触发场景。
- 正文使用指令式表达，保持核心流程精简。
- 详细标准、案例和变体放入按需读取的 `references/`。
- 引用公共契约和网络依赖，不复制整套基础知识。
- 写明事实不足、权限不足和合规风险时的降级行为。

## 资源

- 重复计算、格式转换和批量检查使用脚本，并实际测试。
- 报告、PPT、表格和视觉模板放入 `assets/`。
- 企业制度、指标、案例和项目资料放入 `references/`。
- 项目专属事实与全局行业标准分开。

## 验证

- 运行 `quick_validate.py` 检查技能目录。
- 运行 `framework/scripts/validate_network.py` 检查网络。
- 用正常和异常样本前测。
- 检查结论能否追溯到事实、指标或明确假设。
- 检查未知字段不编造、财务权限不越界、对外内容已审核。
- 验证通过后将节点状态改为 `active`。
