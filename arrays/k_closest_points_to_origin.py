'''
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
'''

import math
from typing import List

# Approach 1: Use a custom sort function to sort points on the plane based on their distance to origin
# Time is O(nlog(n)) in the best case for sorting
# Space is O(1) - all modifications are in-place
def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    def euclid(point):
        return math.sqrt(point[0]**2 + point[1]**2)
    
    points.sort(key=euclid)
    return points[:K]

# Approach 2: Use a heap
# Time is O(N log(K))
# Space is O(K) to store K elements
import heapq as hq
def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    if not K:
        return []
    
    q = [(x**2 + y**2, [x,y]) for x, y in points]

    # no need to heapify prior
    return list(map(lambda x:x[1], hq.nsmallest(K, q)))


