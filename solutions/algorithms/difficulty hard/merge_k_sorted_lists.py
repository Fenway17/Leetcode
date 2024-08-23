"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

# list contains head of ListNodes!
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        # merge 2 lists at a time until one list is left
        while len(lists) > 1:
            # at least 2 items in lists
            first_node = lists.pop()
            second_node = lists.pop()

            # record order of items
            result = ListNode()
            node = result
            while first_node and second_node:
                if first_node.val <= second_node.val:
                    node.next = first_node # insert node
                    first_node = first_node.next # iterate first
                    node = node.next # iterate result node
                else: # first > second
                    node.next = second_node
                    second_node = second_node.next
                    node = node.next
           
            # check for residual nodes to insert
            if first_node:
                node.next = first_node
            if second_node:
                node.next = second_node

            # input into lists
            lists.append(result.next)
        
        # return final list
        if lists: 
            # non-empty lists
            return lists[0]
        else: 
            return None
