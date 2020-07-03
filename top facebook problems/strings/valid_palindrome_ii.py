'''
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/

Given a string, we need to check whether it is possible to make this string 
a palindrome after removing exactly one character from this.

Note:
It is not the same as saying - can we make a palindrome if we remove one character, meaning by removing and rearranging.
Hint: https://www.geeksforgeeks.org/remove-character-string-make-palindrome/
'''

# Greedy approach
# Use two pointers from two ends, if at any point characters aren't equal
# We need to check whether by removing one of them the rest of the string is a palindrome
# Both cases would need to be checked

def validPalindrome(s: str) -> bool:
    
    def isPalindrome(string:str, start:int, end:int) -> bool:
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True

    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return any([isPalindrome(s, start+1, end), isPalindrome(s, start, end-1)])
    
    #original string is a palindrome
    return True

# pythonic isPalindrome(s)

def isPalindrome(s:str) -> bool:
    i, j = 0, len(s)-1
    return all( s[k] == s[j-k+i] for k in range(i,j))