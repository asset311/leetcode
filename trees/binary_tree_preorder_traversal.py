'''
144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/
'''

from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach 1: Recursive
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        def preorder(root):
            if not root:
                return
            
            result.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return result

# Approach 2: Iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        result = []
        if not root:
            return result
        
        stack = [root]
        while stack:
            root = stack.pop()
            result.append(root.val)
            
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return result

