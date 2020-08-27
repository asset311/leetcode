'''
159. Longest Substring with At Most Two Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

Pattern - sliding window
'''

from collections import defaultdict

# Approach 1: Sliding window
# Keep counts of characters, not their last positions
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # what if we use a familiar sliding window principle
        # we store indices, but also the counts of unique symbols we saw

        n = len(s)
        if n < 3:
            return n
        
        # sliding window left and right pointers
        left = right = 0

        # we can at least have 2 chars as the starting point for max length
        maxlen = 2
        counter = 0

        # hashmap: character -> count of that character
        seen = defaultdict(int)
        
        while right < n:
        
        # keep traversing until we get 2 chars
            rightchar = s[right]
            seen[rightchar] += 1
            # increment counter of unique symbols
            if seen[rightchar] == 1: counter += 1
            right += 1
        
            # slidewindow contains 3 characters
            while counter > 2:
                leftchar = s[left]

                # continue scanning until we get back to 2 unique chars
                if leftchar in seen:
                    seen[leftchar] -= 1
                if seen[leftchar] == 0: counter -= 1
            
                left += 1
        
            maxlen = max(maxlen, left-right)
        
        return maxlen

