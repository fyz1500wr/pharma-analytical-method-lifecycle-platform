# Product-Type / Analytical Method Matrix

## Purpose

This directory stores structured knowledge mapping pharmaceutical product types to analytical test categories and method types.

## Initial MVP Scope

Initial priority:

```text
biologics / recombinant proteins / drug product release and stability
```

## Future Expansion

The matrix must remain extensible to:

- small molecules
- peptides
- monoclonal antibodies
- ADCs
- oligonucleotides
- vaccines
- cell and gene therapies
- complex formulations

## Expected Fields

Future matrix entries should include:

- product type
- molecule type
- dosage form
- sample type
- analytical purpose
- suggested test category
- suggested method type
- required / conditional / optional classification
- rationale
- applicable regulatory sources
- evidence level
- human review flag

## Important Rule

Do not hard-code one product's analytical strategy into the general matrix. Product-specific logic should be documented separately and referenced only when applicable.
