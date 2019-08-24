class Solution:
    def convertToTitle(self, n: int) -> str:
        out = ''
        while n:
            out += chr(ord('A') + (n-1) % 26)
            n = (n - 1) // 26
        return out[::-1]

