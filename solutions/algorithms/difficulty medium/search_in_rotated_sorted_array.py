"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot 
index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:
    # binary search, O(log n) runtime
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums)-1
        middle_index = end_index // 2

        # nums contains DISTINCT values in ASCENDING order, ROTATED
        while True:
            # guard clause
            if middle_index == start_index or middle_index == end_index:
                # 2 numbers left
                if target == nums[start_index]:
                    return start_index
                elif target == nums[end_index]:
                    return end_index
                else: # target not in array
                    return -1

            if nums[start_index] > nums[end_index]:
                # rotation detected
                if nums[middle_index] > nums[start_index]:
                    # max/min cliff on right side
                    if target <= nums[middle_index] and target >= nums[start_index]:
                        # target in left half
                        end_index = middle_index
                        middle_index = (end_index + start_index) // 2
                    else: # target in right half
                        start_index = middle_index
                        middle_index = (end_index + start_index) // 2
                else: # max/min cliff on left side
                    if target >= nums[middle_index] and target <= nums[end_index]:
                        # target in right half
                        start_index = middle_index
                        middle_index = (end_index + start_index) // 2
                    else: # target in left half
                        end_index = middle_index
                        middle_index = (end_index + start_index) // 2

            else: # no rotation
                if target < nums[middle_index]:
                    # target in left half
                    end_index = middle_index
                    middle_index = (end_index + start_index) // 2
                else: # target in right half
                    start_index = middle_index
                    middle_index = (end_index + start_index) // 2