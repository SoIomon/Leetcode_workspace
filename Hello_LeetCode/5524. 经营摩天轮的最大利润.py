from Leetcode_type import *

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        earn = (-1, -1)
        wating = 0
        now_round = 0
        survived = 0
        for i, customer in enumerate(customers):
            now_round += 1
            wating += customer

            if wating >= 4:
                wating -= 4
                survived += 4
                tmp = survived * boardingCost - now_round * runningCost
                earn = earn if tmp < earn[0] else (tmp, now_round)
            else:
                survived += wating
                wating = 0
                tmp = survived * boardingCost - now_round * runningCost
                earn = earn if tmp <= earn[0] else (tmp, now_round)

        while wating > 0:
            now_round += 1

            if wating >= 4:
                wating -= 4
                survived += 4
                tmp = survived * boardingCost - now_round * runningCost
                earn = earn if tmp < earn[0] else (tmp, now_round)
            else:
                survived += wating
                wating = 0
                tmp = survived * boardingCost - now_round * runningCost
                earn = earn if tmp <= earn[0] else (tmp, now_round)

        return earn[1]

print(Solution().minOperationsMaxProfit([10,10,1,0,0],4,4))