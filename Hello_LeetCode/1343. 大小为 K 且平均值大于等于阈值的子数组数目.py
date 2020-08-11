from typing import *


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        tmp = sum(arr[:k])
        res = 1 if tmp >= k*threshold else 0
        start = 0

        for i in range(k, len(arr)):
            tmp = tmp - arr[start] + arr[i]
            if tmp >= threshold * k:
                res += 1
            start += 1
        return res


a = Solution()
b = a.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
print(b)
