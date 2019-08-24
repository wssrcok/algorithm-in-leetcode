import pysnooper

class Solution:
    @pysnooper.snoop()
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        out = [0] * (len(num1) + len(num2))
        pos = len(out) - 1
        for a in reversed(num1):
            tempos = pos
            for b in reversed(num2):
                p = int(a) * int(b) + out[tempos]
                out[tempos] = p % 10
                out[tempos-1] += p // 10
                tempos -= 1
            pos -= 1
        return ''.join([str(o) for o in out]).lstrip('0')

solution = Solution()
print(solution.multiply('99', '99'))

