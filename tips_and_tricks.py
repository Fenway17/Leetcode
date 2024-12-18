from collections import Counter, deque
from functools import cache
import random

# LISTS / RANGE / LEN
nums = [1, 2, 3]
nums2 = [4, 5, 6]
nums = list({1, 2, 3})  # convert set to list
nums.append(4)  # adds to end of list
nums.remove(4)  # removes FIRST occurrence of 4
nums.pop()  # returns last element, removing it
nums.pop(2)  # returns element at index 2, removing it
nums += nums2  # combine lists
length = len(nums)
random.choice(nums)  # random number generator from list
# range(stop), range(start, stop), range(start, stop, step)
range_nums = range(5)  # gives a list of n numbers starting from 0; aka the number 5 is not in it
range_nums = range(length)

# SORT the target list
sorted_target = sorted(nums)
paired_list = list(zip(nums, nums2))
paired_list.sort(key=lambda item: item[0])  # sort based on first list
first, second = zip(*paired_list)  # extract out the sorted lists

# TUPLES
nums_tuple = (1, 2, 3)  # unchangeable; 0-indexed

# DICTIONARY
dict = {1: "one", 2: "two", 3: "three"}
dict.get(1, None)  # gets 1, or None, if it does not exist
dict.pop(1, 0)  # returns AND removes value of key 1, else return default 0; if no default given, will throw error on missing key
for key, value in dict.items():  # obtain key and value
    pass

# COUNTER (subclass of DICTIONARY)
counter = Counter(nums)  # counts occurrences of each element; quick way to convert array to dict type object
counter[1] > 0  # Returns True if the target exists, otherwise False

# INDEX + ITEMS
for index, num in enumerate(nums):  # obtain index and item
    pass

# SET is hash based, referring to an element is O(1)
# operators: "|" union, "&" intersection, "-" difference, "^" symmetric difference (in either, not both)
nums_set = {1, 2, 3}
nums_set = set(nums)  # no duplicates allowed
nums_set.add(4)
nums_set.remove(4)  # can throw KeyError if element missing
nums_set.discard(4)  # won't throw KeyError
nums_set_two = nums_set.copy()

# QUEUE / STACKS
queue = deque()  # deque() is a queue with append and pops for left or right
queue.append(1)
item = queue.popleft()  # pop() is for the right side

# SUBSTRINGS
# string[start:end:step]: slices the string from start to end, taking every step-th character.
# does not include end index
s = "Hello"
substring = s[0:3]  # takes index 0 to 2
char = s[0]  # returns 'H'
char_index = s.index(char)  # returns index
str_list = s.split("e")  # splits string on "e" into multiple strings

# MATH MIN / MAX
min(1, 2)
max(1, 2)
num = 3 // 2  # floor divide operator; = 1
difference = abs(3 - 5)  # returns positive number 2
negative_infinity = float('-inf')
infinity = float('inf')

# STRING -> INT / FLOAT
str(1)
int("1")
float("1.0")

# 2D array of False; represents start and end index of substring that can be split properly
dp = [[False for index in range(len(s))] for index in range(len(s))]

# CACHING recursion function, use for memoizing recursion results
@cache
def recursionHelper(a, b):
    pass