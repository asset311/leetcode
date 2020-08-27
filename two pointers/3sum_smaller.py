'''
259. 3Sum Smaller
https://leetcode.com/problems/3sum-smaller/

Pattern - two pointers
'''
from typing import List
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # can be solved as an adaption of Two Sum II - or 3Sum
        
        nums.sort()
        ans = 0
        
        for i in range(len(nums)):
            ans += self.twoSum(nums, i, target - nums[i])
        
        return ans
    
    def twoSum(self, nums, i, target):
        tot = 0
        lo, hi = i+1, len(nums)-1
        while lo < hi:
            if nums[lo] + nums[hi] < target:
                tot += hi - lo
                lo += 1
            else:
                hi -= 1
        return tot