from Leetcode_type import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        if root.right:
            self.invertTree(root.right)
        if root.left:
            self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        return root