from typing import List

# Approach 1: precomputed cache
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = {}
        self.populateSums()
    
    def populateSums(self):
        for i in range(len(self.nums)):
            self.sums[(0,i)] = sum(self.nums[:i+1])
            
    def sumRange(self, i: int, j: int) -> int:
        if (i,j) in self.sums:
            return self.sums[(i,j)]
        else:
            return self.sums[(0,j)] - self.sums[(0,i-1)]


# Pythonic implementation using cumulative sums
import itertools
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0]+list(itertools.accumulate(self.nums))

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]