---
name: research-vault-maintainer
description: Maintain a local Obsidian academic research knowledge base when an agent has filesystem access to the Vault. Use for ingesting papers from PDFs, arXiv/DOI/publisher/web links or supplied text; multimodal reading of paper text, equations, tables, figures and architecture diagrams; creating standardized paper notes; resolving Topics and Concepts; maintaining a Research Index; integrating evidence-backed cross-paper connections; literature synthesis and comparison; candidate research-gap analysis; Inbox organization; and safe Vault audits. Adapt to the existing Vault and Papers.base instead of imposing a new structure.
version: 1.0.0
author: CarlosLiao
license: MIT
metadata:
  hermes:
    tags: [research, obsidian, knowledge-base, papers, literature-review, vault]
    related_skills: [obsidian, arxiv]
---

# Research Knowledge Base Maintainer

Maintain an Obsidian Vault as a living research knowledge system rather than a collection of summaries. Treat the actual Vault as the source of truth and `Research Index.md` as a compact semantic map/cache.

## Operating principles

- Learn and preserve the existing Vault structure, naming, links, and Base schema before imposing conventions.
- Prefer conservative, incremental edits. Never rewrite human-authored material merely to standardize it.
- Keep evidence, synthesis, and hypothesis distinct. Never present an inference or candidate gap as an established literature fact.
- Use scripts for deterministic indexing/validation only; use model reasoning for semantic classification, synthesis, and research judgments.
- Ignore `.obsidian/` configuration by default. Modify it only on explicit request.
- When a large or structural change is proposed, show the plan and wait for confirmation before rename, merge, delete, mass move, mass link repair, schema change, `Papers.base` modification, or broad Topic restructuring.
- Write note prose in the user's conversation language unless the user specifies otherwise; keep frontmatter values, file/folder names, and Topic/Concept/paper-title strings in English for accuracy. See `references/paper-note-schema.md` for the exact language rule.

## Select a workflow

1. **First use on a Vault**: run Vault Bootstrap below.
2. **New paper / URL / PDF**: follow Paper Intake.
3. **Research question / comparison / gap**: follow Research Analysis.
4. **Inbox organization**: follow Inbox Maintenance.
5. **Vault health request**: run Quick Audit or Deep Audit.

Read only the relevant reference file for the active workflow:
- Paper note schema and rating: `references/paper-note-schema.md`
- Multimodal paper evidence: `references/evidence-protocol.md`
- Topic/Concept resolution and integration: `references/knowledge-integration.md`
- Research Index behavior: `references/research-index.md`
- Synthesis/comparison/gaps: `references/research-synthesis.md`
- Bootstrap, Inbox, audit, permissions: `references/vault-maintenance.md`

## Vault Bootstrap

Before first maintenance of an existing Vault:

1. Confirm the Vault root. A directory containing `.obsidian/` is strong evidence. If multiple candidate Vaults exist, ask which one to use.
2. Do not modify existing research notes during discovery.
3. Run `scripts/scan_vault.py <vault-root>` to build a lightweight structural index when shell execution is available.
4. Locate `Papers.base` or other `.base` files and inspect their existing property expectations.
5. Identify likely Papers, Topics, Concepts, existing research maps, naming conventions, and wikilink patterns.
6. If an existing `Research Index.md`, `Research Map.md`, or equivalent exists, prefer it. Otherwise create `Research Index.md` only after understanding the Vault.
7. Produce an initial audit report. Do not automatically perform rename/merge/delete/schema changes discovered during bootstrap.

## Paper Intake

For a paper supplied as PDF, URL, DOI, arXiv link, publisher/project page, full text, or an existing unprocessed Vault item:

