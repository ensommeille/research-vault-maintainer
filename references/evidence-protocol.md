# Multimodal Evidence Protocol

Treat academic PDFs as multimodal evidence, not extracted text alone.

## Acquisition

For URL/DOI/arXiv inputs, seek complete full text/PDF. If only metadata/abstract is available, state the limitation and do not generate claims that imply full-paper inspection.

## Evidence inventory

Before final synthesis, identify critical:

- method/architecture/pipeline figures;
- main-result tables;
- ablation tables/plots;
- qualitative comparison figures;
- failure cases;
- equations essential to the contribution.

Use captions and surrounding text to locate high-value visuals.

Explicit references such as "as shown in Fig. 2", "Table 3 summarizes", or "ablation in Table 5" make those visuals mandatory evidence when accessible.

## Cross-check

Build Method from method text + equations + architecture visuals + captions.

Build Experiments/Findings from tables/plots + captions + surrounding claims.

Check whether the actual evidence supports the authors' prose.

Do not infer superiority from an author's adjective alone. Inspect the relevant results when possible.

## Reliability

Dense or low-resolution tables can cause row/column or digit errors.

Cross-check critical values against multiple representations when possible.

If a number, label, arrow, or relationship cannot be read reliably, omit it or explicitly mark uncertainty.

Never guess a number to complete a table.

Visual quality metrics and downstream research objectives may diverge. For example, improved reconstruction fidelity does not automatically establish improved identity recognition; treat such links as evidence questions.
