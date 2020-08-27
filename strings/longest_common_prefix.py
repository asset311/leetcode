'''
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
'''

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestCommonPrefix = ''
        
        if not strs:
            return longestCommonPrefix
        
        idx = 0
        for c in strs[0]:
            for i in range(1,len(strs)):
                if idx >= len(strs[i]) or strs[i][idx] != c:
                    return longestCommonPrefix
            longestCommonPrefix += c
            idx += 1
        
        return longestCommonPrefix