#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                up = dp[i-1][j] if i >= 0 else 0
                left = dp[i][j-1] if j >= 0 else 0
                upleft = dp[i-1][j-1] if i >= 0 and j >= 0 else 0
                dp[i][j] = min(up, left, upleft) + 1 if matrix[i][j] == '1' else 0
                res = max(res, dp[i][j])
        return res**2

