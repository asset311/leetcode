'''
119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/
'''

# Recursive with memory
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = []
        memory = {}

        def pascal(row, col):
            if row == 0 or col == 0 or col == row:
                return 1
        
            if not (row-1, col-1) in memory:
                memory[(row-1, col-1)] = pascal(row-1, col-1)
        
            if not (row-1, col) in memory:
                memory[(row-1, col)] = pascal(row-1, col)
        
            return memory[(row-1, col-1)] + memory[(row-1, col)]

        if rowIndex > 0:
            for col in range(0,rowIndex+1):
                output.append(pascal(rowIndex, col))
    
        return output if rowIndex>0 else [1]