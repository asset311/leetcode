'''
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Pattern - sliding window
'''
from typing import List

# Approach 1: Two words are anagrams if and only if they result in equal strings after sorting
# Time is O(m log(m) + n log(n)) where m and n are lengths of s and p - since we do sorting
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_lst = list(p)
        p_lst.sort()
        
        indx = []
        
        i = 0
        j = i + len(p)
        
        while j <= len(s):
            if sorted(s[i:j]) == p_lst:
                indx.append(i)
                
            i, j = i+1, j+1
            
        return indx

# Approach 2: sliding window + 2 counters
# Time is O(m+n) where m and n are lenghts of s and p respectively
# Space is O(m+n)
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indx = []
        ns, np = len(s), len(p)
        p_counter = Counter(p)
        s_counter = Counter()

        # sliding window on the string s
        for i in range(ns):
            # add one more letter
            # on the right side of the window
            s_counter[s[i]] += 1

            # remove one letter from left side if the window exceeds the length
            if i >= np: #means the window is longer than np since i counts from 0
                if s_counter[s[i-np]] == 1:     #the count for this letter is 1
                    del s_counter[s[i-np]]      #simply delete
                else:
                    s_counter[s[i-np]] -=1      # decrement
            
            if s_counter == p_counter:          # for anagrams the counters are the same
                indx.append(i - np + 1)
        
        return indx

# Approach 3: sliding window + 1 counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p) or len(s) == 0:
            return []
        
        p_freq = Counter(p)
        p_counter = len(p_freq)
        begin = end = 0
        ans = []
        
        while end < len(s):
            # first traversal and find substring that contains p's chars
            endchar = s[end]
            if endchar in p_freq:
                p_freq[endchar] -=1
                if p_freq[endchar] == 0: p_counter -=1
            end += 1
            
            while p_counter == 0:

                # check condition
                # found substring of length of p
                if end-begin == len(p):
                    ans.append(begin)
                
                beginchar = s[begin]
                if beginchar in p_freq:
                    p_freq[beginchar] +=1
                    if p_freq[beginchar] > 0: p_counter += 1
                begin += 1
        
        return ans
