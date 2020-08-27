'''
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        curr = self
        s = ''
        while curr:
            s += ' ' + str(curr.val)
            curr = curr.next
        return s

# Approach 1: O(N) time and space
# Convert to array, then use two pointers to determine if it is a palindrome
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        curr = head
        ll = []
        while curr:
            ll.append(curr.val)
            curr = curr.next
        
        left, right = 0, len(ll)-1
        while left < right:
            if ll[left] != ll[right]:
                return False
            left += 1
            right -= 1
        
        return True

# Approach 2: Reverse Second Half In-place
# Use fast and slow runners to find the middle
# Reverse the list in place
# Compare for being palindromes
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # step 1. Find middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow points to the middle of the original linked list
        
        # step 2. Reverse the right part of the linked list
        # prev will point to the head of the reversed part
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # step 3. Start from both lists and compare in sequence
        first, second = head, prev
        
        # the original list is longer, but it doesn't matter
        # since the reversed list will finish earlier
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
    
        return True


