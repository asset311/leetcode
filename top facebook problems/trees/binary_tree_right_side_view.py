'''
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List

# Approach 1: Level order tree traversal
# At each level select the last node on that level
# Time complexity is O(N) where N is the number of nodes
# Space complexity is O(D) where D is the diameter, for a complete binary tree would be N/2
def rightSideView(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    
    queue = deque()
    queue.append(root)
    output = []
            
    while queue:
        level_length = len(queue)   # count the number of nodes on this level
        
        for i in range(level_length):
            node = queue.popleft()
            if i == level_length - 1:   # if the last node on this level, add to output
                output.append(node.val)
            
            # add nodes on the next level to process in the next iteration
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return output
