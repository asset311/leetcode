'''
543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        diam = 0
        def depth(root):
            nonlocal diam
            
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            # diameter so far
            diam = max(diam, left + right)
            
            # depth
            return max(left, right) + 1
        
        depth(root)
        return diam