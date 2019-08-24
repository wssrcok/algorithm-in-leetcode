class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        longer, shorter = max(m,n), min(m, n)
        dp = [1] * shorter
        for i in range(1, longer):
            for j in range(1, shorter):
                dp[j] = dp[j] + dp[j-1]
        return dp[-1]
