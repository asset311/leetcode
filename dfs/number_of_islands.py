'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
from typing import List

# Approach 1: DFS
# This is similar to connected components in a graph
# The difference is how to mark vertices as visited and use immediate neighbors on the grid to explore neighbors
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0
        # go through the matrix to find a new island group
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    ans += 1
                    self.dfs(grid, row, col)        
        return ans


    def dfs(self, grid, row, col):
        
        # check out of bounds condition
        if row < 0 or row >= len(grid) or col<0 or col>= len(grid[0]):
            return
        
        # both doesn't revisit (x) and doesn't count '0'
        if grid[row][col] != '1':
            return

        # mark as visited
        grid[row][col] = 'x'

        # recursively visit its neighbors
        self.dfs(grid, row+1, col)
        self.dfs(grid, row-1, col)
        self.dfs(grid, row, col+1)
        self.dfs(grid, row, col-1)

