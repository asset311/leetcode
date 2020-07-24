'''
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        max_path = -float('inf')    # the lowest possible number

        def max_gain(node):
            nonlocal max_path       # reference the outer max_path var

            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)     # include 0 to handle negative values in subtrees
            right_gain = max(max_gain(node.right), 0)   

            # path involving this node as the root
            current_max_path =  node.val + left_gain + right_gain
            
            # this current path with node as root might be larger than previous, record it
            max_path = max(max_path, current_max_path)

            # can only return a path, not a subtree
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)  # kick off the recursion chain
        return max_path


