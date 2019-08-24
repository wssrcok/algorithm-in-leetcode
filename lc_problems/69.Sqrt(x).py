class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            raise Exception()
        i, j = 0, (x+1) // 2
        while i <= j:
            m = i + (j - i) // 2
            m2 = m * m
            if m2 == x:
                return m
            if m2 < x:
                i = m + 1
            else:
                j = m - 1
        return j
