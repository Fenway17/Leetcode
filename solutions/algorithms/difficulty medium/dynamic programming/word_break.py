"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Dynamic Programming
        # 2D array of False; represents start and end index of substring that can be split properly
        dp = [[False for index in range(len(s))] for index in range(len(s))] # range starts from 0

        # incrementally expand string used
        for i in range(len(s)): # represents end index of string
            for j in range(i+1): # i+1 to account for single char substring
                substring = s[j:i+1] # slice operator excludes end index
                if substring in wordDict:
                    dp[j][i] = True # mark substring existing in word dict
                    if dp[0][j-1]: # if previous chars can be split
                        dp[0][i] = True

        if dp[0][len(s)-1]:
            return True
        else:
            return False