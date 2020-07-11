
'''
621. Task Scheduler
https://leetcode.com/problems/task-scheduler/

'''
from typing import List
from collections import Counter


# Approach 1: Greedy scheduling of most frequent tasks
# Time complexity is O(N) where N is the number of tasks - to create an array
# O(1) sorting the array, which is at most 26 characters (doesn't depend on input)
# Space complexity is O(1) - we store an array of at most 26 slots
def leastInterval(tasks: List[str], n: int) -> int:
    tasks_counter = Counter(tasks)
    frequencies = sorted(tasks_counter.values())  # frequencies of tasks in descending order

    # max frequency
    f_max = frequencies.pop()
    idle_time = (f_max - 1) * n # think of A I I A I I A I I A I I A ... = 8

    while frequencies and idle_time >0:
        idle_time -= min(f_max - 1, frequencies.pop())
    idle_time = max(idle_time, 0)

    return idle_time + len(tasks)

# Approach 2: Mathematically calculate the number of cycles
# The most frequent task is not frequent enough to force the presence of idle slots.
# OR The most frequent task is frequent enough to force some idle slots.

# There are (f_max -1) groups of executing the most frequent task where we have idle times
# Each group has execution of the task + cooling period

def leastInterval(tasks: List[str], n: int) -> int:
    tasks_counter = Counter(tasks)
    frequencies = sorted(tasks_counter.values())

    # max frequency
    f_max = frequencies.pop()

    # count the most frequent tasks
    n_max = frequencies.count(f_max)

    return max(len(tasks), (f_max-1)*(n+1) + n_max)