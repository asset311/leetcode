'''
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

# correct version
# may need an additional check if input can have alphanumeric characters, need to filter them out
# if c.isalnum(): continue    
def isValid(s:str) -> bool:
    left_chars = []
    lookup = {'(':')', '{':'}', '[':']'}

    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()] != c:
            return False

    return not left_chars 

    # Time complexity is O(n) since for each character we perform O(1) operations