'''
'''

# Approach 1: Using binary representation
# can use the fact that powers of 4 in binary without leading zeroes, will be of odd length. 
# And the most significant bit is 1, with all else being 0.
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        binary = (bin(num))[2:]
        if len(binary) % 2 != 0 and binary[0] == '1' and binary.count('1') == 1:
            return True
        return False

# Approach 2: Use math
# x = 4^a. Then a = log4(x) = 1/2 log2(x) needs to be an integer
# so check that log2(x) is even
from math import log2
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and log2(num) % 2 == 0
