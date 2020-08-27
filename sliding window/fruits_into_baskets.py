'''
904. Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/

Pattern - sliding window
'''

from collections import defaultdict
from typing import List

# Approach 1: using sliding window + stepwise shrinking
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # this problem is similar to finding the longest substring with at most 2 distinct characters
        # we use sliding window technique
        
        fruit_frequency = defaultdict(int)
        max_len = 0
        left = 0
        
        for right in range(len(tree)):
            right_fruit = tree[right]
            fruit_frequency[right_fruit] += 1
            
            while len(fruit_frequency) > 2:
                left_fruit = tree[left]
                fruit_frequency[left_fruit] -= 1
                
                if fruit_frequency[left_fruit] == 0:
                    del fruit_frequency[left_fruit]
                
                left += 1
            
            max_len = max(max_len, right-left+1)
        
        return max_len

# Approach 2: sliding window + jump shrinking
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # this problem is similar to finding the longest substring with at most 2 distinct characters
        # we use sliding window technique
        # store indices of to jump when shrinking the window
        
        start = 0
        max_len = 0
        lookup = {}
        
        for i in range(len(tree)):
            lookup[tree[i]] = i
            
            if len(lookup) > 2:
                start = min(lookup.values())+1
                del lookup[tree[start-1]]
            max_len = max(max_len, i-start+1)
        return max_len


