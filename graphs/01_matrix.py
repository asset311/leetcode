'''
542. 01 Matrix
https://leetcode.com/problems/01-matrix/
'''


from collections import defaultdict, deque
from typing import List

# Approach 1: BFS from '1' columns to '0'
# The problem is we do BFS for 1, which is sub-optimal
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m = len(matrix)
        n = len(matrix[0])
        
        def bfs(i,j):
            q = deque()
            q.append((i,j,0))
            
            visited = set()
            visited.add((i,j))
            
            while q:
                x, y, distance = q.popleft()
                if matrix[x][y] == 0:
                    return distance
                
                neighbors = [(x,y+1), (x,y-1), (x-1,y), (x+1,y)]
                for i,j in neighbors:
                    if i<0 or i>=m or j<0 or j>=n:
                        continue
                    if (i,j) not in visited:
                        q.append((i,j,distance+1))
                        visited.add((i,j))
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] = bfs(i,j)
        
        return matrix

# Approach 2: Simultaneous BFS
# Instead of calling BFS from each '1' cell, go in the other direction
# from '0' cell to '1' and update distance - this will be guaranteed to be shortest using BFS
from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        R = len(matrix)
        if R == 0:
            return matrix
        
        C = len(matrix[0])
        
        #dist = defaultdict(lambda: float('inf'))
        queue = deque()
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    queue.append((r,c))
                else:
                    matrix[r][c] = float('inf')

        dr = [-1,1,0,0]
        dc = [0,0,1,-1]

        # bfs
        while queue:
            r, c = queue.popleft()
            
            # 4 directions - east, west, north, south
            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]
                
                # eliminate border cases
                if rr >= 0 and cc >=0 and rr < R and cc < C:
                    if matrix[rr][cc] > matrix[r][c] + 1:
                        matrix[rr][cc] = matrix[r][c] + 1
                        queue.append((rr,cc))
        return matrix
    
        




