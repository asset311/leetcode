'''
67. Add Binary
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

'''

# Approach 1: Brute force binary math
def addBinary(a:str, b:str) -> str:
    stack = []

    # extend the shorter string
    '''
    delta = abs(len(a) - len(b))
    if delta:
        if len(a) > len(b):
            b = ('0'*delta) + b
        else:
            a = ('0'*delta) + a
    '''
    # use built-in function to zero fill
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # perform the addition
    carry = '0'
    for i in range(len(a)-1,-1,-1):
        if a[i] == '1' and b[i] == '1':
            if carry == '1':
                stack.append('1')
            else:
                stack.append('0')
                carry = '1'
        elif (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1'):
            if carry == '1':
                stack.append('0')
            else:
                stack.append('1')
                carry = '0'
        else:
            if carry == '1':
                stack.append('1')
                carry = '0'
            else:
                stack.append('0')

    if carry == '1':
        stack.append('1')
        
    
    res = ''
    for i in range(len(stack)):
        res += stack.pop()
    
    return res

# Approach 2: a classic algorithm which puts emphasis on the carry
# Time complexity is O(max(M,N)) where N and M are lengths of a and b
# Space complexity is O(max(M,N)) to keep the answer
def addBinary(a:str, b:str) -> str:
    answer = []

    # extend with zeroes to make the same length
    n = max(len(a), len(b))
    a = a.zfill(n)
    b = b.zfill(n)

    carry = 0
    for i in range(n-1,-1,-1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1
        
        if carry % 2 == 1:
            answer.append('1')
        else:
            answer.append('0')
        
        carry = carry // 2
    
    if carry:
        answer.append('1')
    
    answer.reverse()
    return ''.join(answer)

# Similar code to above, but slightly more clean
def add_binary_nums(x, y): 
    max_len = max(len(x), len(y)) 

    x = x.zfill(max_len) 
    y = y.zfill(max_len) 
      
    # initialize the result 
    result = '' 
      
    # initialize the carry 
    carry = 0

    # Traverse the string 
    for i in range(max_len - 1, -1, -1): 
        r = carry 
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result 
        carry = 0 if r < 2 else 1     # Compute the carry. carry = r // 2
      
    if carry !=0 : result = '1' + result 

    return result.zfill(max_len) 

