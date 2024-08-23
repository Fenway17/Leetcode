"""
Given a string s, return the longest palindromic substring in s
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result_str = ""
        
        index = 0
        while (index < len(s)):
            current_str = s[index]
            next_index = index+1

            # check for duplicate letters
            while (next_index < len(s) and s[next_index] == s[index]):
                current_str += s[next_index]
                next_index += 1
            
            # check both sides for matching letters
            previous_index = index-1
            while (previous_index >= 0 and next_index < len(s)):
                if s[previous_index] == s[next_index]:
                    current_str = s[previous_index] + current_str + s[next_index]
                    previous_index -= 1
                    next_index += 1
                else:
                    # no matching front and back, finish checking
                    break

            # update result string
            if len(current_str) > len(result_str):
                result_str = current_str

            # update index
            index += 1

        return result_str
    
# can be improved by using Dynamic Programming using a 2D boolean array
# where dp[i][j] will be True if the substring s[i:j+1] is a palindrome, and False otherwise; table is initialized with False values
class SolutionDP:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)): # represents expanding string of characters used
            dp[i][i] = True # marks single character as palindrome
            for j in range(i):
                # check if characters match AND
                # check for string length <=3 OR inner palindrome
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]): 
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1] # IMPORTANT slicing notation: includes j to i, excluding i+1
        return Max_Str