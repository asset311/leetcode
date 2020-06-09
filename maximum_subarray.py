''' 
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

'''

def max_k_subarray_sum(l:list, k:int) -> int:
    #use sliding windows
    msum = wsum = 0
    for i in range(k):
        wsum += l[i]
    
    end = k
    while end < len(l):
        wsum += l[end] - l[end-k]
        msum = max(msum, wsum)
        end += 1
    return msum

def max_subarray_sum(l:list) -> int:
    msum = wsum = 0
    k = 1
    while k < len(l):
        wsum = max_k_subarray_sum(l, k)
        msum = max(wsum, msum)
        k += 1
    return msum