# Validation Protocol Generator

## Purpose

This directory contains the first code-assisted prototype for generating analytical method validation protocol drafts.

The generator uses:

- product profile JSON;
- analytical method JSON;
- validation scope;
- machine-readable validation protocol rules;
- draft-only defaults and human review statements.

## Current Prototype

```text
src/validation_protocol_generator/generate_validation_protocol.py
```

The prototype can generate:

1. a validation protocol draft JSON aligned with `schemas/validation_protocol.schema.json`;
2. a Markdown draft summary;
3. a missing information list inside the Markdown draft;
4. a human review statement.

## Example Command

```bash
python src/validation_protocol_generator/generate_validation_protocol.py \
  --product-profile examples/schema_samples/product_profile.synthetic.json \
  --method-profile examples/schema_samples/analytical_method.synthetic.json \
  --scope full_validation \
  --output-json outputs/validation_protocol.synthetic.generated.json \
  --output-md outputs/validation_protocol.synthetic.generated.md
```

## Important Limitations

- This is a first prototype.
- It does not approve protocols, methods, reports, validation conclusions, or regulatory strategies.
- It uses draft rules and synthetic examples only.
- All generated outputs require analytical lead, QA, RA, and/or method owner review before real use.
