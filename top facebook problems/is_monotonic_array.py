
from typing import List

# Approach 1: Two passes
# Time is O(n)
# Space is O(n) 
def isMonotonic(A: List[int]) -> bool:
    deltas = [0]
    for i in range(len(A)-1):
        deltas.append(A[i+1]-A[i])
    return all([x>=0 for x in deltas]) or all([x<=0 for x in deltas])

# Same as above, but space is O(1)
def isMonotonic(A):
    return all(A[i] < = A[i+1] for i in range(len(A)-1)) or all(A[i]>= A[i+1] for i in range(len(A)-1)) 


# Approach 2: Simple one-pass
# Time is O(n)
# Space is O(1)
def isMonotonic(A):
    increasing = decreasing = True

    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            increasing = False
        if A[i] < A[i+1]:
            decreasing = False
    
    return increasing or decreasing


import unittest
class Test(unittest.TestCase):
    
    def test_all_equal(self):
        A = [1,1,1,1,1]
        result = isMonotonic(A)
        self.assertTrue(result)
    
    def test_all_increasing(self):
        A = [1,2,3,4,5,6]
        result = isMonotonic(A)
        self.assertTrue(result)

    def test_random_sequence(self):
        A = [1,2,2,1,4,3,7,6]
        result = isMonotonic(A)
        self.assertFalse(A)

unittest.main(verbosity=3) 