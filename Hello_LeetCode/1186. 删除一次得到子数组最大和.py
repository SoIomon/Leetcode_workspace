from Leetcode_type import *


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if max(arr) <= 0:
            return max(arr)
        if min(arr) >= 0:
            return sum(arr)

        dp = [0] * len(arr)
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + arr[i]
            else:
                dp[i] = arr[i]

        dp1 = [0] * len(arr)
        dp1[-1] = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            if dp1[i + 1] > 0:
                dp1[i] = dp1[i + 1] + arr[i]
            else:
                dp1[i] = arr[i]

        res = -1e9
        for i in range(len(arr)):
            if arr[i] < 0:
                if i == 0:
                    res = max(res, dp1[i + 1])
                elif i == len(arr) - 1:
                    res = max(res, dp[i - 1])
                else:
                    res = max(res, dp[i - 1], dp1[i + 1], dp1[i + 1] + dp[i - 1])

        return res
