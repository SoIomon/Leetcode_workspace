from Leetcode_type import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def pre_view(root: TreeNode):
            if not root:
                return []
            ans = []
            ans += pre_view(root.left)
            ans += [root.val]
            ans += pre_view(root.right)

            return ans

        tree1 = pre_view(root1)
        tree2 = pre_view(root2)

        i, j = 0, 0
        ans = []
        while i < len(tree1) and j < len(tree2):
            if tree1[i] < tree2[j]:
                ans.append(tree1[i])
                i += 1
            else:
                ans.append(tree2[j])
                j += 1
        ans += tree1[i:] + tree2[j:]
        return ans

