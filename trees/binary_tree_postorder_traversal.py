'''
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/
'''
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach 1: Recursive
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        def postorder(root):
            if not root:
                return
            
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)
        
        postorder(root)
        return result

