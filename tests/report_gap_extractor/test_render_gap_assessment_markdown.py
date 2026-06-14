import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from src.report_gap_extractor.render_gap_assessment_markdown import render_file


class GapAssessmentMarkdownRendererTests(unittest.TestCase):
    def test_render_gap_assessment_markdown(self):
        input_json = REPO_ROOT / "examples" / "report_gap_extraction" / "protocol_report_gap_assessment.synthetic.generated.json"
        with tempfile.TemporaryDirectory() as tmpdir:
            output_md = Path(tmpdir) / "gap_assessment.md"
            render_file(input_json=input_json, output_md=output_md)
            markdown = output_md.read_text(encoding="utf-8")

        self.assertIn("Draft Protocol / Report Gap Assessment", markdown)
        self.assertIn("Assessment Summary", markdown)
        self.assertIn("Gap Table", markdown)
        self.assertIn("PTG-002", markdown)
        self.assertIn("PTG-004", markdown)
        self.assertIn("PTG-005", markdown)
        self.assertIn("PTG-006", markdown)
        self.assertIn("Human Review Statement", markdown)
        self.assertIn("Qualified human review is required", markdown)


if __name__ == "__main__":
    unittest.main()
