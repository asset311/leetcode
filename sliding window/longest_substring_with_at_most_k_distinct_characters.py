'''
340. Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Pattern - sliding window
'''
# Approach 1: Step-wise sliding window
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        # hashtable: character -> count
        char_frequency = defaultdict(int)

        for right in range(len(s)):

            # either increment the frequency or just add character
            # because it is a defaultdict, lookup will create an entry
            rightchar = s[right]
            char_frequency[rightchar] += 1
            
            # shrink the window for as long as we have more than k characters
            while len(char_frequency) > k:
                leftchar = s[left]
                char_frequency[leftchar] -= 1

                if char_frequency[leftchar] == 0:
                    del char_frequency[leftchar]
                left += 1
            
            # check to update the max length so far
            max_len = max(max_len, right-left+1)

        return max_len

# Time complexity O(N), where N is the number of characters in the input string
# Space complexity is O(k) as we'll be storing at most k+1 characters in the hashtable

# Approach 2: Sliding window with jumps
# Store indices instead, and jump to the smallest index to shrink the window
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans=0
        start=0
        dic={}
        for i in range(len(s)):
            dic[s[i]]=i
            if len(dic)>k:
                start=min(dic.values())+1
                del dic[s[start-1]]
            ans=max(ans,i-start+1)
        return ans