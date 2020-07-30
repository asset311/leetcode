'''
78. Subsets
https://leetcode.com/problems/subsets/
'''
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
    
        def helper(start=0, combination=[]):
            result.append(combination[:])
        
            for i in range(start, len(nums)):
                combination.append(nums[i])  # choose
                helper(i+1, combination)     # explore
                combination.pop()            # unchoose
    
        helper()
        return result