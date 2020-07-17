'''
252. Meeting Rooms
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
'''

# Sort the meetings by start time. Then traverse meetings one by one, and check if one meeting ends after the next one begins.

from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key = lambda x: x[0])    #regular sort will do it anyways, but just making sure
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True