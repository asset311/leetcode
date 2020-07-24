class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        head = self
        s = ''
        while head:
            s += ' ' + str(str(head.val))
            head = head.next
        return s

