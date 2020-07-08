

# Time complexity is O(m+n) where m and n are number of elements in lists
# Space is O(m+n) - the resulting list is at most m+n+1 (if there is carry in the end)
def addTwoNumbers(self, a: ListNode, b: ListNode) -> ListNode:
    p = a
    q = b
    ans = dummy_head = ListNode(0)
    carry = 0

    while p or q:   # keep traversing until either of the lists are empty (that's how to deal with non-conformant lists)
        x = p.val if p else 0
        y = q.val if q else 0
        
        sum_ = x + y + carry
        carry = sum_ // 10

        ans.next = ListNode(sum_ % 10)
        ans = ans.next
        
        p = p.next if p else None
        q = q.next if q else None

    if carry:
        ans.next = ListNode(carry)

    return dummy_head.next  #notice that we poin initially to a 0-node, so return next