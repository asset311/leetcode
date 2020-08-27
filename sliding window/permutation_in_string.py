'''
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/

Pattern - sliding window
'''

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1) or len(s1) == 0 or len(s2) == 0:
            return False
        
        # hastable for s2: character -> frequency
        s1_table = Counter(s1)
        counter = len(s1_table)
        
        # two pointers
        left = right = 0
        
        
        while right < len(s2):
            rightchar = s2[right]
            if rightchar in s1_table:
                s1_table[rightchar] -= 1
                if s1_table[rightchar] == 0: counter -= 1
            right += 1
            
            while counter == 0:
                if right - left == len(s1):
                    return True
                
                leftchar = s2[left]
                if leftchar in s1_table:
                    s1_table[leftchar] += 1
                    if s1_table[leftchar] > 0: counter += 1
                
                left += 1
                
        return False

