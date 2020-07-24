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

# combine height and status into one via a named tuple
# at each point we need to know the subtrees height, and whether it is balanced
from collections import namedtuple
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        NodeWithHeightAndBalancedStatus = namedtuple('NodeWithHeightAndBalancedStatus', 'is_balanced height')

        def check_balanced(root):
            # if at the leaf, it is balanced and it's height is -1
            if not root:
                return NodeWithHeightAndBalancedStatus(True, -1)
            
            # check left subtree
            left_result = check_balanced(root.left)
            if not left_result.is_balanced:
                return NodeWithHeightAndBalancedStatus(False, 0)
            
            # check right subtree
            right_result = check_balanced(root.right)
            if not right_result.is_balanced:
                return NodeWithHeightAndBalancedStatus(False, 0)
            
            # if both subtrees are balanced, then this node is only balanced
            # if the difference between subtree heights is at most one
            height = 1 + max(left_result.height, right_result.height)
            is_balanced = abs(left_result.height - right_result.height) <= 1

            return NodeWithHeightAndBalancedStatus(is_balanced, height)
        
        return check_balanced(root).is_balanced