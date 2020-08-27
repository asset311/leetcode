'''
384. Shuffle an Array
https://leetcode.com/problems/shuffle-an-array/
'''

import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = nums[:]  # make a deep copy
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        self.original = self.original[:]
        return self.array
        

    # Fisher-Yates Algorithm for generating random permutations
    # Simply traverse the array and pick a random index in the remaining range of indices
    # then swap - may pick itself, but doesn't affect the result too much 
    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        
        return self.array