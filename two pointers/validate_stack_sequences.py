'''
946. Validate Stack Sequences
https://leetcode.com/problems/validate-stack-sequences/
'''

from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # use two pointers
        stack = []
        
        # second pointer traversing 'popped' array
        pop_pointer = 0
        
        # first pointer is traversing 'pushed' array
        for num in pushed:
            # push an element at each interation
            stack.append(num)
            
            # try to pop from the stack using 'popped' array
            while stack and stack[-1] == popped[pop_pointer]:
                stack.pop()
                pop_pointer += 1
        
        # need to make sure that we exhaused the pop_pointer
        return pop_pointer == len(popped)