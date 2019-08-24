class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    col = ('col', board[i][j], j)
                    row = ('row', board[i][j], i)
                    box = (board[i][j], i//3, j//3)
                    if col in seen or row in seen or box in seen:
                        return False
                    seen.update([col, row, box])
        return True
