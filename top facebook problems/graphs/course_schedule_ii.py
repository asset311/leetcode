'''
210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
'''

from typing import List

# Approach 1: Topological sort with DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # this is about finding the topological sort order
        # if we detect a cycle, then no ordering exists and we return an empty array
        
        # step 1. Construct an adjacency list as a dict: course -> prereq
        adj_list = {course:[] for course in range(numCourses)}
        
        # populate adjacency list from the prerequisites pairs
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        # step 2. Perform a DFS on all courses since ordering is already correct course -> depends on
        course_order = []   # this will have the final ordering
        seen = {}  # each node will be False or True to detect cycles
        
        # this returns False if there is a cycle
        def visit(node):
            if node in seen:
                return seen[node]
            
            seen[node] = False  # mark this node as visiting
            
            for next_node in adj_list[node]:
                res = visit(next_node)
                if not res:         #detected a cycle somewhere
                    return False
            
            course_order.append(node)   # append to topological sort order
            seen[node] = True   #mark as visited
            
            return True
        
        if not all(visit(course) for course in adj_list): # if there was a cycle, at least one will be False
                return []
        
        return course_order

# Approach 2: Topological sort with indegree count (Kahn's Algorithm)
from collections import deque, Counter, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # a different approach using node indegree
        
        # for this approach to work, we need to reverse the dependency structure
        # instead of [course, prereq] we need [prereq, course]
        # allocate an adjacency list of prereq -> course
        # allocate an indegree counter, course -> # of prereq
        adj_list = defaultdict(set)
        in_degree = Counter({course:0 for course in range(numCourses)}) # set prereq for each course as 0 initially
        
        # step 1. Populate adj_list and in_degree
        for course, prereq in prerequisites:
            if course not in adj_list[prereq]:
                adj_list[prereq].add(course)
                in_degree[course] += 1
        
        # step 2. We populate a queue with courses that do not have any prereqs
        # Then we do a BFS, and decrement the in_degree for the course once we process from the queue
        
        course_order = []
        
        queue = deque([course for course in in_degree if in_degree[course] == 0])
        while queue:
            # process course with zero prereqs and add to final order
            course = queue.popleft()
            course_order.append(course)
            
            # update adjacency list and in_degree
            for c in adj_list[course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:   #all prereqs for this course are processed, add to queue
                    queue.append(c)
                    
            # the number of courses in the ordered list must be equal to all numCourse
            # if not, means there was a cycle and ordering is not possible
        if len(course_order) < numCourses:
            return []
        
        return course_order