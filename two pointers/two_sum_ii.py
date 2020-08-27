'''
167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            if sum([numbers[left], numbers[right]]) < target:
                left += 1
            elif sum([numbers[left], numbers[right]]) > target:
                right -= 1
            else:
                return [left+1, right+1]