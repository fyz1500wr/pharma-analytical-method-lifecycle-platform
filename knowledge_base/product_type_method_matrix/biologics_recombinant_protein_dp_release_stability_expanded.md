# Biologics / Recombinant Protein Drug Product Release & Stability — Expanded Method Matrix

## 1. Purpose

This file expands the initial product-type / analytical method matrix for the Phase 1 MVP.

Scope:

```text
Biologics / recombinant proteins / drug product / release and stability
```

This matrix is intended to support method selection, method development planning, validation protocol drafting, and analytical report review.

It is **not** product-specific and must not be treated as a final analytical strategy without product-specific analytical lead, QA, RA, and method owner review.

---

## 2. Applicability

| Field | Scope |
|---|---|
| Product family | Biologics |
| Molecule type | Recombinant protein |
| Sample type | Drug product |
| Primary use cases | Release testing, stability testing |
| Lifecycle stages | Development, registration, commercial lifecycle support |
| Initial regulatory framing | ICH-aligned CMC analytical lifecycle support |

---

## 3. Decision Categories

Use the following classification when recommending analytical categories.

| Classification | Meaning |
|---|---|
| Required | Usually expected for this product/sample/use case unless scientifically justified otherwise |
| Conditional | Needed depending on product, dosage form, route, process, matrix, risk, or regulatory region |
| Optional / supportive | Useful for characterization, troubleshooting, comparability, or development support, but not always required for routine release/stability |
| Not assessable | More information is required before deciding |

---

## 4. Core Analytical Category Matrix

