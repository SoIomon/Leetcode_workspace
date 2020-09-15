from Leetcode_type import *


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        valid = False
        spaces = []

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return

            i, j = spaces[pos]
            for digit in range(9):
                if row[i][digit] == col[j][digit] == block[i // 3][j // 3][digit] == False:
                    row[i][digit] = col[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos+1)
                    row[i][digit] = col[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    row[i][digit] = col[j][digit] = block[i // 3][j // 3][digit] = True

        dfs(0)
