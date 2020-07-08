'''
266. Palindrome Permutation
https://leetcode.com/problems/palindrome-permutation/

Given a string, determine if a permutation of the string could form a palindrome.

'''

# A set of characters can form a palindrome if at most one character occurs odd number of times 
# and all characters occur even number of times.
# Use this fact to maintain a set - adding and removing as you traverse the string
# If the set is larger than 1 in the end, it is not a palindrome.

def canPermutePalindrome(self, s: str) -> bool:
    letters = set()
    for c in s:
        if c in letters:
            letters.remove(c)
        else:
            letters.add(c)
    return len(letters) <=1