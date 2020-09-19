from Leetcode_type import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ans = collections.defaultdict(list)
        queue = [(root, 0, 0)]
        res = []
        while queue:
            node, x, y = queue.pop(0)
            ans[x].append((y, node.val))
            if node.left:
                queue.append((node.left, x-1, y -1))
            if node.right:
                queue.append((node.right, x+1, y -1))

        key_list = list(ans.keys())
        key_list.sort()
        for key in key_list:
            tmp = ans[key]
            tmp.sort(key=lambda x:x[1])
            tmp.sort(key=lambda x:x[0], reverse=True)
            res.append([i[1] for i in tmp])
        return res