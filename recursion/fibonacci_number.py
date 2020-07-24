'''
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
'''

# Recursion with memoization
class Solution:
    def fib(self, N: int) -> int:
        cache = {}
        
        def fib_rec(N):
            if N < 2:
                return N
            if N in cache:
                return cache[N]
            else:
                res = fib_rec(N-1) + fib_rec(N-2)
            cache[N] = res
            return res
        
        return fib_rec(N)