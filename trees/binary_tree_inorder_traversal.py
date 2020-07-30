'''
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
'''
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach 1: Recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        result = []
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return result

# Approach 2: Iterative
'''
While left exists, try going left
If no more left available, try going right by picking the topmost in stack
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        result = []
        if not root:
            return result

        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            result.append(root.val)

            # if there is right subtree, next iteration will push all left nodes on the right subtree
            # if there is no right subtree, next iteration will pick from top of the stack
            root = root.right 

        return result  
