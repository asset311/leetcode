'''
Balancing Elements.
When an element is deleted from an array, the higher-indexed elements shift down one index to fill the gap.
A 'balancing element' is defined as an element that, when deleted from the array, results in the sum 
of the even-indexed elements being equal to the sum of the odd-indexed elements. 
Determine how many balancing element a given array contains.

Example:
arr = [5,5,2,5,8]

When the first or second 5 is deleted, the array becomes [5,2,5,8]
The sum(even) = 5+5 = 10 and sum(odd) = 2+8 = 10.
No other elements of the original array have that property.
There are 2 balancing elements: arr[0] and arr[1]

Write a function that returns an integer denoting the number of balancing elements in the input array
'''

# One way to calculate even and odd sums left and right of each element
# O(n) time complexity
# O(n) space for storing elements
def count_balancing_elements(nums) -> int:
    leftOdd = []
    leftEven = []
    odd = even = 0

    # initialize sum of even and odd left of each element, not including that element
    for i in range(len(nums)):
        leftOdd.append(odd)
        leftEven.append(even)
        if i % 2 == 0:
            even += nums[i]
        else:
            odd += nums[i]
    
    # initiazlie sum of even and odd right of each element, not including that element
    even = odd = 0
    rightOdd = [None]*len(nums)
    rightEven = [None]*len(nums)
    for i in reversed(range(len(nums))):
        rightOdd[i] = odd
        rightEven[i] = even
        if i % 2 == 0:
            even += nums[i]
        else:
            odd += nums[i]

    # element is balancing if sum of odds on the left and evens on the right
    # are equal to the sum of evens on the left and odds on the right
    counter = 0
    for i in range(len(nums)):
        if(leftOdd[i] + rightEven[i] == leftEven[i] + rightOdd[i]):
            counter += 1
    
    return counter

