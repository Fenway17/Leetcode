# Given an integer array nums and an integer k, return the kth largest element in the array.

import heapq
import random

def solution(nums, k):
    # nums is unsorted, and might have duplicates

    # remove duplicates
    num_set = set(nums)
    nums_distinct = list(num_set)

    # sort array nums - desc order
    sorted_array = sorted(nums_distinct, reverse=True)

    # return kth index
    return sorted_array[k-1]

def solution_heap(nums, k):
    # remove duplicates
    num_set = set(nums)
    nums_distinct = list(num_set)

    # loop through distinct nums and add to heap
    heapq.heapify(nums_distinct)  # O(n)
    while len(nums_distinct) > k:  # O(k log n)
        heapq.heappop(nums_distinct)
    
    return nums_distinct[0]

# O(n) best case, O(n^2) worst case
# best case: search cuts in half each repeat, resulting in total 2n runtime
# worst case: pivot chosen is the largest/smallest value each time
def quick_select(nums, k):
    # remove duplicates
    num_set = set(nums)
    nums = list(num_set)
    
    # Target index if the array were sorted
    # e.g., for 1st largest in list of 5, we want index 4
    target = len(nums) - k
    
    # sorts array in-place, returning the pivot index, where left side numbers are smaller than pivot number
    # and right side numbers are larger than pivot number
    def partition(left, right): 
        # Randomize pivot to avoid O(n^2) worst case
        pivot_idx = random.randint(left, right)
        # swap chosen pivot index to the far right
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        
        pivot_num = nums[right]
        fill_ptr = left
        
        for i in range(left, right):
            if nums[i] <= pivot_num:
                # idea: numbers smaller than pivot will be on the left of fill_ptr
                nums[i], nums[fill_ptr] = nums[fill_ptr], nums[i]
                fill_ptr += 1
        
        # swap pivot to the "middle" of the array
        nums[fill_ptr], nums[right] = nums[right], nums[fill_ptr]
        # returned index will be the nth value in ascending order
        return fill_ptr

    def select(left, right): # left and right are array indices
        if left == right:
            return nums[left]
        
        pivot_pos = partition(left, right)
        
        if pivot_pos == target:
            return nums[pivot_pos]
        elif pivot_pos > target:
            return select(left, pivot_pos - 1)
        else:
            return select(pivot_pos + 1, right)

    return select(0, len(nums) - 1)

# Example: 2nd largest in [3,2,3,1,2,4,5,5,6] is 5
print(quick_select([3,2,3,1,2,4,5,5,6], 2))

nums = [1, 3, 7, 0]
print(solution(nums, 2))
print(solution_heap(nums, 2))
print(solution_heap(nums, 1))
# 7, 3, 1 ,0

nums = [1, 3, 7, 7, 7, 0]
print(solution(nums, 2))
print(solution_heap(nums, 2))
# 7, 3, 1 ,0