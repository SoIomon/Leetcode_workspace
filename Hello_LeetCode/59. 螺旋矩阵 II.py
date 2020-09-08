from Leetcode_type import *


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        Matrix = [[0] * n for _ in range(n)]
        v = 1
        i, j = 0, -1
        di, dj = 0, 0
        while v <= n ** 2:
            if i - j == 1 and i + j < n - 1:
                di, dj = 0, 1
            if i + j == n - 1 and i - j < 0:
                di, dj = 1, 0
            if i - j == 0 and i + j > n - 1:
                di, dj = 0, -1
            if i + j == n - 1 and i - j > 0:
                di, dj = -1, 0
            i, j = i + di, j + dj
            Matrix[i][j] = v
            v += 1
        return Matrix


print(Solution().generateMatrix(2))
