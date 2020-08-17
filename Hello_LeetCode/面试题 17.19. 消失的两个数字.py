from typing import *


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        N = len(nums) + 2
        sum_nums = sum(nums)

        sum_missing_two = N * (N + 1) // 2 - sum_nums
        half_sum_missing_two = sum_missing_two//2

        s = 0
        for _, v in enumerate(nums):
            if v <= half_sum_missing_two:
                s += v
        a = half_sum_missing_two * (half_sum_missing_two + 1) // 2 - s
        return [a, sum_missing_two-a]

a = Solution()
b = a.missingTwo([1])
print(b)