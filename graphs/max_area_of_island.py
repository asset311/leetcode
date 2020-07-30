'''
695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/
'''

from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # this problem boils down to finding all connected components
        # then returning the length of the largest one
        
        # for each '1' cell start DFS to find connected component
        # track the number of cells and update the global max_area
        
        def dfs(grid,r,c,area):
            # boundary conditions
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            
            # end dfs if hit water or already visited
            if grid[r][c] != 1:
                return
            
            # mark as visited
            self.area += 1
            grid[r][c] = 'x'
            
            # recursively call on its neighbors
            dfs(grid, r-1, c, self.area)
            dfs(grid, r+1, c, self.area)
            dfs(grid, r, c+1, self.area)
            dfs(grid, r, c-1, self.area)
            
            self.max_area = max(self.max_area, self.area)
        
        
        self.max_area = 0
        
        R = len(grid)
        C = len(grid[0])
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    self.area = 0
                    dfs(grid,r,c,self.area)
        
        print(grid)
        return self.max_area