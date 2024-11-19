# Evaluate Mathematical Expression Without Libraries

# Description:
# Write a function that takes a string `expression` containing a math problem and calculates the result. 
# The math problem may have:
# - Whole numbers (like 1, 42, etc.).
# - The `+` and `-` operators for addition and subtraction.
# - Parentheses `(` and `)` to control the order of operations.
# - Spaces (you can ignore them).

# You **cannot** use Python’s `eval()` function or any similar library.

# ---

# Examples:
# Example 1:
#     Input: 
#     expression = "4 + 5 - (9 + 1 - (5 + 5 - (4 - 3))) + 6"
#     Output: 6

# Example 2:
#     Input: 
#     expression = "(1 + (2 - (3 + 4)))"
#     Output: -4

# Example 3:
#     Input: 
#     expression = "10 - (2 + 3) + 5"
#     Output: 10

from collections import deque

# DISCLAIMER: This solution is not fully tested to work accurately and was mainly used for explaining logic
# Assumptions: integers given are single digits
def evaluate(expression: str):
    stack = deque()
    
    # go through expression
    for char in expression:
        # add to stack
        stack.append(char)
        
        # recognize the parenthesis
        if char == ')':
            # next parenthesis to evaluate, unload the stack and evaluate this sub expression
            result = 0

        while (stack.size() > 1):
            item = stack.pop() # grabs and remove item from stack
            # check if integer, if so check stack for possible negative
            if item.isinstance(int):
                # processing integers
                next_item = stack.pop()
                
                if next_item == '-':
                    item = 0 - item # convert to negative value
            
                # add to result
                result += item
                
                # check end of sub expression
                if item == '(' or None:
                    stack.append(result)
                
    return stack.pop() # final result