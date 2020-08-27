'''
844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/
'''

# Approach 1: Build string
# Use stack and counter of backspacing processing the string backwards
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        # function to process a string and backspace
        def processString(s):
            stack = []
            j = len(s)-1
            backspace = 0

            while j>=0:
                if s[j] == '#':
                    backspace += 1
                elif s[j] != '#' and not backspace:
                    stack.append(s[j])
                elif s[j] != '#' and backspace:
                    backspace -= 1
                j -= 1
            return stack
        
        return processString(S) == processString(T)

# Approach 2: Build string
# Use stack and process the string forward
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def processString(S):
            stack = []
            for c in S:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        return processString(S) == processString(T)

# Approach 3: ideas from approach 1 in pythonic style without additional space
import itertools
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def nextChar(S):
            backspace = 0
            j = len(S) - 1
            while j >= 0:
                if S[j] == '#':
                    backspace += 1
                elif backspace:
                    backspace -= 1
                else:
                    yield S[j]
                j -= 1

        return all(x==y for x,y in itertools.zip_longest(nextChar(S), nextChar(T)))