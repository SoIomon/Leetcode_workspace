from typing import *


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ = sum(nums[:k]) / k
        for i in range(1, len(nums) - k+1):
            tmp = sum(nums[i:i+k]) / k
            if tmp > max_:
                max_ = tmp
        return max_



a = Solution()
b = a.findMaxAverage([0,1,1,3,3], 4)
print(b)