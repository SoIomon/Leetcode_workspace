from typing import *


# class Solution:
#     def PredictTheWinner(self, nums: List[int]) -> bool:
#         def play(start, end, turn):
#             if start == end:
#                 return nums[start] * turn
#             scoreStart = nums[start] * turn + play(start + 1, end, -turn)
#             scoreEnd = nums[end] * turn + play(start, end - 1, -turn)
#             return max(scoreStart * turn, scoreEnd * turn) * turn
#
#         return play(0, len(nums) - 1, 1) >= 0

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for i, num in enumerate(nums):
            dp[i][i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][length - 1] >= 0


a = Solution().PredictTheWinner([1, 5, 2])
print(a)
