from Leetcode_type import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res: List[int] = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop(-1)
            res.append(root.val)
            root = root.right
        return res