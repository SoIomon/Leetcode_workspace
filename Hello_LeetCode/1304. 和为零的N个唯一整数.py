from typing import *

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 == 1:
            result.append(0)
            n -= 1
        for i in range(1, n//2 + 1):
            result.append(i)
            result.append(-1*i)
        return result

a = Solution().sumZero(3)
print(a)