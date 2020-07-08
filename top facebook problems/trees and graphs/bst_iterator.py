'''
173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


# Approach 1: Flattening the BST
# The idea is based is that an iterator operates on something like a list or an array.
# An important property of the binary search tree is that the inorder traversal of a BST gives us the elements in a sorted order.
class BSTIterator:

    def __init__(self, root:TreeNode):
        self.nodes = self._inorder(root)    #array containing all the nodes in a sorted order
        self.i = 0                              #an index that will allow us to keep record of where the iterator is

    def _inorder(self, root):
        if not root:
            return []
        return self._inorder(root.left) + [root.val] + self._inorder(root.right)
    
    def next(self) -> int:
        if self.i < len(self.nodes):
            result = self.nodes[self.i]
            self.i += 1
            return result
        else:
            raise StopIteration
    
    def hasNext(self) -> bool:
        return self.i < len(self.nodes)

# Time complexity is O(N) where N is the number of nodes. It is the time taken to initialize the iterator object
# next() is O(1)
# hasNext() is O(1)

# Space complexity is O(N+h), where O(h) is the space required for the recursive function.
# This does not meet the requirements of the problem, where we need O(h)
# h - height of the tree, for a balanced tree is usually log(N) 



# Approach 2: Use custom stack to control the recursion
# When the iterator is initialized, it will traverse all nodes to the left until leaf - this will be space O(h)
# The stack will maintain the next smallest element, but after we pop it, next() function would need to check if 
# right subtree exists, and will then call to populate stack with the right subtrees left brach.
# We do iterative inorder traversal

class BSTIterator:

    def __init__(self, root: TreeNode):
        # stack for the recursion simulation
        self.stack = []

        # the object will initialize with the left subtree
        self._leftmost_inorder(root)

    # helper function to populate the stack
    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left
    
    # simply needs to check if the stack has any nodes
    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def next(self) -> int:
        # node at the top is the next smallest element
        top_most_node = self.stack.pop()

        # need to maintain the invariant.
        # if the node has a right child, call the helper function for the right child
        if top_most_node.right:
            self._leftmost_inorder(top_most_node.right)
        
        return top_most_node.val


















# Tests
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

iterator = BSTIterator(root)
