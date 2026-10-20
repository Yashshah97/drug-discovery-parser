import unittest
from drug_discovery_parser import parser

class TestParser(unittest.TestCase):

    def test_parse_empty(self):
        with self.assertRaises(ValueError):
            parser.Parser().parse([])

    def test_parse_invalid_token(self):
        parser.Parser().parse(['INVALID'])

    def test_parse_header(self):
        tokens = ['START', 'HEADER', 'STRING', 'VALUE', 1.0, 'END']
        parsed_data = parser.Parser().parse(tokens)
        self.assertEqual(parsed_data['header']['string']['value'], 1.0)

    def test_parse_footer(self):
        tokens = ['START', 'FOOTER', 'STRING', 'VALUE', 2.0, 'END']
        parsed_data = parser.Parser().parse(tokens)
        self.assertEqual(parsed_data['footer']['string']['value'], 2.0)

if __name__ == '__main__':
    unittest.main()
