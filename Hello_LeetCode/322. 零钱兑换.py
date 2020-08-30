from typing import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e9 for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                if i >= coin and dp[i-coin] != 1e9:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        print(dp)
        if dp[amount] == 1e9:
            return -1
        return dp[amount]

a = Solution().coinChange(coins=[1,2,5], amount=11)
print(a)
