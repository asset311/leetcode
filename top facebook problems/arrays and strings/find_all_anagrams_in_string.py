'''
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
from typing import List

# Approach 1: Two words are anagrams if and only if they result in equal strings after sorting 
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

# Approach 2: sliding window + counter hashmaps
# The problem with this implementation is the efficient slicing of the array, so takes a long time for long strings
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        indx = []
        
        i = 0
        j = i + len(p)
        p_counter = Counter(p)
        
        while j <= len(s):
            s_counter = Counter(s[i:j])
            if s_counter == p_counter:
                indx.append(i)
                
            i, j = i+1, j+1
            
        return indx

# The same as approach 2 with efficient implementation of the sliding window
# Time is O(m+n) where m and n are lenghts of s and p respectively
# Space is 
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