"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # keep count of open brackets
        open_list = []

        # check through for invalid closing of brackets
        for char in s:
            # record open brackets
            if char == "(" or char == "[" or char == "{":
                open_list.append(char)

            # for close brackets, check if possible to match to open bracket
            if len(open_list) <= 0:
                # empty list, cannot match
                return False
            if char == ")":
                if open_list.pop() != "(": # pop returns and removes element from list
                    # wrong bracket
                    return False
            if char == "]":
                if open_list.pop() != "[":
                    return False
            if char == "}":
                if open_list.pop() != "{":
                    return False
        
        # check if open list has remaining brackets
        if len(open_list) > 0:
            return False

        # unable to find invalidity
        return True