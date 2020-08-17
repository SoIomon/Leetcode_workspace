from typing import *


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 0
        tmp = 1

        if nums == []:
            return 0

        for i, v in enumerate(nums[1:]):
            if v > nums[i]:
                tmp+=1
            else:
                result = tmp if tmp > result else result
                tmp = 1

        if tmp != 0:
            result = tmp if tmp > result else result

        return result

a = Solution()
b = a.findLengthOfLCIS([1,3,5,7])
print(b)