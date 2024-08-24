"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums will always be length >= 1
        result = nums[0]

        # approach: even vs odd number of negative numbers
        # even -> first pass from start to end will give largest
        # odd -> needs 2 passes, start to end then end to front to find largest
        i = 0
        product = 1 # start product at 1
        while i < len(nums):
            product *= nums[i]
            # update result
            if product > result:
                result = product
            
            if product == 0:
                # reset product to 1, as anything * 0 = 0
                # emulate starting from the next index
                product = 1

            i += 1

        i = len(nums)-1
        product = 1
        while i > 0:
            product *= nums[i]
            # update result
            if product > result:
                result = product
            
            if product == 0:
                # reset product to 1, as anything * 0 = 0
                # emulate starting from the next index
                product = 1

            i -= 1

        return result

class SolutionGreedy:
    # first try O(n^2) solution, TOO SLOW if array is too large
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0] # nums will always be length >= 1

        for index, num in enumerate(nums):
            i = index+1 # get the next number onwards
            product = num
            if product > result:
                result = product
            while i < len(nums):
                product *= nums[i]
                # update result
                if product > result:
                    result = product
                i += 1
        
        return result