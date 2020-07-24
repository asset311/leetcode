'''
278. First Bad Version
https://leetcode.com/problems/first-bad-version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
'''

# This can be solved by using binary search
# We know that if isBadVersion(5) is true, then the faulty version is prior to
# Conversely if isBadVersion(5) if false, then the faulty version is after version 5
# In this case we need to return the lower boundary for the 'first' to be true

# just a placeholder for an API call
def isBadVersion(n):
    return

# Time is O(log(n)) - standard time for binary search
# Space is O(1) - only created simple variables
def firstBadVersion(n):
    l = 1
    r = n
    while l <= r:
        m = l + (r-l) // 2
        if isBadVersion(m):
            r = m - 1
        else:
            l = m + 1
    return l