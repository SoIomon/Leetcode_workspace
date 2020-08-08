from Leetcode_type import *


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        Trees = lambda x: [] if not x else Trees(x.left) + [x] + Trees(x.right)
        a = Trees(root)
        sa = sorted(a, key=lambda x: x.val)
        tmp = [a[i] for i in range(len(a)) if a[i] != sa[i]]
        tmp[0].val, tmp[1].val = tmp[1].val, tmp[0].val
