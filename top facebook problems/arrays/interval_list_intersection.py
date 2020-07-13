'''
986. Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
'''

from typing import List
# Approach 1: Brute-force
# Traverse list A and find all intersections in B
# Time complexity is O(A*B) where A and B are the number of intervals in each - this is in worst case
# In there aren't many intersections, the run time is actually faster
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        output = []
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i][1] < B[j][0]:
                    break
                if B[j][0] <= A[i][1] <= B[j][1] or A[i][0] <= B[j][1] <= A[i][1]:
                    output.append([max(A[i][0], B[j][0]), min(A[i][1],B[j][1])])
        return output


# Approach 2: Merge intervals
# Remember that intervals are disjoint, so it's easy to check when to move pointers
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        
        while i<len(A) and j<len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            
            if lo <= hi:
                ans.append([lo, hi])
            
            if A[i][1] < B[j][1]:
                i +=1
            else:
                j += 1
        
        return ans