'''
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/
'''

# Approach 1: Brute force with optimized space
# We do two passes
# Time complexity - O(n*m)
# Space complexity - O(n+m)
from typing import List
class Solution:
    def setZeroes(self, M: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rs = set()
        cs = set()
        
        for r in range(len(M)):
            for c in range(len(M[0])):
                if M[r][c] == 0:
                    rs.add(r)
                    cs.add(c)
        
        for r in range(len(M)):
            for c in range(len(M[0])):
                if r in rs or c in cs:
                    M[r][c] = 0

# Approach 2: reuse the matrix to mark which rows and cols to zero-out
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0