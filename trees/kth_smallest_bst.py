'''
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

# Recursive solution
# Inorder traversal of BST gives sorted list
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        # inorder traversal
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -=1
            if k == 0:
                return root.val
            
            root = root.right


## RECURSIVE SOLUTION ##
## inorder search on BST will give sorted list ##
def inorder(root):
    if not root:
        return []
    else:
         return inorder(root.left) + [root.val] + inorder(root.right)

    return inorder(root)[k-1]