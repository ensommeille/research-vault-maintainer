# research-vault-maintainer

面向 **Hermes Agent** 的一个 skill，用于把本地的 Obsidian 学术研究知识库（Vault）维护成一个「活的研究知识系统」，而不是一堆摘要的堆砌。

> 📌 `SKILL.md` 是给 Agent 读的操作规范；这份 `README.md` 是给人看的说明。

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
├── agents/openai.yaml        # OpenAI Codex / Claude Code 风格 agent 定义（Hermes 中为惰性文件）
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

把这个目录复制到 Hermes 的 skills 目录即可（`$HERMES_HOME` 默认是 `~/.hermes`，桌面版可能不同，用 `hermes config path` 查看）：

```bash
# macOS / Linux
mkdir -p ~/.hermes/skills/research
cp -r . ~/.hermes/skills/research/research-vault-maintainer/

# Windows（PowerShell，桌面版示例）
$HOME = (hermes config path | Split-Path -Parent)
Copy-Item -Recurse . "$HOME\skills\research\research-vault-maintainer"
```

安装后在新会话中即可调用，或执行 `/reload-skills` 重新扫描。

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
