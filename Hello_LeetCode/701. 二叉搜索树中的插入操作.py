from Leetcode_type import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        p = root
        while p:
            if val < p.val:
                if not p.left:
                    p.left = TreeNode(val)
                    break
                else:
                    p = p.left
            else:
                if not p.right:
                    p.right = TreeNode(val)
                    break
                else:
                    p = p.right

        return root