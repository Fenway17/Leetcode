"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            # no head given
            return
        
        nodes = []
        nodes.append(head)

        # record all nodes
        next_node = head.next
        while next_node:
            # next node exists
            nodes.append(next_node)
            next_node = next_node.next

        # use 2 pointers
        i = 0
        j = len(nodes)-1
        left = True
        while i < j:
            if left:
                nodes[i].next = nodes[j]
                i += 1
                left = False
            else: # right
                nodes[j].next = nodes[i]
                j -= 1
                left = True

        # point last node to None
        nodes[i].next = None
