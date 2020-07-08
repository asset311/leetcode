'''
485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
'''
from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    count = max_count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    return max(max_count, count)



# Initial version
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    prev = nums[0]
    max_count = count = 1 if prev == 1 else 0
    
    for current in range(1,len(nums)):
        if nums[current] == 1:
            if prev == 1:
                count += 1
            else:
                count = 1
        else:
            count = 0
        prev = nums[current]
        max_count = max(count, max_count)
    return max_count