'''
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.
'''

# First solution is to do an inorder traversal of the whole tree to construct an array
# Then just sum the elements in the array in the range

def rangeSumBST(root: TreeNode, L: int, R: int) -> int:
        
    def traverseInorder(root):
        if not root:
            return []
        return traverseInorder(root.left) + [root.val] + traverseInorder(root.right)
        
    arr = traverseInorder(root)
    sum_ = 0
        
    for elem in arr:
        if L <= elem <= R:
            sum_ += elem
        
    return sum_


# do a depth-first search using BST property
# Average: O(log(n)) time | O(log(n)) space
# Worst:   O(n) time      | O(n) space
def rangeSumBST(root: TreeNode, L: int, R: int) -> int:
    ans = 0
    stack = [self]

    while stack:
        node = stack.pop()
        if node:
            if L <= node.val <= R:
                ans += node.val
            elif L < node.val:
                stack.append(node.left)
            elif node.val < R:
                stack.append(node.right)
    return ans
