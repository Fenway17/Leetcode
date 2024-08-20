"""
Given a string s, return the longest palindromic substring in s
"""

# can be improved by using Dynamic Programming using a 2D boolean array
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