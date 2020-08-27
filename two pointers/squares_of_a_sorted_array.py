'''
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

Pattern - two pointers
'''

# We can do this in O(N) time, but need additional space O(N)
from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = [0]*len(A)
        j = len(A)-1
        l, r = 0, len(A)-1
        
        while l<=r:
            left = abs(A[l])
            right = abs(A[r])
            
            if left > right:
                ans[j] = left*left
                l+= 1
            else:
                ans[j] = right*right
                r -=1
            j -=1
        
        return ans
    
# Time complexity - O(N)
# Space complexity - O(N)