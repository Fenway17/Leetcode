"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        # record nodes visited
        visited = []
        current = head
        while current:
            visited.append(current)
            current = current.next

        # remove node; node to remove is at index len(visited)-n
        previous_node = None # could be None
        if len(visited)-n-1 >= 0:
            previous_node = visited[len(visited)-n-1]
        next_node = visited[len(visited)-n].next # could be None
        if previous_node:
            # always link it to next node; could be None
            previous_node.next = next_node
        else: # no previous node
            # node to remove is the first node at head
            return next_node

        return head