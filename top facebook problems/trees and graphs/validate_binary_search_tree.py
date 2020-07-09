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
def isValidBST(self, root: TreeNode) -> bool:
    
    lower_bound = -float('inf')
    upper_bound = float('inf')
    
    def is_valid_bst(root, lower_bound, upper_bound):
        if not root:
            return True
        
        if (root.val <= lower_bound) or (root.val >= upper_bound):
            return False
        
        return is_valid_bst(root.left, lower_bound, root.val) and is_valid_bst(root.right, root.val, upper_bound)
    
    return is_valid_bst(root, lower_bound, upper_bound)


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
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()
        
        if (node.val <= lower_bound) or (node.val >= upper_bound):
            return False
        
        if node.right:
            node_and_bounds_stack.append( (node.right, node.val, upper_bound) )

        if node.left:
            node_and_bounds_stack.append( (node.left, lower_bound, node.val) )
    
    return True
