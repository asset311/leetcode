'''
130. Surrounded Regions
https://leetcode.com/problems/surrounded-regions/
'''

from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board or not board[0]:
            return 
                
        def dfs(board, row, col):
            # don't fall off the board walls
            if row <0 or row>=len(board) or col<0 or col>=len(board[0]):
                return
            
            # end of the connected region
            if board[row][col] != "O":
                return
            
            # flip to 'E'
            board[row][col] = "E"
            
            # explore all the neighbors
            dfs(board, row+1, col)
            dfs(board, row-1, col)
            dfs(board, row, col+1)
            dfs(board, row, col-1)
        
                    
        # Step 2). mark the "escaped" cells with 'E'
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == len(board)-1 or col == len(board[0])-1 or row == 0 or col == 0):
                    if board[row][col] != 'X':
                        dfs(board, row, col)
        
        # Step 3. flip the captured cells ('O'->'X') and the escaped one ('E'->'O')
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O': board[row][col] = 'X'    #captured
                elif board[row][col] == 'E': board[row][col] = 'O'  #escaped

'''
Notes:
1) Optimized by checking all border connected components first
2) Can improve the DFS call by checking boundary conditions before the recursive call (reduces the amount of calls)
3) Mark visited cells in-place rather than maintaining another _visited_ set
'''