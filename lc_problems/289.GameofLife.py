class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        rows, cols = len(board), len(board[0])
        def next_state(row, col):
            neighbors = 0
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if board[i][j] % 2: neighbors += 1  # only check first bit for current state
            nieghbors -= board[row][col] % 2
            if 2 <= neighbors <= 3:
                board[row][col] += 2  # set the second bit to one for next state
        for i in range(rows):
            for j in range(cols):
                board[i][j] = next_state(i, j)
        for i in range(rows):
            for j in range(cols):
                board[i][j] >>= 1
