class Solution:
    def minDistance_naive(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = self.minDistance(word1, word2[1:])
        delete = self.minDistance(word1[1:], word2)
        replace = self.minDistance(word1[1:], word2[1:])
        return 1 + min(insert, delete, replace)

    def minDistance_mem(self, word1: str, word2: str) -> int:
        mem = {}

        def md(i1=0, i2=0):
            if i1 == len(word1) or i2 == len(word2):
                return len(word1) - i1 + len(word2) - i2
            if (i1, i2) not in mem:
                if word1[i1] == word2[i2]:
                    mem[(i1, i2)] = md(i1 + 1, i2 + 1)
                else:
                    insert = md(i1, i2 + 1)
                    delete = md(i1 + 1, i2)
                    replace = md(i1 + 1, i2 + 1)
                    mem[(i1, i2)] = 1 + min(insert, delete, replace)
            return mem[(i1, i2)]

        return md()

    def minDistance_dp(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
        return dp[-1][-1]
