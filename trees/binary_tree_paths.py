'''
257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/
'''
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach 1: Recursion, preorder DFS
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def helper(root, path):
            if not root:
                return
            
            path += str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            else:
                path += '->'
                helper(root.left, path)
                helper(root.right, path)
        
        paths = []
        helper(root, '')
        return paths   

# Approach 2: Iterative, DFS preorder
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        
        return paths  
