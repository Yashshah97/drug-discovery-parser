import unittest
from drug_discovery_parser import reader

class TestReader(unittest.TestCase):
    def test_reader_init(self):
        lines = ["Line 1", "Line 2"]
        reader.Reader(lines)
        self.assertEqual(len(reader.Reader(lines).lines), 2)

    def test_parse_line(self):
        line = " Line 1 "
        result = reader.Reader([])._parse_line(line)
        self.assertEqual(result, line.strip())

    def test_validate_line(self):
        line = "Line 1"
        self.assertTrue(reader.Reader([])._validate_line(line))

    def test_read_valid_lines(self):
        lines = ["Line 1", "Line 2"]
        result = reader.Reader(lines).read()
        self.assertEqual(len(result), 2)

    def test_read_invalid_line(self):
        lines = ["Invalid Line", "Line 2"]
        with self.assertRaises(ValueError):
            reader.Reader(lines).read()

if __name__ == "__main__":
    unittest.main()
