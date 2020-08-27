
'''
15. 3Sum
https://leetcode.com/problems/3sum/
'''

# step 1. Sort the input array - O(n log(n))
# step 2. There will be three pointers - i, lo, hi
# Pointer 'i' will point to the target value
# Pointers 'lo' and 'hi' will do similar job as Two Sum II for sorted array
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # step 1. Sort the input array
        nums.sort()

        # step 2. Start the main loop to point to 'target'
        for i in range(len(nums)):
            
            # since it is sorted, only check negative values
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, res)
        
        return res
    
    
    def twoSum(self, nums, i, res):
        
        lo, hi = i+1, len(nums) - 1
        while lo < hi:
            sum_ = nums[i] + nums[lo] + nums[hi]
            if sum_ < 0 or (lo > i+1 and nums[lo] == nums[lo-1]):
                lo += 1
            elif sum_ > 0 or (hi < len(nums) - 1 and nums[hi] == nums[hi+1]):
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1


