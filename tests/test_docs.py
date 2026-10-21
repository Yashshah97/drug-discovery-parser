import unittest
from drug_discovery_parser import docs

class TestDocsModule(unittest.TestCase):

    def test_get_description(self):
        self.assertEqual(docs.get_description(), "Drug Discovery File-Format Parser")

    def test_get_long_description(self):
        expected = """\
A file-format parser for molecular screening and cheminformatics:
a streaming parser with a validating reader and friendly error messages,
built in pure Python with tests and documentation.
"""
        self.assertEqual(docs.get_long_description(), expected)

    def test_get_metadata(self):
        metadata = docs.get_metadata()
        self.assertIn('name', metadata)
        self.assertIn('version', metadata)
        self.assertIn('author', metadata)
        self.assertIn('description', metadata)
        self.assertIn('long_description', metadata)

if __name__ == '__main__':
    unittest.main()
