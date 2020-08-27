'''
785. Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/

For an explicit solution and explanation, visit
https://www.geeksforgeeks.org/bipartite-graph/
'''

# We treat this as a graph coloring problem
# We should be able to greedily color (legally) the graph if and only if it is bipartite.
from typing import List

# Time complexity O(V+E) where V is the number of vertices, and E is the number of edges
# Space complexity is O(V) to store vertex coloring

# this processes one node at a time from the graph
class Solution(object):
    def isBipartite(self, graph):
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True