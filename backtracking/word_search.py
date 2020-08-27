'''
79. Word Search
https://leetcode.com/problems/word-search/
'''
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking
        
        def backtrack(r, c, suffix):
            
            # base case - found match for each letter in the word
            if len(suffix) == 0:
                return True
            
            # if we are out of bounds and haven't matched all letters yet
            if r<0 or r>=len(board) or c<0 or c>=len(board[0]):
                return False
            
            # if we do not match the first letter of the word, no further exploration needed
            if board[r][c] != suffix[0]:
                return False
            
            ret = False
            
            # mark the choice before exploring further - choose
            board[r][c] = '*'
            
            # explore
            dr = [1,-1,0,0]
            dc = [0,0,1,-1]
            for i in range(len(dr)):
                nr = r+dr[i]
                nc = c+dc[i]
                ret = backtrack(nr, nc, suffix[1:])
                # found, break and do some cleanup before returning
                if ret: break
                    
            # unmark - unchoose
            board[r][c] = suffix[0]
            
            # either matched, or tried all options and did not match
            return ret
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, word):
                    return True
        
        # no match found after all explorations
        return False