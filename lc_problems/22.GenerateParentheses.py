class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        def generate(s='', left=n, right=n):
            if len(s) == 2*n:
                out.append(s)
            else:
                if left > 0:
                    generate(s + '(', left - 1, right)
                if left < right:
                    generate(s + ')', left, right - 1)
        generate()
        return out
