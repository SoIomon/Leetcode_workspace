from Leetcode_type import *

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k <= 0:
            return []
        result = [[i] for i in range(1, n+1)]

        while len(result[0]) != k:
            tmp = result.pop(0)
            for i in range(tmp[-1] + 1, n+1):
                if i not in tmp and n - tmp[-1] >= k - len(tmp):
                    result.append(tmp + [i])

        return result




print(Solution().combine(4, 2))