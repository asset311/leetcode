class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


# Approach 1: Recursive solution, treating the linked list as a graph with potential cycles
class Solution(object):

    def __init__(self):
        self.copiedHash = {}


    def copyRandomList(self, head):

        # base case for recursion
        if not head:
            return
        
        # check if the node was already copied
        if head in self.copiedHash:
            return self.copiedHash[head]
        
        # otherwise make a new node copying the value
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.copiedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

# Approach 2: Iterative with O(N) space
# Time Complexity : O(N) because we make one pass over the original linked list.
# Space Complexity: O(N) to hold references to already visited nodes
class Solution(object):
    def __init__(self):
        self.visitedHash = {}
    
    def getClonedNode(self, node:Node) -> Node:
        # if node exists, it has either been already cloned or needs to be cloned
        if node:
            # the has already been copied, return a reference to it
            if node in self.visitedHash:
                return self.visitedHash[node]
            else:
                self.visitedHash[node] = Node(node.val, None, None)
                return self.visitedHash[node]
        
        return
    
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head
        
        # create a new head node
        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visitedHash[old_node] = new_node

        # iterate through the linked list until we reach null
        while old_node:

            # Get the clones of the nodes referenced by random and next pointers.
            new_node.next = self.getClonedNode(old_node.next)
            new_node.random = self.getClonedNode(old_node.random)

            old_node = old_node.next
            new_node = new_node.next
        
        # return the head of the newly cloned linked list
        return self.visitedHash[head]
