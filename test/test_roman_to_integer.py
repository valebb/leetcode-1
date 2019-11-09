from unittest import TestCase
from solutions.roman_to_integer import Solution


class TestSolution(TestCase):
    def test_3(self):
        self.assertEqual(3, Solution().romanToInt("III"))
        print("done")

    def test_4(self):
        self.assertEqual(4, Solution().romanToInt("IV"))

    def test_9(self):
        self.assertEqual(9, Solution().romanToInt("IX"))

    def test_58(self):
        self.assertEqual(58, Solution().romanToInt("LVIII"))

    def test_1994(self):
        self.assertEqual(1994, Solution().romanToInt("MCMXCIV"))

    def test_sliding_window_generator(self):
        generator = Solution().sliding_window_generator("IVX")
        output = list(generator)
        self.assertListEqual([(1, 5), (5, 10), (10, 0)], output)
