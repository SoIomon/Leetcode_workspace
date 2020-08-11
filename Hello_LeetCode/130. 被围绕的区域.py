from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return
        m = len(board[0])

        def dfs(x, y):
            board[x][y] = 'K'
            if x - 1 >= 0 and board[x - 1][y] == 'O':
                dfs(x - 1, y)
            if y - 1 >= 0 and board[x][y - 1] == 'O':
                dfs(x, y - 1)
            if x + 1 < n and board[x + 1][y] == 'O':
                dfs(x + 1, y)
            if y + 1 < m and board[x][y + 1] == 'O':
                dfs(x, y + 1)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    if i == 0 or i == n-1 or j == 0 or j == m-1:
                        dfs(i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'K':
                    board[i][j] = 'O'


a = Solution()
b = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
a.solve(b)
print(b)
