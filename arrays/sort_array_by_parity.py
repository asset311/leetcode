'''
905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/
'''

from typing import List
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        # We'll maintain two pointers i and j. 
        # The loop invariant is everything below i has parity 0 (ie. A[k] % 2 == 0 when k < i), and everything above j has parity 1.
        # 4 cases for (A[i] % 2, A[j] % 2)
        # (0,1) everything is correct, i++ and j--
        # (0,0) only i place is correct, i++
        # (1,1) only j place is correct, j--
        # (1,0) swap them, then continue
        
        i, j = 0, len(A) - 1
        
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]
            
            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -=1
        
        return A