from Leetcode_type import *
from typing import List


def pre_view(root: TreeNode) -> List[TreeNode]:
    result = []
    if root is None:
        return []
    result.append(root)
    result += pre_view(root.left)
    result += pre_view(root.right)
    return result

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        tmp = pre_view(root)
        root.left = None
        p = root
        for node in tmp[1:]:
            p.left = None
            p.right = node
            p = p.right


if __name__ == '__main__':
    a = Solution()
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    a.flatten(tree)

