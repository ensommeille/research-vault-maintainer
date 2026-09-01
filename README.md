# research-vault-maintainer

一个用于把本地 Obsidian 学术研究知识库（Vault）维护成「活的研究知识系统」的 **Agent skill**，而不是一堆摘要的堆砌。

> 📌 `SKILL.md` 是给 Agent 读的操作规范；这份 `README.md` 是给人看的说明。

## 兼容哪些 Agent

核心是一套通用的 `SKILL.md` 规范（`name` + `description` frontmatter，正文按需加载分文件 reference），不绑定单一 Agent：

| Agent | 兼容性 | 说明 |
|---|---|---|
| Hermes Agent | ✅ 原生 | `SKILL.md` + `references/` + `scripts/` 直接可用 |
| Claude Code | ✅ 兼容 | 支持 SKILL.md 规范，`references/` / `scripts/` 同样适用 |
| OpenAI Codex | ✅ 兼容 | 支持 SKILL.md 规范；`agents/openai.yaml` 是给 Codex 风格子 agent 的可选定义 |
| 其他支持 SKILL.md 规范的 Agent | ✅ 通用 | 只要支持 `name` + `description` frontmatter 即可 |

> 唯一 Hermes 专属的内容是 frontmatter 里的 `metadata.hermes` 字段（仅用于标签与关联 skill），其他 Agent 会自动忽略。`agents/openai.yaml` 在 Hermes 中是惰性文件，在 Codex / Claude Code 风格里可作为子 agent 定义。

## 它能做什么

| 能力 | 说明 |
|---|---|
| 📄 论文录入 | 从 PDF / arXiv / DOI / 出版商链接 / 纯文本录入，做多模态阅读（正文、公式、表格、架构图） |
| 📝 标准化笔记 | 按固定模板生成论文笔记（概述 / 问题与动机 / 方法 / 关键贡献 / 实验 / 关键发现 / 局限性 / 研究相关性 / 关联 / 待解决问题） |
| 🗂 知识组织 | 维护 Topic（研究主题）、Concept（可复用技术概念）页面，以及一个 Research Index（语义导航层） |
| 🔬 文献综合 | 跨论文对比、保留矛盾证据、候选研究缺口分析 |
| 🩺 Vault 体检 | 检查 frontmatter 合法性、断链、重复、孤儿笔记；区分「可直接修复」与「需人工确认」 |

## 设计原则

- **保守增量**：先学习并保留现有 Vault 结构，绝不擅自改写人类写的内容。
- **证据 / 综合 / 假设分离**：不把推断或候选缺口当成既成文献事实。
- **status 由人拥有**：新笔记一律 `status: unread`，Agent 从不自动改状态。
- **语言跟随用户**：笔记正文用用户的对话语言（如中文），但 frontmatter、论文名、Topic/Concept 名保持英文以保证 wikilink 准确；术语采用「中文 (English)」格式。

## 目录结构

```
.
├── SKILL.md                  # Agent 读的操作规范（入口）
├── agents/openai.yaml        # Codex / Claude Code 风格子 agent 定义（Hermes 中为惰性文件）
├── references/               # 按工作流加载的参考规范
│   ├── paper-note-schema.md        # 论文笔记模板与评分规则
│   ├── evidence-protocol.md        # 多模态证据协议
│   ├── knowledge-integration.md    # Topic/Concept 解析与集成
│   ├── research-index.md           # Research Index 行为
│   ├── research-synthesis.md       # 综合 / 对比 / 缺口分析
│   └── vault-maintenance.md        # Bootstrap、Inbox、审计、权限
└── scripts/                  # 确定性索引 / 校验脚本
    ├── scan_vault.py         # 生成 Vault 结构索引
    ├── validate_papers.py    # 校验论文 frontmatter（不修改文件）
    └── check_links.py        # 报告未解析的 wikilink（不修复）
```

## 安装

把目录放到对应 Agent 的 skills 位置即可（具体路径以各 Agent 官方文档为准）：

| Agent | 安装位置（参考） |
|---|---|
| Hermes Agent | `$HERMES_HOME/skills/research/research-vault-maintainer/`（默认 `~/.hermes`） |
| Claude Code | `~/.claude/skills/research-vault-maintainer/`（用户级）或项目内 `.claude/skills/` |
| OpenAI Codex | 项目内 `.codex/skills/` 或用户级 `~/.codex/skills/` |

```bash
# 通用：克隆后复制到目标 skills 目录
git clone https://github.com/ensommeille/research-vault-maintainer.git
cp -r research-vault-maintainer <skills-root>/research/research-vault-maintainer/
```

Hermes 用户也可用 CLI 安装：

```bash
hermes skills install https://github.com/ensommeille/research-vault-maintainer/raw/main/SKILL.md
```

## 三个脚本

```bash
# 生成 Vault 结构索引（-o 输出到文件，否则打印到 stdout）
python scripts/scan_vault.py <vault-root> [-o index.json]

# 校验论文笔记的 frontmatter（只报告，不修改）
python scripts/validate_papers.py <vault-root-or-file>

# 报告未解析的 wikilink 候选（只报告，不修复）
python scripts/check_links.py <vault-root>
```

> 脚本只做确定性的索引与校验；语义分类、综合、研究判断交给模型推理。

## 许可

MIT
