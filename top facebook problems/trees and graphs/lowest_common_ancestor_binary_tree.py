'''
236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict, deque

# Brute-force approach by tracking all previously seen ancestors for each node
# Passes but takes too long, and actually returns a new node with the same value, and not the actual node
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        
        ancestor_map = defaultdict(list)
        
        def BFS(root):
            
            queue = deque()
            queue.append((root,[]))
            
            while queue:
                node, ancestors = queue.popleft()
                
                if node:
                    ancestors = ancestors + [node.val]
                    if node.val == p.val or node.val == q.val:
                        ancestor_map[node.val].extend(ancestors)
                    
                    queue.append((node.left, ancestors))
                    queue.append((node.right, ancestors))
            
        # step 1. BFS traversal
        BFS(root)
        
        # step 2. extract ancestors for the required nodes
        p_ancestors = ancestor_map[p.val]
        q_ancestors = ancestor_map[q.val]
        
        # step 3. get nodes to the same level
        if len(p_ancestors) != len(q_ancestors):
            if len(p_ancestors) < len(q_ancestors):
                for i in range(len(q_ancestors) - len(p_ancestors)):
                    q_ancestors.pop()
            else:
                for i in range(len(p_ancestors) - len(q_ancestors)):
                    p_ancestors.pop()
        
        while p_ancestors and q_ancestors:
            p_ancestor = p_ancestors.pop()
            q_ancestor = q_ancestors.pop()
            if p_ancestor == q_ancestor:
                return TreeNode(p_ancestor)
        
        return root

# Approach 1: Iterative by storing parent pointers
'''
Algorithm

Start from the root node and traverse the tree.
Until we find p and q both, keep storing the parent pointers in a dictionary.
Once we have found both p and q, we get all the ancestors for p using the parent dictionary and add to a set called ancestors.
Similarly, we traverse through ancestors for node q. 
If the ancestor is present in the ancestors set for p, this means this is the first ancestor common between p and q (while traversing upwards) and hence this is the LCA node.
'''
# Time Complexity : O(N), where N is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.
# Space Complexity : O(N). In the worst case space utilized by the stack, 
# the parent pointer dictionary and the ancestor set, would be N each, since the height of a skewed binary tree could be N.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]  # we'll be doing depth-first search
        parent = {root: None}   # dictionary node -> parent

        # traverse the tree until both p and q are found
        # for each node store it's parent in the dictionary 'parent'
        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # populate ancestors for p, at each point pointing back to previous node's parent
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        
        # the first node in q's ancestors that is found in the ancestors of p
        # is the LCA for p and q
        while q not in ancestors:
            q = parent[q]

        return q



        