import unittest
from drug_discovery_parser import errors

class TestErrors(unittest.TestCase):

    def test_invalid_file_format(self):
        error = errors.InvalidFileFormat("Expected CSV format, but got JSON")
        self.assertEqual(str(error), "Invalid file format: Expected CSV format, but got JSON")

    def test_invalid_data(self):
        error = errors.InvalidData("Invalid value for 'age' field")
        self.assertEqual(str(error), "Invalid data: Invalid value for 'age' field")

    def test_unexpected_token(self):
        error = errors.UnexpectedToken('END', 'BEGIN')
        self.assertEqual(str(error), "Unexpected token 'BEGIN' (expected 'END')")

    def test_missing_required_field(self):
        error = errors.MissingRequiredField("name")
        self.assertEqual(str(error), "Missing required field 'name'")

if __name__ == '__main__':
    unittest.main()
