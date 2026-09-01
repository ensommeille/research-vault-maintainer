# Knowledge Integration

## Index-first resolution

Do not scan the entire Vault for every paper.

Read the Research Index, derive candidate Topics/Concepts/relations, then retrieve only relevant files.

Before creating a new Topic/Concept, run a targeted duplicate/alias search even when the Index has no match.

Order:

`Reuse -> Alias/normalize -> Create`.

## Topic

Topic = what is being researched.

A new Topic should satisfy at least two of:

1. an independently meaningful research problem/direction;
2. capable of accumulating multiple papers;
3. capable of developing into a useful mini-survey with approaches/findings/limitations/questions/gaps.

Usually assign 1-3 Topics.

Prefer informative research levels rather than every ancestor category.

## Concept

Concept = reusable technical knowledge central to understanding a paper's method/contribution.

Create Concepts more strictly than Topics.

Incidental optimizers, backbones, or metrics should not become Concepts unless central to the research contribution.

If an entity already exists as a Topic or Concept, preserve the Vault's classification rather than creating a duplicate in another role.

## New pages

Do not create empty link targets.

A new Concept should minimally explain definition, role in this research context, and meaningful uses/papers.

A new Topic should support a living research map such as:

- Overview
- Key Problems
- Approaches
- Key Papers
- Current Findings
- Limitations
- Open Questions
- Research Gaps

Preserve existing Topic structure when present rather than forcing this template.

## Paper relationships

Store semantic paper relationships in the Paper note's Connections section.

Useful language includes:

- extends
- improves upon
- builds on
- uses
- same problem
- similar approach
- different approach
- contrasts with
- evaluates against
- shares dataset
- supports
- challenges

Every relationship must state why it exists.

Prefer high/medium-confidence relationships: explicit citation/direct comparison/extension, or meaningfully comparable work on the same problem.

Do not link papers merely because both use a generic technique.

Do not normally edit the older paper to add a reverse link; Obsidian backlinks provide reverse discoverability.

Incrementally update an existing dedicated "Subsequent Work"-style section only when consistent with that note's structure.

## Topic updates

Update a Topic only when a paper materially enriches or changes understanding of it.

Do not update broad ancestor Topics for every new paper.

Prefer incremental merge/append over rewrite.

Preserve contradictory evidence instead of overwriting earlier conclusions.

Important Topic claims should link to supporting Paper notes.

## Concept updates

Be more conservative than Topic updates.

Usually add meaningful usage/context; change definitions/mechanisms only when new evidence truly changes understanding.

## Knowledge types

Always distinguish:

- Evidence: directly supported by a paper/experiment.
- Synthesis: pattern inferred across multiple evidence sources, with links.
- Hypothesis: proposed explanation/question requiring validation.

Never silently promote a hypothesis to evidence.
