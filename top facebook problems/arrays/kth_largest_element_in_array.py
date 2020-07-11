'''
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''

import heapq
from typing import List


# Approach 0: Brute-force by sorting
# Time complexity is O(N log(N))
def findKthLargest(self, nums: List[int], k: int) -> int:
    nums.sort()
    return nums[-k]

# Approach 1: use a heap
# In case of python, we can use built-in function to return k largest element
# Then we just take the last returned

# Time complexity - O(N log(k))
# Space complexity - O(k) to store the heap elements 

def findKthLargest(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k,nums)[-1]

# Approach 2: Quickselect
# The general idea is similar to Quicksort where we randomly choose a pivot