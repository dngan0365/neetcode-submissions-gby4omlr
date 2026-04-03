class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(board: List[List[str]], row: int):
            unique = set()
            for i in range(0,9):
                if board[row][i] != '.' and board[row][i] in unique:
                    return False
                elif board[row][i] != '.':
                    unique.add(board[row][i])
            return True

        def check_col(board: List[List[str]], col: int):
            unique = set()
            for i in range(0,9):
                if board[i][col] != '.' and board[i][col] in unique:
                    return False
                elif board[i][col] != '.':
                    unique.add(board[i][col])
            return True

        def check_box(board: List[List[str]], row_ind: int, col_ind: int):
            row = row_ind * 3
            col = col_ind * 3
            unique = set()
            for i in range(row, row+3):
                for j in range(col, col+3):
                    if board[i][j] != '.' and board[i][j] in unique:
                        return False
                    elif board[i][j] != '.':
                        unique.add(board[i][j])
            return True
        for i in range(0, 9):
            temp = check_row(board, i)
            if not temp:
                return False

        for i in range(0,9):
            temp = check_col(board, i)
            if not temp:
                return False

        for i in range(0, 3):
            for j in range(0, 3):
                temp = check_box(board, i, j)
                if not temp:
                    return False
        return True
