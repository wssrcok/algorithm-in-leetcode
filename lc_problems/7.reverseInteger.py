class Solution:
    def reverse(self, x: int) -> int:
        sign = x < 0
        x = abs(x)
        out = 0
        while x:
            out = out * 10 + x % 10
            x //= 10
        if (not sign and out > (1<<31)-1) or (sign and out > (1<<31)):
            return 0
        return out if not sign else -out
