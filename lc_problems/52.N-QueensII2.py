class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0
        board = [-1] * n

        def explore(col=0):
            if col == n:
                return 1
            out = 0
            for row in range(n):
                if can_place(row, col):
                    board[col] = row
                    out += explore(col + 1)
            return out   

        def can_place(row, col):
            for j in range(col):
                if board[j] == row:
                    return False
                if board[j] == row + (col - j) or\
                        board[j] == row - (col - j):
                    return False
            return True

        return explore()
                

