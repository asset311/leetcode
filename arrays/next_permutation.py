'''
31. Next Permutation
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,3,2 → 2,1,3 
1,1,5 → 1,5,1
'''

# Step 1. Start from the right and find the first decreasing element
# Step 2. If found, then start from the right to find the first element that is larger than the first decreasing element (found in step 1)
# Step 3. Swap them
# Step 4. Reverse all elements to the right of the swapped position
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # find first decreasing element
        i = len(nums) - 2
        while i >=0 and nums[i+1] <= nums[i]:   #traverse from the right until first decreasing element
            i -= 1
        
        # if it exists, go back and find number just larger than nums[i]
        if i != -1:
            j = len(nums) - 1
            while nums[j] <= nums[i]: #traverse from the right to find number larger than nums[i]
                j -= 1
            nums[i], nums[j] = nums[j], nums[i] #swap them
        
        # reverse to the right of i
        nums[i+1:] = nums[:i:-1] if i!=-1 else reversed(nums)   # either reverses the whole array, or just right of i if i is not at the start