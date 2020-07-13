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

# Time complexity is O(nlog(n)) because of sorting, the rest is O(n)
# Space is O(n) for the new array + O(1) for a variable
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
    if len(intervals) == 0:
        return intervals
    
    answer = []
    intervals.sort()
    prev_merged = intervals[0]

    for i in range(1,len(intervals)):
        if prev_merged[1] >= intervals[i][0]:
            prev_merged[1] = max(prev_merged[1], intervals[i][1])
        else:
            answer.append(prev_merged)
            prev_merged = intervals[i]
    answer.append(prev_merged)

    return answer


# Cleaner code without creating an additional variable
# Time is O(nlog(n)) and space is O(1) because we aren't creating a new sorted array
def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged