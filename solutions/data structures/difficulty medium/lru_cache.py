"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
    Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""

class LRUCache:
    # Node to be used in a doubly linked list to check for LRU
    class Node:
        def __init__(self, key: int, value: int, next_node = None, prev_node = None):
            self.key = key
            self.value = value
            self.next_node = next_node
            self.prev_node = prev_node

    # approach: dict has key: int and value: Node, with doubly linked list to check for LRU
    def __init__(self, capacity: int):
        self.capacity = capacity # always >= 1
        self.dict = {} # stores key value pairs
        self.head = self.Node(-1, -1) # start of list
        self.tail = self.Node(-1, -1) # end of list
        # link head and tail
        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    # helper method for nodes
    def remove_node(self, node):
        # link node's sides together
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node
    
    # helper method for nodes
    def add_node_to_head(self, node):
        # link node to front of list
        node.next_node = self.head.next_node
        node.prev_node = self.head
        # relink sides of node
        self.head.next_node.prev_node = node
        self.head.next_node = node

    def get(self, key: int) -> int:
        if key in self.dict:
            # update LRU cache
            node = self.dict[key]
            self.remove_node(node)
            self.add_node_to_head(node)
            return node.value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        # key always >= 0, value always >= 0
        if key in self.dict:
            node = self.dict[key]
            node.value = value # update node's value
            # update LRU cache
            self.remove_node(node)
            self.add_node_to_head(node)
        else: # new key
            # check capacity
            if self.capacity > 0:
                self.capacity -= 1
                
            else: # no capacity
                # remove LRU item from list
                node_to_remove = self.tail.prev_node
                self.remove_node(node_to_remove)
                # remove LRU from dict
                self.dict.pop(node_to_remove.key)

            # insert new node into start of list
            new_node = self.Node(key, value)
            self.add_node_to_head(new_node)
            
            # insert new key
            self.dict[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)