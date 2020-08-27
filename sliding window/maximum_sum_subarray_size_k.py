'''
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Pattern - sliding window
'''

def max_sub_array_of_size_k(k, arr):

  max_sum = window_sum = 0
  start = 0
  for end in range(len(arr)):
    window_sum += arr[end]
    if end >= k-1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[start]
      start += 1
  return max_sum