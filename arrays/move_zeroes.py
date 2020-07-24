'''
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
from typing import List
# Approach 1: use additional array
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    arr = [0]*n
    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            arr[k] = nums[i]
            k += 1
    
    nums[:] = arr

# Approach 2: no new array, replace in place using the same logic
# Time is O(n) + O(n-k) where k is the number of non-zero elements, so total is O(n)
# Space is O(1)
def moveZeroes(nums: List[int]) -> None:
    n = len(nums)
    k = 0
        
    # move all the non-zero values to the front
    for i in range(n):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1
        
    # need to populate the rest with 0
    while k < len(nums):
        nums[k] = 0 
        k += 1
