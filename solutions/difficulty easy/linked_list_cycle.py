"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            # empty list
            return False

        slow_node = head
        fast_node = head.next
        if fast_node == None:
            # reached end, no loop
            return False

        while slow_node != fast_node:
            # increment fast twice, slow once
            # if loop exists, fast will reach slow at some point
            fast_node = fast_node.next
            if fast_node == None:
                return False
            
            fast_node = fast_node.next
            if fast_node == None:
                return False

            slow_node = slow_node.next
        
        # loop found
        return True

        