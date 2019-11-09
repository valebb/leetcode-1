from unittest import TestCase

from solutions.longest_common_prefix import Solution


class TestLongestCommonPrefix(TestCase):
    def test_example_1(self):
        input = ["flower", "flow", "flight"]
        output = "fl"
        self.assertEqual(
            output,
            Solution().longestCommonPrefix(input)
        )

    def test_example_2(self):
        input = ["dog", "racecar", "car"]
        output = ""
        self.assertEqual(
            output,
            Solution().longestCommonPrefix(input)
        )
