from collections import deque

# LISTS / RANGE / LEN
nums = [1, 2, 3]
nums.append(4)
length = len(nums)
# range(stop), range(start, stop), range(start, stop, step)
range_nums = range(5) # gives a list of n numbers starting from 0; aka the number 5 is not in it

# DICTIONARY
dict = {1: "one", 2: "two", 3: "three"}
dict.get(1, None)
for key, value in dict.items(): # obtain key and value
    pass

# INDEX + ITEMS
for index, num in enumerate(nums): # obtain index and item
    pass

# SET is hash based, referring to an element is O(1)
# operators: "|" union, "&" intersection, "-" difference, "^" symmetric difference (in either, not both)
nums = [1, 2, 3] 
nums_set = set(nums) # no duplicates allowed; {1, 2, 3}
nums_set.add(4)
nums_set.remove(4)

# QUEUE / STACKS
queue = deque() # deque() is a queue with append and pops for left or right
queue.add(1)
item = queue.popleft() # pop() is for the right side

# TWO POINTERS / SLIDING WINDOW
# use 2 separate pointers

# SUBSTRINGS
# string[start:end:step]: slices the string from start to end, taking every step-th character.
# does not include end index
s = "Hello"
substring = s[0:3] # takes index 0 to 2

# Dynamic Programming
# 2D array of False; represents start and end index of substring that can be split properly
dp = [[False for index in range(len(s))] for index in range(len(s))]