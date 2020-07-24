'''
207. Course Schedule
https://leetcode.com/problems/course-schedule/
'''

from typing import List

# Approach: Topological sort using DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # step 0 - initialize adj_list
        adj_list = {course:[] for course in range(numCourses)}
        #adj_list = defaultdict(list)
        
        # step 1 - populate the adj_list
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        # step 2 - do depth-first search
        seen = {}
        output = []
        
        def visit(node):
            if node in seen:
                return seen[node]   # will return False if processing, i.e. detected a cycle
            
            seen[node] = False      # mark as processing
            for next_node in adj_list[node]:
                res = visit(next_node)
                if not res:         # detected a cycle further down the recursive call
                    return False
            
            seen[node] = True       # mark as visited (processed)
            return True
        
        if not all(visit(node) for node in adj_list):   # if there was a cycle anywhere, no topological sort exists, i.e. not possible to take all classes
            return False
        
        return True
        