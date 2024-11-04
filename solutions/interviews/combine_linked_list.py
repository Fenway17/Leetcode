# You are given the head of a linked list, which contains a series of integers separated by 0's. 
# The beginning and end of the linked list will have Node.val == 0.

# For every two consecutive 0's, merge all the nodes lying in between them into a single node 
# whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

# Return the head of the modified linked list.

# Example 1:
# Input: head = [0,3,1,0,4,5,2,0]
# Output: [4,11]
# Explanation: 
# - The sum of the nodes between the 1st 0 and the 2nd 0 is: 3 + 1 = 4.
# - The sum of the nodes between the 2nd 0 and 3rd 0 is : 4 + 5 + 2 = 11.

# Example 2:
# Input: head = [0,1,0,3,0,2,2,0]
# Output: [1,3,4]
# Explanation: 
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 1 = 1.
# - The sum of the nodes marked in red: 3 = 3.
# - The sum of the nodes marked in yellow: 2 + 2 = 4.
 
# Constraints:
# The number of nodes in the list is in the range [3, 2 * 105].
# 0 <= Node.val <= 1000
# There are no two consecutive nodes with Node.val == 0.
# The beginning and end of the linked list have Node.val == 0.

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node
    
def combineLinkedList(linked_list_node):
    result_head = Node(-1)
    current_result = result_head

    # go through the linked list
    current = linked_list_node
    new_value = 0
    while (current != None):
        current_value = current.value
        
        # check if 0
        if current_value == 0:
            # check if new node can be created
            if new_value != 0:
                # create new node
                new_node = Node(new_value)

                # add it into result
                current_result.next = new_node
                current_result = current_result.next
                
                # reset new_value to 0
                new_value = 0
        else: 
            # add to new value
            new_value += current_value

        current = current.next

    return result_head.next

# Input: head = [0,3,1,0,4,5,2,0]
# Output: [4,11]
# Explanation: 
# - The sum of the nodes between the 1st 0 and the 2nd 0 is: 3 + 1 = 4.
# - The sum of the nodes between the 2nd 0 and 3rd 0 is : 4 + 5 + 2 = 11.

print("Example 1")

linked_list = Node(0, Node(3, Node(1, Node(0, Node(4, Node(5, Node(2, Node(0))))))))
new_linked_list = combineLinkedList(linked_list)

while new_linked_list != None:
    print(new_linked_list.value)
    new_linked_list = new_linked_list.next

# Input: head = [0,1,0,3,0,2,2,0]
# Output: [1,3,4]
# Explanation: 
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 1 = 1.
# - The sum of the nodes marked in red: 3 = 3.
# - The sum of the nodes marked in yellow: 2 + 2 = 4.

print("Example 2")

linked_list = Node(0, Node(1, Node(0, Node(3, Node(0, Node(2, Node(2, Node(0))))))))
new_linked_list = combineLinkedList(linked_list)

while new_linked_list != None:
    print(new_linked_list.value)
    new_linked_list = new_linked_list.next