"""
Unit tests and integration tests for the file-format parser.
"""

import unittest
from io import StringIO

class TestDrugDiscoveryParser(unittest.TestCase):

    def test_valid_file(self):
        # Create a valid file-like object
        data = """[molecule]
name = "Molecule1"
formula = "C2H6O"

[molecule]
name = "Molecule2"
formula = "C3H8O"""

        f = StringIO(data)
        from drug_discovery_parser import parse_file  # noqa F401

        try:
            parse_file(f)
        except Exception as e:
            self.fail(f"Unexpected error: {e}")

    def test_invalid_file(self):
        # Create an invalid file-like object
        data = """[molecule]
name = "Molecule1"
formula = "C2H6O"

[molecule]"""

        f = StringIO(data)
        from drug_discovery_parser import parse_file  # noqa F401

        with self.assertRaises(ValueError):
            parse_file(f)

    def test_empty_file(self):
        # Create an empty file-like object
        data = ""

        f = StringIO(data)
        from drug_discovery_parser import parse_file  # noqa F401

        with self.assertRaises(ValueError):
            parse_file(f)

if __name__ == "__main__":
    unittest.main()
