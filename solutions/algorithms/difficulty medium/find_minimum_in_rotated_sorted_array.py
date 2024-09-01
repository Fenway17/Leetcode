"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 

For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

from typing import List

class Solution:
    # binary search, O(log n) runtime
    def findMin(self, nums: List[int]) -> int:
        start_index = 0
        end_index = len(nums)-1
        middle_index = end_index // 2
        while True:
            if nums[middle_index] < nums[end_index]:
                # min is on left half
                end_index = middle_index
                middle_index = (end_index + start_index) // 2
            elif nums[middle_index] > nums[start_index]:
                # min is on right half
                start_index = middle_index
                middle_index = (end_index + start_index) // 2
            else: # middle index is now same as start or end; 2 or less numbers left
                return min(nums[start_index], nums[end_index])

class SolutionGreedy:
    # linear search, O(n) runtime
    def findMin(self, nums: List[int]) -> int:
        current_min = nums[0] # n is at least 1
        for num in nums:
            if num < current_min:
                # would be the actual min of the array
                return num

        return current_min