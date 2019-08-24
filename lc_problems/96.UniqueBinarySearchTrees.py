class Solution:
    def numTrees_mem(self, n: int) -> int:
        mem = {}
        def backtrack(curr=n):
            if curr == 0:
                return 1
            if curr not in mem:
                mem[curr] = 0
                for i in range(curr):
                    left = backtrack(i)
                    right = backtrack(curr-i-1)
                    mem[curr] += left * right
            return mem[curr]
        return backtrack()

    def numTrees_dp(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]

    dp = [1]
    def numTrees_static_dp(self, n: int) -> int:
        if n < len(self.dp):
            return self.dp[n]
        for i in range(len(self.dp), n+1):
            self.dp.append(0)
            for j in range(i):
                self.dp[i] += self.dp[j] * self.dp[i-j-1]
        return self.dp[n]
