from Leetcode_type import *
import math

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            for j in range(1, i):
                if math.gcd(i, j) == 1:
                    result.append(f'{j}/{i}')
        return result

print(Solution().simplifiedFractions(3))