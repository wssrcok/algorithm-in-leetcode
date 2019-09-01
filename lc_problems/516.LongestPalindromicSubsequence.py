class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        algorithm:
        for big window start from i to end:
            for small window start from i to j:
                if s[i] != s[j]:
                    record the max(dp[i+1, j], dp[i, j-1]) in dp[i][j]    
                if s[i] == s[j]:
                    dp[i][j] += 2
                _max = max(dp[i][j], _max)
        '''
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in reversed(range(n):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][-1]
