'''
137. Single Number II
https://leetcode.com/problems/single-number-ii/
'''

# Approach 1: Using additional space
from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        
        for k in counter.keys():
            if counter[k] == 1:
                return k

