''' 
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

'''
# optimal solution that runs in O(n)
# n = (-2,1,-3,4,-1,2,1,-5,4)
# Kadane's algorithm is able to find the maximum sum of a contiguous subarray in an array with a runtime of O(n)
from typing import List
def maxSubArray(self, nums: List[int]) -> int:
    maxEndingHere = maxSoFar = nums[0]
    for num in nums[1:]:
        maxEndingHere = max(maxEndingHere+num, num)
        maxSoFar = max(maxSoFar, maxEndingHere)

    return maxSoFar
