'''
405. Convert a Number to Hexadecimal
https://leetcode.com/problems/convert-a-number-to-hexadecimal/

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
https://en.wikipedia.org/wiki/Two%27s_complement

Note:

 1. All letters in hexadecimal (a-f) must be in lowercase.
 2. The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
 3. The given number is guaranteed to fit within the range of a 32-bit signed integer.
 4. You must not use any method provided by the library which converts/formats the number to hex directly.

'''

# two's complement, assuming 32-bit signed integers
def int_to_hex(n:int) -> str:
    stack = []  #used to store remainders
    int_to_hex = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    
    if n == 0:
        return '0'

    elif n<0:   #convert the base if negative
        n *=-1
        n = pow(2,32) - n
    
    while n>0:
        stack.append(n%16)
        n = n // 16
    
    res = ''
    while stack:
        i = stack.pop()
        res += str(i) if i<10 else int_to_hex[i]
    
    return res