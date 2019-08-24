class Solution():
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = []
        curr = [-1] * n

        def claim(row, col):
            for i in range(row):
                if curr[i] == col:
                    return False
                row_diff = abs(row - i)
                if curr[i] == col + row_diff or curr[i] == col - row_diff:
                    return False
            curr[row] = col
            return True

        def backtrack(row=0):
            if row == n:
                out.append([''.join(['.' if j != i else 'Q' for j in range(n)]) for i in curr])
            else:
                for col in range(n):
                    if claim(row, col):
                        backtrack(row+1)
                        curr[row] = -1

        backtrack()
        return out
