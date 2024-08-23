"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        # range(start, stop, step) for index based loops
        i = 0 # start from 0
        current_substring = ""
        for index in range(i, len(s)):
            # adopt sliding window method
            if s[index] not in current_substring:
                current_substring += s[index]
            else:
                existing_index = current_substring.index(s[index])
                current_substring = current_substring[existing_index+1:] # slice substring
                current_substring += s[index] # add char

            # update max length
            if (len(current_substring) > result):
                result = len(current_substring)

        return result
        