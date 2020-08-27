'''
114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
'''

# Approach 1: Do a preorder traversal, and then update the original tree
# Not exactly in place, but A solution.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return root
        
        if not root.left and not root.right:
            return root
        
        tree = self.preorder(root)
        
        for node in tree:
            root.right = node
            root.left = None
            root = root.right
            
        
    def preorder(self, root: TreeNode) -> List[TreeNode]:
        result = []
        
        def dfs(root):
            if not root:
                return
            result.append(root)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return result

# Approach 2: Recursive solution that modifies nodes in-place
class Solution:
    def flatten(self, root: TreeNode) -> None:
        self.flattenTree(root)
    
    def flattenTree(self, node: TreeNode):
        # base case 1 - null node
        if not node:
            return node
        
        # base case 2 - left node, just return node itself
        if not node.left and not node.right:
            return node
        
        # recursively flatten left subtree
        leftTail = self.flattenTree(node.left)

        # recursively flatten right subtree
        rightTail = self.flattenTree(node.right)

        # rewire the tree only if there is a left subtree
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        
        # need to return the rightmost node after rewiring
        return rightTail if rightTail else leftTail
'''
Time Complexity: O(N) since we process each node of the tree exactly once.
Space Complexity: O(N) which is occupied by the recursion stack. 
The problem statement doesn't mention anything about the tree being balanced or not and hence, 
the tree could be e.g. left skewed and in that case the longest branch (and hence the number of nodes in the recursion stack) would be NN.
'''



