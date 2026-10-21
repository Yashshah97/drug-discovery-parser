"""Smoke tests for errors."""
import unittest

from drug_discovery_parser import errors


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(errors, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(errors) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
