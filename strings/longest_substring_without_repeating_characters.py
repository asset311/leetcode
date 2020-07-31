'''
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Pattern - sliding window
'''

# Approach 1: Accumulate with hashtable - slow
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        
        for i in range(len(s)):
            freq_table = {}
            end = i
            length = 0
            
            while end < len(s):
                char = s[end]
                if char not in freq_table:
                    freq_table[char] = 1
                    length += 1
                    max_length = max(length, max_length)
                else:
                    break
                end += 1
        
        return max_length


# Approach 2: Optimized sliding window - faster
# Keep hashmap: character -> its rightmost position
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # instead of starting new hashtable, accumulating and checking
        # we have a sliding window where we store indices and skip to the right place
        # after encountering a repeating character
        
        begin = end = 0
        ans = 0
        seen = {}
        
        while end < len(s):
            endchar = s[end]
            
            # if we encounter a repeated character
            # advance 'begin' pointer unless it's already past it
            if endchar in seen:
                begin = max(begin, seen[endchar]+1)
            
            seen[endchar] = end
            end += 1
            
            ans = max(ans, end-begin)
        
        return ans

# More optimized pythonic solution
# the key is that we are storing indices, and that's why it is a sliding window
# the window is sliding, but there is no explicit scanning by 'start' pointer
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxlength = start = 0

        for i, c in enumerate(s):
            if c in seen:
                start = max(seen[c]+1, start)
            maxlength = max(maxlength, i-start+1)
            seen[c] = i
            
        return maxlength