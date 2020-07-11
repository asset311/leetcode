'''
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
'''

# Approach 1: Brute force
# Time complexity is O(n^2)
# Space complexity is O(n)

def productExceptSelf(nums):
    arr = []
    for i in range(len(nums)):
        prd = 1
        for j in range(len(nums)):
            if j != i:
                prd *= nums[j]
        arr.append(prd)
    return arr

# Approach 2: use a similar approach to Balancing Element problem
# calculate left and right product at position i
# then the overall product at i is the product of left and right

# Time complexity is O(n) - even though we do two loops, those are sequential, so additive
# Space complexity is O(n) - we allocate 3 additional arrays of length n
def productExceptSelf(nums):
    
    num = 1
    leftPrd = []
    for i in range(len(nums)):
        leftPrd.append(num)
        num = num * nums[i]
    
    num = 1
    rightPrd = [None]*len(nums)
    for i in reversed(range(len(nums))):
        rightPrd[i] = num
        num = num*nums[i]
    
    arr = [None]*len(nums)
    for i in range(len(nums)):
        arr[i] = leftPrd[i] * rightPrd[i]
    
    return arr

# Approach 3: only allocate one additional array, the principle stays the same
# O(n) time complexity
# O(1) if we don't count the additional array that needs to be returned
# otherwise it is also O(n)
def productExceptSelf(nums):

    products_of_all_ints_except_at_index = [None]*len(nums)

    # holds products of all numbers before i
    product_so_far = 1
    for i in range(len(nums)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= nums[i]
    
    # now we just populate backwards
    product_so_far = 1
    for i in range(len(nums)-1,-1,-1):
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= nums[i]
    
    return products_of_all_ints_except_at_index
