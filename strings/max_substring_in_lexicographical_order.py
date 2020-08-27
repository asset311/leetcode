'''
1163. Last Substring in Lexicographical Order
https://leetcode.com/problems/last-substring-in-lexicographical-order/
'''

# Approach 1: Brute-force based on suffixes
def lastSubstring(s: str) -> str:
    mx = ''
    for i in range(len(s)):
        mx = max(mx, s[i:])
    return mx

# Approach 2: Use three pointers
class Solution:
    def lastSubstring(self, s: str) -> str:
        # checking against i, k is used for consecutive duplicate letters
        # j is used to find the next suffix letter greater than pointing at i
        i, j, k = 0, 1, 0
        n = len(s)
        
        while j+k < n:
            if s[i+k] == s[j+k]:  # duplicate
                k += 1
                continue
            elif s[i+k] > s[j+k]:   # keep trying to find the next suffix letter that is greater
                j = j + k + 1
            else:                   # next pointing suffix letter is greater, jump to that letter
                i = max(i+k+1, j)
                j = i+1
            k = 0
        
        return s[i:]

