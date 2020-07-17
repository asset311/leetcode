'''
297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Approach 1: Use DFS
# Time Complexity is O(N) as we traverse all nodes of the tree
# Space Complexity is O(N) because of function call stack storing for each node
from collections import deque
class Codec:

    def serialize(self, root):
        
        def rserialize(root, string):
            if not root:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')
    
    def deserialize(self, data):
        index = 0
        def rdeserialize(l):
            nonlocal index

            if l[index] == 'None':
                index += 1
                return
            
            root = TreeNode(l[index])
            index += 1
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)

            return root
        l = data.split(',')
        return rdeserialize(l)

# Approach 2: Use BFS
# Time Complexity is O(N)
# Space Complexity is O(N) for the queue in both cases
class Codec:

    def serialize(self, root):
        
        if not root:
            return ''
        
        queue = deque()
        queue.append(root)
        string = ''
        while queue:
            node = queue.popleft()
            if not node:
                string += 'None,'
                continue
            string += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
        
        return string
    
    def deserialize(data):
        if not data:
            return None
        
        l = data.split(',')
        root = TreeNode(int(l[0]))
        i = 1

        queue = deque()
        queue.append(root)

        while queue and i<len(l):
            node = queue.popleft()
            if l[i] != 'None':
                left = TreeNode(int(l[i]))
                node.left = left
                queue.append(left)
            i += 1
            if l[i] != 'None':
                right = TreeNode(int(l[i]))
                node.right = right
                queue.append(right)
            i += 1
        
        return root

