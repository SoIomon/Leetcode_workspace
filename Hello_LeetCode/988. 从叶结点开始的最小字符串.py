from Leetcode_type import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ''
        queue = [root]
        ans = [chr(root.val + 97)]
        res = []
        while queue:
            tmp = queue.pop(0)
            tmp_str = ans.pop(0)
            if tmp.right:
                queue.append(tmp.right)
                ans.append(tmp_str + chr(tmp.right.val + 97))
            if tmp.left:
                queue.append(tmp.left)
                ans.append(tmp_str + chr(tmp.left.val + 97))
            if not tmp.left and not tmp.right:
                res.append(tmp_str[::-1])
        return min(res)