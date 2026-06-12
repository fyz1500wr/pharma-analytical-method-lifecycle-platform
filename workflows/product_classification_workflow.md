# Product Classification Workflow

## Purpose

Classify the pharmaceutical product and analytical intent before recommending analytical methods.

## Inputs

- Product name
- Product type
- Molecule type
- Dosage form
- Route of administration
- Sample type
- Development stage
- Analytical purpose
- Target regulatory regions
- Known CQAs
- Known constraints

## Steps

1. Confirm sample context: raw material, IPC, DS, DP, placebo, stability sample, reference standard, or other.
2. Identify product type and molecule type.
3. Identify intended analytical purpose.
4. Identify regulatory regions and lifecycle stage.
5. Capture CQAs and known risks.
6. List missing information.
7. Route to product-type / analytical method matrix.

## Outputs

- Product profile JSON
- Analytical intent summary
- Missing information list
- Initial risk flags
- Recommended next workflow

## Human Review

Classification results must be reviewed when used for CMC, QA, RA, vendor-facing, or regulatory work.
