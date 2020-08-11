class Solution:
    def tictactoe(self, board: List[str]) -> str:
        H = len(board[0])
        ## 行满足
        for i in range(H):
            last_char = board[i][0]
            exist_row = True
            for j in range(1, H):
                if last_char != board[i][j]:
                    exist_row = False
                    break
            if exist_row and last_char != " ":
                return last_char
        ## 列满足
        for i in range(H):
            last_char = board[0][i]
            exist_col = True
            for j in range(1, H):
                if last_char != board[j][i]:
                    exist_col = False
                    break
            if exist_col and last_char != " ":
                return last_char
        ## 对角线满足
        cor_1, cor_2 = board[H - 1][0], board[H - 1][H - 1]
        cor1_exist, cor2_exist = True, True

        for i in range(1, H):
            if board[H - 1 - i][i] != cor_1:
                cor1_exist = False
                break
        if cor1_exist and cor_1 != " ":
            return cor_1
        for i in range(H):
            if board[H - 1 - i][H - 1 - i] != cor_2:
                cor2_exist = False
                break
        if cor2_exist and cor_2 != " ":
            return cor_2
        ## 判断是否存在空格
        for string in board:
            if string.count(" ") > 0:
                return "Pending"
        return "Draw"