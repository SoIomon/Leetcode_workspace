from Leetcode_type import *


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MODULO = 10 ** 9 + 7
        odd, even = 0, 1
        subarrays = 0
        total = 0

        for x in arr:
            total += x
            subarrays += (odd if total % 2 == 0 else even)
            if total % 2 == 0:
                even += 1
            else:
                odd += 1

        return subarrays % MODULO

