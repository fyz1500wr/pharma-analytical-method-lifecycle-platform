# Validation Characteristic Selection Matrix

## 1. Purpose

This file defines first-pass rules for selecting validation characteristics based on analytical purpose and method type.

The matrix is intended for draft generation only and requires human review before GxP, vendor-facing, or regulatory use.

---

## 2. Validation Characteristic Categories

| Characteristic | Typical Purpose |
|---|---|
| Specificity / selectivity | Demonstrate that the method measures the intended analyte or attribute without unacceptable interference |
| Accuracy | Demonstrate closeness of measured value to expected or reference value |
| Precision | Demonstrate variability under defined conditions |
| Repeatability | Precision under same analyst, instrument, lab, and short time frame |
| Intermediate precision | Precision across days, analysts, instruments, columns, reagent lots, or other internal variables |
| Linearity / calibration model | Demonstrate response relationship across range where applicable |
| Range / reportable range | Define interval where method performance is acceptable |
| LOD / LOQ | Define detection or quantitation limits where low-level detection is intended |
| Robustness | Demonstrate method tolerance to small deliberate variations |
| System suitability | Confirm method system performance before or during sample analysis |
| Sample / reagent stability | Demonstrate prepared sample or reagent stability under intended use conditions |
| Parallelism | Demonstrate comparable dilution-response behavior, often important for bioassay, immunoassay, and relative potency methods |
| Matrix effect | Demonstrate that product matrix or sample matrix does not bias method response |

---

## 3. Selection by Analytical Purpose

| Analytical Purpose | Usually Include | Conditional / Consider | Common Exclusions / Notes |
|---|---|---|---|
| Identity | Specificity / selectivity | Precision, robustness, sample stability | Accuracy and linearity may not apply for qualitative identity unless quantitative output is used |
| Assay / content | Specificity, accuracy, precision, repeatability, intermediate precision, range, linearity or calibration model, system suitability | Robustness, sample stability, reagent stability, matrix effect | LOD/LOQ only if low-level detection/quantitation is part of intended use |
| Potency | Specificity/selectivity or method specificity, precision, repeatability, intermediate precision, range, system suitability | Accuracy, relative accuracy, parallelism, matrix effect, robustness, sample/reagent stability | Linearity may be replaced by curve model suitability for non-linear bioassays |
| Purity / related substances | Specificity, precision, range, system suitability | Accuracy, linearity, LOQ, robustness, sample stability | LOD/LOQ often relevant for impurity methods, but depends on reporting requirement |
| Impurity / residual impurity | Specificity, accuracy, precision, range, LOQ, system suitability | LOD, linearity/calibration model, robustness, matrix effect | Acceptance criteria should reflect intended reporting level |
| Degradation / stability-indicating | Specificity, precision, range, system suitability | Accuracy, robustness, forced degradation rationale, sample stability | Stability-indicating claim requires evidence that degradation does not confound result |
| Microbiological quality | Method suitability, specificity where applicable, precision where meaningful | Robustness, sample hold time, inhibition/enhancement, recovery | Q2-style characteristics may not map directly; use method-specific suitability logic |
| Endotoxin | Method suitability, inhibition/enhancement, range, system suitability where applicable | Robustness, sample dilution strategy | Product matrix interference is often central |
| Characterization only | Method suitability and rationale | Precision, specificity, robustness as needed | Full validation may not be required unless used for release/stability decision |
| Method transfer | Comparative performance, precision, system suitability | Intermediate precision, ruggedness, equivalence criteria | Full validation may not be required if prior validation is acceptable |

---

## 4. Selection by Method Type

| Method Type | Usually Include | Key Conditional Items | Reviewer Notes |
|---|---|---|---|
| HPLC / UPLC assay | Specificity, accuracy, precision, linearity, range, system suitability | Robustness, sample stability, LOQ | Confirm sample prep recovery and matrix interference if DP matrix is complex |
| SEC-HPLC | Specificity/resolution, precision, range, system suitability | Accuracy, LOQ, robustness | Aggregates and fragments may need orthogonal support |
| CE-SDS / electrophoresis | Specificity/resolution, precision, range, system suitability | Accuracy, robustness, sample stability | Reduced/non-reduced conditions should be justified if relevant |
| LC-MS / peptide mapping | Specificity, system suitability, precision where quantitative | Accuracy, linearity, range, robustness | Often characterization or identity; validation depends on intended use |
| ELISA | Specificity/selectivity, precision, range, calibration model, system suitability | Accuracy, matrix effect, hook effect, parallelism, reagent stability | Matrix and reagent lot effects are important review points |
| Cell-based bioassay | Specificity or biological specificity, precision, range, curve model suitability, system suitability | Relative accuracy, parallelism, matrix effect, robustness, cell passage, sample/reagent stability | High variability requires careful run design and reference standard strategy |
| Reporter gene assay | Specificity, precision, range, curve model suitability, system suitability | Parallelism, matrix effect, robustness, cell bank/passage controls | Mechanistic relevance should be justified |
| Binding assay / SPR / BLI | Specificity, precision, range, system suitability | Accuracy, matrix effect, regeneration robustness, reference ligand control | Whether binding represents potency must be justified |
| qPCR / ddPCR | Specificity, accuracy, precision, range, LOQ, system suitability | Inhibition control, extraction recovery, robustness | Matrix inhibition and extraction control are central |
| Microbial limits / sterility-related suitability | Method suitability, recovery, inhibition, controls | Hold time, sample prep robustness | Use microbiology-specific suitability rather than forcing Q2 terms |
| Endotoxin | Inhibition/enhancement, range, controls | Dilution strategy, product interference | Route and limit justification are critical |

---

## 5. Inclusion Rationale Requirement

For every included validation characteristic, the draft protocol should state:

1. why the characteristic is needed;
2. what experiment will evaluate it;
3. what acceptance criteria or decision criteria will be used;
4. what evidence supports the criteria;
5. whether criteria are final, proposed, or data-dependent;
6. whether human review is required.

---

## 6. Exclusion Rationale Requirement

For any commonly expected characteristic that is excluded, the draft protocol should state:

1. why it is not applicable;
2. whether the method is qualitative, quantitative, limit, characterization-only, or supportive;
3. whether another characteristic or control addresses the risk;
4. whether SME / QA / RA review is required.

---

## 7. Human Review Statement

All selections generated from this matrix require human review before use.
