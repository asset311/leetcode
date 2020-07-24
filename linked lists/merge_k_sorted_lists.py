'''
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
from functools import reduce
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach 0: brute force - convert to array, and generate a new linked list
#Time complexity : O(Nlog N) where NN is the total number of nodes.
#Collecting all the values costs O(N) time.
#A stable sorting algorithm costs O(Nlog N) time.
#Iterating for creating the linked list costs O(N) time.

#Space complexity : O(N).
#Sorting cost O(N) space (depends on the algorithm you choose).
#Creating a new linked list costs O(N) space.

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = point = ListNode(0)
        nodes = []

        # populate the array
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        
        nodes.sort()
        for x in nodes:
            point.next = ListNode(x)
            point = point.next
        
        return head.next

# Approach 1: use function folding, or reduce
# The complexity is O(kN) where k is the number of linked lists.
# Function folding takes a long time, so would need to implement iteratively
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if not lists:
            return
        
        def mergeTwoSortedLists(l1: ListNode, l2: ListNode) -> ListNode:
            
            if not l1 and not l2:
                return
            
            if not l1 or not l2:
                return l1 if l1 else l2
            
            prehead = ListNode(-1)
            prev = prehead
            
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next
            
            prev.next = l1 if l1 else l2
            return prehead.next
        
        return reduce(mergeTwoSortedLists, lists)


# Approach 2: Merge with Divide And Conquer
# The idea is to pair up k lists and merge each pair.
# Then iteratively merge the lists - the main trick is to figure out how to backtrack on merging
# Time Complexity is O(N log(k)) where k is the number of lists
# Merging two sorted lists is O(N) and we do it log(k) times
# Space complexity is O(1)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def mergeTwoSortedLists(l1: ListNode, l2: ListNode) -> ListNode:
            prev = prehead = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next
            prev.next = l1 if l1 else l2
            
            return prehead.next
        
        
        amount = len(lists)
        interval = 1
        
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = mergeTwoSortedLists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0] if amount > 0 else lists