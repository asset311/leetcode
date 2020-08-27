'''
286. Walls and Gates
https://leetcode.com/problems/walls-and-gates/
'''
from typing import List
from collections import deque


# The key is to recognize that if we search from gates to empty rooms
# We are guaranteed to find the shortest path by using BFS
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # this is similar to 01-matrix
        # our distances are already marked as INF
        # start BFS from 0 values, and update distance
        
        
        R = len(rooms)
        if R == 0:
            return
        
        C = len(rooms[0])
        
        # specify neighbor coordinates
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        
        # push all 0 cell coordinates onto the queue
        # we'll be going from gates to empty rooms
        queue = deque()
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        # bfs
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                # the next cell must be at most 1 step away from gates
                # as the neighbouring cell, so if not, upgrade and push back to the queue
                if nr>=0 and nc>=0 and nr<R and nc<C:
                    if rooms[nr][nc] > rooms[r][c] + 1:
                        rooms[nr][nc] = rooms[r][c] + 1
                        queue.append((nr,nc))