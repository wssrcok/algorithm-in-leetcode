class Solution:
    def grayCode(self, n: int) -> List[int]:
        out = [0]
        for i in range(n):
            out += [o + (1<<i) for o in reversed(out)]
        return out
