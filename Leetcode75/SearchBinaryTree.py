from pyparsing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Iterate through the tree until root becomes None
        while root is not None:
            # If current node's value is less than the target value, move to the right subtree
            if root.val < val:
                root = root.right
            # If current node's value is greater than the target value, move to the left subtree
            elif root.val > val:
                root = root.left
            # If current node's value is equal to the target value, return the current node
            else:
                return root
        # If the target value is not found in the tree, return None
        return None
