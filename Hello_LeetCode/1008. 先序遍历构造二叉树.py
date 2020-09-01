from Leetcode_type import *

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        split = 0
        for i, v in enumerate(preorder):
            if v <= preorder[0]:
                split = i

        left_tree = preorder[1:split+1]
        right_tree = preorder[split+1:]

        result = TreeNode(preorder[0])
        result.left = self.bstFromPreorder(left_tree)
        result.right = self.bstFromPreorder(right_tree)

        return result


a = Solution().bstFromPreorder([8,5,1,7,10,12])
print(a)