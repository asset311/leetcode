'''
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

from typing import List
# Time Complexity is O(nlog(n)) 
# Space Complexity is O(1) if we do not count the array for the result

# Step 1. Sort the array for adjacent intervals to be next to each other
# Step 2. Greedily merge intervals by looking at the last merged
def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Different more explicit implementation
def mergeIntervals(intervals):
    # allocate a new array to store new intervals
    intervals.sort()
    merged = [intervals[0]]
    # traverse the intervals, merging with the last one
    # intervals can be merged if a[1] >= b[0], then new interval c = [min(a[0],b[0]), max(a[1], b[1])]
    # otherwise add the new interval and proceed

    for interval in intervals[1:]:
        last_merged = merged[-1]
        if last_merged[1] >= interval[0]:
            merged[-1] = [min(last_merged[0], interval[0]), max(last_merged[1], interval[1])]
        else:
            merged.append(interval)
    
    return merged