1. Identify the paper and check for a high-confidence duplicate using URL/DOI/arXiv ID/title metadata where available.
2. For a link, seek the complete paper or PDF rather than relying on the abstract page. If full text cannot be obtained, explicitly downgrade the analysis and never imply a full-paper read.
3. Follow `references/evidence-protocol.md`. Read text and critical visual evidence, especially architecture figures, result tables, ablations, qualitative results, and failure cases.
4. Read the Research Index first, then perform targeted Vault retrieval. Verify before creating any new Topic or Concept.
5. Follow `references/knowledge-integration.md` to resolve Topics, Concepts, and meaningful paper relationships.
6. Generate the note using `references/paper-note-schema.md`. Every newly created paper note MUST have `status: unread`. Never infer another status from how deeply the agent read the paper.
7. Assign `rating` from 1-5 based on value to the user's research, not general academic prestige or paper quality.
8. Integrate only meaningful new knowledge into relevant Topic/Concept pages. Do not update every ancestor Topic merely because it is linked.
9. Delta-update the Research Index only when the research map materially changes.
10. Run a quick validation on the created/changed paper note when possible.

## Research Analysis

Use progressive evidence depth rather than reading the whole Vault:

1. Landscape question -> Research Index.
2. Topic synthesis -> Research Index + relevant Topic pages.
3. Cross-paper analysis -> relevant Topic pages + Paper notes.
4. Evidence-critical comparison -> Paper notes + original paper tables/figures/protocol as needed.

Follow `references/research-synthesis.md`. In particular:
- Organize synthesis around research problems/approaches, not a sequence of paper summaries.
- Check experimental comparability before ranking methods by reported numbers.
- Preserve conflicting evidence.
- Build candidate gaps through `Evidence -> Synthesis -> Hypothesis -> Candidate Gap`.
- State "not found in the current Vault" rather than "not found in the literature" unless an external literature search has verified the latter.

## Inbox Maintenance

Classify Inbox items before acting. Process recognizable papers through Paper Intake; associate research notes/ideas when confidence is high; report duplicate candidates; leave unknown items untouched. Preserve original PDFs unless an established Vault convention says where they belong or the user has approved a policy. See `references/vault-maintenance.md`.

## Audits

Use `scripts/validate_papers.py` and `scripts/check_links.py` for deterministic checks when available.

- **Quick Audit**: current changes, schema validity, newly introduced broken links, duplicate candidates, and Index consistency.
- **Deep Audit**: whole-Vault structure, papers, Topics, Concepts, links, properties, duplicates, orphans, knowledge integrity, and Research Index reconciliation.

A validator may flag an invalid `status`, but MUST NOT repair or change an existing status. Status is human-owned.

## Human-owned status

Allowed values are exactly:

`unread`, `skimmed`, `studied`, `reproduced`

Rules:
- New AI-created paper notes: always `unread`.
- Never change an existing paper's status automatically, even after deep analysis or reproduction assistance.
- If `status: reproduced` exists without reproduction notes, report the inconsistency; do not downgrade status.

## Modification permissions

May perform automatically when justified:
- Create a new Paper note.
- Set new Paper status to `unread`.
- Assign a new Paper rating.
- Reuse existing Topic/Concept pages.
- Create a necessary Topic/Concept after Index-first lookup and targeted duplicate verification.
- Create meaningful wikilinks.
- Incrementally update a relevant Topic.
- Conservatively add Concept usage information.
- Delta-update the Research Index.

Require user confirmation before:
- Rename, merge, or delete.
- Mass file moves or mass link repair.
- Changing schemas or `Papers.base`.
- Large Topic restructuring.
- Overwriting substantial human-authored text.
- Changing an existing rating unless the user explicitly requested rerating.

## Local-agent safety

- Treat filesystem writes as potentially synced by Obsidian Sync, Git, OneDrive, iCloud, Syncthing, or similar systems.
- If a large operation is requested and the Vault is a Git repository, surface that fact and make changes reviewable; never commit unless explicitly requested.
- Never assume a missing wikilink is an error; it may intentionally reserve a future note.
- Prefer omission over fabrication when a paper figure/table/number cannot be read reliably.
