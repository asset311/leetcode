

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def reorderList(self, head: ListNode) -> None:
    if not head:
        return head
    
    # find the middle of the list
    # in 1->2->3->4->5->6 find 4
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # slow points to the middle node now
    # reverse the second half of the list in-place
    # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    
    # merge two sorted lists 
    # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next


# A more explicit solution, non-pythonic
def reorderList(self, head: ListNode) -> None:		
        if not head or not head.next:
            return
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        slow.next = None
        prev = None
        while current:
            current_next = current.next
            current.next = prev
            prev = current
            current = current_next
        
        first = head
        second = prev
        while second:
            first_next = first.next
            first.next = second
            first = first_next
            
            second_next = second.next
            second.next = first
            second = second_next