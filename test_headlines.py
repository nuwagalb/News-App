import unittest
from headlines import SampleTest

class SampleTestTestCase(unittest.TestCase):
    def setUp(self):
        self.sample = SampleTest()

    def test_add_method_returns_value_of_adding_two_methods(self):
        self.assertEqual(self.sample.add(2, 3), 5)