#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
class Solution:
    def countPrimes(self, n: int) -> int:
        dp = [1] * n
        dp[:2] = [0] * 2
        for i in range(2, n):
            if dp[i]:
                j = i
                while i * j < n:
                    dp[i*j] = 0
                    j += 1
        return sum(dp)


