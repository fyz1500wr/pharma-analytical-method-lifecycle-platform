import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from src.validation_protocol_generator.render_validation_protocol_markdown import render_file


class ValidationProtocolMarkdownRendererTests(unittest.TestCase):
    def test_render_file_creates_markdown(self):
        input_json = REPO_ROOT / "examples" / "generated" / "validation_protocol.synthetic.generated.json"
        with tempfile.TemporaryDirectory() as tmpdir:
            output_md = Path(tmpdir) / "rendered.md"
            render_file(input_json=input_json, output_md=output_md)
            markdown = output_md.read_text(encoding="utf-8")

        self.assertIn("Draft Validation Protocol", markdown)
        self.assertIn("AI-assisted draft only", markdown)
        self.assertIn("templates/validation_protocol_template.md", markdown)
        self.assertIn("Human Review Statement", markdown)
        self.assertIn("Selected Validation Characteristics", markdown)
        self.assertIn("Evidence Sources", markdown)


if __name__ == "__main__":
    unittest.main()
