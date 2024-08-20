"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""

# can possibly be further improved using Dynamic Programming. See longest_palindromic_substring.py for details

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        
        index = 0
        while (index < len(s)):
            current_str = s[index]
            next_index = index+1
            result += 1 # each individual char is a palindrome

            # check for duplicate letters
            while (next_index < len(s) and s[next_index] == s[index]):
                current_str += s[next_index]
                next_index += 1
                result += 1
            
            # check both sides for matching letters
            previous_index = index-1
            while (previous_index >= 0 and next_index < len(s)):
                if s[previous_index] == s[next_index]:
                    current_str = s[previous_index] + current_str + s[next_index]
                    previous_index -= 1
                    next_index += 1
                    result += 1
                else:
                    # no matching front and back, finish checking
                    break

            # update index
            index += 1

        return result