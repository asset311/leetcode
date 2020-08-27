'''
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/
'''

# Naive implementation
# Time complexity - O(N*M)
# Space complexity - O(N+M) for final array
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
        return list(set(res))


# Time complexity - O(N+M) where N and M are lengths of two arrays
# Space complexity - O(N+M)
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        return list(n1 & n2)


