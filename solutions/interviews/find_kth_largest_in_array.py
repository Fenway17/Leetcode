# Given an integer array nums and an integer k, return the kth largest element in the array.

import heapq

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


nums = [1, 3, 7, 0]
print(solution(nums, 2))
print(solution_heap(nums, 2))
print(solution_heap(nums, 1))
# 7, 3, 1 ,0

nums = [1, 3, 7, 7, 7, 0]
print(solution(nums, 2))
print(solution_heap(nums, 2))
# 7, 3, 1 ,0