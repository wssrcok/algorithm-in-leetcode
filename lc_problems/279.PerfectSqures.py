class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        for i in range(1, n+1):
            j = 1
            val = dp[-1] + 1
            while j*j < i:
                val = min(val, 1 + dp[i-j*j])
                j += 1
            dp.append(val)
        return dp[-1]

                
