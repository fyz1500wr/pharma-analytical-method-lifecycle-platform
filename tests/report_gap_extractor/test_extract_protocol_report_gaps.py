import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from src.report_gap_extractor.extract_protocol_report_gaps import extract_gaps, read_json


class ProtocolReportGapExtractorTests(unittest.TestCase):
    def setUp(self):
        self.review_content_path = REPO_ROOT / "examples" / "report_gap_extraction" / "protocol_report_review_content.synthetic.json"
        self.mapping_path = REPO_ROOT / "knowledge_base" / "validation_gap_rules" / "machine_readable" / "protocol_to_report_gap_mapping.json"

    def test_extracts_expected_gaps(self):
        review_content = read_json(self.review_content_path)
        mapping_payload = read_json(self.mapping_path)
        assessment = extract_gaps(review_content, mapping_payload)

        self.assertEqual(assessment["assessment_type"], "protocol_report_gap_assessment_draft")
        self.assertEqual(assessment["gap_count"], 4)
        self.assertTrue(assessment["human_review_required"])
        self.assertIn("advisory only", assessment["human_review_statement"])

        gap_ids = {gap["gap_id"] for gap in assessment["gaps"]}
        self.assertEqual(gap_ids, {"PTG-002", "PTG-004", "PTG-005", "PTG-006"})
        self.assertNotIn("PTG-001", gap_ids)
        self.assertNotIn("PTG-009", gap_ids)

        for gap in assessment["gaps"]:
            self.assertTrue(gap["reviewer_question"])
            self.assertTrue(gap["feedback_targets"])
            self.assertTrue(gap["human_review_required"])


if __name__ == "__main__":
    unittest.main()
