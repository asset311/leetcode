'''
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: Recursive - divide and conquer
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1

# Approach 2: Recursive DFS (preorder)
# preorder because at each node we calculate if the depth at this node is larger than the global maxdepth so far
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0

        def preorder(root, curr_depth):
            nonlocal depth
            if not root:
                return
            
            depth = max(depth, curr_depth)

            preorder(root.left, curr_depth+1)
            preorder(root.right, curr_depth+1)
        
        preorder(root, 1)
        return depth

