from Leetcode_type import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        root_i = nums.index(max(nums))
        root = TreeNode(nums[root_i])
        root.left = self.constructMaximumBinaryTree(nums[:root_i])
        root.right = self.constructMaximumBinaryTree(nums[root_i+1:])
        return root


