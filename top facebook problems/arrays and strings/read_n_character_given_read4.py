'''
157. Read N Characters Given Read4
https://leetcode.com/problems/read-n-characters-given-read4/

Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

 
Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.
The return value is the number of actual characters read.
Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

Note: buf4[] is destination not source, the results from read4 will be copied to buf4[]
'''


# Approach 1: write into a temporary buffer then copy n chars to the final buffer
# Space is O(n)
def read(self, buf, n):
    requests = math.ceil(n / 4)     #figure out how many times to call read4
    final_array = []
    actual_n = 0
    
    while requests:
        buf4 = [None]*4
        r = read4(buf4)
        actual_n += r   # keep track of the actual number of chars read
        
        if r == 0:  # no more characters to read
            break

        final_array.extend(buf4)
        requests -= 1
    
    actual_n = min(actual_n, n)
    
    buf[:] = final_array[:actual_n]


# Approach 2: write directly into the output buffer
# Space is O(1)
def read(self, buf, n):
    idx = 0
    while n > 0:
        # read file to buf4
        buf4 = [None]*4
        r = read4(buf4)
        
        # if no more char in file, return
        if r ==0:
            return idx
        
        # write buf4 into buf directly
        for i in range(min(l, n)):  # in case n is less than 4 in the end
            buf[idx] = buf4[i]
            idx += 1
            n -= 1
    return idx

