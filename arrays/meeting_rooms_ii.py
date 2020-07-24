'''
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/
'''


# Approach 1: Priority Queues
'''
Algorithm

1. Sort the given meetings by their start time.
2. Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
3. For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
4. If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
5. If not, then we allocate a new room and add it to the heap.
6. After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.
'''
import heapq
from typing import List

# Time Complexity is O(N log(N)) where N is the number of meetings
# Sorting is O(N log(N)) + O(N log(N)) for popping/pushing N items to the min-heap
# Space Complexity is O(N) if all meetings require a new room
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        # sort intervals by their start time
        intervals.sort(key=lambda x: x[0])
        
        # initialize a min-heap
        free_rooms = []
        
        # allocate a room for the first meeting
        # push the end time of this meeting onto heap
        heapq.heappush(free_rooms, intervals[0][1])
        
        for interval in intervals[1:]:
            
            if free_rooms[0] <= interval[0]:
                heapq.heappop(free_rooms)
                
            heapq.heappush(free_rooms, interval[1])
        
        return len(free_rooms)

# Approach 2: Chronological ordering
# We treat start and end times separately

# Time Complexity is O(N log(N)) because of sorting of two arrays
# Space Complexity is O(N) because we allocate 3 arrays of size at most N
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # no meetings, no rooms occupied
        if not intervals:
            return 0
        
        # separate lists for start and end times, the meeting pairs are no longer preserved
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        used_rooms = 0
        start_pointer = 0
        end_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < len(intervals):

            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_times[start_pointer] >= end_times[end_pointer]:
                # free up a room and increment the end_pointer
                used_rooms -= 1
                end_pointer += 1

            # We do this in any case, allocating a new room and progressing the start_pointer
            # previous check will guarantee that we are reusing rooms
            used_rooms += 1
            start_pointer += 1
        
        return used_rooms




