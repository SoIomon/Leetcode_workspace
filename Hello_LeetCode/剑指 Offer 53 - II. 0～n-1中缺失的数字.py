from typing import *


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         for i, v in enumerate(nums):
#             if i != v:
#                 return i
#         return len(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if m == nums[m]:
                i = m + 1
            else:
                j = m - 1
        return i


a = Solution()
b = a.missingNumber([0])
print(b)
