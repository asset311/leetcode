'''
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list

Reverse a singly linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach 1: use a stack 
# Time is O(n) since we traverse the whole list
# Space is O(n) for stack to keep all the nodes
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        stack = []
        
        ptr = head
        while ptr.next:
            stack.append(ptr)
            ptr = ptr.next
        
        new_head = ptr
        
        while stack:
            ptr.next = stack.pop()
            ptr = ptr.next
        ptr.next = None
        
        return new_head

# Approach 2: replace pointers in-place
# Time is O(n)
# Space is O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev

# Approach 3: recursive
# Time is O(n)
# Space is O(n) for the function call stack
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head