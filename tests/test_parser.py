"""Smoke tests for parser."""
import unittest

from drug_discovery_parser import parser


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(parser, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(parser) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
