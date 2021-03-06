'''
1048. Longest String Chain
https://leetcode.com/problems/longest-string-chain/

'''
from typing import List

# Approach 1: Backtracking
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        all_chains = []
        for word in words:
            all_chains.extend(self.createChains(word, words))
        return max(map(len,all_chains))

    def createChains(self, word, words):
        result = []
        step = [word]
        dictionary = set(words)

        self.helper(word, step, dictionary, result)
        return result

    def helper(self, word, step, dictionary, result):
        result.append(step[:])

        for i in range(len(word)-1,-1, -1):
            substring = word[:i]+word[i+1:]

            if substring in dictionary: # choose
                step.append(substring)
                self.helper(substring, step, dictionary, result) # explore
                step.pop() # unchoose


# Approach 2: DFS
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # consider this as a graph problem
        # 'bdca' has edges to ['bca', 'bda','bdc','dca'] etc.
        # we can do DFS on each 'word' in the set of 'words'

        # keep track of length of sequence for each word
        # this also acts as visited nodes
        dp = {word: 0 for word in words}

        def dfs(word):
            if word not in dp:  # return if not in the dictionary, base case
                return 0
            
            # each unvisited node has 0 as it's sequence length
            if not dp[word]:
                # max sequence is stored
                dp[word] = max([dfs(word[:i]+word[i+1:]) + 1 for i in range(len(word))])
            return dp[word]
        
        return max([dfs(word) for word in dp if not dp[word]])






