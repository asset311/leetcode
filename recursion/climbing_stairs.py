'''
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        
        def climbStairs_rec(n):
            
            if n <= 2:
                return n
            if n in cache:
                return cache[n]
            else:
                res = climbStairs_rec(n-1) + climbStairs_rec(n-2)
            cache[n] = res
            return res
        
        return climbStairs_rec(n)