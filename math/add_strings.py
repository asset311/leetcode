'''
415. Add Strings
https://leetcode.com/problems/add-strings/

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
You are allowed to convert individual digits into int
'''

from typing import List

# use regular high school math to add with carry
def addStrings(num1:str, num2:str) -> str:
    res = []
    carry = 0

    p1 = len(num1) - 1
    p2 = len(num2) - 1

    while p1 >=0 or p2>=0:
        x = int(num1[p1]) if p1 >= 0 else 0
        y = int(num2[p2]) if p2 >= 0 else 0

        tot = (x+y+carry) % 10
        carry = (x+y+carry) // 10

        res.append(tot)

        p1 -= 1
        p2 -= 1
    
    if carry:
        res.append(carry)
    
    return ''.join((str(x) for x in res[::-1]))
