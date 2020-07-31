'''
340. Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Pattern - sliding window
'''

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        # this is a generalization of the k=2 case
        # we use sliding window and keep hashtable: character -> count
        
        n = len(s)
        if n < k:
            return n
    
        # two pointers
        left = right = 0
        
        # hashtable: character -> count
        seen = defaultdict(int)
        
        maxlen = k
        counter = 0
        
        while right < n:
            rightchar = s[right]
            seen[rightchar] += 1
            
            # new character, increment unique counter
            if seen[rightchar] == 1: counter += 1
            right += 1
            
            # more than k distinct characters, trim from the left
            while counter > k:
                leftchar = s[left]
                
                if leftchar in seen:
                    seen[leftchar] -= 1
                if seen[leftchar] == 0: counter -= 1
                
                left += 1
            
            maxlen = max(maxlen, right-left)
        
        return maxlen