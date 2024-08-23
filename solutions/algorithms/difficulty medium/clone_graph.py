"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. 
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. 
You must return the copy of the given node as a reference to the cloned graph.
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        # start by creating an adjacency dict to be used to create deep copy
        adj_dict = {} # each element list represents a node and inside it its neightbors
        queue = deque() # deque() is a queue with append and pops for left or right
        queue.append(node)
        while queue: # while queue is not empty
            current_node = queue.popleft() # pop() is for the right side
            if adj_dict.get(current_node.val, None) == None:
                # new node encountered
                adj_dict[current_node.val] = [] # add node to adj list
                for neighbor in current_node.neighbors:
                    adj_dict[current_node.val].append(neighbor.val) # add val to adj list
                    if adj_dict.get(neighbor.val, None) == None:
                        # new next node
                        queue.append(neighbor)
        
        # recreate graph with adjacency list
        node_dict = {}
        # initialize nodes without neighbors
        for key_val, value_list in adj_dict.items():
            node_dict[key_val] = Node(val = key_val)
        # insert neighbors
        for key_val, value_list in adj_dict.items():
            neighbors_list = []
            for neighbor_val in value_list:
                neighbors_list.append(node_dict[neighbor_val])
            node_dict[key_val].neighbors = neighbors_list
        
        return node_dict[node.val]