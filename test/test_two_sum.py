from unittest import TestCase

from solutions.two_sum import Solution


class TestTwoSum(TestCase):
    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertListEqual(
            Solution().twoSum(nums, target),
            expected
        )
