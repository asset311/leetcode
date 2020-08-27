'''
LRU Cache
https://leetcode.com/problems/lru-cache
'''

# The main idea is to use dictionary: key -> node
# Node contains: key -> value
# Nodes are constructed into doubly-linked list, so that they can remove themselves

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0,0)   # dummy head
        self.tail = Node(0,0)   # dummy tail
        self.head.next = self.tail  #initially connected head -> tail, head <- tail
        self.tail.prev = self.head
    

    def get(self, key):
        # remove and insert itself
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        # check if key is present
        if key in self.dic:
            self._remove(self.dic[key])

        # create a node, and add to chain
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n

        # check if anything needs to be evicted
        # LRU is always pointed to by the head
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    # a node can remove itself
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    # a node can add itself to the tail
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
