class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        firstOb = next((i for i in range(col) if obstacleGrid[0][i] == 1), col)
        dp = [1] * firstOb + [0] * (col - firstOb)
        for i in range(1, row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j != 0:
                    dp[j] += dp[j-1]
        return dp[-1]
        
