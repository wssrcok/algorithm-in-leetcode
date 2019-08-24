class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        z_col = z_row = False
        if matrix[0][0] != 0:
            for i in range(1, len(matrix)):
                if matrix[i][0] == 0:
                    z_col = True
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0:
                    z_row = True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0] * len(matrix[0])
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        z_all = matrix[0][0] == 0
        if z_row or z_all:
            matrix[0] = [0] * len(matrix[0])
        if z_col or z_all:
            for i in range(len(matrix)):
                matrix[i][0] = 0

            
