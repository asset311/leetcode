'''
77. Combinations
https://leetcode.com/problems/combinations/
'''

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def helper(first, combination):
            if len(combination) == k:
                result.append(combination[:])
            
            for i in range(first, n):
                combination.append(nums[i])
                helper(i+1, combination)
                combination.pop()
        
        nums = list(range(1,n+1))
        result = []
        helper(0,[])
        return result