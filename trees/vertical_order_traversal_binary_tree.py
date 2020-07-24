
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, OrderedDict
from collections import deque, defaultdict, OrderedDict

# Approach 1: DFS/BFS with global sorting
# We define a tuple (column, row, value)
# Sorting is performed when constructing the final answer

# Time complexity is dominated by sorting - O(Nlog(N))
# Space complexity is either queue in BFS or function call stack in DFS, which is also O(N)
def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    node_list = []  #tuples will be stored here after traversal

    # preorder traversal
    def DFS(node, row, column):
        if node:
            node_list.append((column, row, node.val))
            DFS(node.left, row + 1, column - 1)
            DFS(node.right, row + 1, column + 1)

    # step 1 - construct the node list, with coordinates
    # we assume root is at (0,0)
    DFS(root, 0, 0)

    # step 2 - sort the node list globally, according to the coordinates
    node_list.sort()

    # step 3 - retrieve the sorted results, grouped by the column index
    # need to track column by column
    output = []
    current_column_index = node_list[0][0]
    current_column = []
    for column, row, value in node_list:
        if column == current_column_index:
            # append to the same column sub-array
            current_column.append(value)
        else:
            # we're done withe column, append to results
            output.append(current_column)
            # start the new column sub-array
            current_column_index = column
            current_column = [value]
    
    # add the very last column
    output.append(current_column)

    return output


def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    node_list = []

    def BFS(root):
        queue = deque()
        queue.append((root, 0, 0))
        while queue:
            node, row, column = queue.popleft()
            if node:
                node_list.append((column, row, node.val))
                queue.append((node.left, row + 1, column - 1))
                queue.append((node.right, row + 1, column + 1 ))
        
    # step 1 - construct the node list with coordinates
    BFS(root)

    # step 2 - sort the node list according to coordinates
    node_list.sort()

    # step 3 - retrive sorted results partitioned by columns
    # use an ordered dictionary for keys
    output = OrderedDict()
    for column, row, value in node_list:
        if not column in output:
            output[column] = [value]
        else:
            output[column] = output[column] + [value]
    
    return output.values()



# Approach 2: BFS/DFS with partition sorting
# instead of doing a global sort, only sort at each row level
# since we sort within columns, it is local and the overall sorting complexity is reduced
# Time Complexity is O(N log(N/k)) where k is the width of the tree (or number of columns in this case)
# Space Complexity is O(N) to store all the nodes info

def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    
    # use default dict that will return empty list, instead of KeyError if not present
    columnTable = defaultdict(list)
    min_column = max_column = 0     #we'll use later to traverse columns in order

    def BFS(root):
        nonlocal min_column, max_column
        queue = deque()
        queue.append((root, 0, 0))

        while queue:
            node, row, column = queue.popleft()
            if node:
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, row + 1, column - 1))
                queue.append((node.right, row + 1, column + 1))

    # step 1. BFS traversal
    BFS(root)

    # extract values from columnTable
    output = []
    for col in range(min_column, max_column+1):
        # sort by row, then by value
        output.append([val for row, val in sorted(columnTable[col])])
    
    return output

def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    
    # use default dict that will return empty list, instead of KeyError if not present
    columnTable = defaultdict(list)
    min_column = max_column = 0

    def DFS(node, row: int, column: int):
        if not node:
            return
        
        nonlocal min_column, max_column
        columnTable[column].append((row, node.val))
        min_column = min(min_column, column)
        max_column = max(max_column, column)

        DFS(node.left, row + 1, column - 1)
        DFS(node.right, row + 1, column + 1)
    
    # step 1. DFS traversal
    DFS(root, 0, 0)

    # extract values from columnTable
    output = []
    for col in range(min_column, max_column + 1):
        # sort by row, then by value
        output.append([val for row, val in sorted(columnTable[col])])
    
    return output



# This solution only partially solves the problem
# Solves for vertical traversal without level sorting
def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    
    def DFS(root, x, axis_map):
        if not root:
            return
        
        if x not in axis_map:
            axis_map[x] = [root.val]
        else:
            axis_map[x] = axis_map[x] + [root.val]
        
        if root.left:
            DFS(root.left, x-1, axis_map)
        if root.right:
            DFS(root.right, x+1, axis_map)
        
        return axis_map
    
    x = 0
    axis_map = DFS(root, x, dict())
    axis = sorted(axis_map.keys())
    
    output = []
    for x in axis:
        output.append(axis_map[x])
    
    return output