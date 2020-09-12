from Leetcode_type import *


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        count = collections.defaultdict(int)

        def sum_up(root: TreeNode) -> int:
            if root:
                left = sum_up(root.left)
                right = sum_up(root.right)
                count[right + left + root.val] += 1
                return root.val + left + right
            else:
                return 0

        sum_up(root)
        max_fre = max([count[i] for i in count.keys()])
        res = []
        for key in count.keys():
            if count[key] == max_fre:
                res.append(key)
        return res