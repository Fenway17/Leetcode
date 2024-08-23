"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result_area = 0
        left_pointer = 0
        right_pointer = len(height) - 1 # two pointer method; allows length to start at max
        length = right_pointer - left_pointer
        
        while (length > 0):
            # update height / area
            final_height = min(height[left_pointer], height[right_pointer])
            current_area = length * final_height

            # update result area
            if current_area > result_area:
                result_area = current_area

            # update pointers
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

            # update length
            length = right_pointer - left_pointer

        return result_area
        