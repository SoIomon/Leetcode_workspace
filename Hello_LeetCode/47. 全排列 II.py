from Leetcode_type import *

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 递归
        # 基线条件
        if len(nums) <= 1:
            return [nums]
        ans = []
        for i, v in enumerate(nums):
            for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                if [v] + j not in ans:
                    ans.append([v]+j)
        return ans


print(Solution().permuteUnique([1,1,2]))