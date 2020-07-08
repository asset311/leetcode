'''
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach 1: create a new linked list
# Time is O(m+n) where m, n are list lengths
# Space is O(m+n) since we create a new list
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    p = l1
    q = l2
    dummy_head = ListNode(0)
    curr = dummy_head
    
    while p or q:
        if not p:
            curr.next = ListNode(q.val)
            q = q.next
        elif not q:
            curr.next = ListNode(p.val)
            p = p.next
        else:
            if p.val < q.val:
                curr.next = ListNode(p.val)
                p = p.next
            else:
                curr.next = ListNode(q.val)
                q = q.next
        curr = curr.next
        
    return dummy_head.next

# Approach 2: update one of the lists in-place - very similar logic to Approach 1, but in-place
# Time is O(m+n) where m, n are list lengths
# Space is O(1) we only created one additional node
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    # maintain an unchanging reference to node ahead of the return node.
    prehead = ListNode(-1)

    #prev always points to the previous node
    prev = prehead
    while l1 and l2:
        if l1.val < l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next

        prev = prev.next
    
    prev.next = l1 if not l1 else l2

    # exactly one of l1 and l2 can be non-null at this point, so connect
    # the non-null list to the end of the merged list.
    return prehead.next
