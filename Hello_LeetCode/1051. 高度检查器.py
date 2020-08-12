from typing import *


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        tmp = sorted(heights)
        for i in range(len(tmp)):
            res = res + 1 if tmp[i] != heights[i] else res + 0
        return res


a = Solution()
b = a.heightChecker([2,1,2,1,1,2,2,1])
print(b)