'''
88. Merge sorted array
https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''
from typing import List
# Approach 1: use built-in sort after merging
# Time is O((m+n)*log(m+n))
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for num in nums2:
        nums1[m] = num
        m += 1
    
    nums1.sort()

# Approach 2: use additional array and re-assign in the end
# Time is O(m+n) 
# Space is O(m+n)
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    C = [0]*(len(nums1)+len(B))
    i = j = k = 0
    while i< len(nums1) and j<len(nums2):
        if nums1[i] < nums2[j]:
            C[k] = nums1[i]
            i += 1
        else:
            C[k] = nums2[j]
            j += 1
        k += 1
    while i< len(nums1):
        C[k] = nums1[i]
        i, k = i+1, k+1
    while j < len(nums2):
        C[k] = nums2[j]
        j, k = j+1, k+1
    
    nums1[:] = C
    
# Approach 3: do not use additional space, make changes in-place
# Since we have space at the end, use that space to populate traversing both arrays from the end
# Time O(m+n)
# Space is O(1)
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    a, b, write_indx = m - 1, n - 1, m + n - 1
    while a>=0 and b>= 0:
        if nums1[a] > nums2[b]:
            a[write_indx] = nums1[a]
            a -= 1
        else:
            A[write_indx] = nums2[b]
            b -= 1
        write_indx -= 1

    while b>=0:
        A[write_indx] = nums2[b]
        write_indx, b = write_indx - 1, b - 1
     









