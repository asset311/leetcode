'''
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring

Pattern - Sliding window
'''

'''
General approach.
1. Create a frequency table for T
2. Start traversing S and check if character is present in T:
    - if in frequency table, then decrement the value of a character
    - once all letters in the frequency table have count of '0', we found a substring containg all in T

3. Start traversing from the beginning of the string again
    - this time if found in frequency table, increment the count
    - once this count for any letter is > 0 means we removed the necessary character
    - our substring no longer contains the necessary chars in T

4. Repeat from where we stopped in 1.

'''
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freq_table = Counter(t)
        freq_counter = len(freq_table)

        ans = ''
        min_len = float('inf')

        begin = end = 0
        while end < len(s):
            
            # good technique to check if T chars are in substring B
            # when all char counts of T are <= 0, it means B contains T's chars
            endchar = s[end]
            if endchar in freq_table:
                freq_table[endchar] -= 1
                if freq_table[endchar] == 0: 
                    freq_counter -= 1

            # keep moving the pointer to the right
            end += 1

            # this would be true if we found a substring of S that contains T
            while freq_counter == 0:
                # check condition
                # potentially found a shorter substring
                if end-begin < min_len:
                    min_len = end-begin
                    ans = s[begin : end]

                # begin iterating from the left trying to trim the substring
                # the trick is we increment T's chars, and when count > 0 we trimmed too much
                startchar = s[begin]
                if startchar in freq_table:
                    freq_table[startchar] += 1
                    if freq_table[startchar] > 0: 
                        freq_counter += 1
                begin += 1

        return ans


