from typing import List

"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
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
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(i, j):
            if f[i][j]:  # 扩展到边界，即与边界的‘O’相连，返回True
                return True
            global visited, path
            visited[i][j] = 1
            path.append((i, j))
            a = b = c = d = False
            if board[i - 1][j] == 'O' and not visited[i - 1][j]:
                a = dfs(i - 1, j)
            if board[i + 1][j] == 'O' and not visited[i + 1][j]:
                b = dfs(i + 1, j)
            if board[i][j - 1] == 'O' and not visited[i][j - 1]:
                c = dfs(i, j - 1)
            if board[i][j + 1] == 'O' and not visited[i][j + 1]:
                d = dfs(i, j + 1)
            if a or b or c or d:
                return True
            return False

        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        global visited, path
        visited = [[0] * n for _ in range(m)]

        # 用f来标记边界的‘O’, 令边界的‘O’对应的f[i][j] = 1
        f = [[0] * n for _ in range(m)]
        for i in range(n):
            if board[0][i] == 'O':
                f[0][i] = 1
            if board[m - 1][i] == 'O':
                f[m - 1][i] = 1
        for i in range(m):
            if board[i][0] == 'O':
                f[i][0] = 1
            if board[i][n - 1] == 'O':
                f[i][n - 1] = 1

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O' and not visited[i][j]:
                    path = []  # 记录路径
                    # dfs(i, j)==False, 说明不与边界的‘O’相连, 则将路径上的‘O’全部变为‘X’
                    # dfs(i, j)==True,  说明与边界的‘O’相连, 此时路径上的‘O’的visited全为1,因此之后也不会被搜索
                    if dfs(i, j) == False:
                        for p, q in path:
                            board[p][q] = 'X'



a = Solution()
b = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
a.solve(b)
print(b)
