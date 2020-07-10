'''
785. Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/

For an explicit solution and explanation, visit
https://www.geeksforgeeks.org/bipartite-graph/
'''

# We treat this as a graph coloring problem
# We should be able to greedily color (legally) the graph if and only if it is bipartite.
from typing import List
from collections import deque

# Time complexity O(V+E) where V is the number of vertices, and E is the number of edges
# Space complexity is O(V) to store vertex coloring
def isBipartite(self, graph: List[List[int]]) -> bool:
    color = {}  # hastable (node: color)
    for node in range(len(graph)):  #for each node we visit its edges (neighbors)
        if node not in color:
            queue = deque()     #queue to hold current node's neighbors
            queue.append(node)
            color[node] = 0
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in color:
                        queue.append(neighbor)
                        color[neighbor] = color[node] ^ 1
                    elif color[neighbor] == color[node]:
                        return False
    return True 