'''
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
'''
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

import math

# Time is O(N)
# Space is O(1)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        current = head
        n = 0
        while current:
            current = current.next
            n += 1
        
        middle = n // 2
        
        current = head
        count = 0
        while count < middle:
            current = current.next
            count += 1
        
        return current

# Time is O(N) but in reality twice as fast as the first solution
# Space is O(1)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# Time is O(N)
# Space is O(N)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]


