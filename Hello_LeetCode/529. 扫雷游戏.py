import copy
from typing import *


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        queue = []
        queue.append((click[0], click[1]))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        while queue:
            x, y = queue.pop(0)
            if board[x][y] == 'M':
                board[x][y] = 'X'
            elif board[x][y] == 'E':
                count = 0
                for dx, dy in directions:
                    if 0 <= x + dx < m and 0 <= y + dy < n and board[x + dx][y + dy] == 'M':
                        count += 1
                if count == 0:
                    board[x][y] = 'B'
                    for dx, dy in directions:
                        if 0 <= x + dx < m and 0 <= y + dy < n and board[x + dx][y + dy] == 'E':
                            queue.append((x + dx, y + dy))
                else:
                    board[x][y] = str(count)

        return board


board = [["E", "E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E", "M"],
         ["E", "E", "M", "E", "E", "E", "E", "E"], ["M", "E", "E", "E", "E", "E", "E", "E"],
         ["E", "E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E", "E"],
         ["E", "E", "E", "E", "E", "E", "E", "E"], ["E", "E", "M", "M", "E", "E", "E", "E"]]

click = [0, 0]

a = Solution()
b = a.updateBoard(board, click)
print(b)
