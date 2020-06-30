'''
'''

# Approach 1: use additional array
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    arr = [0]*n
    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            arr[k] = nums[i]
            k += 1
    
    nums[:] = arr

# Approach 2: no new array, replace in place using the same logic
def moveZeroes(nums: List[int]) -> None:
    n = len(nums)
    k = 0
        
    # move all the non-zero values to the front
    for i in range(n):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1
        
    # need to populate the rest with 0
    if n-k > 0:
        for j in range(k,n):
            nums[j] = 0
