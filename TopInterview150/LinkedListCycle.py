


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    # Check if head is None or if there is only one node
    if not head or not head.next:
        return False
    
    # Initialize slow and fast pointers
    slow = head
    fast = head
    
    # Traverse the linked list with slow and fast pointers
    while slow and fast and fast.next:
        # Move slow pointer one step
        slow = slow.next
        # Move fast pointer two steps
        fast = fast.next.next
        
        # If slow and fast pointers meet, there is a cycle
        if slow == fast:
            return True
    
    # If loop completes without finding a cycle, return False
    return False
