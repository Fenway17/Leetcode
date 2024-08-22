"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        # record order of nodes
        final_order = []
        current_node_1 = list1
        current_node_2 = list2
        while True:
            # check node values to order them
            if current_node_1.val <= current_node_2.val:
                final_order.append(current_node_1)
                current_node_1 = current_node_1.next
                # account for reaching end of one node list
                if not current_node_1:
                    final_order.append(current_node_2)
                    break

            else: # node 1 > node 2
                final_order.append(current_node_2)
                current_node_2 = current_node_2.next
                # account for reaching end of one node list
                if not current_node_2:
                    final_order.append(current_node_1)
                    break
        
        # create final linked node list
        final_head = final_order[0]
        for index, node in enumerate(final_order):
            if index+1 < len(final_order):
                node.next = final_order[index+1]

        return final_head