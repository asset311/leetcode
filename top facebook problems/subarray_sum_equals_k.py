'''
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example:
Input: nums = [1,1,1] k=2
Output: 2 --> [1,1], [1,1]
'''
# Naive solution that will check all subarray sums
# This solution is O(n^2) since there are two nested loops to find all subarrays
def subarraySum(nums, k):
    counter = 0
    for i in range(len(nums)):
        s = nums[i]
        if s == k:
            counter += 1
        j = i+1
        while j <= len(nums)-1:
            s += nums[j]
            if s == k:
                counter += 1
            j += 1
    return counter


# O(n) solution exists that relies on comparing the different between
# cumulative sum and k, and if the difference was already in some cumulative sum prior
# it means that a new subarray of sum k is possible
# O(1) for accessing the previous cumulative sums through hashtable
# https://www.youtube.com/watch?v=bqN9yB0vF08

def subarraySum(nums, k:int) -> int:

    sumdict = {0:1}     # dictionary of cumulative sums and their count
    n = len(nums)       # total nums length
    s = 0               # variable to hold current cumulative sum
    count = 0           # final counter to output

    for num in nums:
        s += num      # update current cumulative sum
        if (s-k) in sumdict:
            count += sumdict[s-k]
        if s in sumdict:    # we already saw subarray with that sum
            sumdict[s] += 1
        else:
            sumdict[s] = 1
    
    return count

