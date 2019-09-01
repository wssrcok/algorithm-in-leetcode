class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 if n != 0 else True

