import unittest
from drug_discovery_parser import streaming_parser

class TestStreamingParser(unittest.TestCase):

    def test_create_streaming_parser(self):
        file_path = 'test.txt'
        with open(file_path, 'w') as f:
            f.write('data')
        
        parser = streaming_parser.create_streaming_parser(file_path)
        self.assertIsInstance(parser, streaming_parser.StreamingParser)

    def test_parse(self):
        file_path = 'test.txt'
        with open(file_path, 'w') as f:
            f.write('data')
        
        parser = streaming_parser.create_streaming_parser(file_path)
        data = list(parser.parse())
        self.assertEqual(len(data), 1)

if __name__ == '__main__':
    unittest.main()
