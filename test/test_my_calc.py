import unittest

from src.my_calc import add_two


class Test(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(add_two(1, 2), 3)