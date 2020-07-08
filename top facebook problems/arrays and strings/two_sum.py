'''
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# Approach 1: Brute force that runs in O(n^2)
# Nested loops to check sums in every subarray starting from the beginning
def twoSum(nums, target): 
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []



# Approach 2: Use hashtable and their position to keep track of previous numbers seen
# If the (target - current) is in the hashtable, then we're done
# Otherwise there is no pair
# IMPORTANT - we are asked to only return 2 numbers, but the array may contain more

# Time is O(n)
# Space is O(n) where n is the number of elements in the array
def twoSum(nums, target):
    val_to_index = {}
    for i,num in enumerate(nums):
        diff = target - num
        if diff not in val_to_index:
            val_to_index[num] = i
        else:
            return [val_to_index[diff],i]