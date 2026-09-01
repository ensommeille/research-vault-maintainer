# Vault Maintenance

## First-run safety

Learn the Vault before modifying it.

Infer organization from paths, properties, content, backlinks, Research Index, and `.base` files.

Do not require fixed `Papers/Topics/Concepts/Inbox` folders.

Ignore `.obsidian/` by default.

Preserve existing research maps and schemas.

## Inbox

Classify each item as:

- Paper
- Research Note
- Research Idea
- Duplicate Candidate
- Unknown

Process papers via Paper Intake.

Associate notes/ideas only when confidence is high.

Report duplicate candidates.

Leave unknown items untouched.

Do not delete an original PDF after note creation.

Move PDFs only according to an established Vault convention or user-approved policy.

## Duplicate papers

High confidence:

- same DOI;
- same arXiv ID;
- same canonical URL.

Medium-high:

- strongly matching normalized title/year/content metadata.

Treat conference/arXiv/journal versions as potentially distinct versions; report rather than automatically merge.

## Duplicate Topics/Concepts

Detect semantic/name duplicates but never automatically merge or rename.

Report:

- candidates;
- likely canonical target;
- rationale;
- affected links.

Wait for confirmation.

## Orphans

Classify rather than equating orphan with garbage:

- Paper with no Topic/Concept: likely needs integration.
- Topic with no papers/subtopics: possible empty shell.
- Concept with no meaningful usage/backlinks: possible unnecessary concept.
- Personal/research note: report only; never infer deletion.

## Broken links

A missing wikilink may intentionally reserve a future note.

Report likely typo targets with confidence.

Mass repair requires confirmation.

## Paper property audit

Intended fields:

`title`, `year`, `url`, `status`, `rating`, `topics`, `concepts`.

Allowed status exactly:

`unread`, `skimmed`, `studied`, `reproduced`.

Never repair/change an existing status automatically.

Rating may be empty in old notes; otherwise integer 1-5.

Do not bulk invent ratings merely for completeness.

Check:

- missing URL;
- malformed properties;
- inconsistent link/list representation;
- duplicate naming;
- likely Topic/Concept role confusion.

Semantic findings are suggestions, not automatic edits.

## Papers.base

Read `.base` files to understand filters/property expectations and ensure generated notes remain compatible.

Do not modify `Papers.base` automatically.

If Skill conventions conflict with the actual Base schema, surface the conflict and ask which schema is canonical.

## Audits

Quick Audit:

- current-operation schema;
- introduced broken links;
- duplicate candidates;
- Index consistency.

Deep Audit:

- full structure;
- Papers;
- Topics;
- Concepts;
- links;
- properties;
- duplicates;
- orphans;
- Research Index reconciliation;
- knowledge integrity.

Organize reports into:

- Critical
- Structural
- Knowledge Integrity
- Links
- Metadata
- Research Index
- Suggested Actions

Separate low-risk fixes from review-required actions.

Knowledge integrity includes:

- unsupported Topic claims;
- synthesis without paper evidence;
- candidate gaps presented as established facts.

## Permissions

Automatic:

- new Paper notes;
- new status `unread`;
- new-paper rating;
- reuse existing entities;
- necessary new entity after verification;
- meaningful links;
- incremental relevant Topic updates;
- conservative Concept usage updates;
- Index delta updates.

Confirmation required:

- rename;
- merge;
- delete;
- mass moves;
- mass link repair;
- schema/Base changes;
- broad Topic restructuring;
- substantial overwrite of human text;
- changing an existing rating unless rerating was explicitly requested.
