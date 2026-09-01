# Research Synthesis, Comparison, and Gaps

## Problem-centric synthesis

Synthesize around research problems, assumptions, approach families, evidence, limitations, conflicts, and unresolved questions.

Do not merely concatenate summaries paper by paper.

## Progressive evidence depth

1. Landscape -> Research Index.
2. Topic synthesis -> Index + Topic pages.
3. Cross-paper comparison -> Topic + relevant Paper notes.
4. Evidence-critical judgment -> Paper notes + original tables/figures/protocols.

## Cross-paper comparison

Select dimensions relevant to the question, such as:

- problem
- assumptions
- core idea
- method
- inputs/outputs
- datasets
- evaluation protocol
- metrics
- baselines
- main evidence
- ablations
- strengths
- limitations
- research relevance

Before comparing reported numbers classify comparability as:

- Directly comparable
- Partially comparable
- Not directly comparable

Check dataset, split/protocol, preprocessing, occlusion setting, metric definition, matcher, and open/closed-set conditions as relevant.

Never rank two methods by headline numbers when protocols are not directly comparable.

Look for explanatory differences:

- what each method assumes;
- what information it ignores/restores;
- where conditions enter;
- what objective is optimized;
- why evidence differs.

## Evidence -> Synthesis -> Hypothesis

Evidence is paper-supported.

Synthesis is a cross-paper pattern and must link supporting papers.

Hypothesis is a proposed explanation or open question and must be labeled accordingly.

Preserve conflicting evidence.

Contradictions are often more useful than forced consensus.

## Candidate research gaps

Derive gaps from evidence rather than generic brainstorming.

Useful classes include:

- Method gap
- Evaluation gap
- Dataset/generalization gap
- Assumption gap
- Contradiction gap
- Integration gap

For each candidate gap provide:

- Evidence / linked papers
- Observed gap
- Why it matters
- Possible research direction
- Confidence: High / Medium / Low
- Verification needed

High: multiple explicit supporting limitations/conflicts or strong direct evidence.

Medium: reasonable structured inference across multiple papers without explicit consensus.

Low: primarily a new hypothesis suggested by the knowledge structure.

## Vault gap vs literature gap

Absence from the Vault proves only "not found in the current Vault".

Do not claim a literature-level novelty gap without external literature search.

When novelty matters, recommend/perform an external search if the agent has web access and the user wants literature-level verification.

Candidate gaps may be added to Topic `Research Gaps` only when clearly labeled Candidate and accompanied by evidence/confidence.

Exploratory ideas can go to Open Questions.
