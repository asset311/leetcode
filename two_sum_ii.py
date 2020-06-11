'''
167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2.

Note:

- Your returned answers (both index1 and index2) are not zero-based.
- You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

# We can do this with a two-pointer technique
# Notice that since the array is sorted we can either move pointers in ascending or descending order
# depending on the comparison to the target
def twoSum(numbers: list, target:int) -> int:
    start, end = 0, len(numbers)-1

    while start < end:
        two_sum = numbers[start] + numbers[end]
        if two_sum == target:
            break 
        elif two_sum > target:
            end = end-1
        else:
            start = start+1
        
    return (start+1,end+1)
