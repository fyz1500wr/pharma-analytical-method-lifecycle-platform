import json
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from src.validation_protocol_generator.generate_validation_protocol import generate


class ValidationProtocolGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.repo_root = REPO_ROOT
        self.rule_dir = self.repo_root / "knowledge_base" / "validation_protocol_rules" / "machine_readable"
        self.schema_path = self.repo_root / "schemas" / "validation_protocol.schema.json"
        self.product_profile = self.repo_root / "examples" / "schema_samples" / "product_profile.synthetic.json"
        self.method_profile = self.repo_root / "examples" / "schema_samples" / "analytical_method.synthetic.json"

    def read_json(self, path):
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def test_machine_readable_rule_files_exist_and_have_required_sections(self):
        characteristic_rules = self.read_json(self.rule_dir / "validation_characteristic_selection_rules.json")
        scope_rules = self.read_json(self.rule_dir / "validation_scope_rules.json")
        defaults = self.read_json(self.rule_dir / "protocol_generation_defaults.json")

        self.assertIn("method_type_rules", characteristic_rules)
        self.assertIn("purpose_modifiers", characteristic_rules)
        self.assertIn("bioassay", characteristic_rules["method_type_rules"])
        self.assertIn("scopes", scope_rules)
        self.assertIn("full_validation", scope_rules["scopes"])
        self.assertIn("human_review_statement", defaults)
        self.assertTrue(defaults["human_review_statement"].strip())

    def test_generator_output_validates_against_schema(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output_json = Path(tmpdir) / "protocol.generated.json"
            output_md = Path(tmpdir) / "protocol.generated.md"

            generate(
                product_profile_path=self.product_profile,
                method_profile_path=self.method_profile,
                scope="full_validation",
                output_json_path=output_json,
                output_md_path=output_md,
            )

            self.assertTrue(output_json.exists())
            self.assertTrue(output_md.exists())

            generated = self.read_json(output_json)
            schema = self.read_json(self.schema_path)
            validator = Draft202012Validator(schema)
            errors = sorted(validator.iter_errors(generated), key=lambda error: error.path)
            self.assertEqual(errors, [])

            self.assertEqual(generated["validation_scope"], "full_validation")
            self.assertTrue(generated["human_review_required"])
            self.assertTrue(generated["human_review_statement"].strip())
            self.assertIn("parallelism", generated["validation_characteristics"])
            self.assertIn("matrix_effect", generated["validation_characteristics"])
            self.assertGreater(len(generated["evidence_sources"]), 0)

            markdown = output_md.read_text(encoding="utf-8")
            self.assertIn("AI-assisted draft only", markdown)
            self.assertIn("Human Review Statement", markdown)
            self.assertIn("Missing Information", markdown)

    def test_unrecognized_scope_is_controlled_to_other(self):
        from src.validation_protocol_generator.generate_validation_protocol import (
            build_protocol_json,
            read_json,
        )

        product = read_json(self.product_profile)
        method = read_json(self.method_profile)
        characteristic_rules = read_json(self.rule_dir / "validation_characteristic_selection_rules.json")
        scope_rules = read_json(self.rule_dir / "validation_scope_rules.json")
        defaults = read_json(self.rule_dir / "protocol_generation_defaults.json")

        protocol = build_protocol_json(
            product_profile=product,
            method_profile=method,
            scope="invalid_scope_value",
            characteristic_rules=characteristic_rules,
            scope_rules=scope_rules,
            defaults=defaults,
        )

        self.assertEqual(protocol["validation_scope"], "other")
        self.assertTrue(protocol["human_review_required"])


if __name__ == "__main__":
    unittest.main()
