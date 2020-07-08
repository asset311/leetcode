'''
189. Rotate Array
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''
from typing import List

# Approach 1: Brute-force
# Time is O(n*k). All numbers are shifted by one step O(n) k times 
# Space is O(1). No extra space is used 
def rotate(nums: List[int], k: int) -> None:
    if k == 0:
        return
    for i in range(k):
        prev = nums[-1]
        for j in range(len(nums)):
            prev, nums[j] = nums[j], prev   


# Approach 2: Using an additional array
# The idea is to calculate the right position for each element
# Time is O(n) for one pass through the array, another for copying
# Space is O(n) for the new array
def rotate(nums: List[int], k:int) -> None:
    n = len(nums)
    rotated_nums = [None]*n

    for i in range(n):
        rotated_nums[(i+k)%n] = nums[i]

    nums[:] = rotated_nums

