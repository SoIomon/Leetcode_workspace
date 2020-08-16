from typing import *


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        queue = []

        n, m = len(grid), len(grid[0])
        for x in range(n):
            for y in range(m):

                if grid[x][y] == 1:
                    tmp_area = 0
                    queue.append((x, y))
                    grid[x][y] = 0

                    while queue:
                        mx, my = queue.pop(0)
                        tmp_area += 1

                        for nx, ny in [(mx - 1, my), (mx + 1, my), (mx, my - 1), (mx, my + 1)]:
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                                queue.append((nx, ny))
                                grid[nx][ny] = 0

                    max_area = tmp_area if tmp_area > max_area else max_area

        return max_area


a = Solution()
island = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
b = a.maxAreaOfIsland(island)
print(b)