| Analytical Category | Release | Stability | Candidate Method Types | Classification | Why It Matters | Product / Dosage Form Dependency | Key Missing Information Prompts | Evidence Level | Human Review |
|---|---:|---:|---|---|---|---|---|---|---|
| Identity | Yes | Conditional | Peptide mapping, LC-MS, immunoassay, electrophoretic method, western blot, product-specific orthogonal identity method | Required for release; conditional for stability | Confirms the drug product contains the intended recombinant protein and supports product traceability | Depends on molecule size, sequence, formulation, excipients, and whether method distinguishes related proteins | What is the identity-defining attribute? Is DS identity already controlled? Is DP matrix interfering? Is orthogonal identity needed? | Internal rule table; official source support required later | Yes |
| Assay / protein content | Yes | Yes | RP-HPLC, UV/Vis, ELISA, LC-based quantitative assay, amino acid analysis for characterization, product-specific quantitative method | Required | Supports content, dose, strength, and stability trend evaluation | Depends on protein concentration, excipient interference, dosage form, extraction recovery, and reportable unit | What is the specification unit? Does extraction recover protein from DP matrix? Does method distinguish active protein from degraded material? | Internal rule table; official source support required later | Yes |
| Potency / biological activity | Yes | Yes | Cell-based bioassay, reporter gene assay, antiviral assay, binding assay, enzymatic assay, mechanism-relevant functional assay | Required when biological activity is a CQA | Demonstrates activity relevant to mechanism or intended biological function | Depends on mechanism of action, reference standard, matrix effect, formulation, dose strength, assay variability | What is the mechanism-relevant response? Is matrix interference assessed? Are parallelism and reference standard strategy addressed? | Internal rule table; official source support required later | Yes |
| Purity / related proteins | Yes | Yes | SEC-HPLC, CE-SDS, SDS-PAGE, RP-HPLC, icIEF, capillary electrophoresis, LC-MS characterization | Required / conditional | Detects aggregates, fragments, variants, impurities, or related proteins | Depends on degradation pathways, protein structure, formulation stress, and route | Which impurities are product-related? Are aggregate and fragment methods both needed? Are variants clinically or quality relevant? | Internal rule table; official source support required later | Yes |
| Aggregates | Yes | Yes | SEC-HPLC, MALS where applicable, DLS supportive, orthogonal particle/aggregate method | Required / conditional | Aggregation can affect safety, potency, immunogenicity risk, and stability | Depends on molecule, concentration, formulation, storage condition, and route | Is SEC sufficient? Are high-molecular-weight species specified? Is orthogonal aggregate characterization needed? | Internal rule table; official source support required later | Yes |
| Fragments / low-molecular-weight species | Conditional | Yes | CE-SDS, reduced/non-reduced electrophoresis, SDS-PAGE, RP-HPLC, LC-MS | Conditional | Fragments can indicate degradation, instability, or process/product-related impurities | Depends on protein cleavage sensitivity, formulation, and stability profile | Are fragments expected? Are they resolved from intact protein? Is quantitation required or only characterization? | Internal rule table; official source support required later | Yes |
| Charge variants / isoforms | Conditional | Conditional | icIEF, ion exchange chromatography, capillary isoelectric focusing | Conditional | Charge variants may affect activity, stability, or comparability | More relevant for complex proteins, glycoproteins, mAbs, or proteins with known deamidation/oxidation risk | Are charge variants CQAs? Are they stability-indicating? Is method for release or characterization only? | Internal rule table; official source support required later | Yes |
| Degradation profile / stability-indicating capability | Conditional | Yes | Stability-indicating LC, SEC, CE-SDS, potency assay, forced degradation-supported methods, orthogonal methods | Required for stability strategy; conditional for release | Supports shelf-life, storage, trend analysis, and degradation control | Depends on known degradation pathways and whether forced degradation is feasible/meaningful | What are expected degradation pathways? Is forced degradation performed or justified as not applicable? Does method separate degradation products from main result? | Internal rule table; official source support required later | Yes |
| Process-related impurities | Conditional | Conditional | HCP ELISA, residual DNA qPCR/ddPCR, residual host-cell protein method, residual process reagent assays | Conditional | Controls residual process impurities relevant to DS/DP quality and safety | Often controlled at DS, but DP testing may be needed depending on process, formulation, or regulatory strategy | Are process impurities controlled at DS? Are DP release tests needed? Are residual levels affected by DP process? | Internal rule table; official source support required later | Yes |
| Host cell protein | Conditional | Conditional | HCP ELISA, orthogonal HCP characterization where applicable | Conditional | Residual HCP may affect safety and quality | Usually DS-focused; DP testing depends on lifecycle strategy and process knowledge | Is HCP controlled at DS? Is DP matrix compatible? Is assay product/process specific? | Internal rule table; official source support required later | Yes |
| Residual host cell DNA | Conditional | Conditional | qPCR, ddPCR, validated residual DNA assay | Conditional | Residual DNA may be a process-related impurity concern | Usually DS-focused; DP testing depends on process and regulatory strategy | Is residual DNA controlled at DS? Is DP testing scientifically justified? Is matrix inhibition assessed? | Internal rule table; official source support required later | Yes |
| Endotoxin | Conditional | Conditional | Bacterial endotoxins test, method suitability / inhibition-enhancement assessment | Conditional / route-dependent | Supports safety for routes where endotoxin risk is relevant | Strongly route-, formulation-, process-, and compendial-context dependent | What is route of administration? Is endotoxin limit defined? Does matrix interfere with BET? | Internal rule table; official source support required later | Yes |
| Microbiological quality | Yes / conditional | Yes / conditional | Microbial limits, bioburden, sterility where applicable | Required / conditional | Supports microbial safety and dosage form quality | Depends on sterile vs non-sterile product, dosage form, route, and manufacturing control | Is product sterile or non-sterile? Which compendial microbiological requirements apply? Does matrix require method suitability? | Internal rule table; official source support required later | Yes |
| Appearance / description | Yes | Yes | Visual inspection, appearance description, color/clarity where applicable | Required / conditional | Detects visible changes, particulates, discoloration, or physical instability | Depends on dosage form: solution, lyophilized, solid dosage, suspension, device, etc. | What is normal appearance? What are unacceptable changes? Are photos or standards needed? | Internal rule table | Yes |
| pH | Conditional | Yes / conditional | pH meter or suitable method | Conditional | pH can affect protein stability, potency, and formulation performance | Relevant for liquid, reconstituted, or extracted samples; less direct for dry solid dosage unless extraction used | Is pH a DP CQA? What sample preparation is used? Does pH change during storage? | Internal rule table | Yes |
| Osmolality | Conditional | Conditional | Osmometer | Conditional | Relevant for injectable or certain liquid dosage forms | Route- and dosage-form dependent | Is osmolality relevant to route or safety? Is method needed for release or characterization? | Internal rule table | Yes |
| Water content / moisture | Conditional | Yes / conditional | Karl Fischer, loss on drying, moisture analyzer | Conditional | Moisture may affect stability, degradation, or solid dosage performance | Relevant for lyophilized or solid dosage forms | Is moisture a stability driver? What limit is justified? Is method stability-indicating? | Internal rule table | Yes |
| Dissolution / disintegration | Conditional | Conditional | Dissolution, disintegration, product-specific release test | Conditional | Supports dosage form performance for solid oral or other dosage forms | Highly dosage-form dependent | Is dissolution/disintegration relevant to release? Does it affect protein exposure or local delivery? | Internal rule table; official source support required later | Yes |
| Dosage unit uniformity / content uniformity | Conditional | Conditional | Content uniformity assay, dose uniformity method | Conditional | Supports consistent unit dose delivery | Relevant for tablets, capsules, lozenges, films, unit-dose forms | Is DP unit-dose? What is assay extraction recovery? Is potency or content used for uniformity? | Internal rule table; official source support required later | Yes |
| Particulate matter | Conditional | Conditional | Visible / subvisible particulate methods where applicable | Conditional | Particles may affect safety and quality | Route- and dosage-form dependent, especially injectables | Is product injectable or parenteral? Are particles expected? Are proteinaceous particles differentiated? | Internal rule table; official source support required later | Yes |
| Container closure / extractables-leachables support | Conditional | Conditional | E/L studies, leachable monitoring, compatibility studies | Conditional | Supports container closure compatibility and long-term quality | Depends on container, route, storage, formulation, and lifecycle stage | Is container closure new? Are leachables a DP stability risk? Are compatibility studies available? | Internal rule table; official source support required later | Yes |

