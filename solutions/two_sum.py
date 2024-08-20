from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_first, num_first in enumerate(nums):
            remainder = target - num_first
            for index_second, num_second in enumerate(nums):
                if index_second == index_first:
                    continue
                    
                if remainder == num_second:
                    result_array = [index_first, index_second]
                    return result_array