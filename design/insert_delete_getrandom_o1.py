'''
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/
'''

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomset = []
        self.indices = {}

    # O(1) amortized, it is O(n) worst case when list needs to double in size
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # check if value exists in the index hashtable
        if val in self.indices:
            return False
        
        # otherwise add to the list and record it's index
        self.indices[val] = len(self.randomset)
        self.randomset.append(val)
        return True

    
    # O(1), since we're removing the last element
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # check if value exists in the index
        if val not in self.indices:
            return False
        
        # overwrite the value to delete with last element value, update index
        # equivalent to swapping
        last_element, idx = self.randomset[-1], self.indices[val]
        self.randomset[idx], self.indices[last_element] = last_element, idx
        
        
        # delete last element
        self.randomset.pop()
        del self.indices[val]
        
        return True
        
    # always O(1) assuming choice is constant operation
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.randomset)