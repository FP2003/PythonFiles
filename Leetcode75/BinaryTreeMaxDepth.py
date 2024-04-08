# Definition for a binary tree node

from pyparsing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    stack = [[root, 1]]  # Initialize stack with root and its depth
    res = 0  # Initialize result variable to store maximum depth

    while stack:
        node, depth = stack.pop()  # Pop node and its depth from stack

        if node:
            res = max(res, depth)  # Update maximum depth
            # Add left and right children of the current node to stack with increased depth
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    
    return res  # Return the maximum depth found
