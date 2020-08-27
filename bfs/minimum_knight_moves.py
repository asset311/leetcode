'''
1197. Minimum Knight Moves
https://leetcode.com/problems/minimum-knight-moves/

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.
'''

# Approach: BFS on legal moves
# This is guaranteed to find the minimum steps, because we count 8 possible moves as 1 step.
# There is a way to speed it up by only considering the correct quadrant

from collections import deque
class Solution:
    def minKnightMoves(self, s: int, e: int) -> int:
        # BFS
        queue = deque() 
        queue.append([0,0,0])   #initial start is x=0, y=0, steps=0

        visited = set()
        visited.add((0,0))

        while queue:
            x, y, steps = queue.popleft()
            if x == s and y == e:
                return steps
        
            # construct a set of nodes that are it's neighbors
            neighbors = [(x-1, y-2), (x-1, y+2), (x-2, y-1), (x-2, y+1), (x+1, y-2), (x+1, y+2), (x+2,y-1), (x+2,y+1)]  # 8 legal moves

            for i,j in neighbors:
                if (i,j) not in visited:
                    queue.append((i,j,steps+1))
                    visited.add((i,j))
        return -1

