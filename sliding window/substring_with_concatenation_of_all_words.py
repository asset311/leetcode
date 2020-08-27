'''
30. Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

Pattern - sliding window
'''

'''
Logic:
s = "barfoothefoobarman"
words = ["foo","bar"]

In this example:
numberOfWords = len(words) = 2
lengthOfWord = len(words[0]) = 3

starting from index 0, we need to check first 3 letters, then next 3 letters
i = 0
'bar'
'foo'
this matches our requirement, add to answer

i = 1
'arf'
immediately doesn't match one any of our words, can ignore

i = 2
'rfo'
immediately doesn't match one any of our words, can ignore

i = 3
'foo'
matches, check next
'the'
doesn't match, continue

'''
from typing import List
from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        # edge cases
        if len(words) == 0 or len(s) == 0 or len(s) < len(words):
            return []
    
        # initialize some counters we'll use
        numberOfWords = len(words)
        lengthOfWord = len(words[0])
        S = len(s)
    
        # create a word frequency count
        lookup = defaultdict(int)
        for word in words:
            lookup[word] += 1
        
        # function to do the sliding window
        # returns False if any of the scanned words, otherwise returns True
        def slidingWindow(startIdx):
            # create a copy of the lookup table, otherwise the original will change
            word_counts = lookup.copy()
            
            for nw in range(numberOfWords):
                wordStartIdx = startIdx + nw*lengthOfWord
                wordEndIdx = wordStartIdx + lengthOfWord
                word = s[wordStartIdx: wordEndIdx]
    
                # if the count of this word is 0, that either means:
                # it was never present in the original words
                # or this word was encountered before and it appears more times than necessary
                if not word_counts[word]:
                    return False
                else:
                    word_counts[word] -= 1
            return True
        
        # scan s and only add indices where slidingWindow returns true
        return [i for i in range(S - numberOfWords * lengthOfWord + 1) if slidingWindow(i)]

