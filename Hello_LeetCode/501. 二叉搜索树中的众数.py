from Leetcode_type import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def mid_view(root: TreeNode):
            nonlocal ele
            if not root:
                return
            mid_view(root.left)
            ele.append(root.val)
            mid_view(root.right)

        ele = []
        mid_view(root)
        count_dict = collections.defaultdict(list)
        for i in set(ele):
            count_dict[ele.count(i)].append(i)
        max_key = max(list(count_dict.keys()))
        return count_dict[max_key]
