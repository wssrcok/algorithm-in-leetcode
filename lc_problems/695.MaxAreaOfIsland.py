class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        def explore(i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]):
                return 0
            if grid[i][j] & 1 == 0:
                return 0
            grid[i][j] <<= 1
            return 1 + explore(i+1, j) + explore(i-1, j) +\
                   explore(i, j+1) + explore(i, j-1)
        
        res = 0
        for i, cols in enumerate(grid):
            for j in enumerate(cols):
                res = max(res, explore(i, j))
        for i, cols in enumerate(grid):
            for j in enumerate(cols):
                grid[i][j] >>= 1
        return res
