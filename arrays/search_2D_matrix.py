'''
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
'''

# Think of the 2D matrix as 1D array since every row is sorted, and it's continuously ascending
# We just need to use a mapping for row and col to check the value
# row = i // total_cols and col = i % total_cols
# Then use regular binary search

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, n*m - 1
        
        while left <= right:
            mid = (left+right) // 2
            mid_elem = matrix[mid // n][mid % n]
            
            if mid_elem == target:
                return True
            
            elif mid_elem < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False