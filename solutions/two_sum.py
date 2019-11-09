"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
from typing import List


class Solution:

    # Slow uses less memory though
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         i_target = target - nums[i]
    #         for j in range(i + 1, len(nums)):
    #             if nums[j] == i_target:
    #                 return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {target - n: i for i, n in enumerate(nums)}
        for i, v in enumerate(nums):
            if v in differences:
                j = differences[v]
                if j != i:
                    return [i, j]
