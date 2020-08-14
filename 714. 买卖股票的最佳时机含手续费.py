from typing import *


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        print(cash, hold)
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
            print(cash, hold)
        return cash


a = Solution()
b = a.maxProfit([1, 3, 2, 8, 4, 9], 2)
print(b)
