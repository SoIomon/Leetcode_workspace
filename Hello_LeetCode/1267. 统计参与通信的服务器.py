from typing import *

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count_m, count_n = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count_m[i] += 1
                    count_n[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (count_m[i] > 1 or count_n[j] > 1):
                    ans += 1
        return ans
