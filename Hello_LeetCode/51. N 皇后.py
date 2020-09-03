from Leetcode_type import *


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag = set()
        undiag = set()
        board = [['.'] * n for _ in range(n)]
        result = []
        def dfs(row_i:int):
            if row_i == n:
                result.append([''.join(line) for line in board])
                return
            for col_i in range(n):
                if col_i not in col and (row_i + col_i) not in diag and (row_i - col_i) not in undiag:
                    board[row_i][col_i] = 'Q'
                    col.add(col_i)
                    diag.add((row_i+col_i))
                    undiag.add((row_i-col_i))
                    dfs(row_i + 1)
                    board[row_i][col_i] = '.'
                    col.discard(col_i)
                    diag.discard(col_i+row_i)
                    undiag.discard(row_i-col_i)
        dfs(0)
        return result


print(Solution().solveNQueens(4))
