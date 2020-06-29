'''
344. Reverse String
https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

'''

from typing import List

def reverseString(self, s: List[str]) -> None:
    start, end = 0, len(s)-1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start, end = start+1, end-1