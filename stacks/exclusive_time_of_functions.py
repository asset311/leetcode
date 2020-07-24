'''
636. Exclusive Time of Functions
https://leetcode.com/problems/exclusive-time-of-functions/
'''
from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        # n = 2
        # logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
        
        ans = [0]*n
        stack = []
        prev_time = 0
        
        # remember that when we start it's the beginning of the time slot
        # when we finish, it's the end of the time slot
        
        # process logs
        for log in logs:
            fn, status, time = log.split(':')
            fn, time = int(fn), int(time)
            
            if status == 'start':
                # push onto the stack and update times
                if stack:   # there is a calling function
                    ans[stack[-1]] += time-prev_time
                
                stack.append(fn)
                prev_time = time
            
            else:
                # pop from the stack and adjust time
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        
        return ans