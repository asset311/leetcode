'''
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0, if no such subarray exists.
'''

# This is a floating size sliding window
# 'end' pointer moves to get to the right sum
# 'left' pointer minimizes the subarray size to get the smallest    
def smallest_subarray_with_given_sum(s, arr):
  start = end = 0
  min_len = float('inf')
  window_sum = 0

  while end < len(arr):
      window_sum += arr[end]
      end += 1
      while window_sum >= s:
          min_len = min(min_len, end-start)
          window_sum -= arr[start]
          start += 1
  
  return min_len if min_len < float('inf') else 0

  # Time complexity: O(N) where N is the number of elements in the array
  # Space complexity: O(1) as we use no extra space