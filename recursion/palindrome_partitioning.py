'''
131. Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/
'''
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # edge case
        if not s:
            return []
    
        # initial call to backtraking, using a helper
        result = [] 
        step = []
        self.helper(s, step, result)

        return result
    
    def helper(self, s:str, step:List[str], result: List[List[str]]) -> None:
        # base case
        if len(s) == 0:
            result.append(step[:])  # need to create a new list, as this will be backtracked
            return
    
        # start a loop to choose a step
        for i in range(1,len(s)+1):
            substring = s[:i]
        
            if self.isPalindrome(substring):
                step.append(substring)   # choose
                self.helper(s[i:], step, result) # explore via recursive call
                step.pop()          # unchoose
    
    def isPalindrome(self, s:str) -> bool:
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True