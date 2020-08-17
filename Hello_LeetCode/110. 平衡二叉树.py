from Leetcode_type import *


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = [root]
        p = []
        depth = 1
        while q != []:
            while q != []:
                tmp = q.pop()
                if tmp.left is not None:
                    p.append(tmp.left)
                if tmp.right is not None:
                    p.append(tmp.right)
            q, p = p, q
            depth += 1
        return depth - 1

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return abs(self.maxDepth(root.right) - self.maxDepth(root.left)) <= 1 and self.isBalanced(
            root.right) and self.isBalanced(root.left)
