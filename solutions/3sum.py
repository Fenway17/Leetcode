"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets
"""

# return distinct triplets!

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums) # sort for processing

        # adopt 2 pointer solution
        i = 0
        while (i < len(nums)):
            first = sorted_nums[i]
            j = i+1 # start from after i
            k = len(nums)-1 # start from the end

            while (j < k): # pointing at 2 different numbers; k is always < length
                second = sorted_nums[j]
                third = sorted_nums[k]
                
                total = first+second+third
                if total == 0:
                    # triplet found
                    result.append([first, second, third])

                    # move j pointer to NON-DUPLICATE
                    while (j <= k and sorted_nums[j] == second):
                        j += 1 # move to next index
                else:
                    # not triplet; move pointers
                    if total < 0:
                        j += 1 # move to next index
                    else: # total > 0
                        k -= 1 # move to next index

            # move i pointer to NON-DUPLICATE
            while (i < len(nums) and sorted_nums[i] == first):
                i += 1

        return result



        