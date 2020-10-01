from Leetcode_type import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left:int, right:int) -> TreeNode:
            if left > right:
                return None

            val = postorder.pop(-1)
            root = TreeNode(val)

            index = idx_map[val]

            root.right = helper(index + 1, right)
            root.left = helper(left, index-1)
            return root

        idx_map = {val:i for i, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)