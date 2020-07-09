'''
50. Pow(x, n)
https://leetcode.com/problems/powx-n/
Implement pow(x, n), which calculates x raised to the power n (x^n).

'''


# Approach 1: Brute-force, multiply by itself n times
# Time is O(n), we multiply x for n times
# Space is O(1), we only need one variable to store the result
def myPow(x, n):
    if n == 0:
        return 1.0
    if n < 0:
        x = 1 / x
        n = -n
    
    ans = 1
    for i in range(n):
        ans = ans * x
    return ans

# Approach 2: Fast Power Algorithm Recursive
# Time is O(log(n)) because each time we reduce computation by half
# Space is O(log(n)) - at each point we need to store 'half' and we do it O(log(n)) times
def myPow(x: float, n: int) -> float:
    if n < 0:
        x = 1/x
        n = -n
    return fastPow(x,n)

def fastPow(x, n):
    if n==0:
        return 1.0
    
    half = fastPow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half*half*x

# Approach 3: Fast Power Algorithm Iterative
# Look up fast power algorithm

