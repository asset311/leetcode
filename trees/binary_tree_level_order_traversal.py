'''
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
Each level needs to be in its own subarray
'''

# Approach 1: Iterative BFS
# We use a queue to maintain the nodes that are inserted level by level
# The trick is to determine what level we are currently reading, which is where we use inner loop

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import List

def levelOrder(root: TreeNode) -> List[List[int]]:
    
    levels = []     # the level to hold nodes level by level
    if not root:
        return levels
    
    queue = collections.deque()
    queue.append(root)
    level = 0

    while queue:
        # start a current level
        levels.append([])
        # number of elements in the current level (queue length at this iteration)
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()
            # add to the current level
            levels[level].append(node.val)

            # add child nodes of the current level
            # in the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # go to next level
        level += 1
    
    return levels   


    
