'''
311. Sparse Matrix Multiplication
https://leetcode.com/problems/sparse-matrix-multiplication/

Given two sparse matrices A and B, return the result of AB.
You may assume that A's column number is equal to B's row number.
'''
from typing import List
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n, l = len(A), len(A[0]), len(B[0])
        
        # check matrices can be multiplied
        if len(B) != n:
            raise ValueError("A's column number must be equal to B's row number")
        
        # allocate final matrix
        C = [[0 for _ in range(l)] for _ in range(m)]  # 0 for num of cols for num of rows
        
        for i, row in enumerate(A):
            for k, elemA in enumerate(row):
                if elemA:
                    for j, elemB in enumerate(B[k]):
                        if elemB:
                            C[i][j] += elemA*elemB
        
        return C
        
        
# the key is identify non-zero elements and only sum those