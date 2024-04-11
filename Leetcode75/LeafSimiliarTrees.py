from pyparsing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Function to find leaf nodes of a binary tree
        def find_leaves(tree):
            if tree == None:  # If tree is empty, return an empty list
                return []
            elif tree.left == tree.right == None:  # If current node is a leaf, return its value
                return [tree.val]
            else:  # Recursively find leaf nodes in the left and right subtrees
                return find_leaves(tree.left) + find_leaves(tree.right)
        
        # Check if the sequences of leaf nodes in both trees are the same
        return find_leaves(root1) == find_leaves(root2)
