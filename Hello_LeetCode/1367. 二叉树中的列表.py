from Leetcode_type import *

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head is None:
            return True
        if root is None:
            return False
        result = False
        if root.val == head.val:
            result = result or self.dfs(head, root)
        return result or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, head: ListNode, root: TreeNode) -> bool:
        if head is None:
            return True
        if root is None:
            return False
        if head.val != root.val:
            return False
        return self.dfs(head.next, root.right) or self.dfs(head.next, root.left)

