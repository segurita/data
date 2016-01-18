import glob
import os
import unittest

from validate import validate_data


class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.json_files = [filename for filename in glob.glob(os.path.join("data", "*json"))]

    def test_data(self):
        for filename in self.json_files:
            self.assertEqual("Valid", validate_data(filename), filename)
