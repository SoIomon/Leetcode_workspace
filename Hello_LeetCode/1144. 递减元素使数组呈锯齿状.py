from typing import *


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        ans1, ans2 = 0, 0
        for i in range(n):
            # 奇数位置
            if i % 2 == 0:
                d1 = nums[i] - nums[i - 1] + 1 if i > 0 and nums[i] >= nums[i - 1] else 0
                d2 = nums[i] - nums[i + 1] + 1 if i < n - 1 and nums[i] >= nums[i + 1] else 0
                ans1 += max(d1, d2)
            # 偶数位置
            else:
                d1 = nums[i] - nums[i - 1] + 1 if nums[i] >= nums[i - 1] else 0
                d2 = nums[i] - nums[i + 1] + 1 if i < n - 1 and nums[i] >= nums[i + 1] else 0
                ans2 += max(d1, d2)
        return min(ans1, ans2)
