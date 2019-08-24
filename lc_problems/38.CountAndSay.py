class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        out = '1'
        count = 1
        for _ in range(1, n):
            curr = ''
            for i in range(1, len(out) + 1):
                if i < len(out) and out[i] == out[i-1]:
                    count += 1
                else:
                    curr += str(count) + out[i-1]
                    count = 1
            out = curr
        return out
