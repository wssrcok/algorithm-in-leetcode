class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        d = self.build_dict(board)
    
    def build_set(self, board):
        s = set() 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].isdigit():
                    d.add('c'+board[i][j]
