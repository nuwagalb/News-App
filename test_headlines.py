import unittest
from headlines import add

class HeadlinesTestCase(unittest.TestCase):
    """class for testing methods used in the headlines module"""

    def test_add_method(self):
        """test for adding two numbers"""
        self.assertEqual(add(2, 3), 5)
