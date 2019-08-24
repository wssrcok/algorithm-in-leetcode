class Solution:
    def longestPalindrome_with_expand(self, s: str) -> str:
        if not s:
            return ""
        out = 1
        outs = s[0]
        for i in range(1, len(s)):
            n1 = self.expand(i-1, i, s)
            n2 = self.expand(i, i, s)
            if max(n1, n2) > out:
                outs = s[i-n2//2:i+n2//2+1] if n2 > n1 else s[i-n1//2+1:i+n1//2+1]
                out = max(n1, n2)          
        return outs

    def expand(self, i, j, s):
        while (i >= 0 and j < len(s) and s[i] == s[j]):
            i, j = i - 1, j + 1
        return j - i - 1

    def longestPalindrome_with_dp(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        left = right = 0
        for width in range(1, n):
            for i in range(0, n-width+1):
                j = i + width - 1
                if s[i] == s[j] and j - i <= 1 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if j - i > right - left:
                        left, right = i, j
        return s[left:right+1] if s else ""               
