class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        out = [[None] * n for _ in range(n)]
        i, j = 0, 0
        turn_right = {(0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1)}
        direction = (0, 1)
        count = 1
        while self.isValid(i, j, out):
            out[i][j] = count
            count += 1
            next_i, next_j = i + direction[0], j + direction[1]
            if not self.isValid(next_i, next_j, out):
                direction = turn_right[direction]
                next_i, next_j = i + direction[0], j + direction[1]
            i, j = next_i, next_j
        return out
                

    def isValid(self, i, j, matrix):
        return len(matrix) > i >= 0 and len(matrix[0]) > j >= 0 and matrix[i][j] is None

