'''
918. Maximum Sum Circular Subarray
https://leetcode.com/problems/maximum-sum-circular-subarray/
'''

from typing import List
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        # kadane algorithm for one interval array
        def kadane(arr):
            ans = curr = -float('inf')
            for x in arr:
                curr = x + max(curr, 0)
                ans = max(ans, curr)
            return ans
        
        # the maximum subarray in a circular array
        # either one interval kadane result or total sum - minimum sum subarray
        # the sum(A) + kadane(B) where B is an inverted sign A
        # take care of boundary condition if kadane(B) is the whole array
        # to mitigate, we do kadane twice with one element removed from start and end
        
        S = sum(A)  # total array sum
        ans1 = kadane(A)
        ans2 = S + kadane([-A[i] for i in range(1, len(A))])
        ans3 = S + kadane([-A[i] for i in range(len(A)-1)])
        return max(ans1, ans2, ans3)