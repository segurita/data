import unittest

from validate import validate_data


class TestSecurity(unittest.TestCase):
    def test_continc1(self):
        self.assertEqual("Valid", validate_data("continc1.json"))
