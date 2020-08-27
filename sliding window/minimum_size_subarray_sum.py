'''
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''

# Approach 1: Brute force
# Time complexity is O(n^2)
# Space complexity is O(1)

# checks sums for each subarray starting from the left element
from typing import List
def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    ans = float('inf')  #needs to be a huge number to make sure min comparison works
    
    for i in range(len(nums)):
        sum_ = 0
        j = i
    
        while j < len(nums):
            sum_ += nums[j]
            if sum_ >= s:
                ans = min(ans, j-i+1)
                break
            j += 1
    
    return 0 if ans == float('inf') else ans


# Approach 2: Sliding window with two pointers
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        # use two-pointers
        min_size = float('inf')
        tot = 0
        begin =  0
        
        for end in range(len(nums)):
            tot += nums[end]
            
            while tot >= s:
                min_size = min(min_size, end+1-begin)
                tot -= nums[begin]
                
                begin += 1
        
        return 0 if min_size == float('inf') else min_size