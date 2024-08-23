"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

# missing number can be the highest number in the range

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        highest_num = 0
        nums_set = set(nums) # O(1) reference time

        # update highest num
        for num in nums:
            if num > highest_num:
                highest_num = num
        
        # check nums for missing number
        for num in range(highest_num + 1): # range starts from 0
            if num not in nums_set:
                return num

        # unable to find missing number; highest num is the missing number
        return highest_num + 1