'''
767. Reorganize String
https://leetcode.com/problems/reorganize-string/
'''

# The key to this approach is priority queue of characters
import heapq as hq
from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        # step 0. Allocate array for the result, Counter to count each char frequency
        output = []
        char_counts = Counter(S)
        
        # step 1. Construct a priority queue with inverse frequency count (use min-heap)
        pq = [(-value, key) for key, value in char_counts.items()] # T: O(n) and S:O(n)
        hq.heapify(pq)  # T: O(n)
        
        # use these vars to hold last added char values
        prev_count, prev_char = 0, ''   
        
        while pq:
            count, char = hq.heappop(pq)
            output += [char]
            
            # check if previously added still remaining, add back to pq
            if prev_count < 0:
                hq.heappush(pq, (prev_count, prev_char))  # T: O(log(n))
            
            # increment counter
            count += 1
            prev_count, prev_char = count, char
        
        result = "".join(output)
        return result if len(result) == len(S) else ""

# Total time is O(n) + O(n) + O(n*log(n)) where n is the number of chars in S
# Space is O(n) + O(n) = O(n)
        