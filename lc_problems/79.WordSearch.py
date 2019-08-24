class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False
        height, width = len(board), len(board[0])
        
        def match(i, j, w=word, visited=set()):
            if len(w) == 0:
                return True
            if not 0 <= i < height or\
                    not 0 <= j < width or\
                    (i, j) in visited:
                return False
            if w[0] != board[i][j]:
                return False
            visited.add((i, j))
            res = match(i+1, j, w[1:], visited) or\
                  match(i, j+1, w[1:], visited) or\
                  match(i-1, j, w[1:], visited) or\
                  match(i, j-1, w[1:], visited)
            if res:
                return True
            visited.remove((i, j))
            return False
        
        for i in range(height):
            for j in range(width):
                if match(i, j):
                    return True
        return False
