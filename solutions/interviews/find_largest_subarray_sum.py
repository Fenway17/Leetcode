# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# [-2,1,-3,4,-1,2,1,-5,4]
# [5,4,-1,7,8]
# [-1,-1,0,-1,-1]

# 6 23 0

# DISCLAIMER: This is not an optimal solution as this is currently O(n^2).
def find_largest_subarray_sum(nums):
    max_sum = 0
    
    for index, num in enumerate(nums):
        current_sum = 0
        current_index = index
        while current_index < len(nums):
            current_sum += nums[current_index]
            
            # check if current sum is new max
            if current_sum > max_sum:
                max_sum = current_sum
            
            # increment current index
            current_index += 1
    
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums_2 = [5,4,-1,7,8]
nums_3 = [-1,-1,0,-1,-1]

result = find_largest_subarray_sum(nums)
result_2 = find_largest_subarray_sum(nums_2)
result_3 = find_largest_subarray_sum(nums_3)

print(result)
print(result_2)
print(result_3)