---

## 5. Method Selection Logic

### 5.1 Release Testing Logic

For recombinant protein drug product release, the platform should normally evaluate whether the analytical strategy covers:

1. identity;
2. content / assay;
3. potency or biological activity, if biological activity is a CQA;
4. purity / impurities / related proteins;
5. aggregate or fragment control where relevant;
6. microbiological quality;
7. dosage-form-specific performance tests;
8. process-related impurities where not fully controlled upstream or where DP-specific risk exists.

### 5.2 Stability Testing Logic

For recombinant protein drug product stability, the platform should evaluate whether the analytical strategy can monitor:

1. potency loss;
2. content change or recovery loss;
3. aggregation;
4. fragmentation;
5. degradation products;
6. charge or structural changes where relevant;
7. appearance or physical instability;
8. dosage-form-specific degradation or performance loss;
9. microbiological or moisture-related changes where applicable.

### 5.3 Conditional Test Logic

A conditional test should become higher priority if one or more of the following applies:

- the attribute is a known or likely CQA;
- prior development data show instability or variability;
- formulation or dosage form introduces matrix risk;
- route of administration increases safety relevance;
- external lab or prior report identifies a recurring gap;
- regulatory feedback or filing strategy requires the attribute;
- method is needed to support comparability or lifecycle change.

---

## 6. Missing Information Prompts

Before finalizing a method recommendation, collect or confirm:

### Product and Formulation

- What is the recombinant protein and its known degradation pathway?
- What is the dosage form?
- What is the route of administration?
- What is the target strength or dose unit?
- What excipients may interfere with analytical methods?
- Is the drug product sterile or non-sterile?

### Analytical Purpose

- Is the method for release, stability, characterization, comparability, or method transfer?
- Is the reportable result intended for specification, trend monitoring, or supportive characterization?
- Are acceptance criteria already defined?
- Are DS and DP control strategies separate or linked?

### Standards and Controls

- What reference standard is used?
- Is a working standard qualified?
- Is reference standard commutability or matrix compatibility relevant?
- Are positive, negative, matrix, and system controls defined?

### Method Development

- What is the sample preparation or extraction procedure?
- Is recovery from DP matrix demonstrated?
- Is matrix interference evaluated?
- Are forced degradation or stress studies available?
- Are orthogonal methods needed?

### Validation / Transfer

- What validation scope is needed?
- Does the range cover the specification and sample concentration?
- Are system suitability criteria meaningful?
- Is precision appropriate for the intended use?
- Is robustness known or still exploratory?
- Is transfer to another lab expected?

---

## 7. Review Flags for PM / Reviewer

Flag for SME review if:

1. potency method is cell-based, reporter gene-based, antiviral, or otherwise high-variability;
2. method claims to be stability-indicating without stress / degradation support;
3. matrix effect is likely but not evaluated;
4. reference standard strategy is unclear;
5. assay range does not clearly cover specification or sample concentration;
6. system suitability criteria are generic and do not monitor critical performance;
7. the method is new, emerging, or not internally mapped;
8. the external lab report lacks raw data, curve fit, chromatogram/electropherogram, or failed-run rationale;
9. method is intended for release but evidence appears characterization-only;
10. DP-specific testing is omitted with no DS/DP control strategy rationale.

---

## 8. Recommended Output Format for Method Selection Workflow

The method selection workflow should output a table with at least the following fields:

| Field | Description |
|---|---|
| analytical_category | Identity, potency, purity, etc. |
| recommendation | Required / Conditional / Optional / Not assessable |
| candidate_methods | Candidate analytical technologies |
| intended_use | Release, stability, characterization, transfer, etc. |
| rationale | Why this category is relevant |
| dependency_notes | Product, dosage form, route, or matrix dependencies |
| missing_information | Information required before final decision |
| risk_flags | Technical or regulatory risks |
| evidence_level | Official source / internal rule / literature / vendor / AI-inferred |
| confidence | High / Medium / Low |
| human_review_required | Yes / No |

---

## 9. Evidence Label

Current status:

```text
Evidence Level: Internal rule table / AI-assisted initial matrix
Confidence: Medium
Human Review Required: Yes
```

This matrix should later be linked to curated evidence packs for ICH, FDA, EMA, TFDA, and other applicable official sources.

---

## 10. Human Review Statement

本文件由 AI 輔助產生，於 GxP、供應商溝通或法規用途使用前，必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。

---

## 11. Direction Control

This file supports Phase 1 MVP and must remain extensible. It must not become:

- a single-product-specific strategy;
- a final release specification;
- an automatic regulatory decision;
- a substitute for analytical SME, QA, RA, or method owner review.
