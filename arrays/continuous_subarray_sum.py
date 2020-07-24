'''
523. Continuous Subarray Sum
https://leetcode.com/problems/continuous-subarray-sum/

Given a list of non-negative numbers and a target integer k, 
write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, 
that is, sums up to n*k where n is also an integer.
'''


import itertools
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # cumulative sums
        sums = list(itertools.accumulate(nums))
        
        # consider each subarray
        for start in range(len(nums)):
            for end in range(start+1, len(nums)):
                summ = sums[end] - sums[start] + nums[start]
                if (summ == k) or (k != 0 and summ % k == 0):
                    return True
                
        return False