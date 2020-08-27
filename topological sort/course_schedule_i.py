'''
207. Course Schedule
https://leetcode.com/problems/course-schedule/
'''

from typing import List

# Approach: Topological sort using DFS

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # we need to find if there is a topological order
                
        # step 0. Initialize adjacency list
        adj_list = {course:[] for course in range(numCourses)}
        
        # step 1. Populate the adjacency list
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        # do a DFS on the graph
        seen = {}
        output = []
        
        
        # this will visit each prerequisite before coming back to it's dependent course
        def visit(course):
            
            if course in seen:
                return seen[course]     # will return False if detects a cycle
            
            seen[course] = False    # being visited
            
            # visit this course's prerequisites
            for prereq in adj_list[course]:
                res = visit(prereq)
                if not res:         # detected a cycle further down the recursive call
                    return False
                
            seen[course] = True     # mark as visited (processed)
            output.append(course)
            
            return True
        
        if not all(visit(course) for course in adj_list):   # if there was a cycle anywhere, no topological sort exists, i.e. not possible to take all classes
            return False
        
        print(output)
        return True
        