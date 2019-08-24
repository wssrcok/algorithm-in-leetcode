class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [-1] * n
        
        def can_place(i, j):
            '''
            test only horizontal and diagnal lines for left side
            '''
            for col in range(j):
                if board[col] == i:  # horizontal
                    return False
                if board[col] == i + (j - col) or\
                        board[col] == i - (j - col):  # diagnal lines
                    return False
            return True

        def explore(col=0):
            if (col == n):
                out.append(['.' * pos + 'Q' + '.' * (n - pos - 1)  for pos in board])
            else:
                for row in range(n):
                    if can_place(row, col):
                        board[col] = row
                        explore(col+1)
        out = []
        explore()
        return out

                    
                
