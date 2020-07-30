'''
547. Friend Circles
https://leetcode.com/problems/friend-circles/
'''
from typing import List

# Approach 1: DFS
# This is similar to connected components in a graph
# We do not construct adjacency matrix, instead use M to directly infer if a vertex is a neighbor

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:       
        def dfs(v):
            if v in visited:
                return

            # perform DFS on neighbors
            visited.add(v)
            for j in range(len(M)):
                if M[v][j] == 1:
                    dfs(j)
        '''
        def dfs(v):
            stack = [v]
            while stack:
                current = stack.pop()
                visited.add(current)
                
                for j in range(len(M[current])):
                    if M[current][j] == 1 and j not in visited:
                        stack.append(j)
        '''
                
        circles = 0
        visited = set()
        for student in range(len(M)):
            if student not in visited:
                circles += 1
                dfs(student)
        
        return circles