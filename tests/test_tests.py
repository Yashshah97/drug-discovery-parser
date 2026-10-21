"""Smoke tests for tests."""
import unittest

from drug_discovery_parser import tests


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(tests, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(tests) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
