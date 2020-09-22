from Leetcode_type import *


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_max_grid = [[(grid[i][j],grid[i][j]) for j in range(n)]for i in range(m)]

        for i in range(1, m):
            val = grid[i][0]
            tmp = [val * k for k in min_max_grid[i-1][0]]
            min_max_grid[i][0] = min(tmp), max(tmp)

        for i in range(1, n):
            val = grid[0][i]
            tmp = [val * k for k in min_max_grid[0][i-1]]
            min_max_grid[0][i] = min(tmp), max(tmp)

        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                tmp = [val * k for k in min_max_grid[i][j - 1]]
                tmp += [val * k for k in min_max_grid[i-1][j]]
                min_max_grid[i][j] = min(tmp), max(tmp)

        if min_max_grid[m-1][n-1][1] < 0:
            return -1
        else:
            return min_max_grid[m-1][n-1][1] % 1000000007


grid = [[ 1, 4,4,0],
             [-2, 0,0,1],
             [ 1,-1,1,1]]
print(Solution().maxProductPath(grid))