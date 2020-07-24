'''
46. Permutations
https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.
'''
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            
            for i in range(first, n):
                # swap
                nums[first], nums[i] = nums[i], nums[first]
                
                backtrack(first + 1)
                
                # swap back
                nums[first], nums[i] = nums[i], nums[first]
                
        n = len(nums)
        output = []
        backtrack()
        
        return output