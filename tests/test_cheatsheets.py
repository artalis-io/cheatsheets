import tempfile
import unittest
from pathlib import Path

from scripts.cheatsheets import Sheet, ValidationError, discover, select, validate_sheet


def valid_data():
    return {
        "id": "sample",
        "title": "Sample",
        "sections": [{"title": "Commands", "blocks": [{"type": "entries", "items": [{"command": "true", "description": "Succeed"}]}]}],
    }


class ValidationTests(unittest.TestCase):
    def test_valid_minimal_sheet(self):
        self.assertEqual(validate_sheet(Sheet(Path("sample.yaml"), valid_data())), [])

    def test_missing_title_and_bad_entry(self):
        data = valid_data()
        del data["title"]
        data["sections"][0]["blocks"][0]["items"][0]["command"] = ""
        errors = validate_sheet(Sheet(Path("sample.yaml"), data))
        self.assertTrue(any("title" in e for e in errors))
        self.assertTrue(any("command and description" in e for e in errors))

    def test_rejects_unsupported_block(self):
        data = valid_data()
        data["sections"][0]["blocks"] = [{"type": "video"}]
        self.assertTrue(any("unsupported" in e for e in validate_sheet(Sheet(Path("sample.yaml"), data))))

    def test_filename_must_match_safe_id(self):
        data = valid_data()
        data["id"] = "../../unsafe"
        errors = validate_sheet(Sheet(Path("different.yaml"), data))
        self.assertTrue(any("id must match" in e for e in errors))
        self.assertTrue(any("filename must match" in e for e in errors))

    def test_verified_on_requires_date(self):
        data = valid_data()
        data["verified_on"] = {"software": "example HEAD"}
        self.assertTrue(any("verified_on.date" in e for e in validate_sheet(Sheet(Path("sample.yaml"), data))))

    def test_table_rows_match_headers(self):
        data = valid_data()
        data["sections"][0]["blocks"] = [{"type": "table", "headers": ["A", "B"], "rows": [["only one"]]}]
        self.assertTrue(any("header column count" in e for e in validate_sheet(Sheet(Path("sample.yaml"), data))))

    def test_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ("one", "two"):
                (root / f"{name}.yaml").write_text("id: duplicate\ntitle: X\nsections: []\n")
            with self.assertRaisesRegex(ValidationError, "duplicate id"):
                discover(root)

    def test_select_rejects_unknown(self):
        sheet = Sheet(Path("sample.yaml"), valid_data())
        with self.assertRaisesRegex(ValidationError, "unknown"):
            select([sheet], ["missing"])


if __name__ == "__main__":
    unittest.main()
