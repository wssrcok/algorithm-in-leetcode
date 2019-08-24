class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [-1] * n  # e.g. [1,2,...] means Q is at row1, col0 and row2 col1
       
        def can_put(row, col):
            for i in range(col):
                if board[i] == row:
                    return False
                diff = abs(i - col)
                if board[i] in (row + diff, row - diff):
                    return False
            return True
            
        def play(col=0):
            if col == n:
                return 1
            count = 0
            for row in range(n):
                if can_put(row, col):
                    board[col] = row
                    count += play(col+1)
                    board[col] = -1
            return count
        
        return play() 
