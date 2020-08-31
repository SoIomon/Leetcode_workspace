from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        grid_x = [[i for i in j] for j in grid]
        grid_y = [[i for i in j] for j in grid]

        for i in range(m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    grid_x[i][j] += grid_x[i][j-1]

        for i in range(1, m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid_y[i][j] += grid_y[i-1][j]

        result = 0
        for i in range(m):
            for j in range(n):
                a = min(grid_x[i][j], grid_y[i][j])
                if a == 0:
                    tmp = 0
                # elif a == 1:
                #     tmp = 1
                else:
                    tmp = 0
                    while a > 0:
                        up = grid_x[i-a+1][j]
                        left = grid_y[i][j-a+1]
                        if up >= a and left >= a:
                            tmpp = a ** 2
                        else:
                            tmpp = 0
                        tmp = tmp if tmp > tmpp else tmpp
                        a -= 1
                result = tmp if tmp > result else result
        return result


grid = [[1,1,1],[1,0,1],[1,1,1]]
# grid = [[1,1,0,0]]
# grid = [[0,1,1,1,1,0],[1,1,0,1,1,0],[1,1,0,1,0,1],[1,1,0,1,1,1],[1,1,0,1,1,1],[1,1,1,1,1,1],[1,0,1,1,1,1],[0,0,1,1,1,1],[1,1,1,1,1,1]]
a = Solution().largest1BorderedSquare(grid)
print(a)