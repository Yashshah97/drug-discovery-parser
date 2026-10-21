"""Smoke tests for streaming_parser."""
import unittest

from drug_discovery_parser import streaming_parser


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(streaming_parser, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(streaming_parser) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
