'''
528. Random Pick with Weight
https://leetcode.com/problems/random-pick-with-weight/
'''

# This is simply a problem about random sampling with weight
# We can use a known Alias method by sampling from uniform distribution
# Adjusting by the total weight, and then finding the right interval where the sampling falls

# Approach 1: Explicit implementation with binary search
import bisect
import random
import itertools
from typing import List

class Solution:
    
    def __init__(self, w:List[int]):
        self.w = w
        self.cum_sums = []
        cum_sum = 0
        for weight in w:
            cum_sum += weight
            self.cum_sums.append(cum_sum)
        self.total_sum = cum_sum
    
    
    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        
        # binary search
        L, R = 0, len(self.cum_sums)
        while L < R:
            M = L + (R - L) // 2
            if target > self.cum_sums[M]:
                L = M+1
            else:
                R = M
        return L

# Pythonic implementation
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.cum_sums = list(itertools.accumulate(w))
        self.total_sum = self.cum_sums[-1]

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        return bisect.bisect_left(self.cum_sums, target)
        