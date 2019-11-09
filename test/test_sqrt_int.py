from unittest import TestCase
from solutions.sqrt_int import Solution


class TestSqrt(TestCase):
    def test_example_1(self):
        self.assertEqual(2, Solution().mySqrt(4))

    def test_example_2(self):
        self.assertEqual(2, Solution().mySqrt(8))
