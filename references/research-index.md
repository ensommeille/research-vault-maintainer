# Research Index

`Research Index.md` is a compact, human-readable and model-readable semantic map of the Vault.

It is a cache/navigation layer, not the source of truth; the actual Vault is authoritative.

## Purpose

Use it to summarize research scope, important Topics/Concepts, high-level research landscape, knowledge state, and meaningful open questions.

It should help both the researcher and the agent navigate without repeatedly reading the whole Vault.

Do not maintain fragile static counts such as `Papers: 18`; use Bases/dynamic queries for counts where appropriate.

## Suggested shape

Preserve an existing equivalent file/structure when available.

Otherwise a useful structure is:

```markdown
# Research Index

## Research Scope
## Topics
## Concepts
## Research Landscape
## Knowledge State
## Open Research Questions
```

The Index should describe structure and meaning, not duplicate every Paper note.

## Retrieval strategy

`Research Index -> candidate entities -> targeted Vault retrieval -> semantic verification`.

If the Index has no exact match, do not immediately create a page.

Search targeted synonyms/nearby terms in the actual Vault first.

## Updating

After Paper Intake, delta-update the Index only if the research map materially changes:

- a new meaningful Topic/Concept;
- new stable approach branch;
- changed knowledge state;
- important open question.

Do not rewrite the Index after every paper.

Stable research landscape belongs in the Index.

Speculative future directions/candidate gaps belong primarily in Topic Open Questions/Research Gaps until sufficiently established.

## Reconciliation

During Deep Audit, compare Index against the actual Vault for:

- missing/stale entities;
- stale links/relationships;
- open questions that may have been resolved by later evidence.

Propose significant semantic upgrades for review rather than silently rewriting human judgments.
