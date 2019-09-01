class Solution:
    def nthUglyNumber(self, n: int) -> int:
        cur = [1]
        i2 = i3 = i5 = 0
        while len(cur) < n:
            while cur[i2] * 2 <= cur[-1]: i2 += 1
            while cur[i3] * 3 <= cur[-1]: i3 += 1
            while cur[i5] * 5 <= cur[-1]: i5 += 1
            cur.append(min(cur[i2] * 2, cur[i3] * 3, cur[i5] * 5))
        return cur[-1]
