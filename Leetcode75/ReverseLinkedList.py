from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # Initialize pointers for previous and current nodes
    previous, current = None, head
    # Traverse through the list until current node becomes None
    while current is not None:
        # Store next node's reference to avoid losing it
        next_node = current.next
        # Reverse the link by pointing current node to previous
        current.next = previous
        # Move pointers one step forward
        previous = current
        current = next_node
    
    # Previous will now point to the head of the reversed list
    return previous

# Create the nodes and link them together
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# The head of the linked list is node1
head = node1

# Reverse the list
reversed_head = reverseList(head)

# Print the reversed list
current = reversed_head
while current is not None:
    print(current.val, end=" ")
    current = current.next