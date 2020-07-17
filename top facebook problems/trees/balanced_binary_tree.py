# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # computes tree height via recursion
    def height(self, root):
        # An empty tree has height -1
        if not root:
            return -1
            
        lheight = self.height(root.left)
        rheight = self.height(root.right)
            
        return 1 + max(lheight, rheight)    
    
    def isBalanced(self, root: TreeNode) -> bool:
        
        # an empty tree is a balanced tree
        if not root:
            return True
        
        # check if subtrees have height within 1
        # if they do, check if subtrees are balanced
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)