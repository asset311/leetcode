'''
4. Median of Two Sorted Array
https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

# Approach 1: Brute-force
# merge two arrays, and then calculate the median of the merged array
# Time complexity - O(m+n)
# Space complexity - O(m+n)
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # naive implementation is to merge two arrays first
        # then calculate median of the merged array
        def merge(a, b):
            i =j = k = 0
            merged = [None]*(len(a)+len(b))
            while i<len(a) and j<len(b):
                if a[i] < b[j]:
                    merged[k] = a[i]
                    i += 1
                else:
                    merged[k] = b[j]
                    j += 1
                k += 1
            
            while i<len(a):
                merged[k] = a[i]
                i,k = i+1, k+1
            
            while j<len(b):
                merged[k] = b[j]
                j,k = j+1, k+1
            
            return merged
        
        merged = merge(nums1, nums2)
        
        n = len(merged)
        
        median = (merged[n//2]) if n % 2 != 0 else (merged[n//2]+merged[n//2 -1]) / 2 
        
        return median

# Approach 2: Use binary search
# The main intuition is to find a partition, such that
# all the elements on the left are less than or equal to
# all the elements on the right side
# Then we found middle elements of the overall array and can calculate median
# We call two partitions as X and Y

def findMedianSortedArrays(nums1: List[int], nums2: List[int]):
    # find the smaller of the two arrays
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)
    
    # X is smaller array than Y, do binary search on X
    x = len(nums1)
    y = len(nums2)

    lo = 0
    hi = x
    while lo <= hi:
        partitionX = (lo + hi) // 2
        partitionY = (x+y) // 2 - partitionX
        print(f'partitionX:{partitionX}, partitionY:{partitionY}')
        maxLeftX = -float('inf') if partitionX == 0 else nums1[partitionX - 1]  
        minRightX = float('inf') if partitionX == x else nums1[partitionX]  

        maxLeftY = -float('inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        if (maxLeftX <= minRightY and maxLeftY<= minRightX):
            print('found')
            if (x+y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + max(minRightX, minRightY)) / 2.0
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            hi = partitionX - 1
        else:
            lo = partitionX + 1
    

'''
This implementation fails, so need to look more into it

'''