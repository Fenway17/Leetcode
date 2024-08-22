from typing import List

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result_length = 0
        num_set = set(nums) # set is hash based, referring to an element is O(1)
        for num in num_set:
            current_num = num
            current_length = 1

            if (current_num - 1 in num_set):
                # previous number in chain exists, skip
                continue

            while (current_num + 1 in num_set):
                current_length += 1
                current_num += 1
            
            if (current_length > result_length):
                result_length = current_length
        
        return result_length