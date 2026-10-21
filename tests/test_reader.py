"""Smoke tests for reader."""
import unittest

from drug_discovery_parser import reader


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(reader, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(reader) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
