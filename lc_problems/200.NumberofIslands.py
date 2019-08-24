class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def explore(i, j):
            if not (0 <= i < rows) or not (0 <= j < cols):
                return
            if grid[i][j] == '0':
                return
            if visited[i][j]:
                return
            visited[i][j] = True
            explore(i+1, j)
            explore(i-1, j)
            explore(i, j+1)
            explore(i, j-1)

        out = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == '1':
                    out += 1
                    explore(i, j)
        return out
