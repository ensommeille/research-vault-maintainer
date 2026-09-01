# Paper Note Schema

## Language

Write note prose in the user's conversation language unless the user specifies otherwise.

- **Frontmatter values stay in English** for accuracy and stable wikilinks: `title` uses the paper's original English title; `topics`/`concepts` use English names; `year`/`url`/`status`/`rating` are language-neutral.
- **Body prose** follows the user's language (e.g. Chinese). Render technical terms as `中文 (English)` — e.g. `条件扩散模型 (Conditional Diffusion Model)`, `水平金字塔映射 (Horizontal Pyramid Mapping)`.
- **Section headings** may be translated to the user's language while preserving the required section semantics (TL;DR → 概述; Problem & Motivation → 问题与动机; Method → 方法; Key Contributions → 关键贡献; Experiments → 实验; Key Findings → 关键发现; Limitations → 局限性; Research Relevance → 研究相关性; Connections → 关联; Open Questions → 待解决问题).
- Topic/Concept pages and the Research Index follow the same rule: prose in the user's language, entity names in English.

## Properties

Use the existing Vault's exact compatible property representation when already established. The intended semantic schema is:

```yaml
---
title:
year:
url:
status: unread
rating:
topics:
concepts:
---
```

Do not add `authors`, `venue`, or `related` by default.

### Status

Allowed: `unread`, `skimmed`, `studied`, `reproduced`.

Status is human-owned. New notes are always `unread`; never automatically change existing status.

### Rating

Rate 1-5 by value to the user's research, not general paper quality/prestige:

- 1: little direct research value; mostly peripheral/background.
- 2: some relevance but limited usefulness to current questions/methods/experiments.
- 3: clearly useful methods, evidence, data, viewpoints, or results.
- 4: highly relevant and materially useful to research direction, method design, experiments, or understanding.
- 5: core value; may directly influence direction/method choice and merits deep comparison or reproduction.

### Topics

Usually 1-3.

Topic = what is being researched: a persistent research area/problem/direction capable of accumulating multiple papers and a living survey.

Prefer informative levels; do not mechanically include all ancestors.

### Concepts

Usually 2-6.

Concept = reusable knowledge/technique central to understanding the work: mechanism, model idea, loss, representation, or experimental concept.

Do not create pages for every incidental optimizer/backbone/metric.

## Body template

```markdown
# {{title}}

## TL;DR

## Problem & Motivation

## Method
### Overview
### Key Components
### Objective / Loss

## Key Contributions
### Claimed by the Authors
### What Actually Matters

## Experiments
### Experimental Setup
### Main Results
### Ablation & Analysis

## Key Findings

## Limitations
### Reported by the Authors
### Additional Observations

## Research Relevance
### Why It Matters
### Potentially Reusable
### Potential Use

## Connections
### Topics
### Concepts
### Related Papers

## Open Questions
```

Required top-level sections:

- TL;DR
- Problem & Motivation
- Method
- Key Contributions
- Experiments
- Key Findings
- Limitations
- Research Relevance
- Connections
- Open Questions

Conditional subsections such as Objective/Loss, Ablation, architecture diagram, failure cases, implementation details, and Reproduction Notes should appear only when useful.

Do not emit empty boilerplate.

## Section rules

- TL;DR: 4-6 sentences answering Problem -> Idea -> Result -> Significance, not a rewritten abstract.
- Problem & Motivation: identify the actual bottleneck, insufficiency of existing approaches, and author's hypothesis when clear.
- Method: explain pipeline and why it is designed that way. Use Mermaid only when it materially improves understanding.
- Formulae: include only formulas supported by the paper; never invent missing equations.
- Contributions: distinguish author-claimed contributions from what materially matters to the user's research.
- Experiments: retain evidence that supports/challenges claims, not every number from every table.
- Key Findings: state what can be learned from evidence, beyond merely listing results.
- Limitations: separate author-reported limitations from additional evidence-grounded observations.
- Research Relevance: explain the rating and connect to the existing Vault where possible.
- Connections: explain why Topic/Concept/Paper links matter. Paper relationships belong here, not in a `related` property.
- Open Questions: formulate testable unresolved questions, not generic future-work filler.

## Reproduction Notes

Only add when reproduction work is actually being undertaken:

```markdown
## Reproduction Notes
### Environment
### Data Preparation
### Implementation
### Hyperparameters
### Deviations from Paper
### Results
### Issues
### Conclusions
```

The agent still never changes `status`; the user controls when it becomes `reproduced`.
