'''
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: 
For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
'''

# We can solve this problem in O(n) time by using two pointers
# Pointers will move in opposite directions, and advance on non-alphanumeric
# If at any point letters aren't equal, it's not a palindrome

def isPalindrome(s:str) -> bool:
    l = list(s)
    start, end = 0, len(l)-1

    while start < end:
        while not l[start].isalnum() and start<end:
            start += 1
        while not l[end].isalnum() and start<end:
            end -= 1
        if l[start].lower() != l[end].lower():
            return False
        start, end = start+1, end-1
    return True

# there is a way to solve this with a stack and queue, but requires more space
# also harder to deal with non-alphanumeric characters