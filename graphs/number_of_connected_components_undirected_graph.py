'''
323. Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
'''
from typing import List


'''
General algorithm:
1. Create a graph from the edges list in the form {v:[neighbors]}
2. Create a set of visited nodes to keep track of already visited nodes
3. In a loop, process new nodes and only increment count when we process a node that hasn't been visited in previous iteration
    - each DFS will be done on individual connected components
'''

# Approach 1: DFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        # iterative DFS
        def dfs(v):
            stack = [v]
            while stack:
                current = stack.pop()
                visited.add(current)

                for e in graph[current]:
                    if e not in visited:
                        stack.append(e)
        '''
        # recursive DFS
        def dfs(v):
            if v in visited:
                return
            
            visited.add(v)
            for e in graph[v]:
                dfs(e)
    
        visited = set() # to keep track of visited nodes
        count = 0
        
        # graph is undirected, so need to add neighbors in both directions
        graph = {x:[] for x in range(n)}
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        for v in range(n):
            if v not in visited:
                count += 1
                dfs(v)
                
        return count

'''
BFS
def countComponents(n, edges):
        g = {x:[] for x in xrange(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        ret = 0
        for i in xrange(n):
            queue = [i]
            ret += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]

        return ret
'''