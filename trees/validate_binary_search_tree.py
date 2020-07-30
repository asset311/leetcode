'''
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach 1: recursive
# Time is O(N) where N is the number of nodes
# Space is O(N) as there will be N calls onto the function call stack
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min_value = -float('inf')
        max_value = float('inf')
        
        def bstChecker(root, min_value, max_value):
            if not root:
                return True
            
            # divide
            left_tree = root.left
            right_tree = root.right
            
            # conquer
            # this checks
            # The left subtree of a node contains only nodes with keys less than the node's key.
            # The right subtree of a node contains only nodes with keys greater than the node's key.
            if (root.val >= max_value) or (root.val <= min_value):
                return False
            
            # combine
            # finally checks that both subtrees are BST
            return all([bstChecker(left_tree, min_value, root.val),
                       bstChecker(right_tree, root.val, max_value)])
        
        return bstChecker(root, min_value, max_value)


# Approach 2: Iterative, the same principle
# Time is O(N)
# Space is O(N) as we still need to maintain a stack of all the nodes to visit
def isValidBST(self, root: TreeNode) -> bool:
    # empty tree is a valid BST
    if not root:
            return True

    #instead of using a function call stack, we design our own
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    # preorder traversal
    while node_and_bounds_stack:
        node, min_value, max_value = node_and_bounds_stack.pop()
        
        if (node.val <= min_value) or (node.val >= max_value):
            return False
        
        if node.right:
            node_and_bounds_stack.append( (node.right, node.val, max_value) )

        if node.left:
            node_and_bounds_stack.append( (node.left, min_value, node.val) )
    
    return True


# Approach 3: Inorder traversal - the most efficient out of all three
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        stack = []
        prev = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if prev and root.val <= prev.val:
                return False
            
            prev = root
            root = root.right

        return True