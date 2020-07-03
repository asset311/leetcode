'''
270. Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
'''

# Approach is very similar to trying to insert a value into a BST
# Keep track of the closest value as you traverse the left or right subtree, based on target and current node
# As you traverse, keep updating closest if you see a closer distance
def closestValue(self, root: TreeNode, target: float) -> int:
    current = root
    closest = current.val
    
    while current:
        if abs(target - closest) > abs(target - current.val):
            closest = current.val
        if target < current.val:
            current = current.left
        elif target > current.val:
            current = current.right
        else:
            break
    return closest