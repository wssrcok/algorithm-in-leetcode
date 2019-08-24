class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def turn_right(direction):
            if direction == (0, 1):
                return (1, 0)
            if direction == (1, 0):
                return (0, -1)
            if direction == (0, -1):
                return (-1, 0)
            if direction == (-1, 0):
                return (0, 1)

        def move(i=0, j=0, direction=(0, 1)):
            if i < 0 or i == len(matrix) or\
                    j < 0 or j == len(matrix[0]) or matrix[i][j] is None:
                return []
            next_i, next_j = i + direction[0], j + direction[1]
            if next_i < 0 or next_i == len(matrix) or\
                    next_j < 0 or next_j == len(matrix[0]) or\
                    matrix[next_i][next_j] is None:
                direction = turn_right(direction)
            val = matrix[i][j]
            matrix[i][j] = None
            return [val] + \
                move(i+direction[0], j+direction[1], direction)
        return move()
